# SHAP-Grounded Sample Reports (log10(IC50))

## RPT-0001 - sildenafil on IGR1
*Evidence: SHAP-0001*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **sildenafil** (master_cpd_id=27872) |
| Gene Target | PDE5A |
| Mechanism / Activity | inhibitor of phosphodiesterase 5A |
| Cell Line | **IGR1** (master_ccl_id=470) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.6165**
- RF-predicted log10(IC50): **0.8086**
- Prediction error (observed - predicted): **-4.4250**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (63 pairs): mean=2.8595, q10=2.4121, median=2.8420, q90=3.5786, sample percentile=1.6
- Cell cohort (235 pairs): mean=0.7249, q10=-1.2375, median=0.9034, q90=2.3441, sample percentile=0.9
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.616 vs 20-NN mean=+3.165 (|Δ|=6.781)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.2658, |SHAP|=0.2658)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0673** (fingerprint_bit; SHAP=+0.0642, |SHAP|=0.0642)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
3. **CCN1 (3491)** (gene_expression; SHAP=+0.0492, |SHAP|=0.0492)  
  _value=5.4432, z=+0.05; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0688** (fingerprint_bit; SHAP=+0.0355, |SHAP|=0.0355)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
5. **fp_0141** (fingerprint_bit; SHAP=+0.0288, |SHAP|=0.0288)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **fp_0280** (fingerprint_bit; SHAP=-0.0268, |SHAP|=0.0268)  
  _present; representative SMARTS `[#6]:[#7](-[#6]):[#6](-[#6]=[#6]):[#7]:[#6]`; present in 1.5% of CTRPv2 compounds; example compounds: B02, temozolomide, omacetaxine mepesuccinate_
7. **fp_0263** (fingerprint_bit; SHAP=+0.0249, |SHAP|=0.0249)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
8. **fp_0771** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| REC1 | haematopoietic and lymphoid tissue | 1.2279190692416035 | more sensitive |
| BV173 | haematopoietic and lymphoid tissue | 2.181564378576872 | more sensitive |
| NCIH1792 | lung | 3.8802766441087178 | more resistant |
| CL11 | large intestine | 3.9826268426344713 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| NVP-ADW742 | IGF1R | -3.7297455843334686 | more sensitive |
| trametinib | MAP2K1;MAP2K2 | -3.614095277657256 | more sensitive |
| AM-580 | RARA | 3.898338443848557 | more resistant |
| necrostatin-7 |  | 3.9254311434583142 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0002 - BRD-K37390332 on SNU1066
*Evidence: SHAP-0002*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K37390332** (master_cpd_id=463198) |
| Gene Target | n/a |
| Mechanism / Activity | product of diversity oriented synthesis |
| Cell Line | **SNU1066** (master_ccl_id=1079) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.8863**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.9516**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (32 pairs): mean=2.2766, q10=1.3888, median=2.2794, q90=3.7298, sample percentile=3.1
- Cell cohort (150 pairs): mean=0.8684, q10=-0.9064, median=1.1519, q90=2.3406, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.886 vs 20-NN mean=+2.285 (|Δ|=6.171)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1389, |SHAP|=0.1389)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0795, |SHAP|=0.0795)  
  _value=7.0344, z=+0.56; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0496, |SHAP|=0.0496)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0518** (fingerprint_bit; SHAP=-0.0414, |SHAP|=0.0414)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **fp_0876** (fingerprint_bit; SHAP=-0.0354, |SHAP|=0.0354)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0196, |SHAP|=0.0196)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| IALM | lung | 0.9839326697016492 | more sensitive |
| MALME3M | skin | 1.167394323184919 | more sensitive |
| LUDLU1 | lung | 3.7538440459298457 | more resistant |
| HCC1395 | breast | 3.83813244471576 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| WP1130 | UCHL5;USP14;USP5;USP9X | -3.6664512375988543 | more sensitive |
| leptomycin B | XPO1 | -3.6135392276029834 | more sensitive |
| KU-60019 | ATM | 3.612359947967774 | more resistant |
| BRD-K86535717 |  | 3.642462947534173 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0003 - PRL-3 inhibitor I on OVCAR5
*Evidence: SHAP-0003*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PRL-3 inhibitor I** (master_cpd_id=411727) |
| Gene Target | PTP4A3 |
| Mechanism / Activity | inhibitor of phosphatase of regenerating liver-3 (PRL3) |
| Cell Line | **OVCAR5** (master_ccl_id=909) |
| Tissue | n/a |
| Histology | n/a |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.7126**
- RF-predicted log10(IC50): **0.8086**
- Prediction error (observed - predicted): **-4.5212**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (89 pairs): mean=2.1390, q10=0.8021, median=2.3452, q90=3.4016, sample percentile=1.1
- Cell cohort (262 pairs): mean=0.7596, q10=-1.2224, median=1.0726, q90=2.0808, sample percentile=1.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.713 vs 20-NN mean=+2.437 (|Δ|=6.150)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.2958, |SHAP|=0.2958)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.2428, |SHAP|=0.2428)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0071** (fingerprint_bit; SHAP=-0.1481, |SHAP|=0.1481)  
  _present; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
4. **fp_0673** (fingerprint_bit; SHAP=+0.0553, |SHAP|=0.0553)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0447, |SHAP|=0.0447)  
  _value=8.7518, z=+1.12; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0359, |SHAP|=0.0359)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0263** (fingerprint_bit; SHAP=+0.0231, |SHAP|=0.0231)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
8. **fp_0771** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SF539 |  | -0.9475326775061932 | more sensitive |
| SAOS2 | bone | -0.6981248492670703 | more sensitive |
| LS123 | large intestine | 3.84716334458568 | more resistant |
| BCPAP | thyroid | 3.9194105435450353 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.804769879540078 | more sensitive |
| triptolide |  | -3.800585077774668 | more sensitive |
| BRD-K42260513 | EZH2 | 3.774916145626324 | more resistant |
| lapatinib | EGFR;ERBB2 | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0004 - BI-2536 on REC1
*Evidence: SHAP-0004*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BI-2536** (master_cpd_id=347813) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **REC1** (master_ccl_id=964) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | mantle cell lymphoma |

### Response Summary
- Observed log10(IC50): **3.7237**
- RF-predicted log10(IC50): **0.2231**
- Prediction error (observed - predicted): **+3.5006**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (702 pairs): mean=-1.1707, q10=-3.0627, median=-1.4995, q90=0.8396, sample percentile=100.0
- Cell cohort (174 pairs): mean=1.4160, q10=0.4475, median=1.4586, q90=2.4740, sample percentile=100.0
- Interpretation: **more resistant than the model predicted**
- Selection reason: curated outlier: observed log10(IC50)=+3.724 vs 20-NN mean=-2.376 (|Δ|=6.100)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7083, |SHAP|=0.7083)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0876** (fingerprint_bit; SHAP=-0.3586, |SHAP|=0.3586)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
3. **PLEK (5341)** (gene_expression; SHAP=+0.1355, |SHAP|=0.1355)  
  _value=9.1757, z=+4.06; markedly above the cross-cell-line mean; recurs in 12 predictable-drug RF signatures_
4. **CD70 (970)** (gene_expression; SHAP=+0.1337, |SHAP|=0.1337)  
  _value=9.2953, z=+2.41; markedly above the cross-cell-line mean; recurs in 12 predictable-drug RF signatures_
5. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1026, |SHAP|=0.1026)  
  _value=1.9194, z=-1.72; below the cross-cell-line mean; recurs in 82 predictable-drug RF signatures_
6. **TRIP6 (7205)** (gene_expression; SHAP=+0.1010, |SHAP|=0.1010)  
  _value=0.4048, z=-2.23; markedly below the cross-cell-line mean; recurs in 11 predictable-drug RF signatures_
7. **fp_0582** (fingerprint_bit; SHAP=-0.0858, |SHAP|=0.0858)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **CCN1 (3491)** (gene_expression; SHAP=-0.0815, |SHAP|=0.0815)  
  _value=1.1875, z=-1.32; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| LUDLU1 | lung | -3.922420843501675 | more sensitive |
| F36P | haematopoietic and lymphoid tissue | -3.921718750999285 | more sensitive |
| TOLEDO | haematopoietic and lymphoid tissue | 1.9416434720326787 | more resistant |
| JHH6 | liver | 3.222415286063116 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ciclopirox | RRM1 | -2.204861307158615 | more sensitive |
| marinopyrrole A | MCL1 | -1.9076053728428988 | more sensitive |
| VU0155056 | PLD1;PLD2 | 3.3474535517834707 | more resistant |
| lovastatin | HMGCR | 3.654504147360732 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0005 - BRD8899 on MDAMB468
*Evidence: SHAP-0005*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD8899** (master_cpd_id=608062) |
| Gene Target | STK33 |
| Mechanism / Activity | inhibitor of serine/threonine kinasase STK33 |
| Cell Line | **MDAMB468** (master_ccl_id=658) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.2395**
- RF-predicted log10(IC50): **0.9797**
- Prediction error (observed - predicted): **-4.2192**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (28 pairs): mean=2.1280, q10=0.9173, median=2.2100, q90=3.5741, sample percentile=3.6
- Cell cohort (271 pairs): mean=0.5478, q10=-1.4279, median=0.6454, q90=1.9627, sample percentile=2.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.240 vs 20-NN mean=+2.719 (|Δ|=5.958)

### Top TreeSHAP Features
1. **fp_0691** (fingerprint_bit; SHAP=-0.2193, |SHAP|=0.2193)  
  _present; representative SMARTS `[#6]-[#8]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: sirolimus, QW-BI-011, AGK-2_
2. **fp_0141** (fingerprint_bit; SHAP=-0.1489, |SHAP|=0.1489)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0876** (fingerprint_bit; SHAP=+0.0968, |SHAP|=0.0968)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
4. **fp_0535** (fingerprint_bit; SHAP=+0.0859, |SHAP|=0.0859)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
5. **fp_0994** (fingerprint_bit; SHAP=+0.0837, |SHAP|=0.0837)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
6. **fp_0518** (fingerprint_bit; SHAP=+0.0604, |SHAP|=0.0604)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0591, |SHAP|=0.0591)  
  _value=7.3851, z=+0.68; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **fp_0157** (fingerprint_bit; SHAP=+0.0576, |SHAP|=0.0576)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| ALLSIL | haematopoietic and lymphoid tissue | 0.4536391220249179 | more sensitive |
| MV411 | haematopoietic and lymphoid tissue | 0.5856724159380117 | more sensitive |
| TOV112D | ovary | 3.792977945366163 | more resistant |
| HUH6 | liver | 3.792977945366163 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GSK461364 | PLK1 | -3.943492943198154 | more sensitive |
| oligomycin A | ATP5L2 | -3.647072361810745 | more sensitive |
| tretinoin | RARA;RARB;RARG | 3.0524441560327693 | more resistant |
| SGX-523 | MET | 3.3835771512631485 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0006 - docetaxel on BL41
*Evidence: SHAP-0006*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **docetaxel** (master_cpd_id=660364) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **BL41** (master_ccl_id=74) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **3.5221**
- RF-predicted log10(IC50): **0.4919**
- Prediction error (observed - predicted): **+3.0302**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (232 pairs): mean=-1.5609, q10=-3.4473, median=-2.4625, q90=1.6247, sample percentile=99.1
- Cell cohort (47 pairs): mean=1.3526, q10=-0.1289, median=1.4988, q90=3.1488, sample percentile=97.9
- Interpretation: **more resistant than the model predicted**
- Selection reason: curated outlier: observed log10(IC50)=+3.522 vs 20-NN mean=-2.431 (|Δ|=5.953)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7530, |SHAP|=0.7530)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.3835, |SHAP|=0.3835)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0767** (fingerprint_bit; SHAP=+0.2494, |SHAP|=0.2494)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **MYLK (4638)** (gene_expression; SHAP=+0.1982, |SHAP|=0.1982)  
  _value=0.0649, z=-1.32; below the cross-cell-line mean; recurs in 20 predictable-drug RF signatures_
5. **CCN1 (3491)** (gene_expression; SHAP=-0.0973, |SHAP|=0.0973)  
  _value=0.5691, z=-1.52; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0582** (fingerprint_bit; SHAP=-0.0545, |SHAP|=0.0545)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
7. **SYTL2 (54843)** (gene_expression; SHAP=+0.0512, |SHAP|=0.0512)  
  _value=3.9672, z=+0.32; near the cross-cell-line mean; recurs in 36 predictable-drug RF signatures_
8. **fp_0204** (fingerprint_bit; SHAP=-0.0416, |SHAP|=0.0416)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HS683 | central nervous system | -3.990623517601181 | more sensitive |
| PECAPJ49 | upper aerodigestive tract | -3.9768469903133754 | more sensitive |
| K029AX | skin | 3.8802766441087178 | more resistant |
| CAKI1 | kidney | 3.8832869440653575 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| MST-312 | TERT | -3.8573113613085375 | more sensitive |
| obatoclax | BCL2;BCL2L1;MCL1 | -1.4492050993286514 | more sensitive |
| tretinoin | RARA;RARB;RARG | 3.455824350222504 | more resistant |
| PF-3758309 | PAK4 | 3.6364423476208927 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0007 - BRD-K14844214 on SUPT1
*Evidence: SHAP-0007*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K14844214** (master_cpd_id=402775) |
| Gene Target | n/a |
| Mechanism / Activity | product of diversity oriented synthesis |
| Cell Line | **SUPT1** (master_ccl_id=1149) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic T cell leukaemia |

### Response Summary
- Observed log10(IC50): **-3.9996**
- RF-predicted log10(IC50): **0.6600**
- Prediction error (observed - predicted): **-4.6597**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (187 pairs): mean=2.0619, q10=1.6718, median=1.9561, q90=2.8912, sample percentile=0.5
- Cell cohort (254 pairs): mean=0.3301, q10=-1.5434, median=0.5308, q90=1.7055, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-4.000 vs 20-NN mean=+1.836 (|Δ|=5.836)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2311, |SHAP|=0.2311)  
  _value=1.3462, z=-1.27; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0568, |SHAP|=0.0568)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0322** (fingerprint_bit; SHAP=-0.0423, |SHAP|=0.0423)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6]`; present in 15.0% of CTRPv2 compounds; example compounds: BRD9876, tamoxifen, BRD9647_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0259, |SHAP|=0.0259)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0237, |SHAP|=0.0237)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0200, |SHAP|=0.0200)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0167, |SHAP|=0.0167)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0443** (fingerprint_bit; SHAP=+0.0147, |SHAP|=0.0147)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| BV173 | haematopoietic and lymphoid tissue | -3.2346727942117948 | more sensitive |
