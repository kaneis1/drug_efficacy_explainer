# SHAP-Grounded Sample Reports (log10(IC50))

## RPT-0001 - AZD7762 on A204
*Evidence: SHAP-0001*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **A204** (master_ccl_id=26) |
| Tissue | soft tissue |
| Histology | rhabdoid tumor |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-1.1810**
- RF-predicted log10(IC50): **-0.3207**
- Prediction error (observed - predicted): **-0.8602**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=8.9
- Cell cohort (355 pairs): mean=0.4788, q10=-1.3209, median=0.6554, q90=1.9305, sample percentile=11.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 1 (A_sanity_check): AZD7762 on A-204 / ACH-000201 (Kidney); observed log10(IC50)=-1.1810.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7413, |SHAP|=0.7413)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3092, |SHAP|=0.3092)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1493, |SHAP|=0.1493)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0677, |SHAP|=0.0677)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0629, |SHAP|=0.0629)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0071** (fingerprint_bit; SHAP=+0.0462, |SHAP|=0.0462)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
7. **fp_0611** (fingerprint_bit; SHAP=-0.0437, |SHAP|=0.0437)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
8. **fp_0518** (fingerprint_bit; SHAP=+0.0423, |SHAP|=0.0423)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

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

## RPT-0002 - SCH-79797 on DAUDI
*Evidence: SHAP-0002*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SCH-79797** (master_cpd_id=375264) |
| Gene Target | F2R |
| Mechanism / Activity | antagonist of proteinase-activated receptor 1 (PAR1) |
| Cell Line | **DAUDI** (master_ccl_id=203) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **-0.0633**
- RF-predicted log10(IC50): **0.2079**
- Prediction error (observed - predicted): **-0.2712**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (781 pairs): mean=0.0087, q10=-0.7471, median=0.0771, q90=0.6485, sample percentile=39.4
- Cell cohort (333 pairs): mean=0.3512, q10=-1.3650, median=0.4756, q90=1.6283, sample percentile=25.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 2 (A_sanity_check): SCH-79797 on Daudi / ACH-000786 (Lymphoid); observed log10(IC50)=-0.0633.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.3733, |SHAP|=0.3733)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0263** (fingerprint_bit; SHAP=-0.2619, |SHAP|=0.2619)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
3. **CCN1 (3491)** (gene_expression; SHAP=-0.0969, |SHAP|=0.0969)  
  _value=0.6288, z=-1.50; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0673** (fingerprint_bit; SHAP=+0.0572, |SHAP|=0.0572)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0141** (fingerprint_bit; SHAP=+0.0571, |SHAP|=0.0571)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **fp_0688** (fingerprint_bit; SHAP=+0.0230, |SHAP|=0.0230)  
  _absent; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
7. **fp_0513** (fingerprint_bit; SHAP=+0.0170, |SHAP|=0.0170)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
8. **fp_0223** (fingerprint_bit; SHAP=+0.0162, |SHAP|=0.0162)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: gossypol, cytochalasin B, erastin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| LMSU | stomach | -3.4605625448212582 | more sensitive |
| KYSE520 | oesophagus | -2.6706931345230025 | more sensitive |
| SNU489 | central nervous system | 1.3133185022219966 | more resistant |
| NCIH2122 | lung | 1.4273551895501138 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GMX-1778 | NAMPT | -3.626515466331264 | more sensitive |
| azacitidine | DNMT1 | -3.6115915101714258 | more sensitive |
| thalidomide | CRBN | 2.928118767823545 | more resistant |
| AT-406 | XIAP | 3.4979685496154613 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0003 - obatoclax on DAUDI
*Evidence: SHAP-0003*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **obatoclax** (master_cpd_id=606142) |
| Gene Target | BCL2;BCL2L1;MCL1 |
| Mechanism / Activity | inhibitor of MCL1, BCL2, and BCL-xL |
| Cell Line | **DAUDI** (master_ccl_id=203) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **-1.3840**
- RF-predicted log10(IC50): **-0.3547**
- Prediction error (observed - predicted): **-1.0294**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (790 pairs): mean=-0.2289, q10=-1.0241, median=-0.2248, q90=0.5700, sample percentile=4.9
- Cell cohort (333 pairs): mean=0.3512, q10=-1.3650, median=0.4756, q90=1.6283, sample percentile=9.9
- Interpretation: **more sensitive than the model predicted**
- Selection reason: Manifest 25_pairs.csv row 3 (A_sanity_check): obatoclax on Daudi / ACH-000786 (Lymphoid); observed log10(IC50)=-1.3840.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.4976, |SHAP|=0.4976)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0329** (fingerprint_bit; SHAP=-0.1799, |SHAP|=0.1799)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
3. **CCN1 (3491)** (gene_expression; SHAP=-0.1335, |SHAP|=0.1335)  
  _value=0.6288, z=-1.50; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0994** (fingerprint_bit; SHAP=-0.1043, |SHAP|=0.1043)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0423** (fingerprint_bit; SHAP=-0.0924, |SHAP|=0.0924)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
