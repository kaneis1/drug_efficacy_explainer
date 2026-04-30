# SHAP-Grounded Sample Reports (log10(IC50))

## RPT-0001 - BI-2536 on REC1
*Evidence: SHAP-0001*

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
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=+3.724, RF OOF predicted -2.285 (Δ_model=+6.009), 20-NN mean=-2.376 (Δ_knn=+6.100). Drug target: PLK1. Cell lineage: Lymphoid / Mature B-Cell Neoplasms. Per-drug R² on held-out cells = 0.27.

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

## RPT-0002 - topotecan on GOS3
*Evidence: SHAP-0002*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **topotecan** (master_cpd_id=44580) |
| Gene Target | TOP1 |
| Mechanism / Activity | inhibitor of topoisomerase I |
| Cell Line | **GOS3** (master_ccl_id=281) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma |

### Response Summary
- Observed log10(IC50): **-3.6393**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-4.6997**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (762 pairs): mean=-0.3539, q10=-1.6236, median=-0.2493, q90=0.6901, sample percentile=0.1
- Cell cohort (188 pairs): mean=0.9655, q10=-0.9632, median=1.1733, q90=2.5119, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.639, RF OOF predicted +1.054 (Δ_model=-4.694), 20-NN mean=+1.516 (Δ_knn=-5.155). Drug target: TOP1. Cell lineage: CNS/Brain / Diffuse Glioma. Per-drug R² on held-out cells = 0.40.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1032, |SHAP|=0.1032)  
  _value=8.0173, z=+0.88; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0691, |SHAP|=0.0691)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0475, |SHAP|=0.0475)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0400, |SHAP|=0.0400)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0152, |SHAP|=0.0152)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0136, |SHAP|=0.0136)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0788** (fingerprint_bit; SHAP=-0.0132, |SHAP|=0.0132)  
  _present; representative SMARTS `[#6]:[#6](-[#6]):[#6]:[#7](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: betulinic acid, CI-976, SRT-1720_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CL34 | large intestine | -3.384235612523065 | more sensitive |
| SNU886 | liver | -3.1800345986891565 | more sensitive |
| ACCMESO1 | pleura | 2.05964723033296 | more resistant |
| SNU201 | central nervous system | 2.3919843455459944 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.0611132621658323 | more sensitive |
| leptomycin B | XPO1 | -2.70137659311846 | more sensitive |
| canertinib | EGFR;ERBB2 | 3.67557624705721 | more resistant |
| selumetinib | MAP2K1;MAP2K2 | 3.979616542677832 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0003 - SN-38 on PANC0504
*Evidence: SHAP-0003*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SN-38** (master_cpd_id=375637) |
| Gene Target | TOP1 |
| Mechanism / Activity | metabolite of irinotecan; inhibitor of topoisomerase I |
| Cell Line | **PANC0504** (master_ccl_id=924) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **3.9917**
- RF-predicted log10(IC50): **-0.8168**
- Prediction error (observed - predicted): **+4.8085**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (527 pairs): mean=-1.4223, q10=-2.8421, median=-1.3624, q90=-0.1771, sample percentile=100.0
- Cell cohort (157 pairs): mean=0.8651, q10=-0.8361, median=0.9768, q90=2.3103, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=+3.992, RF OOF predicted -0.873 (Δ_model=+4.865), 20-NN mean=-0.864 (Δ_knn=+4.855). Drug target: TOP1. Cell lineage: Pancreas / Pancreatic Adenocarcinoma. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.5047, |SHAP|=0.5047)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **fp_0059** (fingerprint_bit; SHAP=-0.4340, |SHAP|=0.4340)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
3. **fp_0240** (fingerprint_bit; SHAP=-0.1751, |SHAP|=0.1751)  
  _present; representative SMARTS `[#6]:[#6](-[#8]-[#6](:[#6]):[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: cytochalasin B, BRD-A94377914, CIL41_
4. **fp_0065** (fingerprint_bit; SHAP=-0.1725, |SHAP|=0.1725)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.1270, |SHAP|=0.1270)  
  _value=5.8956, z=+0.20; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0667** (fingerprint_bit; SHAP=-0.1228, |SHAP|=0.1228)  
  _present; representative SMARTS `[#7]-[#6]-[#6]`; present in 9.6% of CTRPv2 compounds; example compounds: CIL55, BRD4132, cimetidine_
7. **fp_0227** (fingerprint_bit; SHAP=-0.1080, |SHAP|=0.1080)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0141** (fingerprint_bit; SHAP=-0.0797, |SHAP|=0.0797)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNUC1 | large intestine | -3.861294497519686 | more sensitive |
| HEC50B | endometrium | -3.795937834345268 | more sensitive |
| PATU8902 | pancreas | 2.4428584148132075 | more resistant |
| ISTMES1 | pleura | 2.642140271942763 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| brefeldin A | ARF1 | -2.9152647986959623 | more sensitive |
| austocystin D |  | -2.5013549302526004 | more sensitive |
| ML050 | GPER1 | 3.103619255295646 | more resistant |
| etomoxir | CPT1A | 3.151784054601883 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0004 - selumetinib on MINO
*Evidence: SHAP-0004*

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
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.491, RF OOF predicted +0.601 (Δ_model=-4.092), 20-NN mean=+2.044 (Δ_knn=-5.535). Drug target: MAP2K1;MAP2K2. Cell lineage: Lymphoid / Mature B-Cell Neoplasms. Per-drug R² on held-out cells = 0.22.

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

## RPT-0005 - GSK461364 on MDAMB468
*Evidence: SHAP-0005*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GSK461364** (master_cpd_id=649862) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **MDAMB468** (master_ccl_id=658) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.9435**
- RF-predicted log10(IC50): **0.0698**
- Prediction error (observed - predicted): **-4.0132**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (659 pairs): mean=-1.1247, q10=-2.9192, median=-1.7383, q90=1.0518, sample percentile=0.5
- Cell cohort (271 pairs): mean=0.5478, q10=-1.4279, median=0.6454, q90=1.9627, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.943, RF OOF predicted +0.403 (Δ_model=-4.346), 20-NN mean=+1.037 (Δ_knn=-4.981). Drug target: PLK1. Cell lineage: Breast / Invasive Breast Carcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0059** (fingerprint_bit; SHAP=-0.4314, |SHAP|=0.4314)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
2. **fp_0065** (fingerprint_bit; SHAP=-0.1724, |SHAP|=0.1724)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
3. **fp_0227** (fingerprint_bit; SHAP=-0.1081, |SHAP|=0.1081)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0924, |SHAP|=0.0924)  
  _value=7.3851, z=+0.68; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0141** (fingerprint_bit; SHAP=+0.0409, |SHAP|=0.0409)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **fp_0402** (fingerprint_bit; SHAP=-0.0262, |SHAP|=0.0262)  
  _present; representative SMARTS `[#7]-[#15](=[#8])(-[#8])-[#7]`; present in 1.2% of CTRPv2 compounds; example compounds: ifosfamide, topotecan, navitoclax_
7. **fp_0015** (fingerprint_bit; SHAP=-0.0242, |SHAP|=0.0242)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0157** (fingerprint_bit; SHAP=-0.0184, |SHAP|=0.0184)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| GA10 | haematopoietic and lymphoid tissue | -3.9968244931949575 | more sensitive |
| PECAPJ15 | upper aerodigestive tract | -3.962241957923673 | more sensitive |
| CAKI1 | kidney | 2.0114824310267223 | more resistant |
| PANC0203 | pancreas | 2.0722904901508468 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.647072361810745 | more sensitive |
| R428 | AXL | -3.573881401383643 | more sensitive |
| tretinoin | RARA;RARB;RARG | 3.0524441560327693 | more resistant |
| SGX-523 | MET | 3.3835771512631485 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0006 - barasertib on MDAMB468
*Evidence: SHAP-0006*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **barasertib** (master_cpd_id=601923) |
| Gene Target | AURKB |
| Mechanism / Activity | inhibitor of aurora kinase B |
| Cell Line | **MDAMB468** (master_ccl_id=658) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.5277**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.5930**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (409 pairs): mean=0.8872, q10=-2.1932, median=1.6713, q90=2.8052, sample percentile=1.0
- Cell cohort (271 pairs): mean=0.5478, q10=-1.4279, median=0.6454, q90=1.9627, sample percentile=1.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.528, RF OOF predicted +1.058 (Δ_model=-4.586), 20-NN mean=+1.152 (Δ_knn=-4.680). Drug target: AURKB. Cell lineage: Breast / Invasive Breast Carcinoma. Per-drug R² on held-out cells = 0.34.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0932, |SHAP|=0.0932)  
  _value=7.3851, z=+0.68; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0813, |SHAP|=0.0813)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0769, |SHAP|=0.0769)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0187, |SHAP|=0.0187)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0284** (fingerprint_bit; SHAP=-0.0159, |SHAP|=0.0159)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 7.7% of CTRPv2 compounds; example compounds: Bax channel blocker, isoliquiritigenin, curcumin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0151, |SHAP|=0.0151)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0227** (fingerprint_bit; SHAP=+0.0121, |SHAP|=0.0121)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KO52 | haematopoietic and lymphoid tissue | -3.967611494736124 | more sensitive |
| ST486 | haematopoietic and lymphoid tissue | -3.686837341250692 | more sensitive |
| BFTC909 | kidney | 3.970585642807912 | more resistant |
| HCC2279 | lung | 3.973595942764552 | more resistant |

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

## RPT-0007 - dabrafenib on SIGM5
*Evidence: SHAP-0007*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **dabrafenib** (master_cpd_id=687954) |
| Gene Target | BRAF |
| Mechanism / Activity | inhibitor of BRAF |
| Cell Line | **SIGM5** (master_ccl_id=1028) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **-3.8228**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **-4.5365**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (142 pairs): mean=1.0130, q10=-2.5739, median=1.7416, q90=2.3302, sample percentile=1.4
- Cell cohort (282 pairs): mean=0.4099, q10=-1.5785, median=0.5190, q90=1.8935, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.823, RF OOF predicted +0.718 (Δ_model=-4.541), 20-NN mean=+0.763 (Δ_knn=-4.586). Drug target: BRAF. Cell lineage: Myeloid / Acute Myeloid Leukemia. Per-drug R² on held-out cells = 0.53.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2107, |SHAP|=0.2107)  
  _value=0.8123, z=-1.44; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0288, |SHAP|=0.0288)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0220, |SHAP|=0.0220)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0191, |SHAP|=0.0191)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0164, |SHAP|=0.0164)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0015** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0128, |SHAP|=0.0128)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| WM88 | skin | -3.829560592827962 | more sensitive |
| DU4475 | breast | -3.546495708148277 | more sensitive |
| AU565 | breast | 3.648483547447452 | more resistant |
| PATU8988S | pancreas | 3.808029445149362 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| alisertib | AURKA;AURKB | -3.265446167223261 | more sensitive |
| N9-isopropylolomoucine | CCNB1;CDK1;CDK5;CDK5R1 | -3.058266558741365 | more sensitive |
| necrostatin-1 | RIPK1 | 3.073644840945785 | more resistant |
| birinapant | DIABLO;XIAP | 3.642462947534173 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0008 - alisertib on T84
*Evidence: SHAP-0008*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **alisertib** (master_cpd_id=636711) |
| Gene Target | AURKA;AURKB |
| Mechanism / Activity | inhibitor of aurora kinases A and B |
| Cell Line | **T84** (master_ccl_id=1176) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.6782**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.7435**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (521 pairs): mean=0.5344, q10=-1.7044, median=1.0768, q90=1.9444, sample percentile=0.4
- Cell cohort (278 pairs): mean=0.3821, q10=-1.4540, median=0.5911, q90=1.7764, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.678, RF OOF predicted +1.067 (Δ_model=-4.745), 20-NN mean=+0.649 (Δ_knn=-4.327). Drug target: AURKA;AURKB. Cell lineage: Bowel / Colorectal Adenocarcinoma. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1125, |SHAP|=0.1125)  
  _value=3.9419, z=-0.43; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0859, |SHAP|=0.0859)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0550, |SHAP|=0.0550)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0723** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0177, |SHAP|=0.0177)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0127, |SHAP|=0.0127)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0122, |SHAP|=0.0122)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0015** (fingerprint_bit; SHAP=-0.0122, |SHAP|=0.0122)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| JEKO1 | haematopoietic and lymphoid tissue | -3.9125005500802312 | more sensitive |