| LNCAPCLONEFGC | prostate | -1.885103284485098 | more sensitive |
| NCIH2141 | lung | 3.985637142591111 | more resistant |
| HDLM2 | haematopoietic and lymphoid tissue | 3.994668042461031 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.932242396188321 | more sensitive |
| clofarabine |  | -3.8912866012780816 | more sensitive |
| sildenafil | PDE5A | 3.230051853474518 | more resistant |
| fluorouracil | TYMS | 3.744813146059926 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0008 - Mdivi-1 on JHOS2
*Evidence: SHAP-0008*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **Mdivi-1** (master_cpd_id=215497) |
| Gene Target | DNM1 |
| Mechanism / Activity | inhibitor of dynamin 1; inhibitor of mitrochondrial division inhibitor |
| Cell Line | **JHOS2** (master_ccl_id=495) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9864**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0517**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (570 pairs): mean=1.5127, q10=0.8771, median=1.6531, q90=2.0233, sample percentile=0.2
- Cell cohort (200 pairs): mean=0.9145, q10=-1.1322, median=1.1908, q90=2.2818, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.986 vs 20-NN mean=+1.769 (|Δ|=5.755)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0902, |SHAP|=0.0902)  
  _value=9.0138, z=+1.20; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0797, |SHAP|=0.0797)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0570, |SHAP|=0.0570)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0162, |SHAP|=0.0162)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0994** (fingerprint_bit; SHAP=-0.0133, |SHAP|=0.0133)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0124, |SHAP|=0.0124)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0600** (fingerprint_bit; SHAP=+0.0123, |SHAP|=0.0123)  
  _present; representative SMARTS `[#6]:[#6](:[#7]):[#7]`; present in 5.0% of CTRPv2 compounds; example compounds: methotrexate, C6-ceramide, cerulenin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KM12 | large intestine | -3.468138115563649 | more sensitive |
| CHP212 | autonomic ganglia | -3.3254961639817977 | more sensitive |
| CALU1 | lung | 3.6996586467103287 | more resistant |
| KLE | endometrium | 3.7989985452794426 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| momelotinib | JAK1;JAK2 | -3.517877540694729 | more sensitive |
| triptolide |  | -3.222272319811513 | more sensitive |
| PYR-41 | UBA1 | 3.4678655500490634 | more resistant |
| pazopanib | FLT1;FLT3;KDR;KIT;PDGFRB | 3.67557624705721 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0009 - tamoxifen on SKMEL28
*Evidence: SHAP-0009*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **tamoxifen** (master_cpd_id=26972) |
| Gene Target | ESR1;ESR2 |
| Mechanism / Activity | modulator of estrogen receptors |
| Cell Line | **SKMEL28** (master_ccl_id=1043) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.8409**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.9061**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (343 pairs): mean=1.6039, q10=1.0955, median=1.5786, q90=2.3197, sample percentile=0.3
- Cell cohort (143 pairs): mean=1.1031, q10=0.1216, median=1.2357, q90=2.4308, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.841 vs 20-NN mean=+1.880 (|Δ|=5.721)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0920, |SHAP|=0.0920)  
  _value=2.9086, z=-0.77; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0778, |SHAP|=0.0778)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0565, |SHAP|=0.0565)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0154, |SHAP|=0.0154)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0777** (fingerprint_bit; SHAP=+0.0096, |SHAP|=0.0096)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
8. **fp_0994** (fingerprint_bit; SHAP=-0.0088, |SHAP|=0.0088)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MV411 | haematopoietic and lymphoid tissue | -2.4133686760291586 | more sensitive |
| SNU601 | stomach | -1.7098484594057335 | more sensitive |
| HCC1500 | breast | 3.8832869440653575 | more resistant |
| NCIH1568 | lung | 3.9013487438051966 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -2.982950979349351 | more sensitive |
| BRD-K97651142 |  | -2.4737145831377294 | more sensitive |
| C6-ceramide | MAPK1;PPP2CA;UGCG | 3.0163205565530915 | more resistant |
| etomoxir | CPT1A | 3.0556263860612765 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0010 - SID 26681509 on NCIH1651
*Evidence: SHAP-0010*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SID 26681509** (master_cpd_id=411731) |
| Gene Target | CTSL1 |
| Mechanism / Activity | inhibitor of cathepsin L |
| Cell Line | **NCIH1651** (master_ccl_id=155435) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9047**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.9700**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (639 pairs): mean=1.7188, q10=0.8277, median=1.8833, q90=2.3218, sample percentile=0.2
- Cell cohort (182 pairs): mean=0.8203, q10=-1.1709, median=1.0935, q90=2.2994, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.905 vs 20-NN mean=+1.805 (|Δ|=5.709)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1222, |SHAP|=0.1222)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0901, |SHAP|=0.0901)  
  _value=7.1575, z=+0.60; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0831, |SHAP|=0.0831)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0673** (fingerprint_bit; SHAP=-0.0663, |SHAP|=0.0663)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0192, |SHAP|=0.0192)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0160, |SHAP|=0.0160)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0153, |SHAP|=0.0153)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SKMM2 | haematopoietic and lymphoid tissue | -3.613996118177521 | more sensitive |
| OE21 | oesophagus | -3.532396502031166 | more sensitive |
| SW1417 | large intestine | 3.417188750886764 | more resistant |
| REH | haematopoietic and lymphoid tissue | 3.8020088452360823 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| cucurbitacin I |  | -3.5972005107712413 | more sensitive |
| docetaxel |  | -2.988573690796616 | more sensitive |
| BRD-K02251932 |  | 3.329391752043632 | more resistant |
| SR8278 | NR1D1 | 3.765885245756405 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0011 - vincristine on EN
*Evidence: SHAP-0011*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **vincristine** (master_cpd_id=62602) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of mictrotubule assembly |
| Cell Line | **EN** (master_ccl_id=243) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **3.5221**
- RF-predicted log10(IC50): **-1.0504**
- Prediction error (observed - predicted): **+4.5724**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (589 pairs): mean=-1.3333, q10=-2.9338, median=-1.6033, q90=1.3216, sample percentile=100.0
- Cell cohort (199 pairs): mean=1.0301, q10=-1.3342, median=1.3700, q90=2.6121, sample percentile=97.0
- Interpretation: **more resistant than the model predicted**
- Selection reason: curated outlier: observed log10(IC50)=+3.522 vs 20-NN mean=-2.156 (|Δ|=5.678)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-1.1398, |SHAP|=1.1398)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.4941, |SHAP|=0.4941)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0204** (fingerprint_bit; SHAP=-0.1337, |SHAP|=0.1337)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
4. **fp_0767** (fingerprint_bit; SHAP=+0.1061, |SHAP|=0.1061)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
5. **fp_0582** (fingerprint_bit; SHAP=-0.0709, |SHAP|=0.0709)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
6. **fp_0761** (fingerprint_bit; SHAP=-0.0602, |SHAP|=0.0602)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_
7. **fp_0974** (fingerprint_bit; SHAP=-0.0593, |SHAP|=0.0593)  
  _present; representative SMARTS `[#7]-[#6]-[#6]-[#6]-[#6]`; present in 7.5% of CTRPv2 compounds; example compounds: parbendazole, importazole, tacrolimus_
8. **fp_0799** (fingerprint_bit; SHAP=-0.0546, |SHAP|=0.0546)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: ciclopirox, blebbistatin, pifithrin-alpha_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HCC1954 | breast | -3.9905585726829234 | more sensitive |
| DB | haematopoietic and lymphoid tissue | -3.987471614892891 | more sensitive |
| SNU46 | upper aerodigestive tract | 3.287247552650675 | more resistant |
| PATU8902 | pancreas | 3.413680150829547 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| A-804598 | P2RX7 | -3.546881483188342 | more sensitive |
| daporinad | NAMPT | -2.860954268773535 | more sensitive |
| BRD-K66532283 | HDAC1;HDAC2 | 3.85318394449896 | more resistant |
| ABT-737 | BCL2;BCL2L1;BCL2L2 | 3.898338443848557 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0012 - BRD-K02492147 on KMM1
*Evidence: SHAP-0012*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K02492147** (master_cpd_id=415688) |
| Gene Target | n/a |
| Mechanism / Activity | product of diversity oriented synthesis |
| Cell Line | **KMM1** (master_ccl_id=539) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | plasma cell myeloma |

### Response Summary
- Observed log10(IC50): **-3.8827**
- RF-predicted log10(IC50): **1.2029**
- Prediction error (observed - predicted): **-5.0856**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (14 pairs): mean=2.6261, q10=2.0348, median=3.1759, q90=3.6891, sample percentile=7.1
- Cell cohort (82 pairs): mean=1.2583, q10=-0.0603, median=1.3552, q90=2.5023, sample percentile=1.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.883 vs 20-NN mean=+1.723 (|Δ|=5.606)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.1425, |SHAP|=0.1425)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0876** (fingerprint_bit; SHAP=+0.1324, |SHAP|=0.1324)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
3. **fp_0535** (fingerprint_bit; SHAP=+0.1075, |SHAP|=0.1075)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.1030, |SHAP|=0.1030)  
  _value=0.8032, z=-1.44; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0071** (fingerprint_bit; SHAP=+0.0581, |SHAP|=0.0581)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
6. **fp_0994** (fingerprint_bit; SHAP=+0.0551, |SHAP|=0.0551)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **fp_0157** (fingerprint_bit; SHAP=+0.0544, |SHAP|=0.0544)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
8. **fp_0518** (fingerprint_bit; SHAP=+0.0515, |SHAP|=0.0515)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH23 | lung | 1.8790292329345704 | more sensitive |
| VCAP | prostate | 2.3983059754549383 | more sensitive |
| A172 | central nervous system | 3.765885245756405 | more resistant |
| RL | haematopoietic and lymphoid tissue | 3.9133899436317554 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dacarbazine |  | -1.7961304383751833 | more sensitive |
| I-BET151 | BRD2;BRD3;BRD4 | -1.4923436855898864 | more sensitive |
| AA-COCF3 | FAAH;PLA2G4A;PLA2G4B;PLA2G4C;PLA2G4D | 3.5310818491384994 | more resistant |
| isoevodiamine |  | 3.862214844368879 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0013 - SID 26681509 on OE21
*Evidence: SHAP-0013*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SID 26681509** (master_cpd_id=411731) |
| Gene Target | CTSL1 |
| Mechanism / Activity | inhibitor of cathepsin L |
| Cell Line | **OE21** (master_ccl_id=895) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.5324**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.5977**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (639 pairs): mean=1.7188, q10=0.8277, median=1.8833, q90=2.3218, sample percentile=0.5
- Cell cohort (289 pairs): mean=0.5505, q10=-1.3788, median=0.6558, q90=2.0115, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.532 vs 20-NN mean=+2.046 (|Δ|=5.579)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1232, |SHAP|=0.1232)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0899, |SHAP|=0.0899)  
  _value=4.1637, z=-0.36; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0858, |SHAP|=0.0858)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0673** (fingerprint_bit; SHAP=-0.0666, |SHAP|=0.0666)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0194, |SHAP|=0.0194)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0193, |SHAP|=0.0193)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0173, |SHAP|=0.0173)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0059** (fingerprint_bit; SHAP=+0.0160, |SHAP|=0.0160)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH1651 | lung | -3.904738626844117 | more sensitive |