6. **fp_0110** (fingerprint_bit; SHAP=-0.0805, |SHAP|=0.0805)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
7. **fp_0582** (fingerprint_bit; SHAP=-0.0644, |SHAP|=0.0644)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0619, |SHAP|=0.0619)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| ML1 | thyroid | -3.4339057494390954 | more sensitive |
| DND41 | haematopoietic and lymphoid tissue | -3.200995251938773 | more sensitive |
| NCIH226 | lung | 1.5374553086560343 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 1.6484795885885883 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GMX-1778 | NAMPT | -3.626515466331264 | more sensitive |
| azacitidine | DNMT1 | -3.6115915101714258 | more sensitive |
| thalidomide | CRBN | 2.928118767823545 | more resistant |
| AT-406 | XIAP | 3.4979685496154613 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0004 - obatoclax on A2780
*Evidence: SHAP-0004*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **obatoclax** (master_cpd_id=606142) |
| Gene Target | BCL2;BCL2L1;MCL1 |
| Mechanism / Activity | inhibitor of MCL1, BCL2, and BCL-xL |
| Cell Line | **A2780** (master_ccl_id=29) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-0.7250**
- RF-predicted log10(IC50): **-0.1646**
- Prediction error (observed - predicted): **-0.5604**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (790 pairs): mean=-0.2289, q10=-1.0241, median=-0.2248, q90=0.5700, sample percentile=20.3
- Cell cohort (325 pairs): mean=0.3347, q10=-1.2462, median=0.5054, q90=1.6163, sample percentile=16.3
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 4 (A_sanity_check): obatoclax on A2780 / ACH-000657 (Ovary/Fallopian Tube); observed log10(IC50)=-0.7250.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.6725, |SHAP|=0.6725)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0329** (fingerprint_bit; SHAP=-0.1247, |SHAP|=0.1247)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1062, |SHAP|=0.1062)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0423** (fingerprint_bit; SHAP=-0.0931, |SHAP|=0.0931)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
5. **fp_0110** (fingerprint_bit; SHAP=-0.0597, |SHAP|=0.0597)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.0566, |SHAP|=0.0566)  
  _value=4.5022, z=-0.25; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0600** (fingerprint_bit; SHAP=+0.0562, |SHAP|=0.0562)  
  _present; representative SMARTS `[#6]:[#6](:[#7]):[#7]`; present in 5.0% of CTRPv2 compounds; example compounds: methotrexate, C6-ceramide, cerulenin_
8. **fp_0582** (fingerprint_bit; SHAP=-0.0533, |SHAP|=0.0533)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| ML1 | thyroid | -3.4339057494390954 | more sensitive |
| DND41 | haematopoietic and lymphoid tissue | -3.200995251938773 | more sensitive |
| NCIH226 | lung | 1.5374553086560343 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 1.6484795885885883 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | -3.70683697110924 | more sensitive |
| pluripotin | MAPK1;RASAL1 | -2.8199311991155507 | more sensitive |
| epigallocatechin-3-monogallate |  | 2.52179604313311 | more resistant |
| sildenafil | PDE5A | 3.503989149528741 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0005 - obatoclax on NCIH520
*Evidence: SHAP-0005*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **obatoclax** (master_cpd_id=606142) |
| Gene Target | BCL2;BCL2L1;MCL1 |
| Mechanism / Activity | inhibitor of MCL1, BCL2, and BCL-xL |
| Cell Line | **NCIH520** (master_ccl_id=155324) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-0.4511**
- RF-predicted log10(IC50): **-0.1952**
- Prediction error (observed - predicted): **-0.2560**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (790 pairs): mean=-0.2289, q10=-1.0241, median=-0.2248, q90=0.5700, sample percentile=39.9
- Cell cohort (341 pairs): mean=0.6386, q10=-1.2394, median=0.7464, q90=2.0082, sample percentile=17.3
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 5 (A_sanity_check): obatoclax on NCI-H520 / ACH-000395 (Lung); observed log10(IC50)=-0.4511.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.4371, |SHAP|=0.4371)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0329** (fingerprint_bit; SHAP=-0.1803, |SHAP|=0.1803)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
3. **CCN1 (3491)** (gene_expression; SHAP=-0.1336, |SHAP|=0.1336)  
  _value=1.3376, z=-1.27; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0994** (fingerprint_bit; SHAP=-0.1065, |SHAP|=0.1065)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0423** (fingerprint_bit; SHAP=-0.0941, |SHAP|=0.0941)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