| OCILY3 | haematopoietic and lymphoid tissue | -3.4006670451767045 | more sensitive |
| UACC257 | skin | 3.371535951436589 | more resistant |
| SNU869 | biliary tract | 3.371535951436589 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| quizartinib | FLT3 | -3.935260294073839 | more sensitive |
| BRD-K28456706 | HNF4A | -3.8035638981987687 | more sensitive |
| BRD-M00053801 | BCL2 | 3.5942981482279355 | more resistant |
| AZD7545 | PDK2 | 3.9254311434583142 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0009 - GSK461364 on TE4
*Evidence: SHAP-0009*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GSK461364** (master_cpd_id=649862) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **TE4** (master_ccl_id=1191) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.9022**
- RF-predicted log10(IC50): **0.0506**
- Prediction error (observed - predicted): **-3.9528**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (659 pairs): mean=-1.1247, q10=-2.9192, median=-1.7383, q90=1.0518, sample percentile=1.1
- Cell cohort (236 pairs): mean=0.5912, q10=-1.2881, median=0.9029, q90=1.9917, sample percentile=0.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.902, RF OOF predicted +0.406 (Δ_model=-4.308), 20-NN mean=+0.907 (Δ_knn=-4.810). Drug target: PLK1. Cell lineage: Esophagus/Stomach / Esophageal Squamous Cell Carcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0059** (fingerprint_bit; SHAP=-0.4360, |SHAP|=0.4360)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
2. **fp_0065** (fingerprint_bit; SHAP=-0.1724, |SHAP|=0.1724)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
3. **fp_0227** (fingerprint_bit; SHAP=-0.1081, |SHAP|=0.1081)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0903, |SHAP|=0.0903)  
  _value=7.0621, z=+0.57; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0141** (fingerprint_bit; SHAP=+0.0419, |SHAP|=0.0419)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **fp_0402** (fingerprint_bit; SHAP=-0.0290, |SHAP|=0.0290)  
  _present; representative SMARTS `[#7]-[#15](=[#8])(-[#8])-[#7]`; present in 1.2% of CTRPv2 compounds; example compounds: ifosfamide, topotecan, navitoclax_
7. **fp_0015** (fingerprint_bit; SHAP=-0.0238, |SHAP|=0.0238)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0774** (fingerprint_bit; SHAP=-0.0195, |SHAP|=0.0195)  
  _present; representative SMARTS `[#6]=[#7]-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: cerulenin, compound 1B, BRD-K41597374_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| GA10 | haematopoietic and lymphoid tissue | -3.9968244931949575 | more sensitive |
| PECAPJ15 | upper aerodigestive tract | -3.962241957923673 | more sensitive |
| CAKI1 | kidney | 2.0114824310267223 | more resistant |
| PANC0203 | pancreas | 2.0722904901508468 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K70511574 | PLK1 | -3.908907792264956 | more sensitive |
| SB-743921 | KIF11 | -3.1082848338890687 | more sensitive |
| purmorphamine | SMO | 3.756854345886485 | more resistant |
| semagacestat | APH1A;NCSTN;PSEN1;PSENEN | 3.774916145626324 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0010 - barasertib on LCLC97TM1
*Evidence: SHAP-0010*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **barasertib** (master_cpd_id=601923) |
| Gene Target | AURKB |
| Mechanism / Activity | inhibitor of aurora kinase B |
| Cell Line | **LCLC97TM1** (master_ccl_id=600) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | large cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.2033**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.2685**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (409 pairs): mean=0.8872, q10=-2.1932, median=1.6713, q90=2.8052, sample percentile=2.9
- Cell cohort (271 pairs): mean=0.5680, q10=-1.2526, median=0.6919, q90=1.9341, sample percentile=1.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.203, RF OOF predicted +1.068 (Δ_model=-4.272), 20-NN mean=+1.378 (Δ_knn=-4.581). Drug target: AURKB. Cell lineage: Lung / Non-Small Cell Lung Cancer. Per-drug R² on held-out cells = 0.34.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0933, |SHAP|=0.0933)  
  _value=6.0959, z=+0.26; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0801, |SHAP|=0.0801)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0774, |SHAP|=0.0774)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0175, |SHAP|=0.0175)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0284** (fingerprint_bit; SHAP=-0.0160, |SHAP|=0.0160)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 7.7% of CTRPv2 compounds; example compounds: Bax channel blocker, isoliquiritigenin, curcumin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0152, |SHAP|=0.0152)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0227** (fingerprint_bit; SHAP=+0.0121, |SHAP|=0.0121)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KO52 | haematopoietic and lymphoid tissue | -3.967611494736124 | more sensitive |
| ST486 | haematopoietic and lymphoid tissue | -3.686837341250692 | more sensitive |
| BFTC909 | kidney | 3.970585642807912 | more resistant |
| HCC2279 | lung | 3.973595942764552 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.746616399706895 | more sensitive |
| vincristine |  | -3.592467402494473 | more sensitive |
| dexamethasone | NR3C1 | 3.5792466484447365 | more resistant |
| GSK2636771 | PIK3CB | 3.6093496480111344 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0011 - alisertib on CAOV3
*Evidence: SHAP-0011*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **alisertib** (master_cpd_id=636711) |
| Gene Target | AURKA;AURKB |
| Mechanism / Activity | inhibitor of aurora kinases A and B |
| Cell Line | **CAOV3** (master_ccl_id=126) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.1799**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.2452**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (521 pairs): mean=0.5344, q10=-1.7044, median=1.0768, q90=1.9444, sample percentile=1.3
- Cell cohort (236 pairs): mean=0.5617, q10=-1.4169, median=0.8049, q90=1.9728, sample percentile=1.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.180, RF OOF predicted +1.061 (Δ_model=-4.241), 20-NN mean=+1.319 (Δ_knn=-4.499). Drug target: AURKA;AURKB. Cell lineage: Ovary/Fallopian Tube / Ovarian Epithelial Tumor. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1129, |SHAP|=0.1129)  
  _value=7.9636, z=+0.86; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0817, |SHAP|=0.0817)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0547, |SHAP|=0.0547)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0723** (fingerprint_bit; SHAP=+0.0183, |SHAP|=0.0183)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0128, |SHAP|=0.0128)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0127, |SHAP|=0.0127)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0015** (fingerprint_bit; SHAP=-0.0122, |SHAP|=0.0122)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| JEKO1 | haematopoietic and lymphoid tissue | -3.9125005500802312 | more sensitive |
| T84 | large intestine | -3.678246151459168 | more sensitive |
| UACC257 | skin | 3.371535951436589 | more resistant |
| SNU869 | biliary tract | 3.371535951436589 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| cucurbitacin I |  | -3.919785320228274 | more sensitive |
| BI-2536 | PLK1 | -3.416092281504977 | more sensitive |
| BRD8958 | EP300 | 3.7869573454528833 | more resistant |
| sirolimus | MTOR | 3.904359043761836 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0012 - crizotinib on CAPAN2
*Evidence: SHAP-0012*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **crizotinib** (master_cpd_id=628603) |
| Gene Target | ALK;MET |
| Mechanism / Activity | inhibitor of c-MET and ALK |
| Cell Line | **CAPAN2** (master_ccl_id=129) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **-3.0708**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-4.1312**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (765 pairs): mean=0.6958, q10=0.0535, median=0.7825, q90=1.2372, sample percentile=0.1
- Cell cohort (225 pairs): mean=1.0900, q10=-0.4253, median=1.2442, q90=2.4928, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.071, RF OOF predicted +1.062 (Δ_model=-4.133), 20-NN mean=+1.036 (Δ_knn=-4.107). Drug target: ALK;MET. Cell lineage: Pancreas / Pancreatic Adenocarcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1361, |SHAP|=0.1361)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.1019, |SHAP|=0.1019)  
  _value=4.6119, z=-0.22; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0673** (fingerprint_bit; SHAP=-0.0696, |SHAP|=0.0696)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0141** (fingerprint_bit; SHAP=+0.0387, |SHAP|=0.0387)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0362, |SHAP|=0.0362)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0164, |SHAP|=0.0164)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNU5 | stomach | -1.5888974514187928 | more sensitive |
| SNU620 | stomach | -1.4446826222777267 | more sensitive |
| NCIH2444 | lung | 1.9136476824359283 | more resistant |
| TE441T | soft tissue | 3.3594947516100304 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| triptolide |  | -2.293889454211786 | more sensitive |
| bafilomycin A1 | ATP6V0A1 | -2.2560564751016274 | more sensitive |
| lenvatinib | FLT1;FLT3;KDR;KIT;PDGFRA;PDGFRB | 3.549143648878338 | more resistant |
| PYR-41 | UBA1 | 3.9194105435450353 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0013 - indisulam on NCIH2081
*Evidence: SHAP-0013*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **indisulam** (master_cpd_id=411874) |
| Gene Target | CA9 |
| Mechanism / Activity | inhibitor of carbonic anhydrase isoform IX |
| Cell Line | **NCIH2081** (master_ccl_id=155487) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | small cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.4710**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **-4.1846**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (431 pairs): mean=0.7254, q10=-0.3568, median=0.4787, q90=1.8854, sample percentile=0.2
- Cell cohort (266 pairs): mean=0.3004, q10=-1.8868, median=0.3896, q90=1.9581, sample percentile=0.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.471, RF OOF predicted +0.730 (Δ_model=-4.201), 20-NN mean=+0.518 (Δ_knn=-3.989). Drug target: CA9. Cell lineage: Lung / Lung Neuroendocrine Tumor. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2055, |SHAP|=0.2055)  
  _value=1.0466, z=-1.36; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0646, |SHAP|=0.0646)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0292, |SHAP|=0.0292)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0723** (fingerprint_bit; SHAP=+0.0182, |SHAP|=0.0182)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0146, |SHAP|=0.0146)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0015** (fingerprint_bit; SHAP=+0.0126, |SHAP|=0.0126)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0114, |SHAP|=0.0114)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HDLM2 | haematopoietic and lymphoid tissue | -1.51638765981231 | more sensitive |
| TC71 | bone | -1.4275271350730063 | more sensitive |
| OAW28 | ovary | 3.455824350222504 | more resistant |
| CCFSTTG1 | central nervous system | 3.7418028461032864 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.6236608071751935 | more sensitive |
| paclitaxel |  | -3.348381877327357 | more sensitive |
| BMS-270394 | RARG | 3.3414329518701917 | more resistant |
| PYR-41 | UBA1 | 3.862214844368879 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0014 - LBH-589 on MKN45
*Evidence: SHAP-0014*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **LBH-589** (master_cpd_id=54210) |
| Gene Target | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8 |
| Cell Line | **MKN45** (master_ccl_id=683) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | diffuse adenocarcinoma |

### Response Summary
- Observed log10(IC50): **3.8231**
- RF-predicted log10(IC50): **1.6866**
- Prediction error (observed - predicted): **+2.1365**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (779 pairs): mean=-1.4119, q10=-2.3459, median=-1.3810, q90=-0.6424, sample percentile=100.0
- Cell cohort (70 pairs): mean=1.5616, q10=-0.5436, median=1.8231, q90=3.0802, sample percentile=97.1
- Interpretation: **more resistant than the model predicted**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=+3.823, RF OOF predicted -1.263 (Δ_model=+5.086), 20-NN mean=+0.879 (Δ_knn=+2.944). Drug target: HDAC1;HDAC2;HDAC3;HDAC6;HDAC8. Cell lineage: Esophagus/Stomach / Esophagogastric Adenocarcinoma. Per-drug R² on held-out cells = 0.27.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.3434, |SHAP|=0.3434)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **MYLK (4638)** (gene_expression; SHAP=+0.3335, |SHAP|=0.3335)  
  _value=0.1506, z=-1.28; below the cross-cell-line mean; recurs in 20 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.2212, |SHAP|=0.2212)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0071** (fingerprint_bit; SHAP=-0.1500, |SHAP|=0.1500)  
  _present; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
5. **TES (26136)** (gene_expression; SHAP=+0.1418, |SHAP|=0.1418)  
  _value=9.4842, z=+2.03; markedly above the cross-cell-line mean; recurs in 8 predictable-drug RF signatures_
6. **GLB1L2 (89944)** (gene_expression; SHAP=+0.1089, |SHAP|=0.1089)  
  _value=6.4044, z=+2.11; markedly above the cross-cell-line mean; recurs in 10 predictable-drug RF signatures_
7. **fp_0242** (fingerprint_bit; SHAP=-0.1034, |SHAP|=0.1034)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6]:[#16])-[#6](:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: BRD4132, BRD-A94377914, SKI-II_
8. **CEACAM5 (1048)** (gene_expression; SHAP=+0.0937, |SHAP|=0.0937)  
  _value=10.2760, z=+3.95; markedly above the cross-cell-line mean; recurs in 6 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | -3.5164912620559865 | more sensitive |
| KMS26 | haematopoietic and lymphoid tissue | -3.3705757993664016 | more sensitive |
| REC1 | haematopoietic and lymphoid tissue | 2.3257577464999186 | more resistant |
| KMM1 | haematopoietic and lymphoid tissue | 2.6650185516132257 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| topotecan | TOP1 | -2.07301071594 | more sensitive |
| daporinad | NAMPT | -2.03110514626534 | more sensitive |
| BRD1812 |  | 3.9194105435450353 | more resistant |
| tretinoin | RARA;RARB;RARG | 3.9585444429813528 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0015 - topotecan on SNU886
*Evidence: SHAP-0015*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **topotecan** (master_cpd_id=44580) |
| Gene Target | TOP1 |
| Mechanism / Activity | inhibitor of topoisomerase I |
| Cell Line | **SNU886** (master_ccl_id=1128) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed log10(IC50): **-3.1800**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-4.2405**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (762 pairs): mean=-0.3539, q10=-1.6236, median=-0.2493, q90=0.6901, sample percentile=0.4
- Cell cohort (178 pairs): mean=0.3872, q10=-1.3555, median=0.5753, q90=1.8703, sample percentile=2.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.180, RF OOF predicted +1.049 (Δ_model=-4.229), 20-NN mean=+0.673 (Δ_knn=-3.853). Drug target: TOP1. Cell lineage: Liver / Hepatocellular Carcinoma. Per-drug R² on held-out cells = 0.40.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1032, |SHAP|=0.1032)  
  _value=8.6576, z=+1.09; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0682, |SHAP|=0.0682)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0475, |SHAP|=0.0475)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0401, |SHAP|=0.0401)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0180, |SHAP|=0.0180)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0154, |SHAP|=0.0154)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0146, |SHAP|=0.0146)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0788** (fingerprint_bit; SHAP=-0.0135, |SHAP|=0.0135)  
  _present; representative SMARTS `[#6]:[#6](-[#6]):[#6]:[#7](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: betulinic acid, CI-976, SRT-1720_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| GOS3 | central nervous system | -3.63925374767113 | more sensitive |
| CL34 | large intestine | -3.384235612523065 | more sensitive |
| ACCMESO1 | pleura | 2.05964723033296 | more resistant |
| SNU201 | central nervous system | 2.3919843455459944 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K34222889 |  | -3.965978102306373 | more sensitive |
| narciclasine | RHOA | -3.727986897286241 | more sensitive |
| ML031 | S1PR2 | 3.425694854631247 | more resistant |
| VER-155008 | HSPA1A;HSPA1B;HSPA1L | 3.4678655500490634 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0016 - SN-38 on ISTMES1
*Evidence: SHAP-0016*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SN-38** (master_cpd_id=375637) |
| Gene Target | TOP1 |
| Mechanism / Activity | metabolite of irinotecan; inhibitor of topoisomerase I |
| Cell Line | **ISTMES1** (master_ccl_id=480) |
| Tissue | pleura |
| Histology | mesothelioma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **2.6421**
- RF-predicted log10(IC50): **-1.0252**
- Prediction error (observed - predicted): **+3.6673**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (527 pairs): mean=-1.4223, q10=-2.8421, median=-1.3624, q90=-0.1771, sample percentile=99.8
- Cell cohort (208 pairs): mean=0.9001, q10=-0.7393, median=1.0348, q90=2.2542, sample percentile=95.7
- Interpretation: **more resistant than the model predicted**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=+2.642, RF OOF predicted -1.297 (Δ_model=+3.940), 20-NN mean=-1.506 (Δ_knn=+4.148). Drug target: TOP1. Cell lineage: Pleura / Pleural Mesothelioma. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.5058, |SHAP|=0.5058)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **fp_0059** (fingerprint_bit; SHAP=-0.4387, |SHAP|=0.4387)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
3. **fp_0667** (fingerprint_bit; SHAP=-0.1960, |SHAP|=0.1960)  
  _present; representative SMARTS `[#7]-[#6]-[#6]`; present in 9.6% of CTRPv2 compounds; example compounds: CIL55, BRD4132, cimetidine_