| SKMM2 | haematopoietic and lymphoid tissue | -3.613996118177521 | more sensitive |
| SW1417 | large intestine | 3.417188750886764 | more resistant |
| REH | haematopoietic and lymphoid tissue | 3.8020088452360823 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| MLN2480 | ARAF;BRAF;RAF1 | -3.9662708776674194 | more sensitive |
| erlotinib | EGFR;ERBB2 | -2.996818123034092 | more sensitive |
| olaparib | PARP1;PARP2 | 3.473886149962343 | more resistant |
| navitoclax | BCL2;BCL2L1;BCL2L2 | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0014 - selumetinib on MINO
*Evidence: SHAP-0014*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **selumetinib** (master_cpd_id=348991) |
| Gene Target | MAP2K1;MAP2K2 |
| Mechanism / Activity | inhibitor of MEK1 and MEK2 |
| Cell Line | **MINO** (master_ccl_id=680) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | mantle cell lymphoma |

### Response Summary
- Observed log10(IC50): **-3.4912**
- RF-predicted log10(IC50): **0.6342**
- Prediction error (observed - predicted): **-4.1254**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (608 pairs): mean=1.4319, q10=-0.6183, median=1.8027, q90=2.7461, sample percentile=0.2
- Cell cohort (265 pairs): mean=0.1965, q10=-2.0380, median=0.4205, q90=1.7004, sample percentile=2.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.491 vs 20-NN mean=+2.044 (|Δ|=5.535)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2307, |SHAP|=0.2307)  
  _value=0.5607, z=-1.52; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0616, |SHAP|=0.0616)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0538** (fingerprint_bit; SHAP=-0.0433, |SHAP|=0.0433)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0258, |SHAP|=0.0258)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0187, |SHAP|=0.0187)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0176, |SHAP|=0.0176)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0015** (fingerprint_bit; SHAP=+0.0135, |SHAP|=0.0135)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CORL95 | lung | -2.7134906464211794 | more sensitive |
| HS766T | pancreas | -2.5246710451688696 | more sensitive |
| OSRC2 | kidney | 3.970585642807912 | more resistant |
| GOS3 | central nervous system | 3.979616542677832 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.670395694368224 | more sensitive |
| barasertib | AURKB | -3.5692621034187173 | more sensitive |
| BRD-K90370028 |  | 3.750833745973206 | more resistant |
| ML031 | S1PR2 | 3.8682354442821594 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0015 - quizartinib on T84
*Evidence: SHAP-0015*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **quizartinib** (master_cpd_id=640011) |
| Gene Target | FLT3 |
| Mechanism / Activity | inhibtor of VEGFR3 |
| Cell Line | **T84** (master_ccl_id=1176) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9353**
- RF-predicted log10(IC50): **0.8086**
- Prediction error (observed - predicted): **-4.7438**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (190 pairs): mean=1.4581, q10=-0.1039, median=1.6594, q90=2.9306, sample percentile=0.5
- Cell cohort (278 pairs): mean=0.3821, q10=-1.4540, median=0.5911, q90=1.7764, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.935 vs 20-NN mean=+1.591 (|Δ|=5.526)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.2274, |SHAP|=0.2274)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0235** (fingerprint_bit; SHAP=-0.0592, |SHAP|=0.0592)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: blebbistatin, pifithrin-alpha, ML162_
3. **fp_0673** (fingerprint_bit; SHAP=+0.0530, |SHAP|=0.0530)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0437, |SHAP|=0.0437)  
  _value=3.9419, z=-0.43; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0688** (fingerprint_bit; SHAP=+0.0370, |SHAP|=0.0370)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
6. **fp_0263** (fingerprint_bit; SHAP=+0.0265, |SHAP|=0.0265)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
7. **fp_0771** (fingerprint_bit; SHAP=+0.0228, |SHAP|=0.0228)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
8. **fp_0141** (fingerprint_bit; SHAP=+0.0211, |SHAP|=0.0211)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| UO31 |  | -3.802023156223623 | more sensitive |
| KMBC2 | urinary tract | -3.1189971794368985 | more sensitive |
| UACC62 | skin | 3.756854345886485 | more resistant |
| HSC2 | upper aerodigestive tract | 3.84716334458568 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K28456706 | HNF4A | -3.8035638981987687 | more sensitive |
| alisertib | AURKA;AURKB | -3.678246151459168 | more sensitive |
| BRD-M00053801 | BCL2 | 3.5942981482279355 | more resistant |
| AZD7545 | PDK2 | 3.9254311434583142 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0016 - bendamustine on SNU1105
*Evidence: SHAP-0016*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **bendamustine** (master_cpd_id=374755) |
| Gene Target | n/a |
| Mechanism / Activity | DNA alkylator |
| Cell Line | **SNU1105** (master_ccl_id=1083) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma Grade IV |

### Response Summary
- Observed log10(IC50): **-3.8863**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.9516**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (209 pairs): mean=1.5553, q10=0.8000, median=1.6879, q90=2.6456, sample percentile=0.5
- Cell cohort (148 pairs): mean=0.9312, q10=-0.9159, median=1.1409, q90=2.6083, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.886 vs 20-NN mean=+1.634 (|Δ|=5.520)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0875, |SHAP|=0.0875)  
  _value=9.8460, z=+1.47; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0643, |SHAP|=0.0643)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0482, |SHAP|=0.0482)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0366, |SHAP|=0.0366)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0173, |SHAP|=0.0173)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0142, |SHAP|=0.0142)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0139, |SHAP|=0.0139)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0105, |SHAP|=0.0105)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KHM1B | haematopoietic and lymphoid tissue | -3.057000315086881 | more sensitive |
| MOLP2 | haematopoietic and lymphoid tissue | -2.4784903811861323 | more sensitive |
| NCIH23 | lung | 3.630421747707613 | more resistant |
| RH18 | soft tissue | 3.783947045496244 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | -3.3271164238402773 | more sensitive |
| NVP-TAE684 | ALK | -2.8464854642751454 | more sensitive |
| BRD-K11533227 | HDAC1;HDAC2 | 3.744813146059926 | more resistant |
| lapatinib | EGFR;ERBB2 | 3.9404826432415136 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0017 - BRD-K26531177 on CAKI2
*Evidence: SHAP-0017*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K26531177** (master_cpd_id=42319) |
| Gene Target | n/a |
| Mechanism / Activity | analog of the natural product piperlongumine |
| Cell Line | **CAKI2** (master_ccl_id=110) |
| Tissue | kidney |
| Histology | carcinoma |
| Subtype | clear cell renal cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.6831**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.7484**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (708 pairs): mean=1.2033, q10=0.7467, median=1.2274, q90=1.9066, sample percentile=0.3
- Cell cohort (154 pairs): mean=1.2624, q10=-0.6030, median=1.5157, q90=2.7681, sample percentile=0.6
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.683 vs 20-NN mean=+1.825 (|Δ|=5.508)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0907, |SHAP|=0.0907)  
  _value=5.1659, z=-0.04; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0573, |SHAP|=0.0573)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0509, |SHAP|=0.0509)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0178, |SHAP|=0.0178)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0166, |SHAP|=0.0166)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0139, |SHAP|=0.0139)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0116, |SHAP|=0.0116)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0104, |SHAP|=0.0104)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| BICR18 | upper aerodigestive tract | -3.8558174284979754 | more sensitive |
| HCC366 | lung | -3.45413695004494 | more sensitive |
| RERFLCAD1 | lung | 2.575913672896687 | more resistant |
| MKN45 | stomach | 2.8729220754684794 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.165562776974251 | more sensitive |
| SB-743921 | KIF11 | -2.91752923057239 | more sensitive |
| LY-2183240 | FAAH | 3.862214844368879 | more resistant |
| B02 | RAD51 | 3.9826268426344713 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0018 - BCL-LZH-4 on SKNBE2
*Evidence: SHAP-0018*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BCL-LZH-4** (master_cpd_id=688516) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of BCL2, BCL-xL, and MCL1 |
| Cell Line | **SKNBE2** (master_ccl_id=1052) |
| Tissue | autonomic ganglia |
| Histology | neuroblastoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.7546**
- RF-predicted log10(IC50): **0.3465**
- Prediction error (observed - predicted): **-4.1011**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (11 pairs): mean=2.0392, q10=1.8932, median=2.3625, q90=3.5702, sample percentile=9.1
- Cell cohort (310 pairs): mean=0.4958, q10=-1.3925, median=0.6395, q90=1.9426, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.755 vs 20-NN mean=+1.748 (|Δ|=5.503)

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.3945, |SHAP|=0.3945)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.3590, |SHAP|=0.3590)  
  _value=2.3656, z=-0.94; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0501** (fingerprint_bit; SHAP=+0.0777, |SHAP|=0.0777)  
  _absent; representative SMARTS `[#6](-[#6@H])(=[#6])-[#6](-[#6@](-[#6])(-[#8])-[#6@@H])(-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: paclitaxel, myricetin, temozolomide_
4. **fp_0522** (fingerprint_bit; SHAP=+0.0703, |SHAP|=0.0703)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6])/[#6]=[#6](\[#6])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: manumycin A, 16-beta-bromoandrosterone, cyanoquinoline 11_
5. **fp_0087** (fingerprint_bit; SHAP=+0.0545, |SHAP|=0.0545)  
  _absent; representative SMARTS `[#6]:[#6](:[#6](:[#7]:[#6]):[#7]:[#6]):[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: simvastatin, lovastatin, ML031_
6. **fp_0539** (fingerprint_bit; SHAP=+0.0507, |SHAP|=0.0507)  
  _absent; representative SMARTS `[#16]-[#7](-[#6]-[#6]-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: CIL56, nilotinib, ML203_
7. **fp_0141** (fingerprint_bit; SHAP=+0.0486, |SHAP|=0.0486)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
8. **fp_0029** (fingerprint_bit; SHAP=+0.0420, |SHAP|=0.0420)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: sirolimus, vandetanib, BRD1835_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| JHUEM3 | endometrium | 1.8931776427307776 | more sensitive |
| MDAMB468 | breast | 1.968134111651109 | more sensitive |
| NCIH1623 | lung | 3.570215748574817 | more resistant |
| A204 | soft tissue | 3.693638046797049 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.635246001912999 | more sensitive |
| paclitaxel |  | -3.369057794894636 | more sensitive |
| pifithrin-alpha |  | 3.585267248358016 | more resistant |
| etomoxir | CPT1A | 3.747823446016566 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0019 - methotrexate on HCC1438
*Evidence: SHAP-0019*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **methotrexate** (master_cpd_id=30371) |
| Gene Target | DHFR |
| Mechanism / Activity | inhibitor of dihydrofolate reductase |
| Cell Line | **HCC1438** (master_ccl_id=303) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | large cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.8948**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-4.9553**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (405 pairs): mean=-1.8462, q10=-3.0528, median=-1.9884, q90=-0.8495, sample percentile=1.0
- Cell cohort (276 pairs): mean=0.8244, q10=-1.2953, median=1.1148, q90=2.3449, sample percentile=0.4
- Interpretation: **more sensitive than the model predicted**
- Selection reason: curated outlier: observed log10(IC50)=-3.895 vs 20-NN mean=+1.590 (|Δ|=5.485)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1020, |SHAP|=0.1020)  
  _value=9.8768, z=+1.48; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0665, |SHAP|=0.0665)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0493, |SHAP|=0.0493)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0194, |SHAP|=0.0194)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0173, |SHAP|=0.0173)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0133, |SHAP|=0.0133)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0538** (fingerprint_bit; SHAP=-0.0130, |SHAP|=0.0130)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| BEN | lung | -3.999197483447364 | more sensitive |
| MOLM16 | haematopoietic and lymphoid tissue | -3.9305472173264175 | more sensitive |
| NCIH1435 | lung | 2.9817021070517336 | more resistant |
| BECKER | central nervous system | 3.19693855395148 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GSK461364 | PLK1 | -3.239477687839769 | more sensitive |
| GMX-1778 | NAMPT | -3.161609110837368 | more sensitive |
| ML203 | PKM | 3.5371024490517797 | more resistant |
| Repligen 136 | HDAC3 | 3.651493847404092 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0020 - quizartinib on UO31
*Evidence: SHAP-0020*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **quizartinib** (master_cpd_id=640011) |
| Gene Target | FLT3 |
| Mechanism / Activity | inhibtor of VEGFR3 |
| Cell Line | **UO31** (master_ccl_id=1245) |
| Tissue | n/a |
| Histology | n/a |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.8020**
- RF-predicted log10(IC50): **0.8086**
- Prediction error (observed - predicted): **-4.6106**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (190 pairs): mean=1.4581, q10=-0.1039, median=1.6594, q90=2.9306, sample percentile=1.1
- Cell cohort (307 pairs): mean=0.4848, q10=-1.1888, median=0.6892, q90=1.8418, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.802 vs 20-NN mean=+1.677 (|Δ|=5.479)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.2440, |SHAP|=0.2440)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0673** (fingerprint_bit; SHAP=+0.0545, |SHAP|=0.0545)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
3. **fp_0235** (fingerprint_bit; SHAP=-0.0532, |SHAP|=0.0532)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: blebbistatin, pifithrin-alpha, ML162_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0459, |SHAP|=0.0459)  
  _value=9.2947, z=+1.29; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0688** (fingerprint_bit; SHAP=+0.0351, |SHAP|=0.0351)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
6. **fp_0263** (fingerprint_bit; SHAP=+0.0249, |SHAP|=0.0249)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
7. **fp_0771** (fingerprint_bit; SHAP=+0.0228, |SHAP|=0.0228)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
8. **fp_0141** (fingerprint_bit; SHAP=+0.0181, |SHAP|=0.0181)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| T84 | large intestine | -3.935260294073839 | more sensitive |
| KMBC2 | urinary tract | -3.1189971794368985 | more sensitive |
| UACC62 | skin | 3.756854345886485 | more resistant |
| HSC2 | upper aerodigestive tract | 3.84716334458568 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GDC-0941 | PIK3CA;PIK3CB;PIK3CD;PIK3CG | -3.413680150829547 | more sensitive |
| BMS-754807 | IGF1R | -3.3951486458790234 | more sensitive |
| BRD-K04800985 |  | 3.392608051133068 | more resistant |
| Repligen 136 | HDAC3 | 3.967575342851272 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0021 - paclitaxel on HCC1171
*Evidence: SHAP-0021*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **paclitaxel** (master_cpd_id=26956) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **HCC1171** (master_ccl_id=296) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | non small cell carcinoma |

### Response Summary
- Observed log10(IC50): **3.8291**
- RF-predicted log10(IC50): **-0.0718**
- Prediction error (observed - predicted): **+3.9009**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (316 pairs): mean=-2.2562, q10=-3.6252, median=-2.8177, q90=1.1135, sample percentile=100.0
- Cell cohort (155 pairs): mean=1.3931, q10=-0.1987, median=1.4449, q90=2.9314, sample percentile=98.7
- Interpretation: **more resistant than the model predicted**
- Selection reason: curated outlier: observed log10(IC50)=+3.829 vs 20-NN mean=-1.640 (|Δ|=5.469)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.9918, |SHAP|=0.9918)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0997** (fingerprint_bit; SHAP=-0.4692, |SHAP|=0.4692)  
  _present; representative SMARTS `[#7]:[#6](:[#6]):[#6]:[#6]:[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: Bax channel blocker, teniposide, methotrexate_
3. **SLFN13 (146857)** (gene_expression; SHAP=+0.1158, |SHAP|=0.1158)  
  _value=7.1811, z=+2.08; markedly above the cross-cell-line mean; recurs in 14 predictable-drug RF signatures_
4. **CST6 (1474)** (gene_expression; SHAP=+0.1137, |SHAP|=0.1137)  
  _value=9.1376, z=+2.97; markedly above the cross-cell-line mean; recurs in 8 predictable-drug RF signatures_
5. **fp_0963** (fingerprint_bit; SHAP=-0.0826, |SHAP|=0.0826)  
  _present; representative SMARTS `[#6]-[#7]-[#7]-[#6]-[#6]`; present in 0.8% of CTRPv2 compounds; example compounds: procarbazine, KU 0060648, vorapaxar_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0777, |SHAP|=0.0777)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0472, |SHAP|=0.0472)  
  _value=7.6870, z=+0.78; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **CLDN4 (1364)** (gene_expression; SHAP=+0.0422, |SHAP|=0.0422)  
  _value=9.4233, z=+1.52; above the cross-cell-line mean; recurs in 9 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HT1080 | soft tissue | -3.99055223825201 | more sensitive |
