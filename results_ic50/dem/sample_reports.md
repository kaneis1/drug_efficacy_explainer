# Enriched Grounded Reports

## RPT-0001 — clofarabine on MDAMB415
*Evidence: EV-000007*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **clofarabine** (master_cpd_id=660288) |
| Mechanism / Activity | inducer of DNA damage |
| Cell Line | **MDAMB415** (master_ccl_id=652) |
| Tissue | breast |
| Histology | carcinoma |

### Response Summary
- [EV-000007] **clofarabine** on **MDAMB415**: observed AUC = **3.9977**
- [EV-000007] Kernel neighborhood weighted AUC = **-0.8123** (median=-0.8928, q10=-1.7048, q90=0.0475)
- [EV-000007] Global baseline AUC = 0.6419 (median=0.8477)
- [EV-000007] **Interpretation**: more resistant than similar drug-cell pairs

### Distinguishing Molecular Features
1. **fp_0666** (higher; z=8.62, neighborhood=1.000 vs global=0.013)  
  _[SMARTS: `[#6]:[#6]:[#6]:[#6](-[#17]):[#6]`; e.g. paclitaxel, N9-isopropylolomoucine, sirolimus; 5% of drugs]_
2. **fp_0639** (higher; z=6.22, neighborhood=1.000 vs global=0.025)  
  _[SMARTS: `[#6](-[#6@H])(:[#6]:[#6]:[#6]):[#6]`; e.g. BRD-K94991378, BRD-K71935468, QW-BI-011; 2% of drugs]_
3. **fp_1016** (higher; z=5.83, neighborhood=1.000 vs global=0.029)  
  _[SMARTS: `[#7]:[#6]:[#7](-[#6@H](-[#8])-[#6@@H]):[#6](=[#8]):[#7]`; e.g. azacitidine, triptolide, CHM-1; 1% of drugs]_
4. **fp_0527** (higher; z=5.76, neighborhood=1.000 vs global=0.029)  
  _[SMARTS: `[#7]-[#6](:[#6]):[#7]`; e.g. betulinic acid, PRIMA-1, GSK-3 inhibitor IX; 4% of drugs]_