4. **fp_0240** (fingerprint_bit; SHAP=-0.1855, |SHAP|=0.1855)  
  _present; representative SMARTS `[#6]:[#6](-[#8]-[#6](:[#6]):[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: cytochalasin B, BRD-A94377914, CIL41_
5. **fp_0065** (fingerprint_bit; SHAP=-0.1724, |SHAP|=0.1724)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.1229, |SHAP|=0.1229)  
  _value=9.0172, z=+1.20; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0227** (fingerprint_bit; SHAP=-0.1082, |SHAP|=0.1082)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0141** (fingerprint_bit; SHAP=-0.0930, |SHAP|=0.0930)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNUC1 | large intestine | -3.861294497519686 | more sensitive |
| HEC50B | endometrium | -3.795937834345268 | more sensitive |
| PATU8902 | pancreas | 2.4428584148132075 | more resistant |
| PANC0504 | pancreas | 3.9916577425043904 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| B02 | RAD51 | -3.263242722932058 | more sensitive |
| doxorubicin | TOP2A | -3.114407360652994 | more sensitive |
| erlotinib | EGFR;ERBB2 | 3.335412351956912 | more resistant |
| ML239 |  | 3.83813244471576 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0017 - dabrafenib on SCC4
*Evidence: SHAP-0017*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **dabrafenib** (master_cpd_id=687954) |
| Gene Target | BRAF |
| Mechanism / Activity | inhibitor of BRAF |
| Cell Line | **SCC4** (master_ccl_id=1009) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-2.6407**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-3.7060**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (142 pairs): mean=1.0130, q10=-2.5739, median=1.7416, q90=2.3302, sample percentile=10.6
- Cell cohort (255 pairs): mean=0.6377, q10=-1.2674, median=0.7207, q90=2.0277, sample percentile=2.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-2.641, RF OOF predicted +1.062 (Δ_model=-3.703), 20-NN mean=+1.643 (Δ_knn=-4.284). Drug target: BRAF. Cell lineage: Head and Neck / Head and Neck Squamous Cell Carcinoma. Per-drug R² on held-out cells = 0.53.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0903, |SHAP|=0.0903)  
  _value=7.9147, z=+0.85; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0485, |SHAP|=0.0485)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0338, |SHAP|=0.0338)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0186, |SHAP|=0.0186)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0161, |SHAP|=0.0161)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0158, |SHAP|=0.0158)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0108, |SHAP|=0.0108)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| WM88 | skin | -3.829560592827962 | more sensitive |
| SIGM5 | haematopoietic and lymphoid tissue | -3.822828883039944 | more sensitive |
| AU565 | breast | 3.648483547447452 | more resistant |
| PATU8988S | pancreas | 3.808029445149362 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | -3.617227035650021 | more sensitive |
| vincristine |  | -3.0974300500305807 | more sensitive |
| PLX-4720 | BRAF | 3.440772850439305 | more resistant |
| OSI-027 | MTOR | 3.588277548314656 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0018 - AZD7762 on MFE319
*Evidence: SHAP-0018*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **MFE319** (master_ccl_id=672) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.4999**
- RF-predicted log10(IC50): **-0.3873**
- Prediction error (observed - predicted): **-3.1126**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=0.3
- Cell cohort (245 pairs): mean=0.8967, q10=-1.1690, median=1.3052, q90=2.2622, sample percentile=1.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.500, RF OOF predicted -0.283 (Δ_model=-3.217), 20-NN mean=+1.312 (Δ_knn=-4.812). Drug target: CHEK1;CHEK2. Cell lineage: Uterus / Endometrial Carcinoma. Per-drug R² on held-out cells = 0.21.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7450, |SHAP|=0.7450)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3086, |SHAP|=0.3086)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1582, |SHAP|=0.1582)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0701, |SHAP|=0.0701)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0580, |SHAP|=0.0580)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0071** (fingerprint_bit; SHAP=+0.0469, |SHAP|=0.0469)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
7. **fp_0611** (fingerprint_bit; SHAP=-0.0446, |SHAP|=0.0446)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0415, |SHAP|=0.0415)  
  _value=9.7279, z=+1.43; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MDAMB453 | breast | -3.470663800856234 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.8928848395899935 | more sensitive |
| FQI-2 |  | -3.5814275776838884 | more sensitive |
| ML203 | PKM | 3.218010653647959 | more resistant |
| trametinib | MAP2K1;MAP2K2 | 3.7989985452794426 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0019 - Ki8751 on A673
*Evidence: SHAP-0019*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **Ki8751** (master_cpd_id=375560) |
| Gene Target | KDR;KIT;PDGFRA |
| Mechanism / Activity | inhibitor of VEGFR2, c-KIT, and PDGFRA |
| Cell Line | **A673** (master_ccl_id=37) |
| Tissue | bone |
| Histology | Ewings sarcoma peripheral primitive neuroectodermal tumor |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.0652**
- RF-predicted log10(IC50): **1.0543**
- Prediction error (observed - predicted): **-4.1195**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (215 pairs): mean=0.6387, q10=-1.3105, median=0.4948, q90=2.5859, sample percentile=0.9
- Cell cohort (322 pairs): mean=0.4417, q10=-1.3916, median=0.6051, q90=1.7935, sample percentile=1.9
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.065, RF OOF predicted +1.018 (Δ_model=-4.083), 20-NN mean=+0.789 (Δ_knn=-3.854). Drug target: KDR;KIT;PDGFRA. Cell lineage: Bone / Ewing Sarcoma. Per-drug R² on held-out cells = 0.20.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0931, |SHAP|=0.0931)  
  _value=4.5088, z=-0.25; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0856, |SHAP|=0.0856)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0566, |SHAP|=0.0566)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0723** (fingerprint_bit; SHAP=+0.0189, |SHAP|=0.0189)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0189, |SHAP|=0.0189)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0143, |SHAP|=0.0143)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0777** (fingerprint_bit; SHAP=+0.0116, |SHAP|=0.0116)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
8. **fp_0994** (fingerprint_bit; SHAP=-0.0105, |SHAP|=0.0105)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KMS21BM | haematopoietic and lymphoid tissue | -3.973903290054844 | more sensitive |
| MOLM6 | haematopoietic and lymphoid tissue | -3.0207090103658234 | more sensitive |
| NCIH1869 | lung | 3.777926445582964 | more resistant |
| SNU119 | ovary | 3.780936745539604 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| daporinad | NAMPT | -3.986269005005838 | more sensitive |
| GSK461364 | PLK1 | -3.6877616795487302 | more sensitive |
| BRD-K71781559 |  | 2.9398589376544404 | more resistant |
| selumetinib | MAP2K1;MAP2K2 | 3.20897975377804 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0020 - BI-2536 on OVCAR5
*Evidence: SHAP-0020*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BI-2536** (master_cpd_id=347813) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **OVCAR5** (master_ccl_id=909) |
| Tissue | n/a |
| Histology | n/a |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.8048**
- RF-predicted log10(IC50): **-0.8487**
- Prediction error (observed - predicted): **-2.9561**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (702 pairs): mean=-1.1707, q10=-3.0627, median=-1.4995, q90=0.8396, sample percentile=0.9
- Cell cohort (262 pairs): mean=0.7596, q10=-1.2224, median=1.0726, q90=2.0808, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.805, RF OOF predicted -0.509 (Δ_model=-3.296), 20-NN mean=+0.606 (Δ_knn=-4.411). Drug target: PLK1. Cell lineage: Ovary/Fallopian Tube / Ovarian Epithelial Tumor. Per-drug R² on held-out cells = 0.27.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.8879, |SHAP|=0.8879)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0876** (fingerprint_bit; SHAP=-0.4688, |SHAP|=0.4688)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
3. **fp_0582** (fingerprint_bit; SHAP=-0.0808, |SHAP|=0.0808)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
4. **fp_0059** (fingerprint_bit; SHAP=-0.0696, |SHAP|=0.0696)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0271** (fingerprint_bit; SHAP=-0.0693, |SHAP|=0.0693)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, BRD-K94991378_
6. **fp_0994** (fingerprint_bit; SHAP=-0.0402, |SHAP|=0.0402)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0360, |SHAP|=0.0360)  
  _value=8.7518, z=+1.12; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **fp_0600** (fingerprint_bit; SHAP=-0.0353, |SHAP|=0.0353)  
  _absent; representative SMARTS `[#6]:[#6](:[#7]):[#7]`; present in 5.0% of CTRPv2 compounds; example compounds: methotrexate, C6-ceramide, cerulenin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| LUDLU1 | lung | -3.922420843501675 | more sensitive |
| F36P | haematopoietic and lymphoid tissue | -3.921718750999285 | more sensitive |
| JHH6 | liver | 3.222415286063116 | more resistant |
| REC1 | haematopoietic and lymphoid tissue | 3.7237410463634473 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| triptolide |  | -3.800585077774668 | more sensitive |
| niclosamide | STAT3 | -3.7921750287826654 | more sensitive |
| BRD-K42260513 | EZH2 | 3.774916145626324 | more resistant |
| lapatinib | EGFR;ERBB2 | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0021 - etoposide on CAL62
*Evidence: SHAP-0021*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **etoposide** (master_cpd_id=48589) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **CAL62** (master_ccl_id=119) |
| Tissue | thyroid |
| Histology | carcinoma |
| Subtype | anaplastic carcinoma |

### Response Summary
- Observed log10(IC50): **-3.3349**
- RF-predicted log10(IC50): **0.3324**
- Prediction error (observed - predicted): **-3.6673**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (629 pairs): mean=0.4832, q10=-0.6115, median=0.4047, q90=1.6167, sample percentile=0.2
- Cell cohort (179 pairs): mean=0.3192, q10=-1.9297, median=0.6268, q90=1.9585, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.335, RF OOF predicted +0.376 (Δ_model=-3.710), 20-NN mean=+0.578 (Δ_knn=-3.913). Drug target: TOP2A. Cell lineage: Thyroid / Anaplastic Thyroid Cancer. Per-drug R² on held-out cells = 0.31.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.6198, |SHAP|=0.6198)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=+0.1918, |SHAP|=0.1918)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1199, |SHAP|=0.1199)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0876** (fingerprint_bit; SHAP=+0.0684, |SHAP|=0.0684)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
5. **fp_0582** (fingerprint_bit; SHAP=+0.0559, |SHAP|=0.0559)  
  _absent; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