| PANC1005 | pancreas | -3.985570834111101 | more sensitive |
| KATOIII | stomach | 3.5942981482279355 | more resistant |
| CAPAN1 | pancreas | 3.771905845669684 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| NSC48300 | TASP1 | -2.628968950100088 | more sensitive |
| dasatinib | EPHA2;KIT;LCK;SRC;YES1 | -2.5501534388564475 | more sensitive |
| tipifarnib-P2 | FNTA | 3.8652251443255183 | more resistant |
| XL765 | MTOR;PIK3CA;PIK3CB;PIK3CD;PIK3CG;PRKDC | 3.967575342851272 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0022 - paclitaxel on CAPAN1
*Evidence: SHAP-0022*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **paclitaxel** (master_cpd_id=26956) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **CAPAN1** (master_ccl_id=128) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **3.7719**
- RF-predicted log10(IC50): **0.4978**
- Prediction error (observed - predicted): **+3.2741**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (316 pairs): mean=-2.2562, q10=-3.6252, median=-2.8177, q90=1.1135, sample percentile=99.7
- Cell cohort (192 pairs): mean=0.8960, q10=-1.0080, median=1.1596, q90=2.4037, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=+3.772 vs 20-NN mean=-1.695 (|Δ|=5.467)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.8968, |SHAP|=0.8968)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0997** (fingerprint_bit; SHAP=-0.4316, |SHAP|=0.4316)  
  _present; representative SMARTS `[#7]:[#6](:[#6]):[#6]:[#6]:[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: Bax channel blocker, teniposide, methotrexate_
3. **PLAT (5327)** (gene_expression; SHAP=+0.1348, |SHAP|=0.1348)  
  _value=9.2913, z=+2.42; markedly above the cross-cell-line mean; recurs in 19 predictable-drug RF signatures_
4. **fp_0535** (fingerprint_bit; SHAP=+0.1036, |SHAP|=0.1036)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
5. **SLFN13 (146857)** (gene_expression; SHAP=+0.0980, |SHAP|=0.0980)  
  _value=6.4028, z=+1.71; above the cross-cell-line mean; recurs in 14 predictable-drug RF signatures_
6. **CXCL5 (6374)** (gene_expression; SHAP=+0.0882, |SHAP|=0.0882)  
  _value=10.4311, z=+3.82; markedly above the cross-cell-line mean; recurs in 6 predictable-drug RF signatures_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0471, |SHAP|=0.0471)  
  _value=5.2412, z=-0.01; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **PLAAT3 (11145)** (gene_expression; SHAP=+0.0465, |SHAP|=0.0465)  
  _value=8.8760, z=+2.23; markedly above the cross-cell-line mean; recurs in 29 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HT1080 | soft tissue | -3.99055223825201 | more sensitive |
| PANC1005 | pancreas | -3.985570834111101 | more sensitive |
| KATOIII | stomach | 3.5942981482279355 | more resistant |
| HCC1171 | lung | 3.829101544845841 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| WP1130 | UCHL5;USP14;USP5;USP9X | -3.3044515538094448 | more sensitive |
| leptomycin B | XPO1 | -3.215917865022645 | more sensitive |
| TG-100-115 | PIK3CD;PIK3CG | 3.5792466484447365 | more resistant |
| BRD-K11533227 | HDAC1;HDAC2 | 3.654504147360732 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0023 - BRD-K50799972 on BT474
*Evidence: SHAP-0023*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K50799972** (master_cpd_id=596868) |
| Gene Target | n/a |
| Mechanism / Activity | product of diversity oriented synthesis |
| Cell Line | **BT474** (master_ccl_id=97) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **-3.6154**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.6806**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (419 pairs): mean=1.7359, q10=1.2988, median=1.6936, q90=2.2112, sample percentile=0.2
- Cell cohort (177 pairs): mean=0.4388, q10=-1.8164, median=0.7803, q90=1.9324, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.615 vs 20-NN mean=+1.822 (|Δ|=5.437)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0906, |SHAP|=0.0906)  
  _value=3.8151, z=-0.47; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0591, |SHAP|=0.0591)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0517, |SHAP|=0.0517)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0201, |SHAP|=0.0201)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0196, |SHAP|=0.0196)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0792** (fingerprint_bit; SHAP=+0.0142, |SHAP|=0.0142)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0137, |SHAP|=0.0137)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0788** (fingerprint_bit; SHAP=-0.0132, |SHAP|=0.0132)  
  _present; representative SMARTS `[#6]:[#6](-[#6]):[#6]:[#7](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: betulinic acid, CI-976, SRT-1720_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| GDM1 | haematopoietic and lymphoid tissue | -2.871487017593491 | more sensitive |
| NCIH889 | lung | -2.7579386323996937 | more sensitive |
| NCIH2141 | lung | 3.823080944932561 | more resistant |
| HEL | haematopoietic and lymphoid tissue | 3.907369343718476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.6906277468404096 | more sensitive |
| GMX-1778 | NAMPT | -3.50649312399761 | more sensitive |
| IPR-456 | PLAUR | 2.913669328031674 | more resistant |
| C6-ceramide | MAPK1;PPP2CA;UGCG | 3.708689546580248 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0024 - NSC95397 on J82
*Evidence: SHAP-0024*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC95397** (master_cpd_id=50715) |
| Gene Target | CDC25A;CDC25B;CDC25C |
| Mechanism / Activity | inhibitor of cell division cycle 25 phosphatase (CDC25) |
| Cell Line | **J82** (master_ccl_id=482) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.8956**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.9608**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (592 pairs): mean=1.1187, q10=0.3858, median=1.1880, q90=1.7540, sample percentile=0.3
- Cell cohort (220 pairs): mean=1.0517, q10=-0.7724, median=1.3509, q90=2.4068, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.896 vs 20-NN mean=+1.537 (|Δ|=5.433)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0896, |SHAP|=0.0896)  
  _value=9.9459, z=+1.50; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0585, |SHAP|=0.0585)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0490, |SHAP|=0.0490)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0184, |SHAP|=0.0184)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0156, |SHAP|=0.0156)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0149, |SHAP|=0.0149)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0144, |SHAP|=0.0144)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0110, |SHAP|=0.0110)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AM38 | central nervous system | -3.9926719220155897 | more sensitive |
| HT1080 | soft tissue | -2.502253872228975 | more sensitive |
| NCIH1792 | lung | 3.2631651529975563 | more resistant |
| LOUNH91 | lung | 3.624401147794333 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| methotrexate | DHFR | -3.4835730063885526 | more sensitive |
| leptomycin B | XPO1 | -3.144335781767539 | more sensitive |
| SB-525334 | TGFBR1 | 3.8802766441087178 | more resistant |
| neuronal differentiation inducer III |  | 3.922420843501675 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0025 - IPR-456 on HCC4006
*Evidence: SHAP-0025*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **IPR-456** (master_cpd_id=660084) |
| Gene Target | PLAUR |
| Mechanism / Activity | inhibitor of the interaction of urokinase receptor with binding partners |
| Cell Line | **HCC4006** (master_ccl_id=331) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9826**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0479**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (205 pairs): mean=2.0430, q10=1.2680, median=1.9594, q90=3.0500, sample percentile=0.5
- Cell cohort (253 pairs): mean=0.6185, q10=-1.2145, median=0.7713, q90=2.0282, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: curated outlier: observed log10(IC50)=-3.983 vs 20-NN mean=+1.448 (|Δ|=5.431)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1401, |SHAP|=0.1401)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0017** (fingerprint_bit; SHAP=+0.1267, |SHAP|=0.1267)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **CCN1 (3491)** (gene_expression; SHAP=+0.0903, |SHAP|=0.0903)  
  _value=6.9630, z=+0.54; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0673** (fingerprint_bit; SHAP=-0.0681, |SHAP|=0.0681)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0876** (fingerprint_bit; SHAP=-0.0542, |SHAP|=0.0542)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0181, |SHAP|=0.0181)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0175, |SHAP|=0.0175)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0159, |SHAP|=0.0159)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH446 | lung | -2.751888202681307 | more sensitive |