5. **fp_0337** (higher; z=4.24, neighborhood=1.000 vs global=0.053)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6](:[#6](:[#6]):[#7])-[#8]`; e.g. ML311, fumonisin B1, CAL-101; 1% of drugs]_
6. **fp_0642** (higher; z=3.53, neighborhood=1.000 vs global=0.074)  
  _[SMARTS: `[#6]=[#6]-[#6](=[#8])-[#8]`; e.g. tretinoin, AGK-2, BRD8958; 1% of drugs]_
7. **fp_0322** (higher; z=3.16, neighborhood=1.000 vs global=0.091)  
  _[SMARTS: `[#8]-[#6](:[#6]):[#6]`; e.g. BRD9876, tamoxifen, BRD9647; 15% of drugs]_
8. **fp_0587** (higher; z=3.15, neighborhood=1.000 vs global=0.091)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6](:[#6]:[#6]):[#6]:[#6]`; e.g. doxorubicin, BRD9647, ML029; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| clofarabine | HS294T | skin | -0.7734 | 0.5641 |
| clofarabine | SKBR3 | breast | -1.6625 | 0.5585 |
| clofarabine | LN18 | central nervous system | -2.0377 | 0.5479 |
| clofarabine | MDAMB468 | breast | -0.1370 | 0.5472 |
| clofarabine | SF295 | central nervous system | -0.8405 | 0.5387 |

### Scope and Constraints
- [EV-000007] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000007] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0002 — BRD9647 on NALM6
*Evidence: EV-000008*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **BRD9647** (master_cpd_id=37479) |
| Mechanism / Activity | screening hit |
| Cell Line | **NALM6** (master_ccl_id=718) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic B cell leukaemia |

### Response Summary
- [EV-000008] **BRD9647** on **NALM6**: observed AUC = **-3.9968**
- [EV-000008] Kernel neighborhood weighted AUC = **0.8110** (median=0.9200, q10=-0.3324, q90=1.9369)
- [EV-000008] Global baseline AUC = 0.6419 (median=0.8477)
- [EV-000008] **Interpretation**: more sensitive than similar drug-cell pairs

### Distinguishing Molecular Features
1. **LAIR1 (3903)** (higher; z=2.75, neighborhood=6.790 vs global=0.991)
2. **APP (351)** (lower; z=-2.65, neighborhood=1.653 vs global=7.773)
3. **ALOX5AP (241)** (higher; z=2.48, neighborhood=7.057 vs global=1.551)
4. **SRGN (5552)** (higher; z=2.48, neighborhood=11.722 vs global=3.607)
5. **ITGAL (3683)** (higher; z=2.46, neighborhood=6.466 vs global=1.200)
6. **PLEK (5341)** (higher; z=2.46, neighborhood=6.279 vs global=1.010)
7. **LYZ (4069)** (higher; z=2.43, neighborhood=8.684 vs global=1.968)
8. **CCL5 (6352)** (higher; z=2.29, neighborhood=6.036 vs global=1.558)

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| SMER-3 | HT | haematopoietic and lymphoid tissue | -0.7415 | 1.0000 |
| BRD9647 | HT | haematopoietic and lymphoid tissue | 0.9122 | 1.0000 |
| BRD-K11533227 | HPBALL | haematopoietic and lymphoid tissue | 1.2888 | 1.0000 |
| AZD6482 | HPBALL | haematopoietic and lymphoid tissue | 1.6039 | 1.0000 |
| BRD-K35604418 | HPBALL | haematopoietic and lymphoid tissue | 1.3512 | 1.0000 |

### Scope and Constraints
- [EV-000008] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000008] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0003 — BRD-K14844214 on SUPT1
*Evidence: EV-000010*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **BRD-K14844214** (master_cpd_id=402775) |
| Mechanism / Activity | product of diversity oriented synthesis |
| Cell Line | **SUPT1** (master_ccl_id=1149) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic T cell leukaemia |

### Response Summary
- [EV-000010] **BRD-K14844214** on **SUPT1**: observed AUC = **-3.9996**
- [EV-000010] Kernel neighborhood weighted AUC = **0.6264** (median=0.2524, q10=-0.6505, q90=2.0365)
- [EV-000010] Global baseline AUC = 0.6419 (median=0.8477)
- [EV-000010] **Interpretation**: more sensitive than similar drug-cell pairs

### Distinguishing Molecular Features
1. **fp_0202** (higher; z=8.35, neighborhood=0.671 vs global=0.006)  
  _[SMARTS: `[#6]:[#6](-[#8]):[#6]`; e.g. gossypol, teniposide, epigallocatechin-3-monogallate; 7% of drugs]_
2. **fp_0327** (higher; z=4.10, neighborhood=0.671 vs global=0.025)  
  _[SMARTS: `[#7]-[#6](=[#8])/[#6]=[#6]/[#6]`; e.g. NSC23766, topotecan, LBH-589; 2% of drugs]_
3. **fp_0560** (higher; z=3.68, neighborhood=0.278 vs global=0.006)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6]-[#6](:[#6]):[#6]`; e.g. pifithrin-alpha, ML162, ML029; 2% of drugs]_
4. **fp_0969** (higher; z=3.37, neighborhood=0.671 vs global=0.037)  
  _[SMARTS: `[#6]-[#7](:[#6]):[#6]`; e.g. blebbistatin, purmorphamine, IC-87114; 5% of drugs]_
5. **fp_0195** (higher; z=3.30, neighborhood=0.671 vs global=0.038)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6]-[#6]-[#6]`; e.g. ML031, omacetaxine mepesuccinate, BRD1835; 1% of drugs]_
6. **fp_0322** (higher; z=3.16, neighborhood=1.000 vs global=0.091)  
  _[SMARTS: `[#8]-[#6](:[#6]):[#6]`; e.g. BRD9876, tamoxifen, BRD9647; 15% of drugs]_
7. **fp_0878** (higher; z=2.84, neighborhood=0.278 vs global=0.009)  
  _[SMARTS: `[#6]-[#7](-[#6])-[#6]`; e.g. CIL55, isoliquiritigenin, ouabain; 6% of drugs]_
8. **fp_0049** (higher; z=2.43, neighborhood=1.000 vs global=0.145)  
  _[SMARTS: `[#8]-[#6](=[#8])-[#6]`; e.g. MI-1, CID-5951923, BRD-K14844214; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| BRD-K14844214 | NCIH211 | lung | 1.9585 | 1.0000 |
| BRD-K14844214 | D283MED | central nervous system | 1.7867 | 1.0000 |
| BRD-K14844214 | BL70 | haematopoietic and lymphoid tissue | 2.2039 | 1.0000 |
| ML312 | ALLSIL | haematopoietic and lymphoid tissue | 1.8562 | 1.0000 |
| BRD-K14844214 | DAUDI | haematopoietic and lymphoid tissue | 1.9032 | 1.0000 |

### Scope and Constraints
- [EV-000010] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000010] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0004 — methotrexate on BEN
*Evidence: EV-000005*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **methotrexate** (master_cpd_id=30371) |
| Gene Target | DHFR |
| Mechanism / Activity | inhibitor of dihydrofolate reductase |
| Cell Line | **BEN** (master_ccl_id=60) |
| Tissue | lung |
| Histology | carcinoma |

### Response Summary
- [EV-000005] **methotrexate** on **BEN**: observed AUC = **-3.9992**
- [EV-000005] Kernel neighborhood weighted AUC = **-0.1086** (median=0.4487, q10=-2.4478, q90=1.6759)
- [EV-000005] Global baseline AUC = 0.6419 (median=0.8477)
- [EV-000005] **Interpretation**: more sensitive than similar drug-cell pairs

### Distinguishing Molecular Features
1. **fp_0607** (higher; z=4.14, neighborhood=0.544 vs global=0.016)  
  _[SMARTS: `[#6]-[#35]`; e.g. Bax channel blocker, ifosfamide, SB-225002; 12% of drugs]_
2. **fp_0538** (higher; z=3.47, neighborhood=1.000 vs global=0.077)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; e.g. NSC19630, crizotinib, NVP-BSK805; 1% of drugs]_
3. **fp_0281** (higher; z=2.36, neighborhood=0.394 vs global=0.025)  
  _[SMARTS: `[#6]=[#6]-[#6]`; e.g. BRD4132, Bax channel blocker, staurosporine; 4% of drugs]_