6. **fp_0071** (fingerprint_bit; SHAP=+0.0507, |SHAP|=0.0507)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
7. **fp_0110** (fingerprint_bit; SHAP=-0.0473, |SHAP|=0.0473)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
8. **fp_0423** (fingerprint_bit; SHAP=-0.0452, |SHAP|=0.0452)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RS411 | haematopoietic and lymphoid tissue | -2.936037424216468 | more sensitive |
| SUDHL6 | haematopoietic and lymphoid tissue | -2.802739143122314 | more sensitive |
| TUHR14TKB | kidney | 3.910379643675116 | more resistant |
| HS766T | pancreas | 3.967575342851272 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.770803243008764 | more sensitive |
| SB-743921 | KIF11 | -3.1701098288468663 | more sensitive |
| CI-976 | ACAT1 | 2.9021728495718024 | more resistant |
| SKI-II | SPHK1 | 3.6003187481412158 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0022 - GDC-0879 on SKM1
*Evidence: SHAP-0022*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GDC-0879** (master_cpd_id=606248) |
| Gene Target | BRAF |
| Mechanism / Activity | inhibitor of BRAF |
| Cell Line | **SKM1** (master_ccl_id=1039) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **-2.8138**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **-3.5275**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (220 pairs): mean=1.3279, q10=-0.3013, median=1.5923, q90=2.3421, sample percentile=0.5
- Cell cohort (255 pairs): mean=0.2222, q10=-1.8108, median=0.4938, q90=1.7255, sample percentile=2.0
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-2.814, RF OOF predicted +0.720 (Δ_model=-3.534), 20-NN mean=+1.274 (Δ_knn=-4.088). Drug target: BRAF. Cell lineage: Myeloid / Acute Myeloid Leukemia. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2121, |SHAP|=0.2121)  
  _value=1.3145, z=-1.28; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0424, |SHAP|=0.0424)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0015** (fingerprint_bit; SHAP=+0.0331, |SHAP|=0.0331)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0290, |SHAP|=0.0290)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0200, |SHAP|=0.0200)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0792** (fingerprint_bit; SHAP=+0.0159, |SHAP|=0.0159)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0136, |SHAP|=0.0136)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HEP3B217 | liver | -2.2440440661059387 | more sensitive |
| NCIH2405 | lung | -1.3255730258877207 | more sensitive |
| RS411 | haematopoietic and lymphoid tissue | 3.7418028461032864 | more resistant |
| KASUMI2 | haematopoietic and lymphoid tissue | 3.862214844368879 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | -3.7705404013739727 | more sensitive |
| bosutinib | ABL1;SRC | -3.768898594516729 | more sensitive |
| ML031 | S1PR2 | 3.287297613529173 | more resistant |
| BRD-K09344309 |  | 3.5160303493553005 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0023 - teniposide on SNU878
*Evidence: SHAP-0023*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **teniposide** (master_cpd_id=27871) |
| Gene Target | TOP2A;TOP2B |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **SNU878** (master_ccl_id=1127) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed log10(IC50): **-3.7618**
- RF-predicted log10(IC50): **-0.0907**
- Prediction error (observed - predicted): **-3.6711**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (376 pairs): mean=-0.3665, q10=-1.9076, median=-0.1279, q90=0.9344, sample percentile=0.5
- Cell cohort (196 pairs): mean=0.3995, q10=-1.4840, median=0.7436, q90=1.7870, sample percentile=1.0
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-3.762, RF OOF predicted -0.069 (Δ_model=-3.693), 20-NN mean=+0.044 (Δ_knn=-3.806). Drug target: TOP2A;TOP2B. Cell lineage: Liver / Hepatocellular Carcinoma. Per-drug R² on held-out cells = 0.38.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7211, |SHAP|=0.7211)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=+0.1521, |SHAP|=0.1521)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1204, |SHAP|=0.1204)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0423** (fingerprint_bit; SHAP=-0.0772, |SHAP|=0.0772)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
5. **fp_0110** (fingerprint_bit; SHAP=-0.0558, |SHAP|=0.0558)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.0440, |SHAP|=0.0440)  
  _value=5.6133, z=+0.11; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0876** (fingerprint_bit; SHAP=+0.0439, |SHAP|=0.0439)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
8. **fp_0518** (fingerprint_bit; SHAP=+0.0364, |SHAP|=0.0364)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KARPAS620 | haematopoietic and lymphoid tissue | -3.959850677161819 | more sensitive |
| MOLT16 | haematopoietic and lymphoid tissue | -3.3460973808306345 | more sensitive |
| TUHR10TKB | kidney | 1.6704154459394318 | more resistant |
| KPL1 | breast | 2.128282069344347 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| rigosertib | PIK3CA;PIK3CB;PLK1 | -3.9196874711141527 | more sensitive |
| pandacostat | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 | -3.428436191784217 | more sensitive |
| BRD-K75293299 |  | 2.627088772159564 | more resistant |
| nelarabine | POLA1 | 2.880254998512972 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0024 - PD318088 on CHP212
*Evidence: SHAP-0024*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PD318088** (master_cpd_id=660410) |
| Gene Target | MAP2K1;MAP2K2 |
| Mechanism / Activity | inhibitor of MEK1 and MEK2 |
| Cell Line | **CHP212** (master_ccl_id=144) |
| Tissue | autonomic ganglia |
| Histology | neuroblastoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-2.9343**
- RF-predicted log10(IC50): **0.9380**
- Prediction error (observed - predicted): **-3.8723**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (421 pairs): mean=0.4477, q10=-1.4184, median=0.2765, q90=2.7340, sample percentile=0.2
- Cell cohort (248 pairs): mean=0.1812, q10=-1.8349, median=0.3430, q90=1.7599, sample percentile=2.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=-2.934, RF OOF predicted +0.987 (Δ_model=-3.922), 20-NN mean=+0.368 (Δ_knn=-3.303). Drug target: MAP2K1;MAP2K2. Cell lineage: Peripheral Nervous System / Neuroblastoma. Per-drug R² on held-out cells = 0.22.