| HCC15 | lung | -0.6589122771656536 | more sensitive |
| SKMEL30 | skin | 3.889307543978637 | more resistant |
| NCIH1869 | lung | 3.937472343284874 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| NVP-231 | CERK | -3.858002112755049 | more sensitive |
| nakiterpiosin |  | -3.724721518079516 | more sensitive |
| MLN2480 | ARAF;BRAF;RAF1 | 3.6364423476208927 | more resistant |
| EX-527 | SIRT1 | 3.8321118448024807 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0026 - NSC48300 on OVSAHO
*Evidence: SHAP-0026*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC48300** (master_cpd_id=594399) |
| Gene Target | TASP1 |
| Mechanism / Activity | inhibitor of threonine endopeptidase taspase 1 |
| Cell Line | **OVSAHO** (master_ccl_id=915) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **1.7174**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.6521**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (559 pairs): mean=1.4488, q10=0.5444, median=1.6123, q90=2.0170, sample percentile=63.1
- Cell cohort (171 pairs): mean=0.9967, q10=-0.7909, median=1.1541, q90=2.3742, sample percentile=70.8
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.717 matches 20-NN mean=+1.717 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1313, |SHAP|=0.1313)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0882, |SHAP|=0.0882)  
  _value=5.3614, z=+0.03; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0673** (fingerprint_bit; SHAP=-0.0702, |SHAP|=0.0702)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0141** (fingerprint_bit; SHAP=+0.0668, |SHAP|=0.0668)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0374, |SHAP|=0.0374)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0184, |SHAP|=0.0184)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0167, |SHAP|=0.0167)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0146, |SHAP|=0.0146)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HCC1171 | lung | -2.628968950100088 | more sensitive |
| BL70 | haematopoietic and lymphoid tissue | -1.203008050206645 | more sensitive |
| EKVX |  | 3.645473247490812 | more resistant |
| HCC2279 | lung | 3.6725659471005705 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| austocystin D |  | -2.675648698697982 | more sensitive |
| afatinib | EGFR;ERBB2 | -2.5003804508095504 | more sensitive |
| vorapaxar | F2R | 3.624401147794333 | more resistant |
| bleomycin A2 |  | 3.823080944932561 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0027 - BRD-K70511574 on REH
*Evidence: SHAP-0027*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K70511574** (master_cpd_id=648987) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **REH** (master_ccl_id=965) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic B cell leukaemia |

### Response Summary
- Observed log10(IC50): **-0.3763**
- RF-predicted log10(IC50): **0.6141**
- Prediction error (observed - predicted): **-0.9904**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (518 pairs): mean=-0.3537, q10=-1.2769, median=-0.4447, q90=0.6348, sample percentile=57.3
- Cell cohort (200 pairs): mean=0.3162, q10=-1.9230, median=0.5421, q90=1.8845, sample percentile=24.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=-0.376 matches 20-NN mean=-0.376 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2031, |SHAP|=0.2031)  
  _value=0.7411, z=-1.46; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0259** (fingerprint_bit; SHAP=-0.1152, |SHAP|=0.1152)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6]-[#6]-[#6]`; present in 3.3% of CTRPv2 compounds; example compounds: tretinoin, BRD-A94377914, Ki8751_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0783, |SHAP|=0.0783)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0282, |SHAP|=0.0282)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0093** (fingerprint_bit; SHAP=-0.0238, |SHAP|=0.0238)  
  _present; representative SMARTS `[#6]-[#7](-[#6]-[#6]-[#6])-[#6]`; present in 0.2% of CTRPv2 compounds; example compounds: blebbistatin_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0181, |SHAP|=0.0181)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0169, |SHAP|=0.0169)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0155, |SHAP|=0.0155)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| TE4 | oesophagus | -3.908907792264956 | more sensitive |
| 786O | kidney | -3.8988958963353424 | more sensitive |
| ASPC1 | pancreas | 3.922420843501675 | more resistant |
| TT2609C02 | thyroid | 3.9404826432415136 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| PF-184 | IKBKB | -3.676939394929354 | more sensitive |
| BI-2536 | PLK1 | -3.451427880106218 | more sensitive |
| SID 26681509 | CTSL1 | 3.8020088452360823 | more resistant |
| PD 153035 | EGFR | 3.811039745106002 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0028 - TPCA-1 on SW579
*Evidence: SHAP-0028*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **TPCA-1** (master_cpd_id=375564) |
| Gene Target | IKBKB |
| Mechanism / Activity | inhibitor of IKK-2 |
| Cell Line | **SW579** (master_ccl_id=1165) |
| Tissue | thyroid |
| Histology | carcinoma |
| Subtype | anaplastic carcinoma |

### Response Summary
- Observed log10(IC50): **1.1782**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.1130**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (622 pairs): mean=0.8937, q10=0.1374, median=0.7620, q90=1.8023, sample percentile=62.1
- Cell cohort (312 pairs): mean=0.6372, q10=-1.1328, median=0.7578, q90=2.0140, sample percentile=63.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.178 matches 20-NN mean=+1.178 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0918, |SHAP|=0.0918)  
  _value=7.3587, z=+0.67; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0485, |SHAP|=0.0485)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0307, |SHAP|=0.0307)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0792** (fingerprint_bit; SHAP=+0.0204, |SHAP|=0.0204)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0202, |SHAP|=0.0202)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0178, |SHAP|=0.0178)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0176, |SHAP|=0.0176)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0158, |SHAP|=0.0158)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SW948 | large intestine | -3.673258872758358 | more sensitive |
| KP4 | pancreas | -2.954306633724237 | more sensitive |
| ZR7530 | breast | 3.019330856509731 | more resistant |
| NCIH2291 | lung | 3.025351456423011 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.973595942764552 | more sensitive |
| SNS-032 | CDK16;CDK17;CDK2;CDK7;CDK9;CDKL5 | -3.713134461319725 | more sensitive |
| necrostatin-1 | RIPK1 | 2.966263457101701 | more resistant |
| IPR-456 | PLAUR | 3.0373926562495703 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0029 - GDC-0941 on HEC151
*Evidence: SHAP-0029*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GDC-0941** (master_cpd_id=639759) |
| Gene Target | PIK3CA;PIK3CB;PIK3CD;PIK3CG |
| Mechanism / Activity | inhibitor of PI3K kinase activity |
| Cell Line | **HEC151** (master_ccl_id=351) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **0.3712**
- RF-predicted log10(IC50): **0.7356**
- Prediction error (observed - predicted): **-0.3644**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (723 pairs): mean=0.4149, q10=-0.4712, median=0.3972, q90=1.4242, sample percentile=47.9
- Cell cohort (286 pairs): mean=0.6392, q10=-1.1066, median=0.8954, q90=1.7917, sample percentile=32.9
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+0.371 matches 20-NN mean=+0.371 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.3249, |SHAP|=0.3249)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1659, |SHAP|=0.1659)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0673** (fingerprint_bit; SHAP=+0.0573, |SHAP|=0.0573)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0518** (fingerprint_bit; SHAP=-0.0568, |SHAP|=0.0568)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0467, |SHAP|=0.0467)  
  _value=8.0520, z=+0.89; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0342, |SHAP|=0.0342)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0876** (fingerprint_bit; SHAP=-0.0320, |SHAP|=0.0320)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
8. **fp_0455** (fingerprint_bit; SHAP=-0.0268, |SHAP|=0.0268)  
  _present; representative SMARTS `[#6]:[#6](-[#6]-[#7](:[#6]):[#6]):[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BRD-K94991378, SCH-79797, zebularine_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| UO31 |  | -3.413680150829547 | more sensitive |
| NCIH810 | lung | -3.389334789305277 | more sensitive |
| SNU869 | biliary tract | 3.648483547447452 | more resistant |
| JL1 | pleura | 3.783947045496244 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.681061680690678 | more sensitive |
| PIK-93 | PIK3CG | -3.6255826691711626 | more sensitive |
| JW-480 | NCEH1 | 3.747823446016566 | more resistant |
| BRD-M00053801 | BCL2 | 3.8329508006346407 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0030 - Mdivi-1 on SNU1077
*Evidence: SHAP-0030*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **Mdivi-1** (master_cpd_id=215497) |
| Gene Target | DNM1 |
| Mechanism / Activity | inhibitor of dynamin 1; inhibitor of mitrochondrial division inhibitor |
| Cell Line | **SNU1077** (master_ccl_id=1081) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | carcinosarcoma; malignant mesodermal mixed tumor |

### Response Summary
- Observed log10(IC50): **1.4292**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.3639**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (570 pairs): mean=1.5127, q10=0.8771, median=1.6531, q90=2.0233, sample percentile=31.6
- Cell cohort (190 pairs): mean=1.0830, q10=-0.4460, median=1.2754, q90=2.1650, sample percentile=60.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.429 matches 20-NN mean=+1.429 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0901, |SHAP|=0.0901)  
  _value=8.7536, z=+1.12; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0802, |SHAP|=0.0802)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0573, |SHAP|=0.0573)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0166, |SHAP|=0.0166)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0156, |SHAP|=0.0156)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0994** (fingerprint_bit; SHAP=-0.0133, |SHAP|=0.0133)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0124, |SHAP|=0.0124)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0600** (fingerprint_bit; SHAP=+0.0121, |SHAP|=0.0121)  
  _present; representative SMARTS `[#6]:[#6](:[#7]):[#7]`; present in 5.0% of CTRPv2 compounds; example compounds: methotrexate, C6-ceramide, cerulenin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| JHOS2 | ovary | -3.98642689815921 | more sensitive |
| KM12 | large intestine | -3.468138115563649 | more sensitive |
| CALU1 | lung | 3.6996586467103287 | more resistant |
| KLE | endometrium | 3.7989985452794426 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| bortezomib | PSMB1;PSMB2;PSMB5;PSMD1;PSMD2 | -2.0647478598230564 | more sensitive |
| afatinib | EGFR;ERBB2 | -1.962182144440085 | more sensitive |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 3.269185752910836 | more resistant |
| PLX-4032 | BRAF | 3.6906277468404096 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0031 - triptolide on RCHACV
*Evidence: SHAP-0031*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **triptolide** (master_cpd_id=411720) |
| Gene Target | n/a |
| Mechanism / Activity | natural product; inhibitor of RNA polymerase II |
| Cell Line | **RCHACV** (master_ccl_id=958) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic B cell leukaemia |

### Response Summary
- Observed log10(IC50): **-1.7926**
- RF-predicted log10(IC50): **-1.9440**
- Prediction error (observed - predicted): **+0.1514**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (714 pairs): mean=-1.7543, q10=-2.2877, median=-1.7729, q90=-1.1643, sample percentile=48.5
- Cell cohort (298 pairs): mean=0.3523, q10=-1.5451, median=0.5799, q90=1.6180, sample percentile=8.4
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=-1.793 matches 20-NN mean=-1.792 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-1.2672, |SHAP|=1.2672)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.7396, |SHAP|=0.7396)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0093** (fingerprint_bit; SHAP=-0.2296, |SHAP|=0.2296)  
  _present; representative SMARTS `[#6]-[#7](-[#6]-[#6]-[#6])-[#6]`; present in 0.2% of CTRPv2 compounds; example compounds: blebbistatin_
4. **fp_0767** (fingerprint_bit; SHAP=-0.1662, |SHAP|=0.1662)  
  _present; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
5. **CCN1 (3491)** (gene_expression; SHAP=-0.1020, |SHAP|=0.1020)  
  _value=0.8577, z=-1.43; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0761** (fingerprint_bit; SHAP=-0.0794, |SHAP|=0.0794)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_
7. **fp_0799** (fingerprint_bit; SHAP=-0.0552, |SHAP|=0.0552)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: ciclopirox, blebbistatin, pifithrin-alpha_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0298, |SHAP|=0.0298)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| L1236 | haematopoietic and lymphoid tissue | -3.938242791603693 | more sensitive |
| OVCAR5 |  | -3.800585077774668 | more sensitive |
| HCC1171 | lung | 0.4346873137387888 | more resistant |
| HCC1937 | breast | 0.7423399693073777 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.9815237471543328 | more sensitive |
| SNX-2112 | HSP90AA1;HSP90B1 | -3.8268611950734592 | more sensitive |
| NVP-231 | CERK | 2.928419797819209 | more resistant |
| STF-31 | NAMPT | 3.1608149544718027 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0032 - leptomycin B on MDAMB361
*Evidence: SHAP-0032*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **leptomycin B** (master_cpd_id=660086) |
| Gene Target | XPO1 |
| Mechanism / Activity | inhibitor of exportin 1 |
| Cell Line | **MDAMB361** (master_ccl_id=651) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **0.9293**
- RF-predicted log10(IC50): **-0.8999**
- Prediction error (observed - predicted): **+1.8291**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (617 pairs): mean=-2.4358, q10=-3.5008, median=-2.7645, q90=-0.6506, sample percentile=94.8
- Cell cohort (208 pairs): mean=0.8201, q10=-0.9075, median=1.0071, q90=2.1534, sample percentile=47.6
- Interpretation: **more resistant than the model predicted**
- Selection reason: curated normal: observed log10(IC50)=+0.929 matches 20-NN mean=+0.929 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0071** (fingerprint_bit; SHAP=-1.0157, |SHAP|=1.0157)  
  _present; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