6. **fp_0110** (fingerprint_bit; SHAP=-0.0598, |SHAP|=0.0598)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
7. **fp_0582** (fingerprint_bit; SHAP=-0.0590, |SHAP|=0.0590)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0472, |SHAP|=0.0472)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| ML1 | thyroid | -3.4339057494390954 | more sensitive |
| DND41 | haematopoietic and lymphoid tissue | -3.200995251938773 | more sensitive |
| NCIH226 | lung | 1.5374553086560343 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 1.6484795885885883 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.357295127926956 | more sensitive |
| leptomycin B | XPO1 | -3.189005895995981 | more sensitive |
| PRL-3 inhibitor I | PTP4A3 | 3.6213908478376937 | more resistant |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 3.985637142591111 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0006 - obatoclax on A204
*Evidence: SHAP-0006*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **obatoclax** (master_cpd_id=606142) |
| Gene Target | BCL2;BCL2L1;MCL1 |
| Mechanism / Activity | inhibitor of MCL1, BCL2, and BCL-xL |
| Cell Line | **A204** (master_ccl_id=26) |
| Tissue | soft tissue |
| Histology | rhabdoid tumor |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-0.5184**
- RF-predicted log10(IC50): **-0.1471**
- Prediction error (observed - predicted): **-0.3713**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (790 pairs): mean=-0.2289, q10=-1.0241, median=-0.2248, q90=0.5700, sample percentile=33.7
- Cell cohort (355 pairs): mean=0.4788, q10=-1.3209, median=0.6554, q90=1.9305, sample percentile=22.5
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 6 (A_sanity_check): obatoclax on A-204 / ACH-000201 (Kidney); observed log10(IC50)=-0.5184.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.6581, |SHAP|=0.6581)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0329** (fingerprint_bit; SHAP=-0.1246, |SHAP|=0.1246)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1065, |SHAP|=0.1065)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **fp_0423** (fingerprint_bit; SHAP=-0.0940, |SHAP|=0.0940)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
5. **fp_0110** (fingerprint_bit; SHAP=-0.0598, |SHAP|=0.0598)  
  _present; representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`; present in 1.7% of CTRPv2 compounds; example compounds: SNX-2112, TPCA-1, BRD-K66453893_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.0571, |SHAP|=0.0571)  
  _value=5.2402, z=-0.01; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0582** (fingerprint_bit; SHAP=-0.0540, |SHAP|=0.0540)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **fp_0518** (fingerprint_bit; SHAP=+0.0463, |SHAP|=0.0463)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| ML1 | thyroid | -3.4339057494390954 | more sensitive |
| DND41 | haematopoietic and lymphoid tissue | -3.200995251938773 | more sensitive |
| NCIH226 | lung | 1.5374553086560343 | more resistant |
| MJ | haematopoietic and lymphoid tissue | 1.6484795885885883 | more resistant |

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

## RPT-0007 - doxorubicin on HGC27
*Evidence: SHAP-0007*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **doxorubicin** (master_cpd_id=36599) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **HGC27** (master_ccl_id=368) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | undifferentiated adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-1.1839**
- RF-predicted log10(IC50): **0.4325**
- Prediction error (observed - predicted): **-1.6164**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (786 pairs): mean=-0.6755, q10=-1.7129, median=-0.6206, q90=0.1786, sample percentile=21.2
- Cell cohort (356 pairs): mean=0.4009, q10=-1.4062, median=0.6379, q90=1.7865, sample percentile=13.2
- Interpretation: **more sensitive than the model predicted**
- Selection reason: Manifest 25_pairs.csv row 7 (A_sanity_check): doxorubicin on HGC-27 / ACH-000847 (Esophagus/Stomach); observed log10(IC50)=-1.1839.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.4858, |SHAP|=0.4858)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.2028, |SHAP|=0.2028)  
  _value=3.2903, z=-0.64; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.1518, |SHAP|=0.1518)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0744, |SHAP|=0.0744)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0535** (fingerprint_bit; SHAP=-0.0663, |SHAP|=0.0663)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0998** (fingerprint_bit; SHAP=-0.0505, |SHAP|=0.0505)  
  _present; representative SMARTS `[#6]-[#6@H](-[#6]-[#8])-[#7](-[#6])-[#6]`; present in 6.2% of CTRPv2 compounds; example compounds: BRD-K66453893, BRD-K27224038, triptolide_
7. **fp_0501** (fingerprint_bit; SHAP=-0.0368, |SHAP|=0.0368)  
  _present; representative SMARTS `[#6](-[#6@H])(=[#6])-[#6](-[#6@](-[#6])(-[#8])-[#6@@H])(-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: paclitaxel, myricetin, temozolomide_
8. **fp_0539** (fingerprint_bit; SHAP=-0.0354, |SHAP|=0.0354)  
  _present; representative SMARTS `[#16]-[#7](-[#6]-[#6]-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: CIL56, nilotinib, ML203_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH209 | lung | -3.552126870597492 | more sensitive |
| OVCAR5 |  | -3.203143882037899 | more sensitive |
| KATOIII | stomach | 1.9136476824359283 | more resistant |
| HCC1171 | lung | 2.3146196366603515 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| sirolimus | MTOR | -3.955534143024713 | more sensitive |
| KX2-391 | SRC | -3.5083771344862167 | more sensitive |
| palmostatin B | LYPLA1 | 3.172856154298361 | more resistant |
| SKI-II | SPHK1 | 3.428731650612746 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0008 - doxorubicin on DAUDI
*Evidence: SHAP-0008*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **doxorubicin** (master_cpd_id=36599) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **DAUDI** (master_ccl_id=203) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Burkitt lymphoma |

### Response Summary
- Observed log10(IC50): **-2.3904**
- RF-predicted log10(IC50): **-0.8297**
- Prediction error (observed - predicted): **-1.5607**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (786 pairs): mean=-0.6755, q10=-1.7129, median=-0.6206, q90=0.1786, sample percentile=1.8
- Cell cohort (333 pairs): mean=0.3512, q10=-1.3650, median=0.4756, q90=1.6283, sample percentile=3.9
- Interpretation: **more sensitive than the model predicted**
- Selection reason: Manifest 25_pairs.csv row 8 (A_sanity_check): doxorubicin on Daudi / ACH-000786 (Lymphoid); observed log10(IC50)=-2.3904.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.7667, |SHAP|=0.7667)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.4748, |SHAP|=0.4748)  
  _value=0.6288, z=-1.50; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.1001, |SHAP|=0.1001)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0322** (fingerprint_bit; SHAP=-0.0907, |SHAP|=0.0907)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6]`; present in 15.0% of CTRPv2 compounds; example compounds: BRD9876, tamoxifen, BRD9647_
5. **fp_0535** (fingerprint_bit; SHAP=-0.0679, |SHAP|=0.0679)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0522** (fingerprint_bit; SHAP=-0.0535, |SHAP|=0.0535)  
  _present; representative SMARTS `[#6]-[#6@@H](-[#6])/[#6]=[#6](\[#6])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: manumycin A, 16-beta-bromoandrosterone, cyanoquinoline 11_
7. **fp_0501** (fingerprint_bit; SHAP=-0.0528, |SHAP|=0.0528)  
  _present; representative SMARTS `[#6](-[#6@H])(=[#6])-[#6](-[#6@](-[#6])(-[#8])-[#6@@H])(-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: paclitaxel, myricetin, temozolomide_
8. **fp_0998** (fingerprint_bit; SHAP=-0.0512, |SHAP|=0.0512)  
  _present; representative SMARTS `[#6]-[#6@H](-[#6]-[#8])-[#7](-[#6])-[#6]`; present in 6.2% of CTRPv2 compounds; example compounds: BRD-K66453893, BRD-K27224038, triptolide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH209 | lung | -3.552126870597492 | more sensitive |
| OVCAR5 |  | -3.203143882037899 | more sensitive |
| KATOIII | stomach | 1.9136476824359283 | more resistant |
| HCC1171 | lung | 2.3146196366603515 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GMX-1778 | NAMPT | -3.626515466331264 | more sensitive |
| azacitidine | DNMT1 | -3.6115915101714258 | more sensitive |
| thalidomide | CRBN | 2.928118767823545 | more resistant |
| AT-406 | XIAP | 3.4979685496154613 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0009 - doxorubicin on A2780
*Evidence: SHAP-0009*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **doxorubicin** (master_cpd_id=36599) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **A2780** (master_ccl_id=29) |
| Tissue | ovary |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-2.0412**
- RF-predicted log10(IC50): **0.4531**
- Prediction error (observed - predicted): **-2.4944**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (786 pairs): mean=-0.6755, q10=-1.7129, median=-0.6206, q90=0.1786, sample percentile=5.3
- Cell cohort (325 pairs): mean=0.3347, q10=-1.2462, median=0.5054, q90=1.6163, sample percentile=4.9
- Interpretation: **more sensitive than the model predicted**
- Selection reason: Manifest 25_pairs.csv row 9 (A_sanity_check): doxorubicin on A2780 / ACH-000657 (Ovary/Fallopian Tube); observed log10(IC50)=-2.0412.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.4796, |SHAP|=0.4796)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.2027, |SHAP|=0.2027)  
  _value=4.5022, z=-0.25; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.1528, |SHAP|=0.1528)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0750, |SHAP|=0.0750)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0535** (fingerprint_bit; SHAP=-0.0665, |SHAP|=0.0665)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0998** (fingerprint_bit; SHAP=-0.0505, |SHAP|=0.0505)  
  _present; representative SMARTS `[#6]-[#6@H](-[#6]-[#8])-[#7](-[#6])-[#6]`; present in 6.2% of CTRPv2 compounds; example compounds: BRD-K66453893, BRD-K27224038, triptolide_