### Top TreeSHAP Features
1. **fp_0235** (fingerprint_bit; SHAP=-0.1077, |SHAP|=0.1077)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: blebbistatin, pifithrin-alpha, ML162_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0805, |SHAP|=0.0805)  
  _value=4.4936, z=-0.25; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0595, |SHAP|=0.0595)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0407, |SHAP|=0.0407)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0726** (fingerprint_bit; SHAP=-0.0236, |SHAP|=0.0236)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]`; present in 84.2% of CTRPv2 compounds; example compounds: CIL55, BRD4132, BRD6340_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0180, |SHAP|=0.0180)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KO52 | haematopoietic and lymphoid tissue | -2.695367693833445 | more sensitive |
| SNU398 | liver | -2.521859498566052 | more sensitive |
| NCIH2126 | lung | 3.904359043761836 | more resistant |
| DMS53 | lung | 3.916400243588395 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| methotrexate | DHFR | -3.8909721787209386 | more sensitive |
| paclitaxel |  | -3.875639496200864 | more sensitive |
| NSC 74859 | STAT3 | 3.1216810550354848 | more resistant |
| L-685458 | APH1A;NCSTN;PSEN1;PSENEN | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0025 - 1S,3R-RSL-3 on LS1034
*Evidence: SHAP-0025*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **1S,3R-RSL-3** (master_cpd_id=609060) |
| Gene Target | GPX4 |
| Mechanism / Activity | synthetic lethal with HRAS in engineered cells; inhibitor of GPX4 |
| Cell Line | **LS1034** (master_ccl_id=626) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **3.4227**
- RF-predicted log10(IC50): **0.5075**
- Prediction error (observed - predicted): **+2.9152**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (784 pairs): mean=-0.7253, q10=-1.9264, median=-0.7926, q90=0.4911, sample percentile=99.9
- Cell cohort (252 pairs): mean=0.6265, q10=-1.3341, median=0.8438, q90=2.0359, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: LLM-explainable abnormal: observed log10(IC50)=+3.423, RF OOF predicted -0.663 (Δ_model=+4.085), 20-NN mean=+0.356 (Δ_knn=+3.067). Drug target: GPX4. Cell lineage: Bowel / Colorectal Adenocarcinoma. Per-drug R² on held-out cells = 0.27.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7781, |SHAP|=0.7781)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0876** (fingerprint_bit; SHAP=-0.1567, |SHAP|=0.1567)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
3. **CCN1 (3491)** (gene_expression; SHAP=-0.0985, |SHAP|=0.0985)  
  _value=1.4439, z=-1.24; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0518** (fingerprint_bit; SHAP=+0.0942, |SHAP|=0.0942)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **fp_0582** (fingerprint_bit; SHAP=-0.0825, |SHAP|=0.0825)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
6. **NQO1 (1728)** (gene_expression; SHAP=+0.0733, |SHAP|=0.0733)  
  _value=9.2976, z=+0.79; near the cross-cell-line mean; recurs in 58 predictable-drug RF signatures_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0702, |SHAP|=0.0702)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **ERBB3 (2065)** (gene_expression; SHAP=+0.0488, |SHAP|=0.0488)  
  _value=7.0761, z=+1.51; above the cross-cell-line mean; recurs in 19 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MHHCALL3 | haematopoietic and lymphoid tissue | -3.4143197348658587 | more sensitive |
| NOMO1 | haematopoietic and lymphoid tissue | -3.2484737631904275 | more sensitive |
| A2058 | skin | 1.832401846765979 | more resistant |
| COLO800 | skin | 3.446793450352585 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| CD-1530 | RARG | -3.5106068385127114 | more sensitive |
| LY-2183240 | FAAH | -3.2250905583503693 | more sensitive |
| sirolimus | MTOR | 3.260154853040917 | more resistant |
| pevonedistat | NAE1 | 3.395618351089708 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0026 - teniposide on CAL29
*Evidence: SHAP-0026*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **teniposide** (master_cpd_id=27871) |
| Gene Target | TOP2A;TOP2B |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **CAL29** (master_ccl_id=115) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **-0.0258**
- RF-predicted log10(IC50): **-0.0472**
- Prediction error (observed - predicted): **+0.0214**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (376 pairs): mean=-0.3665, q10=-1.9076, median=-0.1279, q90=0.9344, sample percentile=54.5
- Cell cohort (183 pairs): mean=0.4234, q10=-1.3798, median=0.6838, q90=1.8488, sample percentile=30.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=-0.026, RF OOF predicted -0.020 (Δ_model=-0.006), 20-NN mean=-0.038 (Δ_knn=+0.012). Drug target: TOP2A;TOP2B. Cell lineage: Bladder/Urinary Tract / Bladder Urothelial Carcinoma. Per-drug R² on held-out cells = 0.38.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7185, |SHAP|=0.7185)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=+0.1552, |SHAP|=0.1552)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1203, |SHAP|=0.1203)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0423** (fingerprint_bit; SHAP=-0.0767, |SHAP|=0.0767)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
5. **fp_0110** (fingerprint_bit; SHAP=-0.0558, |SHAP|=0.0558)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
6. **fp_0876** (fingerprint_bit; SHAP=+0.0495, |SHAP|=0.0495)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0469, |SHAP|=0.0469)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0440, |SHAP|=0.0440)  
  _value=8.3630, z=+0.99; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KARPAS620 | haematopoietic and lymphoid tissue | -3.959850677161819 | more sensitive |
| SNU878 | liver | -3.7617615660677353 | more sensitive |
| TUHR10TKB | kidney | 1.6704154459394318 | more resistant |
| KPL1 | breast | 2.128282069344347 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| KX2-391 | SRC | -3.79500917429421 | more sensitive |
| parbendazole |  | -3.651075404298096 | more sensitive |
| PLX-4720 | BRAF | 3.1337222548620445 | more resistant |
| I-BET151 | BRD2;BRD3;BRD4 | 3.862214844368879 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0027 - KPT185 on SH4
*Evidence: SHAP-0027*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KPT185** (master_cpd_id=660935) |
| Gene Target | XPO1 |
| Mechanism / Activity | inhibitor of exportin 1 |
| Cell Line | **SH4** (master_ccl_id=1025) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **0.3890**
- RF-predicted log10(IC50): **0.3960**
- Prediction error (observed - predicted): **-0.0070**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (533 pairs): mean=-0.2379, q10=-1.4401, median=-0.2953, q90=1.0788, sample percentile=73.5
- Cell cohort (221 pairs): mean=0.8095, q10=-1.2393, median=0.9284, q90=2.2622, sample percentile=29.4
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.389, RF OOF predicted +0.383 (Δ_model=+0.007), 20-NN mean=+0.401 (Δ_knn=-0.012). Drug target: XPO1. Cell lineage: Skin / Melanoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.4674, |SHAP|=0.4674)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1894, |SHAP|=0.1894)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0071** (fingerprint_bit; SHAP=-0.1601, |SHAP|=0.1601)  
  _present; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
4. **fp_0284** (fingerprint_bit; SHAP=-0.1335, |SHAP|=0.1335)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 7.7% of CTRPv2 compounds; example compounds: Bax channel blocker, isoliquiritigenin, curcumin_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0658, |SHAP|=0.0658)  
  _value=7.1816, z=+0.61; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0673** (fingerprint_bit; SHAP=+0.0548, |SHAP|=0.0548)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
7. **fp_0771** (fingerprint_bit; SHAP=-0.0389, |SHAP|=0.0389)  
  _present; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
8. **fp_0688** (fingerprint_bit; SHAP=+0.0315, |SHAP|=0.0315)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AM38 | central nervous system | -3.0159463087332163 | more sensitive |
| MOLM16 | haematopoietic and lymphoid tissue | -2.417106659364093 | more sensitive |
| HS895T | skin | 3.0163205565530915 | more resistant |
| NCIH2172 | lung | 3.230051853474518 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.735046434208283 | more sensitive |
| trametinib | MAP2K1;MAP2K2 | -3.721917606681183 | more sensitive |
| pandacostat | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 | 3.907369343718476 | more resistant |
| nelarabine | POLA1 | 3.961554742937993 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0028 - PRIMA-1 on SUDHL10
*Evidence: SHAP-0028*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PRIMA-1** (master_cpd_id=50131) |
| Gene Target | TP53 |
| Mechanism / Activity | re-activator of the pro-apoptotic activity of mutant p53 |
| Cell Line | **SUDHL10** (master_ccl_id=1140) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | diffuse large B cell lymphoma |

### Response Summary
- Observed log10(IC50): **0.7151**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **+0.0014**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (695 pairs): mean=1.5212, q10=0.7914, median=1.4892, q90=2.4957, sample percentile=8.1
- Cell cohort (213 pairs): mean=0.3240, q10=-1.3628, median=0.3960, q90=1.7949, sample percentile=60.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.715, RF OOF predicted +0.718 (Δ_model=-0.003), 20-NN mean=+0.731 (Δ_knn=-0.016). Drug target: TP53. Cell lineage: Lymphoid / Mature B-Cell Neoplasms. Per-drug R² on held-out cells = 0.32.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2095, |SHAP|=0.2095)  
  _value=1.2141, z=-1.31; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0307, |SHAP|=0.0307)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0274, |SHAP|=0.0274)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0200, |SHAP|=0.0200)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0176, |SHAP|=0.0176)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0152, |SHAP|=0.0152)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0015** (fingerprint_bit; SHAP=+0.0123, |SHAP|=0.0123)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0118, |SHAP|=0.0118)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SF126 | central nervous system | -2.2782858317732804 | more sensitive |
| DOHH2 | haematopoietic and lymphoid tissue | -1.0716122751844672 | more sensitive |
| A172 | central nervous system | 3.170064425126585 | more resistant |
| 8MGBA | central nervous system | 3.344279461046979 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.2073001342305267 | more sensitive |
| paclitaxel |  | -3.1272866493952587 | more sensitive |
| necrostatin-1 | RIPK1 | 2.991547840959746 | more resistant |
| myricetin |  | 3.4528140502658644 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0029 - PRIMA-1 on A204
*Evidence: SHAP-0029*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PRIMA-1** (master_cpd_id=50131) |
| Gene Target | TP53 |
| Mechanism / Activity | re-activator of the pro-apoptotic activity of mutant p53 |
| Cell Line | **A204** (master_ccl_id=26) |
| Tissue | soft tissue |
| Histology | rhabdoid tumor |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0627**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-0.0026**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (695 pairs): mean=1.5212, q10=0.7914, median=1.4892, q90=2.4957, sample percentile=23.5
- Cell cohort (355 pairs): mean=0.4788, q10=-1.3209, median=0.6554, q90=1.9305, sample percentile=63.9
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.063, RF OOF predicted +1.067 (Δ_model=-0.004), 20-NN mean=+1.044 (Δ_knn=+0.019). Drug target: TP53. Cell lineage: Kidney / Rhabdoid Cancer. Per-drug R² on held-out cells = 0.32.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0900, |SHAP|=0.0900)  
  _value=5.2402, z=-0.01; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0501, |SHAP|=0.0501)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0406, |SHAP|=0.0406)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0191, |SHAP|=0.0191)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0152, |SHAP|=0.0152)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0150, |SHAP|=0.0150)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0115, |SHAP|=0.0115)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SF126 | central nervous system | -2.2782858317732804 | more sensitive |
| DOHH2 | haematopoietic and lymphoid tissue | -1.0716122751844672 | more sensitive |
| A172 | central nervous system | 3.170064425126585 | more resistant |
| 8MGBA | central nervous system | 3.344279461046979 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | -3.896431184203615 | more sensitive |
| leptomycin B | XPO1 | -3.1065307403769165 | more sensitive |
| BRD-K42260513 | EZH2 | 3.633432047664253 | more resistant |
| BCL-LZH-4 |  | 3.693638046797049 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0030 - Compound 7d-cis on JVM3
*Evidence: SHAP-0030*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **Compound 7d-cis** (master_cpd_id=411805) |
| Gene Target | XPO1 |
| Mechanism / Activity | inhibitor of CRM1-mediated nucleocytoplasmic transport |
| Cell Line | **JVM3** (master_ccl_id=511) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | chronic lymphocytic leukaemia; small lymphocytic lymphoma |

### Response Summary
- Observed log10(IC50): **0.7573**
- RF-predicted log10(IC50): **0.7676**
- Prediction error (observed - predicted): **-0.0103**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (594 pairs): mean=1.1250, q10=0.3561, median=1.1986, q90=1.6641, sample percentile=22.2
- Cell cohort (264 pairs): mean=0.1542, q10=-1.8477, median=0.3737, q90=1.6365, sample percentile=63.6
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.757, RF OOF predicted +0.751 (Δ_model=+0.007), 20-NN mean=+0.738 (Δ_knn=+0.019). Drug target: XPO1. Cell lineage: Lymphoid / Mature B-Cell Neoplasms. Per-drug R² on held-out cells = 0.28.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.1787, |SHAP|=0.1787)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.1068, |SHAP|=0.1068)  
  _value=0.3996, z=-1.57; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0673** (fingerprint_bit; SHAP=+0.0810, |SHAP|=0.0810)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0688** (fingerprint_bit; SHAP=+0.0296, |SHAP|=0.0296)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
5. **fp_0141** (fingerprint_bit; SHAP=+0.0242, |SHAP|=0.0242)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **fp_0771** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
7. **fp_0263** (fingerprint_bit; SHAP=+0.0226, |SHAP|=0.0226)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
8. **fp_0223** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: gossypol, cytochalasin B, erastin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH2029 | lung | -2.540167254057764 | more sensitive |
| MALME3M | skin | -2.4243174412006803 | more sensitive |
| CAKI2 | kidney | 3.771905845669684 | more resistant |
| JHH6 | liver | 3.9585444429813528 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| temsirolimus | MTOR | -3.470875850005703 | more sensitive |
| neopeltolide |  | -3.39702822968223 | more sensitive |
| VU0155056 | PLD1;PLD2 | 3.061475055902689 | more resistant |
| C6-ceramide | MAPK1;PPP2CA;UGCG | 3.3173505522170728 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0031 - NVP-BSK805 on FU97
*Evidence: SHAP-0031*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NVP-BSK805** (master_cpd_id=660434) |
| Gene Target | JAK2 |
| Mechanism / Activity | inhibitor of Janus kinase 2 |
| Cell Line | **FU97** (master_ccl_id=259) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | diffuse adenocarcinoma |

### Response Summary
- Observed log10(IC50): **0.6578**
- RF-predicted log10(IC50): **0.6386**
- Prediction error (observed - predicted): **+0.0192**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (765 pairs): mean=1.0644, q10=0.6348, median=1.0904, q90=1.4828, sample percentile=13.1
- Cell cohort (196 pairs): mean=0.4157, q10=-1.5033, median=0.6396, q90=1.7319, sample percentile=51.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.658, RF OOF predicted +0.675 (Δ_model=-0.017), 20-NN mean=+0.650 (Δ_knn=+0.008). Drug target: JAK2. Cell lineage: Esophagus/Stomach / Esophagogastric Adenocarcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2377, |SHAP|=0.2377)  
  _value=2.3784, z=-0.94; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.1367, |SHAP|=0.1367)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0673** (fingerprint_bit; SHAP=-0.0823, |SHAP|=0.0823)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0538** (fingerprint_bit; SHAP=-0.0409, |SHAP|=0.0409)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0177, |SHAP|=0.0177)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0015** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0141** (fingerprint_bit; SHAP=+0.0164, |SHAP|=0.0164)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | -0.6124780049136491 | more sensitive |
| MV411 | haematopoietic and lymphoid tissue | -0.5812971797155102 | more sensitive |
| EFO21 | ovary | 2.1887259937511314 | more resistant |
| PECAPJ41CLONED2 | upper aerodigestive tract | 2.197686825635169 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dacarbazine |  | -3.97936010288796 | more sensitive |
| GSK461364 | PLK1 | -3.6710661989170377 | more sensitive |
| NVP-231 | CERK | 3.395618351089708 | more resistant |
| AZ-3146 | TTK | 3.862214844368879 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0032 - KW-2449 on F36P
*Evidence: SHAP-0032*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KW-2449** (master_cpd_id=660413) |
| Gene Target | AURKA;FLT3 |
| Mechanism / Activity | inhibitor of FLT3 and AURKA |
| Cell Line | **F36P** (master_ccl_id=253) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **0.7418**
- RF-predicted log10(IC50): **0.7676**
- Prediction error (observed - predicted): **-0.0258**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (764 pairs): mean=1.0118, q10=0.1305, median=1.1934, q90=1.6468, sample percentile=28.0
- Cell cohort (323 pairs): mean=0.4488, q10=-1.2250, median=0.5744, q90=1.8777, sample percentile=57.6
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.742, RF OOF predicted +0.736 (Δ_model=+0.006), 20-NN mean=+0.717 (Δ_knn=+0.024). Drug target: AURKA;FLT3. Cell lineage: Myeloid / Acute Myeloid Leukemia. Per-drug R² on held-out cells = 0.31.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.1875, |SHAP|=0.1875)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.1069, |SHAP|=0.1069)  
  _value=1.0098, z=-1.38; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0918, |SHAP|=0.0918)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0673** (fingerprint_bit; SHAP=+0.0885, |SHAP|=0.0885)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0518** (fingerprint_bit; SHAP=-0.0404, |SHAP|=0.0404)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0296, |SHAP|=0.0296)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0771** (fingerprint_bit; SHAP=+0.0229, |SHAP|=0.0229)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
8. **fp_0263** (fingerprint_bit; SHAP=+0.0226, |SHAP|=0.0226)  
  _absent; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -2.837989680310906 | more sensitive |
| MHHCALL3 | haematopoietic and lymphoid tissue | -2.6414368206643624 | more sensitive |
| 769P | kidney | 2.3487514697537315 | more resistant |
| ISHIKAWAHERAKLIO02ER | endometrium | 2.3567638360533087 | more resistant |

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

## RPT-0033 - nutlin-3 on NCIH23
*Evidence: SHAP-0033*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **nutlin-3** (master_cpd_id=411722) |
| Gene Target | MDM2 |
| Mechanism / Activity | inhibitor of p53-MDM2 interaction |
| Cell Line | **NCIH23** (master_ccl_id=127991) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | non small cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.0580**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-0.0073**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (759 pairs): mean=1.6504, q10=0.8266, median=1.8174, q90=2.1684, sample percentile=17.0
- Cell cohort (281 pairs): mean=0.4834, q10=-1.4742, median=0.6050, q90=1.8796, sample percentile=60.9
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.058, RF OOF predicted +1.058 (Δ_model=-0.000), 20-NN mean=+1.089 (Δ_knn=-0.031). Drug target: MDM2. Cell lineage: Lung / Non-Small Cell Lung Cancer. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0955, |SHAP|=0.0955)  
  _value=7.9572, z=+0.86; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0621, |SHAP|=0.0621)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0567, |SHAP|=0.0567)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0169, |SHAP|=0.0169)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0163, |SHAP|=0.0163)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0162, |SHAP|=0.0162)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0123, |SHAP|=0.0123)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0119, |SHAP|=0.0119)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MELHO | skin | -1.0680040966274147 | more sensitive |
| NCIH1581 | lung | -0.5459536490575645 | more sensitive |
| SKMEL28 | skin | 2.7806581432446795 | more resistant |
| SNB75 |  | 3.008192746670164 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| docetaxel |  | -3.55489199642353 | more sensitive |
| methotrexate | DHFR | -3.4109782761501783 | more sensitive |
| RAF265 | BRAF;KDR | 3.4859273497889025 | more resistant |
| bendamustine |  | 3.630421747707613 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0034 - vorinostat on YAPC
*Evidence: SHAP-0034*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **vorinostat** (master_cpd_id=56554) |
| Gene Target | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8 |
| Cell Line | **YAPC** (master_ccl_id=1277) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0550**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-0.0103**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (742 pairs): mean=0.4576, q10=-0.0227, median=0.4802, q90=0.8944, sample percentile=95.4
- Cell cohort (162 pairs): mean=0.6910, q10=-1.0756, median=0.9270, q90=2.0749, sample percentile=56.2
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.055, RF OOF predicted +1.068 (Δ_model=-0.013), 20-NN mean=+1.072 (Δ_knn=-0.017). Drug target: HDAC1;HDAC2;HDAC3;HDAC6;HDAC8. Cell lineage: Pancreas / Pancreatic Adenocarcinoma. Per-drug R² on held-out cells = 0.29.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0899, |SHAP|=0.0899)  
  _value=5.5028, z=+0.07; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0766, |SHAP|=0.0766)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0493, |SHAP|=0.0493)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0155, |SHAP|=0.0155)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0154, |SHAP|=0.0154)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0129, |SHAP|=0.0129)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0994** (fingerprint_bit; SHAP=-0.0106, |SHAP|=0.0106)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KMS27 | haematopoietic and lymphoid tissue | -3.269626996057971 | more sensitive |
| YD38 | upper aerodigestive tract | -1.493710838484675 | more sensitive |
| CJM | skin | 1.5469931477171994 | more resistant |
| HS822T | bone | 1.602382666919372 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.4549237666838177 | more sensitive |
| daporinad | NAMPT | -3.122252287449491 | more sensitive |
| BRD-K80183349 | HDAC1;HDAC2 | 2.8065026495752967 | more resistant |
| TG-100-115 | PIK3CD;PIK3CG | 3.651493847404092 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0035 - JQ-1 on SKMEL24
*Evidence: SHAP-0035*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **JQ-1** (master_cpd_id=616354) |
| Gene Target | BRDT |
| Mechanism / Activity | inhibitor of bromodomain (BRD) and extra-C terminal domain (BET) proteins |
| Cell Line | **SKMEL24** (master_ccl_id=1042) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0831**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.0178**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (636 pairs): mean=0.3443, q10=-0.8032, median=0.2006, q90=1.6939, sample percentile=72.2
- Cell cohort (226 pairs): mean=1.0541, q10=-0.6021, median=1.2461, q90=2.4307, sample percentile=46.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.083, RF OOF predicted +1.064 (Δ_model=+0.019), 20-NN mean=+1.071 (Δ_knn=+0.012). Drug target: BRDT. Cell lineage: Skin / Melanoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0908, |SHAP|=0.0908)  
  _value=6.9034, z=+0.52; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0762, |SHAP|=0.0762)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0503, |SHAP|=0.0503)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0175, |SHAP|=0.0175)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0164, |SHAP|=0.0164)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0148, |SHAP|=0.0148)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0120, |SHAP|=0.0120)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0096, |SHAP|=0.0096)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AMO1 | haematopoietic and lymphoid tissue | -2.868436018946039 | more sensitive |
| SCC25 | upper aerodigestive tract | -2.790840405808785 | more sensitive |
| OV56 | ovary | 3.461844950135784 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 3.476896449918983 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dabrafenib | BRAF | -3.1799759431901777 | more sensitive |
| tandutinib | FLT3;KIT | -2.698617739713456 | more sensitive |
| IC-87114 | PIK3CD | 3.7869573454528833 | more resistant |
| PYR-41 | UBA1 | 3.808029445149362 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0036 - GDC-0879 on SNU61
*Evidence: SHAP-0036*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GDC-0879** (master_cpd_id=606248) |
| Gene Target | BRAF |
| Mechanism / Activity | inhibitor of BRAF |
| Cell Line | **SNU61** (master_ccl_id=1115) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0741**
- RF-predicted log10(IC50): **1.0369**
- Prediction error (observed - predicted): **+0.0371**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (220 pairs): mean=1.3279, q10=-0.3013, median=1.5923, q90=2.3421, sample percentile=34.5
- Cell cohort (235 pairs): mean=0.6059, q10=-1.1394, median=0.7888, q90=1.9318, sample percentile=60.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.074, RF OOF predicted +1.052 (Δ_model=+0.022), 20-NN mean=+1.084 (Δ_knn=-0.010). Drug target: BRAF. Cell lineage: Bowel / Colorectal Adenocarcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0662, |SHAP|=0.0662)  
  _value=2.7128, z=-0.83; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0561, |SHAP|=0.0561)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0471, |SHAP|=0.0471)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0318, |SHAP|=0.0318)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0204, |SHAP|=0.0204)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0792** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0132, |SHAP|=0.0132)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SKM1 | haematopoietic and lymphoid tissue | -2.8138291508357574 | more sensitive |
| HEP3B217 | liver | -2.2440440661059387 | more sensitive |
| RS411 | haematopoietic and lymphoid tissue | 3.7418028461032864 | more resistant |
| KASUMI2 | haematopoietic and lymphoid tissue | 3.862214844368879 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.6526124137441833 | more sensitive |
| paclitaxel |  | -3.3950048741771863 | more sensitive |
| BRD-K80183349 | HDAC1;HDAC2 | 3.2059694538214 | more resistant |
| NPC-26 |  | 3.648483547447452 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0037 - NVP-BSK805 on 253JBV
*Evidence: SHAP-0037*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NVP-BSK805** (master_cpd_id=660434) |
| Gene Target | JAK2 |
| Mechanism / Activity | inhibitor of Janus kinase 2 |
| Cell Line | **253JBV** (master_ccl_id=9) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **1.0458**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-0.0147**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (765 pairs): mean=1.0644, q10=0.6348, median=1.0904, q90=1.4828, sample percentile=45.4
- Cell cohort (160 pairs): mean=0.7117, q10=-0.9923, median=0.9971, q90=1.9569, sample percentile=51.2
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.046, RF OOF predicted +1.063 (Δ_model=-0.018), 20-NN mean=+1.028 (Δ_knn=+0.018). Drug target: JAK2. Cell lineage: Bladder/Urinary Tract / Bladder Urothelial Carcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1424, |SHAP|=0.1424)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.1023, |SHAP|=0.1023)  
  _value=8.7218, z=+1.11; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0673** (fingerprint_bit; SHAP=-0.0755, |SHAP|=0.0755)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0141** (fingerprint_bit; SHAP=+0.0434, |SHAP|=0.0434)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0187, |SHAP|=0.0187)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0179, |SHAP|=0.0179)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | -0.6124780049136491 | more sensitive |
| MV411 | haematopoietic and lymphoid tissue | -0.5812971797155102 | more sensitive |
| EFO21 | ovary | 2.1887259937511314 | more resistant |
| PECAPJ41CLONED2 | upper aerodigestive tract | 2.197686825635169 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| pazopanib | FLT1;FLT3;KDR;KIT;PDGFRB | -3.1760475326425723 | more sensitive |
| KU-60019 | ATM | -2.46160653705852 | more sensitive |
| phloretin | SLC5A1 | 3.1283217971184905 | more resistant |
| ML083 | PKM | 3.8050191451927216 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0038 - SN-38 on HCC1500
*Evidence: SHAP-0038*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SN-38** (master_cpd_id=375637) |
| Gene Target | TOP1 |
| Mechanism / Activity | metabolite of irinotecan; inhibitor of topoisomerase I |
| Cell Line | **HCC1500** (master_ccl_id=305) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **-1.0253**
- RF-predicted log10(IC50): **-0.9158**
- Prediction error (observed - predicted): **-0.1095**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (527 pairs): mean=-1.4223, q10=-2.8421, median=-1.3624, q90=-0.1771, sample percentile=62.2
- Cell cohort (267 pairs): mean=0.8283, q10=-0.9914, median=1.0085, q90=2.2550, sample percentile=10.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=-1.025, RF OOF predicted -1.012 (Δ_model=-0.014), 20-NN mean=-1.048 (Δ_knn=+0.022). Drug target: TOP1. Cell lineage: Breast / Breast Ductal Carcinoma In Situ. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.5044, |SHAP|=0.5044)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **fp_0059** (fingerprint_bit; SHAP=-0.4343, |SHAP|=0.4343)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
3. **fp_0240** (fingerprint_bit; SHAP=-0.1754, |SHAP|=0.1754)  
  _present; representative SMARTS `[#6]:[#6](-[#8]-[#6](:[#6]):[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: cytochalasin B, BRD-A94377914, CIL41_
4. **fp_0065** (fingerprint_bit; SHAP=-0.1725, |SHAP|=0.1725)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
5. **fp_0667** (fingerprint_bit; SHAP=-0.1604, |SHAP|=0.1604)  
  _present; representative SMARTS `[#7]-[#6]-[#6]`; present in 9.6% of CTRPv2 compounds; example compounds: CIL55, BRD4132, cimetidine_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.1185, |SHAP|=0.1185)  
  _value=4.8499, z=-0.14; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0227** (fingerprint_bit; SHAP=-0.1080, |SHAP|=0.1080)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0141** (fingerprint_bit; SHAP=-0.0821, |SHAP|=0.0821)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNUC1 | large intestine | -3.861294497519686 | more sensitive |