2. **fp_0141** (fingerprint_bit; SHAP=-0.9128, |SHAP|=0.9128)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **EPN3 (55040)** (gene_expression; SHAP=+0.1730, |SHAP|=0.1730)  
  _value=7.9143, z=+3.15; markedly above the cross-cell-line mean; recurs in 11 predictable-drug RF signatures_
4. **fp_0925** (fingerprint_bit; SHAP=-0.1349, |SHAP|=0.1349)  
  _present; representative SMARTS `[#6]:[#6](:[#6](-[#6]):[#6]:[#6])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: gossypol, isoliquiritigenin, mitomycin_
5. **fp_0535** (fingerprint_bit; SHAP=-0.1128, |SHAP|=0.1128)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0017** (fingerprint_bit; SHAP=-0.0895, |SHAP|=0.0895)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
7. **SELENOP (6414)** (gene_expression; SHAP=+0.0870, |SHAP|=0.0870)  
  _value=7.8055, z=+2.47; markedly above the cross-cell-line mean; recurs in 22 predictable-drug RF signatures_
8. **IGFBP5 (3488)** (gene_expression; SHAP=+0.0827, |SHAP|=0.0827)  
  _value=8.1452, z=+2.13; markedly above the cross-cell-line mean; recurs in 16 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RCHACV | haematopoietic and lymphoid tissue | -3.9815237471543328 | more sensitive |
| MOLM16 | haematopoietic and lymphoid tissue | -3.9519264960551865 | more sensitive |
| NCIH441 | lung | 3.6906277468404096 | more resistant |
| SNU489 | central nervous system | 3.8652251443255183 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.136732554818684 | more sensitive |
| bafilomycin A1 | ATP6V0A1 | -2.552319534204732 | more sensitive |
| PD318088 | MAP2K1;MAP2K2 | 3.639452647577533 | more resistant |
| AGK-2 | SIRT2 | 3.708689546580248 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0033 - nakiterpiosin on ST486
*Evidence: SHAP-0033*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **nakiterpiosin** (master_cpd_id=417452) |
| Gene Target | n/a |
| Mechanism / Activity | natural product; inhibitor of microtubule assembly |
| Cell Line | **ST486** (master_ccl_id=1137) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **-0.4684**
- RF-predicted log10(IC50): **-0.5380**
- Prediction error (observed - predicted): **+0.0696**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (545 pairs): mean=-0.4462, q10=-1.1195, median=-0.4672, q90=0.1580, sample percentile=49.9
- Cell cohort (297 pairs): mean=0.2747, q10=-1.5273, median=0.4403, q90=1.6784, sample percentile=22.9
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=-0.468 matches 20-NN mean=-0.468 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.8209, |SHAP|=0.8209)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.4848, |SHAP|=0.4848)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0767** (fingerprint_bit; SHAP=+0.1600, |SHAP|=0.1600)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.1090, |SHAP|=0.1090)  
  _value=2.3513, z=-0.94; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0747, |SHAP|=0.0747)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0912** (fingerprint_bit; SHAP=+0.0541, |SHAP|=0.0541)  
  _absent; representative SMARTS `[#6]-[#6](-[#7]-[#6])-[#6](:[#6]):[#6]`; present in 1.5% of CTRPv2 compounds; example compounds: importazole, itraconazole, necrostatin-1_
7. **fp_0974** (fingerprint_bit; SHAP=+0.0472, |SHAP|=0.0472)  
  _absent; representative SMARTS `[#7]-[#6]-[#6]-[#6]-[#6]`; present in 7.5% of CTRPv2 compounds; example compounds: parbendazole, importazole, tacrolimus_
8. **fp_0582** (fingerprint_bit; SHAP=-0.0446, |SHAP|=0.0446)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| 253J | urinary tract | -3.804376274073242 | more sensitive |
| HCC4006 | lung | -3.724721518079516 | more sensitive |
| JHUEM3 | endometrium | 2.577117792879343 | more resistant |
| NCIH2342 | lung | 3.350463851740111 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| AM-580 | RARA | -3.8097008064442015 | more sensitive |
| oligomycin A | ATP5L2 | -3.756854345886485 | more sensitive |
| quizartinib | FLT3 | 2.928720827814873 | more resistant |
| NSC 74859 | STAT3 | 2.989912892811798 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0034 - KHS101 on SNUC2A
*Evidence: SHAP-0034*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KHS101** (master_cpd_id=660819) |
| Gene Target | TACC3 |
| Mechanism / Activity | binder of TACC3, a component of the centrosome and mitotic spindle |
| Cell Line | **SNUC2A** (master_ccl_id=1131) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **1.2904**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.2251**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (731 pairs): mean=1.1002, q10=0.6278, median=1.1435, q90=1.5357, sample percentile=67.9
- Cell cohort (198 pairs): mean=0.7010, q10=-1.2917, median=0.9370, q90=2.1852, sample percentile=64.6
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.290 matches 20-NN mean=+1.290 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0889, |SHAP|=0.0889)  
  _value=5.5362, z=+0.08; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0610, |SHAP|=0.0610)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0488, |SHAP|=0.0488)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0191, |SHAP|=0.0191)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0161, |SHAP|=0.0161)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0105, |SHAP|=0.0105)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CJM | skin | -1.6852433943383844 | more sensitive |
| SNU423 | liver | -1.5840387345793867 | more sensitive |
| MC116 | haematopoietic and lymphoid tissue | 3.2541342531276367 | more resistant |
| AMO1 | haematopoietic and lymphoid tissue | 3.84716334458568 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| cerulenin | FASN;HMGCS1 | -3.965693246914807 | more sensitive |
| Mdivi-1 | DNM1 | -2.557121586232295 | more sensitive |
| BRD-K13999467 |  | 3.877266344152078 | more resistant |
| barasertib | AURKB | 3.934462043328234 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0035 - SNS-032 on GSS
*Evidence: SHAP-0035*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SNS-032** (master_cpd_id=606254) |
| Gene Target | CDK16;CDK17;CDK2;CDK7;CDK9;CDKL5 |
| Mechanism / Activity | inhibitor of cyclin-dependent kinases |
| Cell Line | **GSS** (master_ccl_id=285) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-0.8609**
- RF-predicted log10(IC50): **0.4265**
- Prediction error (observed - predicted): **-1.2874**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (560 pairs): mean=-0.8552, q10=-1.8176, median=-0.7183, q90=-0.0367, sample percentile=41.1
- Cell cohort (281 pairs): mean=0.3723, q10=-1.0870, median=0.5845, q90=1.6539, sample percentile=14.9
- Interpretation: **more sensitive than the model predicted**
- Selection reason: curated normal: observed log10(IC50)=-0.861 matches 20-NN mean=-0.861 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0235** (fingerprint_bit; SHAP=-0.1440, |SHAP|=0.1440)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: blebbistatin, pifithrin-alpha, ML162_
2. **fp_0059** (fingerprint_bit; SHAP=-0.1285, |SHAP|=0.1285)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
3. **fp_0065** (fingerprint_bit; SHAP=-0.0482, |SHAP|=0.0482)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
4. **fp_0538** (fingerprint_bit; SHAP=-0.0406, |SHAP|=0.0406)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_
5. **fp_0726** (fingerprint_bit; SHAP=-0.0302, |SHAP|=0.0302)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]`; present in 84.2% of CTRPv2 compounds; example compounds: CIL55, BRD4132, BRD6340_
6. **fp_0227** (fingerprint_bit; SHAP=-0.0274, |SHAP|=0.0274)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0159, |SHAP|=0.0159)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNU620 | stomach | -3.929547414946706 | more sensitive |
| BICR31 | upper aerodigestive tract | -3.895154187941655 | more sensitive |
| KPNYN | autonomic ganglia | 2.296256806924849 | more resistant |
| PATU8988T | pancreas | 2.6782638714224407 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ELCPK |  | -3.9878297843714425 | more sensitive |
| AM-580 | RARA | -3.818258490491944 | more sensitive |
| darinaparsin |  | 3.377556551349869 | more resistant |
| cimetidine | HRH2 | 3.877266344152078 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0036 - bosutinib on FADU
*Evidence: SHAP-0036*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **bosutinib** (master_cpd_id=660346) |
| Gene Target | ABL1;SRC |
| Mechanism / Activity | inhibitor of SRC and ABL1 |
| Cell Line | **FADU** (master_ccl_id=255) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **0.7700**
- RF-predicted log10(IC50): **0.6762**
- Prediction error (observed - predicted): **+0.0937**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (721 pairs): mean=0.6329, q10=0.0105, median=0.6756, q90=1.2069, sample percentile=60.3
- Cell cohort (285 pairs): mean=0.9919, q10=-0.7281, median=1.2876, q90=2.2131, sample percentile=34.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+0.770 matches 20-NN mean=+0.770 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.3520, |SHAP|=0.3520)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1285, |SHAP|=0.1285)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0876** (fingerprint_bit; SHAP=-0.0503, |SHAP|=0.0503)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
4. **fp_0673** (fingerprint_bit; SHAP=+0.0488, |SHAP|=0.0488)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0468, |SHAP|=0.0468)  
  _value=5.4549, z=+0.06; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0338, |SHAP|=0.0338)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0771** (fingerprint_bit; SHAP=-0.0238, |SHAP|=0.0238)  
  _present; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
8. **fp_0263** (fingerprint_bit; SHAP=+0.0225, |SHAP|=0.0225)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SKM1 | haematopoietic and lymphoid tissue | -3.768898594516729 | more sensitive |
| HPAC | pancreas | -3.3151189695879046 | more sensitive |
| AGS | stomach | 3.251123953170997 | more resistant |
| CAMA1 | breast | 3.443783150395945 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.868222271064546 | more sensitive |
| ML050 | GPER1 | -3.451550949443244 | more sensitive |
| BRD-K42260513 | EZH2 | 3.491947949702182 | more resistant |
| GSK525762A | BRD2;BRD3;BRD4 | 3.892317843935277 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0037 - NSC23766 on A172
*Evidence: SHAP-0037*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC23766** (master_cpd_id=44503) |
| Gene Target | RAC1;TIAM1;TRIO |
| Mechanism / Activity | inhibitor of RAC1-GEF interaction; prevents Rac1 activation by Rac-specific guanine nucleotide exchange factors (GEFs) TrioN and Tiam1 |
| Cell Line | **A172** (master_ccl_id=25) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma Grade IV |

### Response Summary
- Observed log10(IC50): **1.2481**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.1828**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (704 pairs): mean=1.9744, q10=1.2117, median=2.1603, q90=2.8314, sample percentile=11.1
- Cell cohort (219 pairs): mean=0.7385, q10=-1.2320, median=0.9443, q90=2.2073, sample percentile=62.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.248 matches 20-NN mean=+1.248 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0866, |SHAP|=0.0866)  
  _value=7.3990, z=+0.68; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0863, |SHAP|=0.0863)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0361, |SHAP|=0.0361)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0360, |SHAP|=0.0360)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0263** (fingerprint_bit; SHAP=-0.0299, |SHAP|=0.0299)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0183, |SHAP|=0.0183)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0158, |SHAP|=0.0158)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0134, |SHAP|=0.0134)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH322 | lung | -3.2596384282262307 | more sensitive |
| AM38 | central nervous system | -3.0434132561628497 | more sensitive |
| HPAFII | pancreas | 3.732771946233367 | more resistant |
| KYSE510 | oesophagus | 3.744962176746956 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| docetaxel |  | -2.859924468860488 | more sensitive |
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -2.62041507800492 | more sensitive |
| BRD-K02492147 |  | 3.765885245756405 | more resistant |
| BRD-K92856060 |  | 3.8652251443255183 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0038 - prochlorperazine on OE21
*Evidence: SHAP-0038*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **prochlorperazine** (master_cpd_id=33166) |
| Gene Target | DRD2 |
| Mechanism / Activity | inhibitor of dopamine receptor D2 |
| Cell Line | **OE21** (master_ccl_id=895) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.2284**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.1631**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (732 pairs): mean=1.3284, q10=0.9113, median=1.3404, q90=1.7208, sample percentile=28.8
- Cell cohort (289 pairs): mean=0.5505, q10=-1.3788, median=0.6558, q90=2.0115, sample percentile=64.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.228 matches 20-NN mean=+1.228 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1516, |SHAP|=0.1516)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0883, |SHAP|=0.0883)  
  _value=4.1637, z=-0.36; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0876** (fingerprint_bit; SHAP=-0.0637, |SHAP|=0.0637)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0533, |SHAP|=0.0533)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0326, |SHAP|=0.0326)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0110, |SHAP|=0.0110)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CAL62 | thyroid | -1.7848060265146026 | more sensitive |
| KM12 | large intestine | -1.7309345655880466 | more sensitive |
| MKN7 | stomach | 3.5562924655657966 | more resistant |
| PATU8988T | pancreas | 3.989646996486941 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| MLN2480 | ARAF;BRAF;RAF1 | -3.9662708776674194 | more sensitive |
| SID 26681509 | CTSL1 | -3.532396502031166 | more sensitive |
| olaparib | PARP1;PARP2 | 3.473886149962343 | more resistant |
| navitoclax | BCL2;BCL2L1;BCL2L2 | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0039 - tipifarnib-P1 on T24
*Evidence: SHAP-0039*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **tipifarnib-P1** (master_cpd_id=417417) |
| Gene Target | FNTA |
| Mechanism / Activity | inhibitor of farnesyltransferase |
| Cell Line | **T24** (master_ccl_id=1172) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.6301**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **+0.5696**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (541 pairs): mean=1.1124, q10=0.1198, median=1.3372, q90=1.7189, sample percentile=84.3
- Cell cohort (272 pairs): mean=1.1327, q10=-0.5667, median=1.3307, q90=2.5552, sample percentile=61.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.630 matches 20-NN mean=+1.630 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1245, |SHAP|=0.1245)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0983, |SHAP|=0.0983)  
  _value=9.3473, z=+1.31; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0818, |SHAP|=0.0818)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0535** (fingerprint_bit; SHAP=-0.0397, |SHAP|=0.0397)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0350, |SHAP|=0.0350)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0155** (fingerprint_bit; SHAP=-0.0314, |SHAP|=0.0314)  
  _present; representative SMARTS `[#6]-[#6]-[#6]-[#7]-[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: betulinic acid, ouabain, SB-431542_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0177, |SHAP|=0.0177)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0767** (fingerprint_bit; SHAP=+0.0174, |SHAP|=0.0174)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLP8 | haematopoietic and lymphoid tissue | -3.000019827622767 | more sensitive |
| CMK | haematopoietic and lymphoid tissue | -2.190709059788642 | more sensitive |
| KP2 | pancreas | 3.862214844368879 | more resistant |
| HCC38 | breast | 3.898338443848557 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.794366566873361 | more sensitive |
| YK 4-279 | DHX9;ERG;ETV1 | -3.6457405958086393 | more sensitive |
| ML258 | BCL2L10 | 3.973595942764552 | more resistant |
| trametinib | MAP2K1;MAP2K2 | 3.9916577425043904 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0040 - SR-II-138A on SKMEL30
*Evidence: SHAP-0040*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SR-II-138A** (master_cpd_id=411770) |
| Gene Target | EIF4A2;EIF4E;EIF4G1 |
| Mechanism / Activity | silvestrol analog; inhibits translation by modulating the eIF4F complex |
| Cell Line | **SKMEL30** (master_ccl_id=1045) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-1.1695**
- RF-predicted log10(IC50): **-1.4180**
- Prediction error (observed - predicted): **+0.2485**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (684 pairs): mean=-1.7429, q10=-2.7267, median=-1.7151, q90=-0.9483, sample percentile=81.4
- Cell cohort (158 pairs): mean=1.0016, q10=-0.7498, median=1.1666, q90=2.3552, sample percentile=7.6
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=-1.169 matches 20-NN mean=-1.169 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-1.1549, |SHAP|=1.1549)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.5867, |SHAP|=0.5867)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0767** (fingerprint_bit; SHAP=-0.2455, |SHAP|=0.2455)  
  _present; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **fp_0939** (fingerprint_bit; SHAP=-0.1374, |SHAP|=0.1374)  
  _present; representative SMARTS `N`; present in 3.5% of CTRPv2 compounds; example compounds: niclosamide, SB-225002, compound 1B_