4. **fp_0195** (higher; z=1.85, neighborhood=0.394 vs global=0.038)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6]-[#6]-[#6]`; e.g. ML031, omacetaxine mepesuccinate, BRD1835; 1% of drugs]_
5. **fp_0328** (higher; z=1.69, neighborhood=0.130 vs global=0.005)  
  _[SMARTS: `[#6]:[#6](:[#6](:[#7]:[#6]):[#6]:[#6]):[#6]`; e.g. GSK-3 inhibitor IX, necrostatin-1, SID 26681509; 3% of drugs]_
6. **fp_0333** (higher; z=1.68, neighborhood=0.714 vs global=0.137)  
  _[SMARTS: `[#6]:[#6](:[#6]):[#6]`; e.g. BRD6340, Bax channel blocker, gossypol; 26% of drugs]_
7. **fp_0963** (higher; z=1.65, neighborhood=0.614 vs global=0.106)  
  _[SMARTS: `[#6]-[#7]-[#7]-[#6]-[#6]`; e.g. procarbazine, KU 0060648, vorapaxar; 1% of drugs]_
8. **fp_0975** (higher; z=1.62, neighborhood=0.524 vs global=0.081)  
  _[SMARTS: `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; e.g. simvastatin, parbendazole, lovastatin; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| methotrexate | LS513 | large intestine | -0.9390 | 1.0000 |
| methotrexate | SNU16 | stomach | -2.4863 | 1.0000 |
| methotrexate | IPC298 | skin | -1.4876 | 1.0000 |
| methotrexate | SW948 | large intestine | -2.5565 | 1.0000 |
| methotrexate | GSS | stomach | -2.4473 | 1.0000 |

### Scope and Constraints
- [EV-000005] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000005] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0005 — istradefylline on KASUMI2
*Evidence: EV-000006*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **istradefylline** (master_cpd_id=687694) |
| Gene Target | ADORA2A |
| Mechanism / Activity | antagonist of the adenosine A2A receptor |
| Cell Line | **KASUMI2** (master_ccl_id=519) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | acute lymphoblastic B cell leukaemia |

### Response Summary
- [EV-000006] **istradefylline** on **KASUMI2**: observed AUC = **3.9977**
- [EV-000006] Kernel neighborhood weighted AUC = **0.6914** (median=0.6872, q10=-0.3693, q90=1.7421)
- [EV-000006] Global baseline AUC = 0.6419 (median=0.8477)
- [EV-000006] **Interpretation**: more resistant than similar drug-cell pairs

### Distinguishing Molecular Features
1. **fp_0017** (higher; z=2.33, neighborhood=1.000 vs global=0.156)  
  _[SMARTS: `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; e.g. bexarotene, SR-II-138A, CR-1-31B; 2% of drugs]_
2. **fp_0071** (higher; z=2.03, neighborhood=0.475 vs global=0.047)  
  _[SMARTS: `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; e.g. N9-isopropylolomoucine, purmorphamine, IC-87114; 5% of drugs]_
3. **fp_0894** (higher; z=1.89, neighborhood=0.105 vs global=0.003)  
  _[SMARTS: `[#6]-[#6](=[#8])-[#6@H]1-[#8]-[#6@H]-1-[#6]`; e.g. cerulenin, BRD-K66453893, neratinib; 2% of drugs]_
4. **fp_0385** (higher; z=1.82, neighborhood=0.905 vs global=0.190)  
  _[SMARTS: `[#7]-[#6](:[#7]):[#16]`; e.g. dasatinib, BRD-A94377914, selumetinib; 4% of drugs]_
5. **fp_0799** (higher; z=1.64, neighborhood=0.635 vs global=0.114)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6]`; e.g. ciclopirox, blebbistatin, pifithrin-alpha; 4% of drugs]_
6. **fp_0748** (higher; z=1.51, neighborhood=0.105 vs global=0.004)  
  _[SMARTS: `[#6]-[#6](-[#6])-[#7](:[#6]:[#7]):[#6](:[#6]):[#7]`; e.g. N9-isopropylolomoucine, dexamethasone, LY-2183240; 1% of drugs]_
7. **fp_0999** (higher; z=1.50, neighborhood=0.465 vs global=0.073)  
  _[SMARTS: `[#7]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]`; e.g. tacedinaline, entinostat, Merck60; 3% of drugs]_
8. **fp_0362** (higher; z=1.41, neighborhood=0.255 vs global=0.027)  
  _[SMARTS: `[#8]-[#6](=[#8])-[#6]`; e.g. staurosporine, vincristine, omacetaxine mepesuccinate; 3% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| axitinib | NAMALWA | haematopoietic and lymphoid tissue | 0.4636 | 1.0000 |
| sunitinib | DV90 | lung | 0.6165 | 1.0000 |
| sunitinib | IPC298 | skin | 0.7780 | 1.0000 |
| SU11274 | NAMALWA | haematopoietic and lymphoid tissue | -0.3677 | 1.0000 |
| AA-COCF3 | NAMALWA | haematopoietic and lymphoid tissue | 0.7186 | 1.0000 |

### Scope and Constraints
- [EV-000006] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000006] Statements are grounded in this evidence entry only and do not imply causality.

---