7. **fp_0501** (fingerprint_bit; SHAP=-0.0366, |SHAP|=0.0366)  
  _present; representative SMARTS `[#6](-[#6@H])(=[#6])-[#6](-[#6@](-[#6])(-[#8])-[#6@@H])(-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: paclitaxel, myricetin, temozolomide_
8. **fp_0539** (fingerprint_bit; SHAP=-0.0354, |SHAP|=0.0354)  
  _present; representative SMARTS `[#16]-[#7](-[#6]-[#6]-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: CIL56, nilotinib, ML203_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH209 | lung | -3.552126870597492 | more sensitive |
| OVCAR5 |  | -3.203143882037899 | more sensitive |
| KATOIII | stomach | 1.9136476824359283 | more resistant |
| HCC1171 | lung | 2.3146196366603515 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | -3.70683697110924 | more sensitive |
| pluripotin | MAPK1;RASAL1 | -2.8199311991155507 | more sensitive |
| epigallocatechin-3-monogallate |  | 2.52179604313311 | more resistant |
| sildenafil | PDE5A | 3.503989149528741 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0010 - doxorubicin on NCIH520
*Evidence: SHAP-0010*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **doxorubicin** (master_cpd_id=36599) |
| Gene Target | TOP2A |
| Mechanism / Activity | inhibitor of topoisomerase II |
| Cell Line | **NCIH520** (master_ccl_id=155324) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-0.1530**
- RF-predicted log10(IC50): **-0.8557**
- Prediction error (observed - predicted): **+0.7027**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (786 pairs): mean=-0.6755, q10=-1.7129, median=-0.6206, q90=0.1786, sample percentile=76.8
- Cell cohort (341 pairs): mean=0.6386, q10=-1.2394, median=0.7464, q90=2.0082, sample percentile=22.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 10 (A_sanity_check): doxorubicin on NCI-H520 / ACH-000395 (Lung); observed log10(IC50)=-0.1530.

### Top TreeSHAP Features
1. **fp_0329** (fingerprint_bit; SHAP=-0.7743, |SHAP|=0.7743)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: NSC23766, PD 153035, gefitinib_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.4798, |SHAP|=0.4798)  
  _value=1.3376, z=-1.27; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0322** (fingerprint_bit; SHAP=-0.0903, |SHAP|=0.0903)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6]`; present in 15.0% of CTRPv2 compounds; example compounds: BRD9876, tamoxifen, BRD9647_
4. **fp_0141** (fingerprint_bit; SHAP=+0.0851, |SHAP|=0.0851)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0535** (fingerprint_bit; SHAP=-0.0664, |SHAP|=0.0664)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0522** (fingerprint_bit; SHAP=-0.0555, |SHAP|=0.0555)  
  _present; representative SMARTS `[#6]-[#6@@H](-[#6])/[#6]=[#6](\[#6])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: manumycin A, 16-beta-bromoandrosterone, cyanoquinoline 11_
7. **fp_0501** (fingerprint_bit; SHAP=-0.0530, |SHAP|=0.0530)  
  _present; representative SMARTS `[#6](-[#6@H])(=[#6])-[#6](-[#6@](-[#6])(-[#8])-[#6@@H])(-[#6])-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: paclitaxel, myricetin, temozolomide_
8. **fp_0998** (fingerprint_bit; SHAP=-0.0514, |SHAP|=0.0514)  
  _present; representative SMARTS `[#6]-[#6@H](-[#6]-[#8])-[#7](-[#6])-[#6]`; present in 6.2% of CTRPv2 compounds; example compounds: BRD-K66453893, BRD-K27224038, triptolide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH209 | lung | -3.552126870597492 | more sensitive |
| OVCAR5 |  | -3.203143882037899 | more sensitive |
| KATOIII | stomach | 1.9136476824359283 | more resistant |
| HCC1171 | lung | 2.3146196366603515 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.357295127926956 | more sensitive |
| leptomycin B | XPO1 | -3.189005895995981 | more sensitive |
| PRL-3 inhibitor I | PTP4A3 | 3.6213908478376937 | more resistant |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 3.985637142591111 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0011 - N9-isopropylolomoucine on SNU761
*Evidence: SHAP-0011*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **N9-isopropylolomoucine** (master_cpd_id=45093) |
| Gene Target | CCNB1;CDK1;CDK5;CDK5R1 |
| Mechanism / Activity | inhibitor of CDK1/cyclin B and CDK5/p35 complexes |
| Cell Line | **SNU761** (master_ccl_id=1122) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed log10(IC50): **-3.7423**
- RF-predicted log10(IC50): **1.0604**
- Prediction error (observed - predicted): **-4.8028**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (634 pairs): mean=1.6083, q10=0.6019, median=1.7966, q90=2.4534, sample percentile=0.2
- Cell cohort (218 pairs): mean=0.8996, q10=-0.3539, median=1.0415, q90=1.9177, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 11 (B_outlier): N9-isopropylolomoucine on SNU-761 / ACH-000537 (Liver); observed log10(IC50)=-3.7423.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1363, |SHAP|=0.1363)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0997, |SHAP|=0.0997)  
  _value=8.7822, z=+1.13; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0870, |SHAP|=0.0870)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0673** (fingerprint_bit; SHAP=-0.0726, |SHAP|=0.0726)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0191, |SHAP|=0.0191)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0161, |SHAP|=0.0161)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0158, |SHAP|=0.0158)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0144, |SHAP|=0.0144)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH2405 | lung | -3.4501315501022933 | more sensitive |