5. **fp_0963** (fingerprint_bit; SHAP=-0.0992, |SHAP|=0.0992)  
  _present; representative SMARTS `[#6]-[#7]-[#7]-[#6]-[#6]`; present in 0.8% of CTRPv2 compounds; example compounds: procarbazine, KU 0060648, vorapaxar_
6. **fp_0761** (fingerprint_bit; SHAP=-0.0676, |SHAP|=0.0676)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_
7. **fp_0799** (fingerprint_bit; SHAP=-0.0526, |SHAP|=0.0526)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: ciclopirox, blebbistatin, pifithrin-alpha_
8. **fp_0235** (fingerprint_bit; SHAP=-0.0522, |SHAP|=0.0522)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: blebbistatin, pifithrin-alpha, ML162_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| VMRCLCD | lung | -3.933854741071595 | more sensitive |
| HPBALL | haematopoietic and lymphoid tissue | -3.885439806375562 | more sensitive |
| JHH6 | liver | 1.6601804260868562 | more resistant |
| SNU489 | central nervous system | 1.764211424751105 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| OSI-027 | MTOR | -3.2783691672046014 | more sensitive |
| BRD-K97651142 |  | -3.224961385131124 | more sensitive |
| B02 | RAD51 | 3.503989149528741 | more resistant |
| IPR-456 | PLAUR | 3.889307543978637 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0041 - parthenolide on NAMALWA
*Evidence: SHAP-0041*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **parthenolide** (master_cpd_id=411792) |
| Gene Target | n/a |
| Mechanism / Activity | natural product; modulator of ROS; modulator of NF-kappa-B signaling |
| Cell Line | **NAMALWA** (master_ccl_id=719) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **0.5196**
- RF-predicted log10(IC50): **0.6875**
- Prediction error (observed - predicted): **-0.1680**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (413 pairs): mean=1.0336, q10=0.4118, median=1.1198, q90=1.5716, sample percentile=15.7
- Cell cohort (263 pairs): mean=0.3693, q10=-1.5932, median=0.5235, q90=1.8006, sample percentile=49.8
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+0.520 matches 20-NN mean=+0.519 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2245, |SHAP|=0.2245)  
  _value=0.5840, z=-1.51; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0440, |SHAP|=0.0440)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0322** (fingerprint_bit; SHAP=-0.0300, |SHAP|=0.0300)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6]`; present in 15.0% of CTRPv2 compounds; example compounds: BRD9876, tamoxifen, BRD9647_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0281, |SHAP|=0.0281)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0192, |SHAP|=0.0192)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0147, |SHAP|=0.0147)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0269** (fingerprint_bit; SHAP=+0.0126, |SHAP|=0.0126)  
  _absent; representative SMARTS `[#6]-[#6](-[#6]-[#6](-[#6])-[#6])-[#7]`; present in 1.0% of CTRPv2 compounds; example compounds: CIL55, ciclosporin, BRD-K66532283_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0123, |SHAP|=0.0123)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| IALM | lung | -2.3299784187812222 | more sensitive |
| A101D | skin | -1.1663984091095618 | more sensitive |
| MONOMAC1 | haematopoietic and lymphoid tissue | 3.792977945366163 | more resistant |
| RKN | soft tissue | 3.7989985452794426 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | -3.879720069825522 | more sensitive |
| lapatinib | EGFR;ERBB2 | -3.790786210394052 | more sensitive |
| NSC 74859 | STAT3 | 2.587657198852948 | more resistant |
| tretinoin | RARA;RARB;RARG | 3.84415304462904 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0042 - importazole on TE441T
*Evidence: SHAP-0042*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **importazole** (master_cpd_id=46792) |
| Gene Target | KPNB1 |
| Mechanism / Activity | inhibitor of importin |
| Cell Line | **TE441T** (master_ccl_id=1192) |
| Tissue | soft tissue |
| Histology | rhabdomyosarcoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **0.9693**
- RF-predicted log10(IC50): **1.0616**
- Prediction error (observed - predicted): **-0.0923**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (294 pairs): mean=0.9193, q10=-0.1060, median=1.0536, q90=1.6684, sample percentile=43.2
- Cell cohort (282 pairs): mean=0.6198, q10=-1.1057, median=0.7800, q90=1.9557, sample percentile=55.3
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+0.969 matches 20-NN mean=+0.969 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1799, |SHAP|=0.1799)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0860, |SHAP|=0.0860)  
  _value=2.8787, z=-0.78; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0518** (fingerprint_bit; SHAP=-0.0783, |SHAP|=0.0783)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0506, |SHAP|=0.0506)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0190, |SHAP|=0.0190)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0176, |SHAP|=0.0176)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0151, |SHAP|=0.0151)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0109, |SHAP|=0.0109)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| LNCAPCLONEFGC | prostate | -3.221587798428049 | more sensitive |
| OV7 | ovary | -2.735993860697093 | more sensitive |
| COLO829 | skin | 3.811039745106002 | more resistant |
| SF126 | central nervous system | 3.8170603450192817 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.6605247472740112 | more sensitive |
| RITA | MDM2;TP53 | -3.5474507417579675 | more sensitive |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 2.7450925304598446 | more resistant |
| crizotinib | ALK;MET | 3.3594947516100304 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0043 - DBeQ on SNU1196
*Evidence: SHAP-0043*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **DBeQ** (master_cpd_id=199337) |
| Gene Target | VCP |
| Mechanism / Activity | inhibitor of p97 in cells |
| Cell Line | **SNU1196** (master_ccl_id=1085) |
| Tissue | biliary tract |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.3186**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.2533**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (735 pairs): mean=0.7969, q10=0.5534, median=0.7571, q90=1.2829, sample percentile=94.7
- Cell cohort (187 pairs): mean=0.6568, q10=-1.3518, median=0.9471, q90=2.0514, sample percentile=64.2
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.319 matches 20-NN mean=+1.319 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0951, |SHAP|=0.0951)  
  _value=4.5417, z=-0.24; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0700, |SHAP|=0.0700)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0488, |SHAP|=0.0488)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0210, |SHAP|=0.0210)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0166, |SHAP|=0.0166)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0156, |SHAP|=0.0156)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0134, |SHAP|=0.0134)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0175** (fingerprint_bit; SHAP=+0.0118, |SHAP|=0.0118)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 37.8% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, ML006_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| OC314 | ovary | -3.686185437666952 | more sensitive |
| SUDHL4 | haematopoietic and lymphoid tissue | -3.475510782018499 | more sensitive |
| SNU398 | liver | 2.650870141817018 | more resistant |
| NCIH2052 | pleura | 2.830284019232751 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| brefeldin A | ARF1 | -3.9277273780534143 | more sensitive |
| cytarabine hydrochloride |  | -2.8515367447494784 | more sensitive |
| isoevodiamine |  | 2.9085518181053867 | more resistant |
| LY-2157299 | TGFBR1 | 3.630421747707613 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0044 - NSC23766 on RT112
*Evidence: SHAP-0044*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC23766** (master_cpd_id=44503) |
| Gene Target | RAC1;TIAM1;TRIO |
| Mechanism / Activity | inhibitor of RAC1-GEF interaction; prevents Rac1 activation by Rac-specific guanine nucleotide exchange factors (GEFs) TrioN and Tiam1 |
| Cell Line | **RT112** (master_ccl_id=997) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.4660**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.4008**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (704 pairs): mean=1.9744, q10=1.2117, median=2.1603, q90=2.8314, sample percentile=22.7
- Cell cohort (208 pairs): mean=0.6241, q10=-0.9826, median=0.8296, q90=1.9398, sample percentile=74.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.466 matches 20-NN mean=+1.466 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.0865, |SHAP|=0.0865)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0863, |SHAP|=0.0863)  
  _value=4.8726, z=-0.13; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0364, |SHAP|=0.0364)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0358, |SHAP|=0.0358)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0263** (fingerprint_bit; SHAP=-0.0302, |SHAP|=0.0302)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0184, |SHAP|=0.0184)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0164, |SHAP|=0.0164)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0155, |SHAP|=0.0155)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH322 | lung | -3.2596384282262307 | more sensitive |