| HEC50B | endometrium | -3.795937834345268 | more sensitive |
| ISTMES1 | pleura | 2.642140271942763 | more resistant |
| PANC0504 | pancreas | 3.9916577425043904 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.9268186754244576 | more sensitive |
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.278931604706384 | more sensitive |
| Ki8751 | KDR;KIT;PDGFRA | 3.7688955457130446 | more resistant |
| tamoxifen | ESR1;ESR2 | 3.8832869440653575 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0039 - apicidin on T84
*Evidence: SHAP-0039*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **apicidin** (master_cpd_id=61097) |
| Gene Target | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8 |
| Cell Line | **T84** (master_ccl_id=1176) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **0.0286**
- RF-predicted log10(IC50): **0.0160**
- Prediction error (observed - predicted): **+0.0127**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (762 pairs): mean=-0.1742, q10=-1.0946, median=-0.0472, q90=0.4703, sample percentile=55.8
- Cell cohort (278 pairs): mean=0.3821, q10=-1.4540, median=0.5911, q90=1.7764, sample percentile=31.7
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.029, RF OOF predicted +0.008 (Δ_model=+0.021), 20-NN mean=+0.013 (Δ_knn=+0.016). Drug target: HDAC1;HDAC2;HDAC3;HDAC6;HDAC8. Cell lineage: Bowel / Colorectal Adenocarcinoma. Per-drug R² on held-out cells = 0.37.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7593, |SHAP|=0.7593)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0876** (fingerprint_bit; SHAP=-0.4527, |SHAP|=0.4527)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
3. **fp_0271** (fingerprint_bit; SHAP=+0.0905, |SHAP|=0.0905)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, BRD-K94991378_
4. **fp_0582** (fingerprint_bit; SHAP=-0.0471, |SHAP|=0.0471)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
5. **fp_0617** (fingerprint_bit; SHAP=+0.0455, |SHAP|=0.0455)  
  _present; representative SMARTS `[#7]-[#6]-[#6](-[#7]-[#6])=[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: nutlin-3, BMS-754807, bafilomycin A1_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.0448, |SHAP|=0.0448)  
  _value=3.9419, z=-0.43; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0437, |SHAP|=0.0437)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **fp_0218** (fingerprint_bit; SHAP=+0.0430, |SHAP|=0.0430)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#7]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD4132, myricetin, manumycin A_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| GA10 | haematopoietic and lymphoid tissue | -2.7444537586026185 | more sensitive |
| MONOMAC6 | haematopoietic and lymphoid tissue | -2.493220735640912 | more sensitive |
| RERFLCAI | lung | 1.502814269084568 | more resistant |
| SW1783 | central nervous system | 1.5424776977822396 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| quizartinib | FLT3 | -3.935260294073839 | more sensitive |
| BRD-K28456706 | HNF4A | -3.8035638981987687 | more sensitive |
| BRD-M00053801 | BCL2 | 3.5942981482279355 | more resistant |
| AZD7545 | PDK2 | 3.9254311434583142 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0040 - indisulam on DANG
*Evidence: SHAP-0040*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **indisulam** (master_cpd_id=411874) |
| Gene Target | CA9 |
| Mechanism / Activity | inhibitor of carbonic anhydrase isoform IX |
| Cell Line | **DANG** (master_ccl_id=201) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **1.0635**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-0.0017**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (431 pairs): mean=0.7254, q10=-0.3568, median=0.4787, q90=1.8854, sample percentile=58.9
- Cell cohort (231 pairs): mean=0.9611, q10=-0.9276, median=1.2282, q90=2.4254, sample percentile=45.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.064, RF OOF predicted +1.067 (Δ_model=-0.003), 20-NN mean=+1.024 (Δ_knn=+0.039). Drug target: CA9. Cell lineage: Pancreas / Pancreatic Adenocarcinoma. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0881, |SHAP|=0.0881)  
  _value=4.2487, z=-0.33; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0830, |SHAP|=0.0830)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0482, |SHAP|=0.0482)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0353, |SHAP|=0.0353)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0176, |SHAP|=0.0176)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0138, |SHAP|=0.0138)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0109, |SHAP|=0.0109)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH2081 | lung | -3.4709701472858043 | more sensitive |
| HDLM2 | haematopoietic and lymphoid tissue | -1.51638765981231 | more sensitive |
| OAW28 | ovary | 3.455824350222504 | more resistant |
| CCFSTTG1 | central nervous system | 3.7418028461032864 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K71935468 |  | -3.2036860598677817 | more sensitive |
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.138017527392144 | more sensitive |
| myricetin |  | 3.654504147360732 | more resistant |
| quizartinib | FLT3 | 3.702668946666969 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0041 - selumetinib on NCIH2009
*Evidence: SHAP-0041*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **selumetinib** (master_cpd_id=348991) |
| Gene Target | MAP2K1;MAP2K2 |
| Mechanism / Activity | inhibitor of MEK1 and MEK2 |
| Cell Line | **NCIH2009** (master_ccl_id=155476) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **1.0805**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **+0.0201**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (608 pairs): mean=1.4319, q10=-0.6183, median=1.8027, q90=2.7461, sample percentile=32.2
- Cell cohort (188 pairs): mean=0.5811, q10=-1.4325, median=0.7199, q90=2.0216, sample percentile=61.7
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.081, RF OOF predicted +1.047 (Δ_model=+0.033), 20-NN mean=+1.090 (Δ_knn=-0.010). Drug target: MAP2K1;MAP2K2. Cell lineage: Lung / Non-Small Cell Lung Cancer. Per-drug R² on held-out cells = 0.22.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0992, |SHAP|=0.0992)  
  _value=6.2678, z=+0.32; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0766, |SHAP|=0.0766)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0486, |SHAP|=0.0486)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0188, |SHAP|=0.0188)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0183, |SHAP|=0.0183)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0174, |SHAP|=0.0174)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0132, |SHAP|=0.0132)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0538** (fingerprint_bit; SHAP=-0.0123, |SHAP|=0.0123)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MINO | haematopoietic and lymphoid tissue | -3.491184776129752 | more sensitive |
| CORL95 | lung | -2.7134906464211794 | more sensitive |
| OSRC2 | kidney | 3.970585642807912 | more resistant |
| GOS3 | central nervous system | 3.979616542677832 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GSK461364 | PLK1 | -3.293650295953027 | more sensitive |
| ELCPK |  | -3.151641603793197 | more sensitive |
| IU1 | USP14 | 3.5371024490517797 | more resistant |
| temsirolimus | MTOR | 3.7237410463634473 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0042 - teniposide on FUOV1
*Evidence: SHAP-0042*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **teniposide** (master_cpd_id=27871) |
| Gene Target | TOP2A;TOP2B |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **FUOV1** (master_ccl_id=261) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | serous carcinoma |

### Response Summary
- Observed log10(IC50): **0.0211**
- RF-predicted log10(IC50): **-0.0472**
- Prediction error (observed - predicted): **+0.0683**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (376 pairs): mean=-0.3665, q10=-1.9076, median=-0.1279, q90=0.9344, sample percentile=56.4
- Cell cohort (166 pairs): mean=0.7136, q10=-0.8373, median=0.8684, q90=1.9968, sample percentile=24.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.021, RF OOF predicted -0.020 (Δ_model=+0.041), 20-NN mean=+0.023 (Δ_knn=-0.001). Drug target: TOP2A;TOP2B. Cell lineage: Ovary/Fallopian Tube / Ovarian Epithelial Tumor. Per-drug R² on held-out cells = 0.38.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7254, |SHAP|=0.7254)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=+0.1617, |SHAP|=0.1617)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1205, |SHAP|=0.1205)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0423** (fingerprint_bit; SHAP=-0.0757, |SHAP|=0.0757)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0587, |SHAP|=0.0587)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0110** (fingerprint_bit; SHAP=-0.0558, |SHAP|=0.0558)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0448, |SHAP|=0.0448)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0441, |SHAP|=0.0441)  
  _value=7.9505, z=+0.86; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KARPAS620 | haematopoietic and lymphoid tissue | -3.959850677161819 | more sensitive |
| SNU878 | liver | -3.7617615660677353 | more sensitive |
| TUHR10TKB | kidney | 1.6704154459394318 | more resistant |
| KPL1 | breast | 2.128282069344347 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.4043837210088035 | more sensitive |
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | -3.20979794709928 | more sensitive |
| temozolomide |  | 3.564195148661537 | more resistant |
| procarbazine |  | 3.9404826432415136 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0043 - etoposide on MOLM16
*Evidence: SHAP-0043*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **etoposide** (master_cpd_id=48589) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **MOLM16** (master_ccl_id=693) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **-0.0727**
- RF-predicted log10(IC50): **0.1059**
- Prediction error (observed - predicted): **-0.1786**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (629 pairs): mean=0.4832, q10=-0.6115, median=0.4047, q90=1.6167, sample percentile=25.9
- Cell cohort (259 pairs): mean=0.0891, q10=-1.8323, median=0.3082, q90=1.7002, sample percentile=39.4
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=-0.073, RF OOF predicted -0.038 (Δ_model=-0.035), 20-NN mean=-0.082 (Δ_knn=+0.009). Drug target: TOP2A. Cell lineage: Myeloid / Acute Myeloid Leukemia. Per-drug R² on held-out cells = 0.31.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.5436, |SHAP|=0.5436)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=+0.1951, |SHAP|=0.1951)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1195, |SHAP|=0.1195)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.1038, |SHAP|=0.1038)  
  _value=0.7315, z=-1.47; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0938, |SHAP|=0.0938)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0110** (fingerprint_bit; SHAP=-0.0780, |SHAP|=0.0780)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
7. **fp_0582** (fingerprint_bit; SHAP=+0.0549, |SHAP|=0.0549)  
  _absent; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **fp_0071** (fingerprint_bit; SHAP=+0.0502, |SHAP|=0.0502)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CAL62 | thyroid | -3.334947385168918 | more sensitive |
| RS411 | haematopoietic and lymphoid tissue | -2.936037424216468 | more sensitive |
| TUHR14TKB | kidney | 3.910379643675116 | more resistant |
| HS766T | pancreas | 3.967575342851272 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.9519264960551865 | more sensitive |
| methotrexate | DHFR | -3.9305472173264175 | more sensitive |
| ML031 | S1PR2 | 3.113271560174685 | more resistant |
| UNC0321 | EHMT2 | 3.588277548314656 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0044 - PX-12 on RH18
*Evidence: SHAP-0044*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PX-12** (master_cpd_id=609124) |
| Gene Target | TXN |
| Mechanism / Activity | inhibitor of thioredoxin-1 |
| Cell Line | **RH18** (master_ccl_id=973) |
| Tissue | soft tissue |
| Histology | rhabdomyosarcoma |
| Subtype | alveolar |

### Response Summary
- Observed log10(IC50): **1.4239**
- RF-predicted log10(IC50): **1.4309**
- Prediction error (observed - predicted): **-0.0070**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (655 pairs): mean=1.4466, q10=0.6765, median=1.5574, q90=2.1563, sample percentile=40.5
- Cell cohort (245 pairs): mean=0.7651, q10=-0.7591, median=0.9049, q90=1.9630, sample percentile=73.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.424, RF OOF predicted +1.428 (Δ_model=-0.004), 20-NN mean=+1.470 (Δ_knn=-0.047). Drug target: TXN. Cell lineage: Soft Tissue / Rhabdomyosarcoma. Per-drug R² on held-out cells = 0.29.

### Top TreeSHAP Features
1. **fp_0777** (fingerprint_bit; SHAP=-0.7414, |SHAP|=0.7414)  
  _present; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
2. **fp_0141** (fingerprint_bit; SHAP=+0.5402, |SHAP|=0.5402)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0535** (fingerprint_bit; SHAP=+0.1124, |SHAP|=0.1124)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
4. **fp_0518** (fingerprint_bit; SHAP=+0.0813, |SHAP|=0.0813)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0804, |SHAP|=0.0804)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0175** (fingerprint_bit; SHAP=+0.0785, |SHAP|=0.0785)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 37.8% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, ML006_
7. **fp_0994** (fingerprint_bit; SHAP=+0.0775, |SHAP|=0.0775)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
8. **fp_0157** (fingerprint_bit; SHAP=+0.0521, |SHAP|=0.0521)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| COLO205 | large intestine | -2.5040946572930176 | more sensitive |
| JHH5 | liver | -1.738402172545869 | more sensitive |
| GMS10 | central nervous system | 3.2803466439679525 | more resistant |
| SW1353 | bone | 3.85017364454232 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| 1S,3R-RSL-3 | GPX4 | -2.671027573488263 | more sensitive |
| ISOX | HDAC6 | -2.405709532731568 | more sensitive |
| bendamustine |  | 3.783947045496244 | more resistant |
| BRD6340 |  | 3.859204544412239 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0045 - PX-12 on ONCODG1
*Evidence: SHAP-0045*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PX-12** (master_cpd_id=609124) |
| Gene Target | TXN |
| Mechanism / Activity | inhibitor of thioredoxin-1 |
| Cell Line | **ONCODG1** (master_ccl_id=898) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **1.3392**
- RF-predicted log10(IC50): **1.3879**
- Prediction error (observed - predicted): **-0.0487**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (655 pairs): mean=1.4466, q10=0.6765, median=1.5574, q90=2.1563, sample percentile=37.4
- Cell cohort (232 pairs): mean=0.6554, q10=-1.1122, median=0.9248, q90=2.0952, sample percentile=69.4
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.339, RF OOF predicted +1.376 (Δ_model=-0.037), 20-NN mean=+1.350 (Δ_knn=-0.011). Drug target: TXN. Cell lineage: Ovary/Fallopian Tube / Ovarian Epithelial Tumor. Per-drug R² on held-out cells = 0.29.

### Top TreeSHAP Features
1. **fp_0777** (fingerprint_bit; SHAP=-0.7644, |SHAP|=0.7644)  
  _present; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
2. **fp_0141** (fingerprint_bit; SHAP=+0.5757, |SHAP|=0.5757)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0535** (fingerprint_bit; SHAP=+0.1167, |SHAP|=0.1167)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
4. **fp_0876** (fingerprint_bit; SHAP=+0.0816, |SHAP|=0.0816)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
5. **fp_0518** (fingerprint_bit; SHAP=+0.0789, |SHAP|=0.0789)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
6. **fp_0994** (fingerprint_bit; SHAP=+0.0776, |SHAP|=0.0776)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **fp_0175** (fingerprint_bit; SHAP=+0.0714, |SHAP|=0.0714)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 37.8% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, ML006_
8. **fp_0071** (fingerprint_bit; SHAP=+0.0527, |SHAP|=0.0527)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| COLO205 | large intestine | -2.5040946572930176 | more sensitive |
| JHH5 | liver | -1.738402172545869 | more sensitive |
| GMS10 | central nervous system | 3.2803466439679525 | more resistant |
| SW1353 | bone | 3.85017364454232 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ELCPK |  | -3.5538017074578203 | more sensitive |
| vincristine |  | -3.065901414240462 | more sensitive |
| temsirolimus | MTOR | 3.3263814520869923 | more resistant |
| brivanib | FLT1;KDR | 3.461844950135784 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0046 - olaparib on SNU398
*Evidence: SHAP-0046*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **olaparib** (master_cpd_id=411867) |
| Gene Target | PARP1;PARP2 |
| Mechanism / Activity | inhibitor of poly (ADP-ribose) polymerase 1 and 2 |
| Cell Line | **SNU398** (master_ccl_id=1101) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed log10(IC50): **1.0785**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.0132**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (512 pairs): mean=1.8866, q10=0.7167, median=2.0256, q90=2.9214, sample percentile=21.1
- Cell cohort (207 pairs): mean=0.6195, q10=-1.3006, median=0.9765, q90=2.0192, sample percentile=56.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.079, RF OOF predicted +1.055 (Δ_model=+0.023), 20-NN mean=+1.111 (Δ_knn=-0.032). Drug target: PARP1;PARP2. Cell lineage: Liver / Hepatocellular Carcinoma. Per-drug R² on held-out cells = 0.23.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1927, |SHAP|=0.1927)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0883, |SHAP|=0.0883)  
  _value=4.9507, z=-0.11; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0509, |SHAP|=0.0509)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0518** (fingerprint_bit; SHAP=-0.0444, |SHAP|=0.0444)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **fp_0876** (fingerprint_bit; SHAP=-0.0374, |SHAP|=0.0374)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0330, |SHAP|=0.0330)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0193, |SHAP|=0.0193)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0513** (fingerprint_bit; SHAP=+0.0180, |SHAP|=0.0180)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCO2 | haematopoietic and lymphoid tissue | -1.3328125943479665 | more sensitive |
| SKCO1 | large intestine | -1.0208131448057514 | more sensitive |
| HCC1833 | lung | 3.783947045496244 | more resistant |
| TOLEDO | haematopoietic and lymphoid tissue | 3.9194105435450353 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| gossypol | BCL2;BCL2L1;LDHA;LDHB;LDHC | -3.8499446531445103 | more sensitive |
| leptomycin B | XPO1 | -3.7577705901300127 | more sensitive |
| selumetinib | MAP2K1;MAP2K2 | 3.7237410463634473 | more resistant |
| ML239 |  | 3.9314517433715945 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0047 - TG-101348 on JHH4
*Evidence: SHAP-0047*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **TG-101348** (master_cpd_id=411808) |
| Gene Target | JAK2 |
| Mechanism / Activity | inhibitor of Janus kinase 2 |
| Cell Line | **JHH4** (master_ccl_id=488) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed log10(IC50): **0.8964**
- RF-predicted log10(IC50): **0.8849**
- Prediction error (observed - predicted): **+0.0114**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (768 pairs): mean=0.6573, q10=0.1184, median=0.6629, q90=1.2268, sample percentile=68.1
- Cell cohort (272 pairs): mean=0.7239, q10=-1.2744, median=0.8991, q90=2.1782, sample percentile=50.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.896, RF OOF predicted +0.943 (Δ_model=-0.047), 20-NN mean=+0.886 (Δ_knn=+0.010). Drug target: JAK2. Cell lineage: Liver / Hepatocellular Carcinoma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **fp_0059** (fingerprint_bit; SHAP=-0.1567, |SHAP|=0.1567)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
2. **fp_0017** (fingerprint_bit; SHAP=+0.1150, |SHAP|=0.1150)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0065** (fingerprint_bit; SHAP=+0.0846, |SHAP|=0.0846)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
4. **CCN1 (3491)** (gene_expression; SHAP=+0.0703, |SHAP|=0.0703)  
  _value=7.0415, z=+0.57; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0673** (fingerprint_bit; SHAP=-0.0690, |SHAP|=0.0690)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
6. **fp_0227** (fingerprint_bit; SHAP=-0.0404, |SHAP|=0.0404)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
7. **fp_0141** (fingerprint_bit; SHAP=+0.0372, |SHAP|=0.0372)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
8. **fp_0513** (fingerprint_bit; SHAP=+0.0180, |SHAP|=0.0180)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH716 | large intestine | -2.1369492669066075 | more sensitive |
| JVM2 | haematopoietic and lymphoid tissue | -1.4095233104298224 | more sensitive |
| MESSA | soft tissue | 3.36551535152331 | more resistant |
| SU8686 | pancreas | 3.829101544845841 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| TW-37 | BCL2;BCL2L1 | -3.6047426994611502 | more sensitive |
| oligomycin A | ATP5L2 | -3.545900015996808 | more sensitive |
| sildenafil | PDE5A | 3.829101544845841 | more resistant |
| JW-480 | NCEH1 | 3.877266344152078 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0048 - BRD-K80183349 on KYSE70
*Evidence: SHAP-0048*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K80183349** (master_cpd_id=376307) |
| Gene Target | HDAC1;HDAC2 |
| Mechanism / Activity | inhibitor of HDAC1 and HDAC2 |
| Cell Line | **KYSE70** (master_ccl_id=589) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **0.9910**
- RF-predicted log10(IC50): **1.0253**
- Prediction error (observed - predicted): **-0.0343**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (390 pairs): mean=1.6071, q10=0.4791, median=1.7302, q90=2.5914, sample percentile=26.4
- Cell cohort (191 pairs): mean=0.6907, q10=-1.0958, median=0.8486, q90=2.1406, sample percentile=55.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+0.991, RF OOF predicted +1.003 (Δ_model=-0.012), 20-NN mean=+1.043 (Δ_knn=-0.052). Drug target: HDAC1;HDAC2. Cell lineage: Esophagus/Stomach / Esophageal Squamous Cell Carcinoma. Per-drug R² on held-out cells = 0.33.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1296, |SHAP|=0.1296)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0518** (fingerprint_bit; SHAP=-0.0694, |SHAP|=0.0694)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
3. **CCN1 (3491)** (gene_expression; SHAP=+0.0586, |SHAP|=0.0586)  
  _value=2.6955, z=-0.83; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0489, |SHAP|=0.0489)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0184, |SHAP|=0.0184)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0184, |SHAP|=0.0184)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0140, |SHAP|=0.0140)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0102, |SHAP|=0.0102)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AMO1 | haematopoietic and lymphoid tissue | -0.9134515731248348 | more sensitive |
| SUDHL4 | haematopoietic and lymphoid tissue | -0.5968226640594746 | more sensitive |
| PECAPJ41CLONED2 | upper aerodigestive tract | 3.8411427446724 | more resistant |
| YD8 | upper aerodigestive tract | 3.85318394449896 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | -3.35917167763552 | more sensitive |
| SB-743921 | KIF11 | -3.1647153377127557 | more sensitive |
| KU-60019 | ATM | 3.576236348488097 | more resistant |
| VAF-347 | AHR | 3.8321118448024807 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0049 - olaparib on RL952
*Evidence: SHAP-0049*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **olaparib** (master_cpd_id=411867) |
| Gene Target | PARP1;PARP2 |
| Mechanism / Activity | inhibitor of poly (ADP-ribose) polymerase 1 and 2 |
| Cell Line | **RL952** (master_ccl_id=981) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | mixed adenosquamous carcinoma |

### Response Summary
- Observed log10(IC50): **1.0778**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **+0.0125**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (512 pairs): mean=1.8866, q10=0.7167, median=2.0256, q90=2.9214, sample percentile=20.9
- Cell cohort (232 pairs): mean=0.4495, q10=-1.3837, median=0.6404, q90=1.9279, sample percentile=65.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.078, RF OOF predicted +1.062 (Δ_model=+0.016), 20-NN mean=+1.127 (Δ_knn=-0.049). Drug target: PARP1;PARP2. Cell lineage: Uterus / Endometrial Carcinoma. Per-drug R² on held-out cells = 0.23.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1726, |SHAP|=0.1726)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0884, |SHAP|=0.0884)  
  _value=7.4155, z=+0.69; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0503, |SHAP|=0.0503)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0518** (fingerprint_bit; SHAP=-0.0433, |SHAP|=0.0433)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
5. **fp_0876** (fingerprint_bit; SHAP=-0.0342, |SHAP|=0.0342)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0330, |SHAP|=0.0330)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0181, |SHAP|=0.0181)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0513** (fingerprint_bit; SHAP=+0.0180, |SHAP|=0.0180)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCO2 | haematopoietic and lymphoid tissue | -1.3328125943479665 | more sensitive |
| SKCO1 | large intestine | -1.0208131448057514 | more sensitive |
| HCC1833 | lung | 3.783947045496244 | more resistant |
| TOLEDO | haematopoietic and lymphoid tissue | 3.9194105435450353 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SMER-3 | CUL1;SKP1 | -3.81686271254478 | more sensitive |
| tivozanib | FLT1;FLT3;KDR | -3.6748402442280015 | more sensitive |
| BRD-K29313308 | HDAC3 | 3.3986286510463475 | more resistant |
| GSK-3 inhibitor IX |  | 3.702668946666969 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0050 - JQ-1 on SF295
*Evidence: SHAP-0050*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **JQ-1** (master_cpd_id=616354) |
| Gene Target | BRDT |
| Mechanism / Activity | inhibitor of bromodomain (BRD) and extra-C terminal domain (BET) proteins |
| Cell Line | **SF295** (master_ccl_id=1018) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma Grade IV |

### Response Summary
- Observed log10(IC50): **1.0301**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-0.0352**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (636 pairs): mean=0.3443, q10=-0.8032, median=0.2006, q90=1.6939, sample percentile=70.3
- Cell cohort (146 pairs): mean=0.7466, q10=-0.8610, median=0.9946, q90=2.1007, sample percentile=52.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: LLM-explainable normal: observed log10(IC50)=+1.030, RF OOF predicted +1.058 (Δ_model=-0.028), 20-NN mean=+1.066 (Δ_knn=-0.036). Drug target: BRDT. Cell lineage: CNS/Brain / Diffuse Glioma. Per-drug R² on held-out cells = 0.25.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0910, |SHAP|=0.0910)  
  _value=6.8038, z=+0.49; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0800, |SHAP|=0.0800)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0505, |SHAP|=0.0505)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0173, |SHAP|=0.0173)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0148, |SHAP|=0.0148)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0119, |SHAP|=0.0119)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0106, |SHAP|=0.0106)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AMO1 | haematopoietic and lymphoid tissue | -2.868436018946039 | more sensitive |
| SCC25 | upper aerodigestive tract | -2.790840405808785 | more sensitive |
| OV56 | ovary | 3.461844950135784 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 3.476896449918983 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| daporinad | NAMPT | -3.3503029069013626 | more sensitive |
| leptomycin B | XPO1 | -2.534809745117362 | more sensitive |
| necrostatin-1 | RIPK1 | 2.764659480178003 | more resistant |
| PRL-3 inhibitor I | PTP4A3 | 3.425721350656106 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---