| HEYA8 | ovary | -3.249811182668611 | more sensitive |
| SKUT1 | soft tissue | 3.455824350222504 | more resistant |
| FUOV1 | ovary | 3.549143648878338 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| cucurbitacin I |  | -3.37396871681732 | more sensitive |
| GMX-1778 | NAMPT | -1.8822311802975769 | more sensitive |
| A-804598 | P2RX7 | 3.6274114477509736 | more resistant |
| SJ-172550 | MDM2;TP53 | 3.642462947534173 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0012 - chlorambucil on MDAMB453
*Evidence: SHAP-0012*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **chlorambucil** (master_cpd_id=25334) |
| Gene Target | n/a |
| Mechanism / Activity | DNA alkylator |
| Cell Line | **MDAMB453** (master_ccl_id=657) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.6833**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.7486**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (589 pairs): mean=1.8527, q10=0.9424, median=2.0374, q90=2.5906, sample percentile=0.2
- Cell cohort (300 pairs): mean=0.6302, q10=-0.9367, median=0.8558, q90=1.9525, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 12 (B_outlier): chlorambucil on MDA-MB-453 / ACH-000910 (Breast); observed log10(IC50)=-3.6833.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0898, |SHAP|=0.0898)  
  _value=5.7358, z=+0.15; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0682, |SHAP|=0.0682)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0502, |SHAP|=0.0502)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0192, |SHAP|=0.0192)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0059** (fingerprint_bit; SHAP=+0.0151, |SHAP|=0.0151)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0150, |SHAP|=0.0150)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0114, |SHAP|=0.0114)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| OCIM1 | haematopoietic and lymphoid tissue | -2.6219232994889987 | more sensitive |
| TF1 | haematopoietic and lymphoid tissue | -1.4207301191307804 | more sensitive |
| HCC1171 | lung | 3.618380547881054 | more resistant |
| IM95 | stomach | 3.696648346753689 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | -3.821189916412671 | more sensitive |
| AZD7762 | CHEK1;CHEK2 | -3.470663800856234 | more sensitive |
| pyrazolanthrone | MAPK10;MAPK8;MAPK9 | 3.476896449918983 | more resistant |
| CHIR-99021 | GSK3B | 3.877266344152078 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0013 - NSC23766 on NCIH322
*Evidence: SHAP-0013*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC23766** (master_cpd_id=44503) |
| Gene Target | RAC1;TIAM1;TRIO |
| Mechanism / Activity | inhibitor of RAC1-GEF interaction; prevents Rac1 activation by Rac-specific guanine nucleotide exchange factors (GEFs) TrioN and Tiam1 |
| Cell Line | **NCIH322** (master_ccl_id=155305) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.2596**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.3249**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (704 pairs): mean=1.9744, q10=1.2117, median=2.1603, q90=2.8314, sample percentile=0.1
- Cell cohort (258 pairs): mean=0.8308, q10=-1.2289, median=1.2995, q90=2.2578, sample percentile=2.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 13 (B_outlier): NSC23766 on NCI-H322 / ACH-000837 (Lung); observed log10(IC50)=-3.2596.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.0870, |SHAP|=0.0870)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0865, |SHAP|=0.0865)  
  _value=6.9296, z=+0.53; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0378, |SHAP|=0.0378)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0362, |SHAP|=0.0362)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0263** (fingerprint_bit; SHAP=-0.0304, |SHAP|=0.0304)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]-[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: chlorambucil, methotrexate, ouabain_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0165, |SHAP|=0.0165)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0158, |SHAP|=0.0158)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AM38 | central nervous system | -3.0434132561628497 | more sensitive |
| PANC1 | pancreas | -2.627078080061276 | more sensitive |
| HPAFII | pancreas | 3.732771946233367 | more resistant |
| KYSE510 | oesophagus | 3.744962176746956 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.6326806202412736 | more sensitive |
| BI-2536 | PLK1 | -3.603051451288218 | more sensitive |
| CID-5951923 | KLF5 | 3.20897975377804 | more resistant |
| RO4929097 | APH1A;NCSTN;PSEN1;PSENEN | 3.281226952737395 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0014 - ML050 on FADU
*Evidence: SHAP-0014*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **ML050** (master_cpd_id=153820) |
| Gene Target | GPER1 |
| Mechanism / Activity | antagonist of GPR30 |
| Cell Line | **FADU** (master_ccl_id=255) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.4516**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.5168**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (374 pairs): mean=1.7804, q10=1.1949, median=1.7857, q90=2.5364, sample percentile=0.3
- Cell cohort (285 pairs): mean=0.9919, q10=-0.7281, median=1.2876, q90=2.2131, sample percentile=0.7
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 14 (B_outlier): ML050 on FaDu / ACH-000846 (Head and Neck); observed log10(IC50)=-3.4516.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.0924, |SHAP|=0.0924)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0794, |SHAP|=0.0794)  
  _value=5.4549, z=+0.06; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0498, |SHAP|=0.0498)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0185, |SHAP|=0.0185)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0171, |SHAP|=0.0171)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0129, |SHAP|=0.0129)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0994** (fingerprint_bit; SHAP=-0.0110, |SHAP|=0.0110)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0109, |SHAP|=0.0109)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| TE6 | oesophagus | -3.447228430900364 | more sensitive |