| AM38 | central nervous system | -3.0434132561628497 | more sensitive |
| HPAFII | pancreas | 3.732771946233367 | more resistant |
| KYSE510 | oesophagus | 3.744962176746956 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| tretinoin | RARA;RARB;RARG | -3.9919782640036594 | more sensitive |
| paclitaxel |  | -3.6128780338130273 | more sensitive |
| neratinib | EGFR;ERBB2 | 3.1277016549487646 | more resistant |
| JQ-1 | BRDT | 3.3745462513932294 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0045 - ciclopirox on SNU899
*Evidence: SHAP-0045*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **ciclopirox** (master_cpd_id=28784) |
| Gene Target | RRM1 |
| Mechanism / Activity | substituted pyridone antimycotic; inhibitor of the iron-dependent enzyme ribonucleotide reductase |
| Cell Line | **SNU899** (master_ccl_id=1129) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.5163**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.4510**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (633 pairs): mean=0.4821, q10=-0.1867, median=0.4707, q90=1.2239, sample percentile=93.4
- Cell cohort (176 pairs): mean=0.8651, q10=-0.7325, median=0.9968, q90=2.2051, sample percentile=70.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.516 matches 20-NN mean=+1.516 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0877, |SHAP|=0.0877)  
  _value=7.2679, z=+0.64; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0482, |SHAP|=0.0482)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0446, |SHAP|=0.0446)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0384, |SHAP|=0.0384)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0155, |SHAP|=0.0155)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0151, |SHAP|=0.0151)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0107, |SHAP|=0.0107)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH526 | lung | -2.716941767143448 | more sensitive |
| REC1 | haematopoietic and lymphoid tissue | -2.204861307158615 | more sensitive |
| MKN45 | stomach | 2.941063057637096 | more resistant |
| OSRC2 | kidney | 3.2390827533444377 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -2.761744048088553 | more sensitive |
| SNX-2112 | HSP90AA1;HSP90B1 | -2.067485640427718 | more sensitive |
| IU1 | USP14 | 3.774916145626324 | more resistant |
| STF-31 | NAMPT | 3.8652251443255183 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0046 - NVP-TAE684 on F36P
*Evidence: SHAP-0046*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NVP-TAE684** (master_cpd_id=606249) |
| Gene Target | ALK |
| Mechanism / Activity | inhibitor of ALK and ALK-NPM fusion protein |
| Cell Line | **F36P** (master_ccl_id=253) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **0.3992**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **-0.3144**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (728 pairs): mean=0.1692, q10=-0.8304, median=0.3259, q90=0.9729, sample percentile=55.6
- Cell cohort (323 pairs): mean=0.4488, q10=-1.2250, median=0.5744, q90=1.8777, sample percentile=43.7
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+0.399 matches 20-NN mean=+0.399 (|Δ|=0.000)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2091, |SHAP|=0.2091)  
  _value=1.0098, z=-1.38; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1427, |SHAP|=0.1427)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0518** (fingerprint_bit; SHAP=-0.0693, |SHAP|=0.0693)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0393, |SHAP|=0.0393)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0179, |SHAP|=0.0179)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0777** (fingerprint_bit; SHAP=+0.0101, |SHAP|=0.0101)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
8. **fp_0673** (fingerprint_bit; SHAP=+0.0091, |SHAP|=0.0091)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SUDHL1 | haematopoietic and lymphoid tissue | -3.488849741119767 | more sensitive |
| RPMI6666 |  | -2.9903758766882897 | more sensitive |
| JHOC5 | ovary | 1.9657258716857973 | more resistant |
| SNU719 | stomach | 2.2658527773627863 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.921718750999285 | more sensitive |
| docetaxel |  | -2.986318494369896 | more sensitive |
| bleomycin A2 |  | 2.875438518582348 | more resistant |
| olaparib | PARP1;PARP2 | 3.019330856509731 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0047 - 16-beta-bromoandrosterone on HCC4006
*Evidence: SHAP-0047*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **16-beta-bromoandrosterone** (master_cpd_id=411726) |
| Gene Target | n/a |
| Mechanism / Activity | dehydroepiandrosterone (DHEA) analog |
| Cell Line | **HCC4006** (master_ccl_id=331) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **1.3841**
- RF-predicted log10(IC50): **1.3082**
- Prediction error (observed - predicted): **+0.0760**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (176 pairs): mean=1.1325, q10=0.2259, median=1.1779, q90=1.8346, sample percentile=61.4
- Cell cohort (253 pairs): mean=0.6185, q10=-1.2145, median=0.7713, q90=2.0282, sample percentile=66.8
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.384 matches 20-NN mean=+1.384 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.4907, |SHAP|=0.4907)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0767** (fingerprint_bit; SHAP=+0.2733, |SHAP|=0.2733)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
3. **fp_0535** (fingerprint_bit; SHAP=-0.2093, |SHAP|=0.2093)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
4. **fp_0725** (fingerprint_bit; SHAP=+0.1065, |SHAP|=0.1065)  
  _absent; representative SMARTS `N`; present in 3.7% of CTRPv2 compounds; example compounds: cimetidine, dacarbazine, pifithrin-alpha_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0884, |SHAP|=0.0884)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0864** (fingerprint_bit; SHAP=+0.0779, |SHAP|=0.0779)  
  _absent; representative SMARTS `[#7]=[#6]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: mitomycin, omacetaxine mepesuccinate, PAC-1_
7. **fp_0654** (fingerprint_bit; SHAP=+0.0747, |SHAP|=0.0747)  
  _absent; representative SMARTS `[#7]-[#16](-[#6](:[#6](-[#8]):[#6]):[#6]:[#6])(=[#8])=[#8]`; present in 3.3% of CTRPv2 compounds; example compounds: KU-55933, FQI-1, NSC30930_
8. **fp_0912** (fingerprint_bit; SHAP=+0.0594, |SHAP|=0.0594)  
  _absent; representative SMARTS `[#6]-[#6](-[#7]-[#6])-[#6](:[#6]):[#6]`; present in 1.5% of CTRPv2 compounds; example compounds: importazole, itraconazole, necrostatin-1_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MINO | haematopoietic and lymphoid tissue | -3.555598002619139 | more sensitive |
| KMS20 | haematopoietic and lymphoid tissue | -1.396532653982373 | more sensitive |
| MV411 | haematopoietic and lymphoid tissue | 3.503989149528741 | more resistant |
| NCIH1092 | lung | 3.762874945799765 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| IPR-456 | PLAUR | -3.9826268426344713 | more sensitive |
| NVP-231 | CERK | -3.858002112755049 | more sensitive |
| MLN2480 | ARAF;BRAF;RAF1 | 3.6364423476208927 | more resistant |
| EX-527 | SIRT1 | 3.8321118448024807 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0048 - MK-2206 on SKMEL31
*Evidence: SHAP-0048*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **MK-2206** (master_cpd_id=377381) |
| Gene Target | AKT1 |
| Mechanism / Activity | inhibitor of AKT1 |
| Cell Line | **SKMEL31** (master_ccl_id=1046) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.3640**
- RF-predicted log10(IC50): **0.8897**
- Prediction error (observed - predicted): **+0.4742**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (674 pairs): mean=0.9855, q10=0.2617, median=1.1397, q90=1.4631, sample percentile=85.5
- Cell cohort (154 pairs): mean=1.1509, q10=-0.2551, median=1.2673, q90=2.3488, sample percentile=54.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.364 matches 20-NN mean=+1.364 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0059** (fingerprint_bit; SHAP=-0.1522, |SHAP|=0.1522)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
2. **fp_0065** (fingerprint_bit; SHAP=+0.0761, |SHAP|=0.0761)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
3. **CCN1 (3491)** (gene_expression; SHAP=+0.0621, |SHAP|=0.0621)  
  _value=6.0846, z=+0.26; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0227** (fingerprint_bit; SHAP=-0.0443, |SHAP|=0.0443)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
5. **fp_0017** (fingerprint_bit; SHAP=+0.0370, |SHAP|=0.0370)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
6. **fp_0141** (fingerprint_bit; SHAP=+0.0287, |SHAP|=0.0287)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0183, |SHAP|=0.0183)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0792** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| WM1799 | skin | -2.8209770035566137 | more sensitive |
| NCIH929 | haematopoietic and lymphoid tissue | -2.731351032827141 | more sensitive |
| TT2609C02 | thyroid | 2.9886257969520056 | more resistant |
| NCIH1395 | lung | 3.136732554818684 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| tacrolimus | PPP3CA;PPP3CB;PPP3CC;PPP3R1;PPP3R2 | -3.212363264616154 | more sensitive |
| oligomycin A | ATP5L2 | -2.0241256908446097 | more sensitive |
| ceranib-2 | ACER1;ACER2;ACER3;ASAH1;ASAH2;ASAH2B | 3.85017364454232 | more resistant |
| pifithrin-mu | HSPA1A;HSPA1B;HSPA1L;TP53 | 3.904359043761836 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0049 - sunitinib on ACCMESO1
*Evidence: SHAP-0049*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **sunitinib** (master_cpd_id=374750) |
| Gene Target | FLT1;FLT3;KDR;KIT;PDGFRA;PDGFRB |
| Mechanism / Activity | inhibitor of VEGFRs, c-KIT, and PDGFR alpha and beta |
| Cell Line | **ACCMESO1** (master_ccl_id=41) |
| Tissue | pleura |
| Histology | mesothelioma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0918**
- RF-predicted log10(IC50): **0.8086**
- Prediction error (observed - predicted): **+0.2833**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (772 pairs): mean=0.8469, q10=0.4378, median=0.8397, q90=1.3683, sample percentile=70.7
- Cell cohort (177 pairs): mean=1.1921, q10=-0.1540, median=1.3462, q90=2.5113, sample percentile=37.9
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.092 matches 20-NN mean=+1.092 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.3002, |SHAP|=0.3002)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.2135, |SHAP|=0.2135)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0071** (fingerprint_bit; SHAP=-0.1202, |SHAP|=0.1202)  
  _present; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
4. **fp_0673** (fingerprint_bit; SHAP=+0.0730, |SHAP|=0.0730)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0466, |SHAP|=0.0466)  
  _value=7.9349, z=+0.85; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0876** (fingerprint_bit; SHAP=-0.0354, |SHAP|=0.0354)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
7. **fp_0688** (fingerprint_bit; SHAP=+0.0351, |SHAP|=0.0351)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
8. **fp_0263** (fingerprint_bit; SHAP=+0.0250, |SHAP|=0.0250)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -2.3410380013572207 | more sensitive |
| MV411 | haematopoietic and lymphoid tissue | -2.316321629957783 | more sensitive |
| REC1 | haematopoietic and lymphoid tissue | 2.11563880952646 | more resistant |
| MKN45 | stomach | 2.2031233458398565 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K97651142 |  | -2.6559791008899523 | more sensitive |
| sorafenib | BRAF;FLT3;KDR;RAF1 | -2.4330746730303137 | more sensitive |
| NVP-231 | CERK | 3.166835554385082 | more resistant |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 3.916400243588395 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0050 - pitstop2 on A498
*Evidence: SHAP-0050*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **pitstop2** (master_cpd_id=660985) |
| Gene Target | CLTA;CLTB;CLTC;CLTCL1 |
| Mechanism / Activity | inhibitor of clathrin and clathrin-independent endocytosis |
| Cell Line | **A498** (master_ccl_id=33) |
| Tissue | kidney |
| Histology | carcinoma |
| Subtype | renal cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.8274**
- RF-predicted log10(IC50): **0.8185**
- Prediction error (observed - predicted): **+1.0090**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (109 pairs): mean=2.1035, q10=1.5219, median=1.8751, q90=3.0416, sample percentile=45.9
- Cell cohort (101 pairs): mean=0.9095, q10=-0.6783, median=1.1641, q90=2.1536, sample percentile=78.2
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: curated normal: observed log10(IC50)=+1.827 matches 20-NN mean=+1.828 (|Δ|=0.000)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.2925, |SHAP|=0.2925)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1228, |SHAP|=0.1228)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0673** (fingerprint_bit; SHAP=+0.0532, |SHAP|=0.0532)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0452, |SHAP|=0.0452)  
  _value=7.2846, z=+0.65; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0876** (fingerprint_bit; SHAP=-0.0448, |SHAP|=0.0448)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0350, |SHAP|=0.0350)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0263** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
8. **fp_0771** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH1666 | lung | 0.2069054551918249 | more sensitive |
| NCIH1792 | lung | 1.0976486676593376 | more sensitive |
| JHH2 | liver | 3.916400243588395 | more resistant |
| RVH421 | skin | 3.994668042461031 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| afatinib | EGFR;ERBB2 | -3.975037715199819 | more sensitive |
| RITA | MDM2;TP53 | -3.9272620724404974 | more sensitive |
| IU1 | USP14 | 3.0975986553823662 | more resistant |
| necrostatin-7 |  | 3.3865874512197887 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---