| A4FUK | haematopoietic and lymphoid tissue | -2.72640395037609 | more sensitive |
| BCPAP | thyroid | 3.8682354442821594 | more resistant |
| EHEB | haematopoietic and lymphoid tissue | 3.871245744238798 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.868222271064546 | more sensitive |
| AA-COCF3 | FAAH;PLA2G4A;PLA2G4B;PLA2G4C;PLA2G4D | -3.397619940260407 | more sensitive |
| BRD-K42260513 | EZH2 | 3.491947949702182 | more resistant |
| GSK525762A | BRD2;BRD3;BRD4 | 3.892317843935277 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0015 - BRD1835 on MONOMAC6
*Evidence: SHAP-0015*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD1835** (master_cpd_id=404070) |
| Gene Target | EZH2 |
| Mechanism / Activity | product of diversity oriented synthesis; screening hit |
| Cell Line | **MONOMAC6** (master_ccl_id=702) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- Observed log10(IC50): **-3.3440**
- RF-predicted log10(IC50): **0.8039**
- Prediction error (observed - predicted): **-4.1480**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (401 pairs): mean=1.9688, q10=1.5533, median=2.0425, q90=2.4850, sample percentile=0.2
- Cell cohort (159 pairs): mean=0.4263, q10=-1.8508, median=0.6891, q90=1.8400, sample percentile=1.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 15 (B_outlier): BRD1835 on MONO-MAC-6 / ACH-000006 (Myeloid); observed log10(IC50)=-3.3440.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.1844, |SHAP|=0.1844)  
  _value=0.7669, z=-1.46; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.1234, |SHAP|=0.1234)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0518** (fingerprint_bit; SHAP=-0.0659, |SHAP|=0.0659)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
4. **fp_0062** (fingerprint_bit; SHAP=+0.0458, |SHAP|=0.0458)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
5. **fp_0017** (fingerprint_bit; SHAP=+0.0393, |SHAP|=0.0393)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0190, |SHAP|=0.0190)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0179, |SHAP|=0.0179)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0114, |SHAP|=0.0114)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MINO | haematopoietic and lymphoid tissue | -2.7700867527095365 | more sensitive |
| NCIH810 | lung | -1.9483639988625392 | more sensitive |
| NCIH2444 | lung | 3.3084208993336985 | more resistant |
| KYSE180 | oesophagus | 3.422711050699466 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K34222889 |  | -3.875401560742161 | more sensitive |
| SN-38 | TOP1 | -3.2502383243426527 | more sensitive |
| etomoxir | CPT1A | 3.245103353257717 | more resistant |
| CIL70 |  | 3.335412351956912 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0017 - ML203 on JIMT1
*Evidence: SHAP-0017*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **ML203** (master_cpd_id=411816) |
| Gene Target | PKM |
| Mechanism / Activity | activator of muscle pyruvate kinase (PKM2) |
| Cell Line | **JIMT1** (master_ccl_id=501) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **-3.6063**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.6716**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (116 pairs): mean=1.9820, q10=0.7830, median=2.0079, q90=3.2210, sample percentile=0.9
- Cell cohort (177 pairs): mean=0.7520, q10=-1.2189, median=1.1788, q90=2.2546, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 17 (B_outlier): ML203 on JIMT-1 / ACH-000711 (Breast); observed log10(IC50)=-3.6063.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1632, |SHAP|=0.1632)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0805, |SHAP|=0.0805)  
  _value=6.6182, z=+0.43; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0518** (fingerprint_bit; SHAP=-0.0748, |SHAP|=0.0748)  
  _present; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
4. **fp_0017** (fingerprint_bit; SHAP=+0.0514, |SHAP|=0.0514)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0186, |SHAP|=0.0186)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0178, |SHAP|=0.0178)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0777** (fingerprint_bit; SHAP=+0.0114, |SHAP|=0.0114)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
8. **fp_0062** (fingerprint_bit; SHAP=+0.0100, |SHAP|=0.0100)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RI1 | haematopoietic and lymphoid tissue | -1.853973811829227 | more sensitive |
| WSUDLCL2 | haematopoietic and lymphoid tissue | -0.4210338051526424 | more sensitive |
| LOVO | large intestine | 3.7989985452794426 | more resistant |
| GP2D | large intestine | 3.859204544412239 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K70511574 | PLK1 | -3.695465998617446 | more sensitive |
| KU-60019 | ATM | -3.319547158936804 | more sensitive |
| erismodegib |  | 3.759864645843125 | more resistant |
| pyrazolanthrone | MAPK10;MAPK8;MAPK9 | 3.970585642807912 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0018 - BRD-K51490254 on L540
*Evidence: SHAP-0018*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K51490254** (master_cpd_id=616355) |
| Gene Target | HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC6 and HDAC8 |
| Cell Line | **L540** (master_ccl_id=594) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | Hodgkin lymphoma |

### Response Summary
- Observed log10(IC50): **-3.5904**
- RF-predicted log10(IC50): **0.7137**
- Prediction error (observed - predicted): **-4.3041**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (253 pairs): mean=1.9750, q10=1.4504, median=1.9383, q90=2.7827, sample percentile=0.4
- Cell cohort (305 pairs): mean=0.5265, q10=-1.1941, median=0.7232, q90=1.7566, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 18 (B_outlier): BRD-K51490254 on L-540 / ACH-000806 (Lymphoid); observed log10(IC50)=-3.5904.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=-0.2094, |SHAP|=0.2094)  
  _value=0.4259, z=-1.56; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0659, |SHAP|=0.0659)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0301, |SHAP|=0.0301)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0202, |SHAP|=0.0202)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0160, |SHAP|=0.0160)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0138, |SHAP|=0.0138)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0015** (fingerprint_bit; SHAP=+0.0127, |SHAP|=0.0127)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
8. **fp_0876** (fingerprint_bit; SHAP=+0.0116, |SHAP|=0.0116)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NB1 | autonomic ganglia | -1.181473264520588 | more sensitive |
| ECC10 | stomach | -0.8355669933045253 | more sensitive |
| EJM | haematopoietic and lymphoid tissue | 3.7869573454528833 | more resistant |
| RERFLCAD2 | lung | 3.967575342851272 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.3902714033448933 | more sensitive |
| BI-2536 | PLK1 | -2.684325392580488 | more sensitive |
| Compound 1541A | CASP3;CASP6;CASP7 | 3.428731650612746 | more resistant |
| SCH-529074 | TP53 | 3.506609037221434 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0019 - N9-isopropylolomoucine on AN3CA
*Evidence: SHAP-0019*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **N9-isopropylolomoucine** (master_cpd_id=45093) |
| Gene Target | CCNB1;CDK1;CDK5;CDK5R1 |
| Mechanism / Activity | inhibitor of CDK1/cyclin B and CDK5/p35 complexes |
| Cell Line | **AN3CA** (master_ccl_id=50) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.2225**
- RF-predicted log10(IC50): **1.0565**
- Prediction error (observed - predicted): **-4.2790**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (634 pairs): mean=1.6083, q10=0.6019, median=1.7966, q90=2.4534, sample percentile=0.6
- Cell cohort (270 pairs): mean=0.5861, q10=-1.5270, median=0.6826, q90=2.1904, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 19 (B_outlier): N9-isopropylolomoucine on AN3 CA / ACH-000940 (Uterus); observed log10(IC50)=-3.2225.

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1421, |SHAP|=0.1421)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0995, |SHAP|=0.0995)  
  _value=4.3236, z=-0.31; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0922, |SHAP|=0.0922)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0673** (fingerprint_bit; SHAP=-0.0750, |SHAP|=0.0750)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0195, |SHAP|=0.0195)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0162, |SHAP|=0.0162)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0059** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNU761 | liver | -3.742345198448852 | more sensitive |
| NCIH2405 | lung | -3.4501315501022933 | more sensitive |
| SKUT1 | soft tissue | 3.455824350222504 | more resistant |
| FUOV1 | ovary | 3.549143648878338 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| manumycin A | FNTA;FNTB | -3.8997333675840182 | more sensitive |
| parbendazole |  | -3.442109168816573 | more sensitive |
| Ch-55 | RARA;RARB;RARG | 3.2390827533444377 | more resistant |
| ML083 | PKM | 3.3865874512197887 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0020 - Ko-143 on JHUEM3
*Evidence: SHAP-0020*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **Ko-143** (master_cpd_id=418172) |
| Gene Target | ABCG2 |
| Mechanism / Activity | inhibitor of breast cancer resistance protein multidrug transporter (BCRP) |
| Cell Line | **JHUEM3** (master_ccl_id=499) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.4507**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-4.5160**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (452 pairs): mean=1.4463, q10=0.6782, median=1.4344, q90=2.3820, sample percentile=0.4
- Cell cohort (248 pairs): mean=0.5626, q10=-1.3097, median=0.7182, q90=2.1931, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 20 (B_outlier): Ko-143 on JHUEM-3 / ACH-000173 (Uterus); observed log10(IC50)=-3.4507.

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0921, |SHAP|=0.0921)  
  _value=7.9489, z=+0.86; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0742, |SHAP|=0.0742)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0591, |SHAP|=0.0591)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0197, |SHAP|=0.0197)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0535** (fingerprint_bit; SHAP=+0.0182, |SHAP|=0.0182)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0159, |SHAP|=0.0159)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0777** (fingerprint_bit; SHAP=+0.0109, |SHAP|=0.0109)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_
8. **fp_0064** (fingerprint_bit; SHAP=+0.0091, |SHAP|=0.0091)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]`; present in 52.8% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, ML006_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MJ | haematopoietic and lymphoid tissue | -3.6661335714710335 | more sensitive |
| AM38 | central nervous system | -2.724726895944213 | more sensitive |
| RPMI8226 | haematopoietic and lymphoid tissue | 3.9194105435450353 | more resistant |
| SNU387 | liver | 3.9404826432415136 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| docetaxel |  | -3.318193736202091 | more sensitive |
| BMS-754807 | IGF1R | -3.2094739163790065 | more sensitive |
| BRD8958 | EP300 | 3.8802766441087178 | more resistant |
| necrostatin-1 | RIPK1 | 3.994668042461031 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0021 - AZD7762 on GCT
*Evidence: SHAP-0021*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **GCT** (master_ccl_id=271) |
| Tissue | soft tissue |
| Histology | malignant fibrous histiocytoma pleomorphic sarcoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **0.0929**
- RF-predicted log10(IC50): **-0.3147**
- Prediction error (observed - predicted): **+0.4076**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=73.9
- Cell cohort (311 pairs): mean=0.6968, q10=-1.0843, median=0.8437, q90=1.9853, sample percentile=25.4
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 21 (C_generalization): AZD7762 on GCT / ACH-000835 (Soft Tissue); observed log10(IC50)=+0.0929.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7311, |SHAP|=0.7311)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3087, |SHAP|=0.3087)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1477, |SHAP|=0.1477)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0741, |SHAP|=0.0741)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0549, |SHAP|=0.0549)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0518** (fingerprint_bit; SHAP=+0.0475, |SHAP|=0.0475)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0471, |SHAP|=0.0471)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **fp_0611** (fingerprint_bit; SHAP=-0.0439, |SHAP|=0.0439)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | -3.342248778117806 | more sensitive |
| docetaxel |  | -2.8810426678835523 | more sensitive |
| BRD-A71883111 | IDH1 | 3.5431230489650587 | more resistant |
| BRD-K29313308 | HDAC3 | 3.714710146493528 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0022 - AZD7762 on NCIH2452
*Evidence: SHAP-0022*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **NCIH2452** (master_ccl_id=155520) |
| Tissue | pleura |
| Histology | mesothelioma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-0.6016**
- RF-predicted log10(IC50): **-0.3125**
- Prediction error (observed - predicted): **-0.2892**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=37.4
- Cell cohort (236 pairs): mean=0.8693, q10=-0.8763, median=1.0943, q90=2.1634, sample percentile=13.1
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 22 (C_generalization): AZD7762 on NCI-H2452 / ACH-000092 (Pleura); observed log10(IC50)=-0.6016.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7210, |SHAP|=0.7210)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3084, |SHAP|=0.3084)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1471, |SHAP|=0.1471)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0709, |SHAP|=0.0709)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0457, |SHAP|=0.0457)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0611** (fingerprint_bit; SHAP=-0.0437, |SHAP|=0.0437)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0421, |SHAP|=0.0421)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0415, |SHAP|=0.0415)  
  _value=8.1409, z=+0.92; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| GSK461364 | PLK1 | -3.5146707479234816 | more sensitive |
| FQI-1 |  | -2.917213554864061 | more sensitive |
| BRD8899 | STK33 | 3.597308448184575 | more resistant |
| KU-55933 | ATM | 3.84716334458568 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0023 - AZD7762 on T24
*Evidence: SHAP-0023*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **T24** (master_ccl_id=1172) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **0.3256**
- RF-predicted log10(IC50): **-0.2994**
- Prediction error (observed - predicted): **+0.6250**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=83.5
- Cell cohort (272 pairs): mean=1.1327, q10=-0.5667, median=1.3307, q90=2.5552, sample percentile=23.2
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 23 (C_generalization): AZD7762 on T24 / ACH-000018 (Bladder/Urinary Tract); observed log10(IC50)=+0.3256.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7204, |SHAP|=0.7204)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3083, |SHAP|=0.3083)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1437, |SHAP|=0.1437)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0727, |SHAP|=0.0727)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0071** (fingerprint_bit; SHAP=+0.0470, |SHAP|=0.0470)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
6. **fp_0876** (fingerprint_bit; SHAP=+0.0442, |SHAP|=0.0442)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
7. **fp_0611** (fingerprint_bit; SHAP=-0.0438, |SHAP|=0.0438)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0416, |SHAP|=0.0416)  
  _value=9.3473, z=+1.31; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

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

## RPT-0024 - AZD7762 on NCIH1341
*Evidence: SHAP-0024*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **NCIH1341** (master_ccl_id=155400) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | small cell carcinoma |

### Response Summary
- Observed log10(IC50): **-0.5202**
- RF-predicted log10(IC50): **-0.3395**
- Prediction error (observed - predicted): **-0.1807**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=44.1
- Cell cohort (303 pairs): mean=0.3736, q10=-1.4067, median=0.5144, q90=1.7881, sample percentile=20.8
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 24 (C_generalization): AZD7762 on NCI-H1341 / ACH-000129 (Cervix); observed log10(IC50)=-0.5202.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7563, |SHAP|=0.7563)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3149, |SHAP|=0.3149)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1481, |SHAP|=0.1481)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0876** (fingerprint_bit; SHAP=+0.0626, |SHAP|=0.0626)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
5. **fp_0071** (fingerprint_bit; SHAP=+0.0472, |SHAP|=0.0472)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
6. **fp_0611** (fingerprint_bit; SHAP=-0.0435, |SHAP|=0.0435)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0405, |SHAP|=0.0405)  
  _value=4.8599, z=-0.14; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **fp_0997** (fingerprint_bit; SHAP=+0.0369, |SHAP|=0.0369)  
  _absent; representative SMARTS `[#7]:[#6](:[#6]):[#6]:[#6]:[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: Bax channel blocker, teniposide, methotrexate_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.762874945799765 | more sensitive |
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | -3.472413299613394 | more sensitive |
| BRD-K50799972 |  | 3.500978849572101 | more resistant |
| fumonisin B1 | CERS1;CERS2;CERS3;CERS4;CERS5;CERS6 | 3.9314517433715945 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0025 - AZD7762 on SNU308
*Evidence: SHAP-0025*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **SNU308** (master_ccl_id=1097) |
| Tissue | biliary tract |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **0.1881**
- RF-predicted log10(IC50): **-0.3135**
- Prediction error (observed - predicted): **+0.5016**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (783 pairs): mean=-0.3569, q10=-1.1432, median=-0.4246, q90=0.4819, sample percentile=77.7
- Cell cohort (163 pairs): mean=0.8734, q10=-0.7192, median=1.1400, q90=2.0961, sample percentile=27.0
- Interpretation: **close to the model prediction and cohort baselines**
- Selection reason: Manifest 25_pairs.csv row 25 (C_generalization): AZD7762 on SNU-308 / ACH-000141 (Biliary Tract); observed log10(IC50)=+0.1881.

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.7233, |SHAP|=0.7233)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0157** (fingerprint_bit; SHAP=-0.3083, |SHAP|=0.3083)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_
3. **fp_0032** (fingerprint_bit; SHAP=-0.1477, |SHAP|=0.1477)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
4. **fp_0994** (fingerprint_bit; SHAP=-0.0644, |SHAP|=0.0644)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0876** (fingerprint_bit; SHAP=+0.0462, |SHAP|=0.0462)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
6. **fp_0071** (fingerprint_bit; SHAP=+0.0450, |SHAP|=0.0450)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
7. **fp_0611** (fingerprint_bit; SHAP=-0.0437, |SHAP|=0.0437)  
  _present; representative SMARTS `[#6](-[#6@@H])(=[#8])-[#6@H]`; present in 1.2% of CTRPv2 compounds; example compounds: methotrexate, sirolimus, oligomycin A_
8. **CCN1 (3491)** (gene_expression; SHAP=+0.0410, |SHAP|=0.0410)  
  _value=5.5293, z=+0.08; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| MOLM13 | haematopoietic and lymphoid tissue | -3.697066847669615 | more sensitive |
| MFE319 | endometrium | -3.499889506044168 | more sensitive |
| MALME3M | skin | 3.091578055469087 | more resistant |
| MKN45 | stomach | 3.20295915386476 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | -2.141351172825898 | more sensitive |
| bortezomib | PSMB1;PSMB2;PSMB5;PSMD1;PSMD2 | -2.0808649774851538 | more sensitive |
| dacarbazine |  | 3.070505955772608 | more resistant |
| barasertib | AURKB | 3.5461333489216984 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---
