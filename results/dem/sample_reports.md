# Enriched Grounded Reports

## RPT-0001 — ouabain on TUHR10TKB
*Evidence: EV-000010*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **ouabain** (master_cpd_id=37190) |
| Gene Target | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 |
| Mechanism / Activity | cardiac glycoside; inhibitor of the Na+/K+-ATPase |
| Cell Line | **TUHR10TKB** (master_ccl_id=1213) |
| Tissue | kidney |
| Histology | carcinoma |

### Response Summary
- [EV-000010] **ouabain** on **TUHR10TKB**: observed AUC = **29.3500**
- [EV-000010] Kernel neighborhood weighted AUC = **7.8738** (median=7.7118, q10=4.4858, q90=10.8793)
- [EV-000010] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000010] **Interpretation**: exceptionally resistant (AUC far above both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0109** (higher; z=10.07, neighborhood=0.508 vs global=0.003)  
  _[SMARTS: `[#15]-[#7]-[#6]`; e.g. cyclophosphamide, ouabain, apicidin; 2% of drugs]_
2. **fp_0767** (higher; z=6.54, neighborhood=1.000 vs global=0.023)  
  _[SMARTS: `[#6]-[#7](-[#6])-[#6]`; e.g. Bax channel blocker, trifluoperazine, parbendazole; 11% of drugs]_
3. **fp_0557** (higher; z=6.44, neighborhood=0.508 vs global=0.006)  
  _[SMARTS: `[#6](-[#6@@H])(:[#6]:[#6]:[#6]):[#6]`; e.g. paclitaxel, NSC23766, importazole; 6% of drugs]_
4. **fp_0156** (higher; z=6.44, neighborhood=0.508 vs global=0.006)  
  _[SMARTS: `[#6]:[#6](-[#8]-[#6@@H](-[#8])-[#6@@]):[#6]`; e.g. austocystin D, necrostatin-7, NVP-231; 1% of drugs]_
5. **fp_0939** (higher; z=4.91, neighborhood=0.492 vs global=0.010)  
  _[SMARTS: `N`; e.g. niclosamide, SB-225002, compound 1B; 4% of drugs]_
6. **fp_0273** (higher; z=4.27, neighborhood=0.508 vs global=0.014)  
  _[SMARTS: `[#6]=[#6](-[#16])-[#6]`; e.g. BRD4132, NSC23766, tanespimycin; 2% of drugs]_
7. **fp_0479** (higher; z=4.17, neighborhood=0.492 vs global=0.013)  
  _[SMARTS: `[#6]-[#6]=[#6]`; e.g. compound 1B, SCH-79797, AA-COCF3; 2% of drugs]_
8. **fp_0997** (higher; z=4.11, neighborhood=0.508 vs global=0.015)  
  _[SMARTS: `[#7]:[#6](:[#6]):[#6]:[#6]:[#6]`; e.g. Bax channel blocker, teniposide, methotrexate; 5% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| CR-1-31B | TUHR10TKB | kidney | 10.5180 | 0.5300 |
| ouabain | TUHR4TKB | kidney | 6.7512 | 0.1600 |
| CR-1-31B | TUHR4TKB | kidney | 7.9218 | 0.1600 |
| ouabain | MG63 | bone | 3.8460 | 0.1600 |
| CR-1-31B | OSRC2 | kidney | 9.7785 | 0.1500 |

### Scope and Constraints
- [EV-000010] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000010] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0002 — cytarabine hydrochloride on SKMEL2
*Evidence: EV-000008*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **cytarabine hydrochloride** (master_cpd_id=62690) |
| Mechanism / Activity | inducer of DNA damage |
| Cell Line | **SKMEL2** (master_ccl_id=1041) |
| Tissue | skin |
| Histology | malignant melanoma |

### Response Summary
- [EV-000008] **cytarabine hydrochloride** on **SKMEL2**: observed AUC = **27.1820**
- [EV-000008] Kernel neighborhood weighted AUC = **12.5114** (median=12.9875, q10=9.4966, q90=14.6350)
- [EV-000008] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000008] **Interpretation**: exceptionally resistant (AUC far above both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0529** (higher; z=8.22, neighborhood=1.000 vs global=0.015)  
  _[SMARTS: `[#6](-[#6@])-[#6]-[#6@@H](-[#6@@H])-[#6@]`; e.g. ouabain, 16-beta-bromoandrosterone, ABT-737; 1% of drugs]_
2. **fp_0743** (higher; z=6.91, neighborhood=1.000 vs global=0.020)  
  _[SMARTS: `[#6]-[#16](=[#8])(=[#8])-[#7]-[#6](:[#6]):[#6]`; e.g. ciclosporin, belinostat, CHIR-99021; 1% of drugs]_
3. **fp_0929** (higher; z=5.95, neighborhood=1.000 vs global=0.027)  
  _[SMARTS: `[#6]-[#6](:[#6]:[#6]):[#6]:[#6]`; e.g. BRD4132, ciclopirox, LY-2183240; 3% of drugs]_
4. **fp_0836** (higher; z=5.00, neighborhood=1.000 vs global=0.038)  
  _[SMARTS: `[#6]-[#8]-[#6]-[#6]-[#8]`; e.g. ML083, selumetinib, ML203; 2% of drugs]_
5. **fp_0923** (higher; z=4.59, neighborhood=1.000 vs global=0.045)  
  _[SMARTS: `[#6]:[#6]:[#6](-[#6]-[#16]):[#6](-[#6]):[#16]`; e.g. CIL55, TGX-221, CIL55A; 1% of drugs]_
6. **fp_0340** (higher; z=4.18, neighborhood=1.000 vs global=0.054)  
  _[SMARTS: `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](-[#6])-[#6]`; e.g. SB-431542, apicidin, ML311; 1% of drugs]_
7. **fp_0712** (higher; z=3.84, neighborhood=1.000 vs global=0.064)  
  _[SMARTS: `[#6]-[#7](-[#6]-[#6]-[#7])-[#6]`; e.g. betulinic acid, parbendazole, daporinad; 2% of drugs]_
8. **fp_0547** (higher; z=3.62, neighborhood=1.000 vs global=0.071)  
  _[SMARTS: `[#6]-[#6]=[#6]`; e.g. simvastatin, lovastatin, piperlongumine; 5% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| cytarabine hydrochloride | SUIT2 | pancreas | 12.9515 | 1.0000 |
| cytarabine hydrochloride | SQ1 | lung | 17.5470 | 1.0000 |
| cytarabine hydrochloride | HCC1937 | breast | 15.2280 | 1.0000 |
| cytarabine hydrochloride | SNU8 | ovary | 14.3590 | 1.0000 |
| cytarabine hydrochloride | HCT116 | large intestine | 13.9400 | 1.0000 |

### Scope and Constraints
- [EV-000008] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000008] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0003 — N9-isopropylolomoucine on CADOES1
*Evidence: EV-000002*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **N9-isopropylolomoucine** (master_cpd_id=45093) |
| Gene Target | CCNB1;CDK1;CDK5;CDK5R1 |
| Mechanism / Activity | inhibitor of CDK1/cyclin B and CDK5/p35 complexes |
| Cell Line | **CADOES1** (master_ccl_id=108) |
| Tissue | bone |
| Histology | Ewings sarcoma peripheral primitive neuroectodermal tumor |

### Response Summary
- [EV-000002] **N9-isopropylolomoucine** on **CADOES1**: observed AUC = **0.0835**
- [EV-000002] Kernel neighborhood weighted AUC = **12.0956** (median=12.3555, q10=9.7663, q90=13.7757)
- [EV-000002] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000002] **Interpretation**: exceptionally sensitive (AUC far below both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0456** (higher; z=5.82, neighborhood=0.410 vs global=0.005)  
  _[SMARTS: `[#7]-[#6]-[#6]`; e.g. ML006, Bax channel blocker, gossypol; 32% of drugs]_
2. **fp_0439** (higher; z=5.21, neighborhood=0.410 vs global=0.006)  
  _[SMARTS: `[#7]-[#6@@H](-[#6])-[#8]-[#6@@H](-[#6@H])-[#6]`; e.g. decitabine, tosedostat, PX-12; 1% of drugs]_
3. **fp_0992** (higher; z=3.99, neighborhood=0.760 vs global=0.034)  
  _[SMARTS: `[#16]-[#6](:[#6]:[#6]:[#6]):[#6]`; e.g. MG-132, L-685458, avrainvillamide; 2% of drugs]_
4. **fp_0538** (higher; z=3.83, neighborhood=1.000 vs global=0.064)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; e.g. NSC19630, crizotinib, NVP-BSK805; 1% of drugs]_
5. **fp_0495** (higher; z=3.53, neighborhood=1.000 vs global=0.074)  
  _[SMARTS: `[#6]:[#6](:[#6]:[#6](-[#6]):[#6]):[#6]`; e.g. BRD9876, procarbazine, doxorubicin; 2% of drugs]_
6. **fp_0272** (higher; z=3.28, neighborhood=0.760 vs global=0.049)  
  _[SMARTS: `[#6]-[#6](=[#8])-[#6]`; e.g. niclosamide, blebbistatin, tacrolimus; 2% of drugs]_
7. **fp_0328** (higher; z=2.98, neighborhood=0.240 vs global=0.006)  
  _[SMARTS: `[#6]:[#6](:[#6](:[#7]:[#6]):[#6]:[#6]):[#6]`; e.g. GSK-3 inhibitor IX, necrostatin-1, SID 26681509; 3% of drugs]_
8. **fp_0725** (higher; z=2.69, neighborhood=0.760 vs global=0.070)  
  _[SMARTS: `N`; e.g. cimetidine, dacarbazine, pifithrin-alpha; 4% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| tipifarnib-P2 | MV411 | haematopoietic and lymphoid tissue | 6.6149 | 1.0000 |
| N9-isopropylolomoucine | CMK | haematopoietic and lymphoid tissue | 13.0400 | 1.0000 |
| StemRegenin 1 | DMS79 | lung | 12.7110 | 1.0000 |
| StemRegenin 1 | OPM2 | haematopoietic and lymphoid tissue | 11.9880 | 1.0000 |
| N9-isopropylolomoucine | CA46 | haematopoietic and lymphoid tissue | 11.9510 | 1.0000 |

### Scope and Constraints
- [EV-000002] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000002] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0004 — regorafenib on EOL1
*Evidence: EV-000004*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **regorafenib** (master_cpd_id=628613) |
| Gene Target | BRAF;KDR;KIT;RET |
| Mechanism / Activity | inhibitor of BRAF, RET, KIT, and VEGFR2 |
| Cell Line | **EOL1** (master_ccl_id=244) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- [EV-000004] **regorafenib** on **EOL1**: observed AUC = **0.1085**
- [EV-000004] Kernel neighborhood weighted AUC = **11.7531** (median=12.3290, q10=10.8555, q90=14.6102)
- [EV-000004] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000004] **Interpretation**: exceptionally sensitive (AUC far below both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0633** (higher; z=6.70, neighborhood=0.942 vs global=0.019)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6]`; e.g. gossypol, tanespimycin, manumycin A; 3% of drugs]_
2. **fp_0888** (higher; z=4.49, neighborhood=0.942 vs global=0.042)  
  _[SMARTS: `[#7]:[#6](-[#7]-[#6](:[#6]):[#6]):[#6]`; e.g. niclosamide, piperlongumine, PD 153035; 5% of drugs]_
3. **fp_0774** (higher; z=3.82, neighborhood=0.942 vs global=0.057)  
  _[SMARTS: `[#6]=[#7]-[#7]`; e.g. cerulenin, compound 1B, BRD-K41597374; 1% of drugs]_
4. **fp_0062** (higher; z=3.78, neighborhood=1.000 vs global=0.065)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#16]`; e.g. Merck60, cytarabine hydrochloride, VX-680; 4% of drugs]_
5. **fp_0679** (higher; z=3.78, neighborhood=0.942 vs global=0.058)  
  _[SMARTS: `[#6]-[#6]-[#6]`; e.g. paclitaxel, doxorubicin, ouabain; 9% of drugs]_
6. **fp_0455** (higher; z=3.50, neighborhood=0.942 vs global=0.067)  
  _[SMARTS: `[#6]:[#6](-[#6]-[#7](:[#6]):[#6]):[#6]`; e.g. BRD-K94991378, SCH-79797, zebularine; 2% of drugs]_
7. **fp_0597** (higher; z=3.48, neighborhood=0.942 vs global=0.068)  
  _[SMARTS: `[#6](-[#6@@H])-[#6@@H](-[#6])-[#6]=[#6]`; e.g. simvastatin, lovastatin, tacrolimus; 1% of drugs]_
8. **fp_0877** (higher; z=3.44, neighborhood=0.958 vs global=0.071)  
  _[SMARTS: `[#6]-[#7](:[#6]):[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; e.g. selumetinib, ML029, nutlin-3; 1% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| sorafenib | EOL1 | haematopoietic and lymphoid tissue | 0.1728 | 0.8400 |
| WZ4002 | EOL1 | haematopoietic and lymphoid tissue | 10.8150 | 0.5800 |
| saracatinib | EOL1 | haematopoietic and lymphoid tissue | 7.0704 | 0.5400 |
| regorafenib | MOLM13 | haematopoietic and lymphoid tissue | 6.6237 | 0.4800 |
| regorafenib | MV411 | haematopoietic and lymphoid tissue | 7.1288 | 0.4700 |

### Scope and Constraints
- [EV-000004] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000004] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0005 — SCH-529074 on MESSA
*Evidence: EV-000007*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **SCH-529074** (master_cpd_id=609062) |
| Gene Target | TP53 |
| Mechanism / Activity | activator of mutant p53 |
| Cell Line | **MESSA** (master_ccl_id=668) |
| Tissue | soft tissue |
| Histology | sarcoma |

### Response Summary
- [EV-000007] **SCH-529074** on **MESSA**: observed AUC = **22.3390**
- [EV-000007] Kernel neighborhood weighted AUC = **12.5213** (median=13.2020, q10=9.0083, q90=14.7763)
- [EV-000007] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000007] **Interpretation**: exceptionally resistant (AUC far above both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0663** (higher; z=3.41, neighborhood=0.550 vs global=0.024)  
  _[SMARTS: `[#6]-[#7](-[#6])-[#6]`; e.g. chlorambucil, sitagliptin, compound 1B; 2% of drugs]_
2. **fp_0540** (higher; z=1.85, neighborhood=0.174 vs global=0.008)  
  _[SMARTS: `[#6]-[#6]-[#6]`; e.g. phloretin, chlorambucil, methotrexate; 8% of drugs]_
3. **fp_0902** (higher; z=1.81, neighborhood=1.000 vs global=0.234)  
  _[SMARTS: `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; e.g. teniposide, NSC23766, etoposide; 1% of drugs]_
4. **fp_0893** (higher; z=1.77, neighborhood=0.306 vs global=0.026)  
  _[SMARTS: `[#6]=[#8]`; e.g. CIL55, tretinoin, betulinic acid; 61% of drugs]_
5. **fp_0486** (higher; z=1.72, neighborhood=1.000 vs global=0.252)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#6]`; e.g. CIL55, paclitaxel, procarbazine; 18% of drugs]_
6. **fp_0491** (higher; z=1.67, neighborhood=0.354 vs global=0.037)  
  _[SMARTS: `[#6]-[#7]-[#6]`; e.g. NSC23766, PD 153035, purmorphamine; 11% of drugs]_
7. **fp_0305** (higher; z=1.65, neighborhood=0.306 vs global=0.029)  
  _[SMARTS: `[#6]-[#6]-[#7]`; e.g. Bax channel blocker, cyclophosphamide, tacrolimus; 4% of drugs]_
8. **fp_0180** (higher; z=1.62, neighborhood=0.171 vs global=0.010)  
  _[SMARTS: `[#6]-[#6]-[#7](-[#6])-[#6]`; e.g. doxorubicin, compound 1B, brefeldin A; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| SCH-529074 | NCIH1581 | lung | 12.2880 | 1.0000 |
| BIRB-796 | TE441T | soft tissue | 14.3420 | 1.0000 |
| BIRB-796 | TOV112D | ovary | 13.8120 | 1.0000 |
| SCH-529074 | SBC5 | lung | 13.3650 | 1.0000 |
| BIRB-796 | SBC5 | lung | 14.9490 | 1.0000 |

### Scope and Constraints
- [EV-000007] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000007] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0006 — foretinib on EOL1
*Evidence: EV-000003*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **foretinib** (master_cpd_id=628607) |
| Gene Target | KDR;MET |
| Mechanism / Activity | inhibitor of MET and VEGFR2 |
| Cell Line | **EOL1** (master_ccl_id=244) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- [EV-000003] **foretinib** on **EOL1**: observed AUC = **0.0691**
- [EV-000003] Kernel neighborhood weighted AUC = **9.5686** (median=9.6166, q10=6.8418, q90=12.7022)
- [EV-000003] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000003] **Interpretation**: exceptionally sensitive (AUC far below both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0728** (higher; z=7.90, neighborhood=0.878 vs global=0.012)  
  _[SMARTS: `Br`; e.g. Bax channel blocker, manumycin A, SB-225002; 5% of drugs]_
2. **fp_0700** (higher; z=7.87, neighborhood=0.858 vs global=0.012)  
  _[SMARTS: `[#6]:[#6](:[#6]):[#7]`; e.g. sildenafil, methotrexate, N9-isopropylolomoucine; 7% of drugs]_
3. **fp_0380** (higher; z=7.01, neighborhood=0.858 vs global=0.015)  
  _[SMARTS: `[#6]-[#6](-[#6])-[#7]-[#6]`; e.g. procarbazine, GSK-3 inhibitor IX, CIL70; 3% of drugs]_
4. **fp_0640** (higher; z=6.29, neighborhood=0.858 vs global=0.018)  
  _[SMARTS: `[#6]-[#6]-[#8]`; e.g. doxorubicin, compound 1B, dexamethasone; 2% of drugs]_
5. **fp_0108** (higher; z=5.44, neighborhood=0.858 vs global=0.024)  
  _[SMARTS: `[#6](-[#6@@])(:[#6](-[#8]-[#6@]):[#6]:[#6]):[#6]`; e.g. omacetaxine mepesuccinate, RITA, SR-II-138A; 1% of drugs]_
6. **fp_0147** (higher; z=4.90, neighborhood=0.858 vs global=0.029)  
  _[SMARTS: `N`; e.g. azacitidine, paclitaxel, methotrexate; 23% of drugs]_
7. **fp_0521** (higher; z=4.89, neighborhood=0.858 vs global=0.030)  
  _[SMARTS: `[#6]-[#6](=[#8])-[#8]-[#6@H]`; e.g. paclitaxel, staurosporine, cerulenin; 1% of drugs]_
8. **fp_1003** (higher; z=4.37, neighborhood=0.902 vs global=0.041)  
  _[SMARTS: `[#6]-[#7](-[#6])-[#16](=[#8])(=[#8])-[#6](:[#6]):[#6]`; e.g. BRD4132, IC-87114, BRD-K66453893; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| foretinib | SUDHL8 | haematopoietic and lymphoid tissue | 9.8567 | 0.9900 |
| foretinib | SUDHL4 | haematopoietic and lymphoid tissue | 9.5582 | 0.9900 |
| foretinib | CHP126 | autonomic ganglia | 9.4961 | 0.9900 |
| foretinib | L428 | haematopoietic and lymphoid tissue | 11.9240 | 0.9900 |
| foretinib | KYO1 | haematopoietic and lymphoid tissue | 6.3112 | 0.9900 |

### Scope and Constraints
- [EV-000003] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000003] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0007 — nilotinib on BT549
*Evidence: EV-000001*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **nilotinib** (master_cpd_id=374749) |
| Gene Target | ABL1;BCR;KIT |
| Mechanism / Activity | inhibitor of ABL1, BCR, and c-KIT |
| Cell Line | **BT549** (master_ccl_id=99) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- [EV-000001] **nilotinib** on **BT549**: observed AUC = **23.7050**
- [EV-000001] Kernel neighborhood weighted AUC = **14.2751** (median=14.4855, q10=12.3835, q90=15.7423)
- [EV-000001] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000001] **Interpretation**: exceptionally resistant (AUC far above both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0934** (higher; z=11.68, neighborhood=1.000 vs global=0.007)  
  _[SMARTS: `[#6]-[#6@H](-[#6])/[#6]=[#6](\[#6])-[#6@@H]`; e.g. ciclosporin, sirolimus, parthenolide; 2% of drugs]_
2. **fp_0680** (higher; z=7.11, neighborhood=1.000 vs global=0.019)  
  _[SMARTS: `[#6]-[#6]-[#6@H]`; e.g. CIL55, simvastatin, lovastatin; 6% of drugs]_
3. **fp_0929** (higher; z=5.95, neighborhood=1.000 vs global=0.027)  
  _[SMARTS: `[#6]-[#6](:[#6]:[#6]):[#6]:[#6]`; e.g. BRD4132, ciclopirox, LY-2183240; 3% of drugs]_
4. **fp_1010** (higher; z=5.09, neighborhood=1.000 vs global=0.037)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6]`; e.g. topotecan, LBH-589, FGIN-1-27; 3% of drugs]_
5. **fp_0811** (higher; z=4.56, neighborhood=1.000 vs global=0.046)  
  _[SMARTS: `[#16]-[#6](:[#6]):[#6]`; e.g. VX-680, axitinib, navitoclax; 2% of drugs]_
6. **fp_0774** (higher; z=4.07, neighborhood=1.000 vs global=0.057)  
  _[SMARTS: `[#6]=[#7]-[#7]`; e.g. cerulenin, compound 1B, BRD-K41597374; 1% of drugs]_
7. **fp_0679** (higher; z=4.02, neighborhood=1.000 vs global=0.058)  
  _[SMARTS: `[#6]-[#6]-[#6]`; e.g. paclitaxel, doxorubicin, ouabain; 9% of drugs]_
8. **fp_0538** (higher; z=3.83, neighborhood=1.000 vs global=0.064)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; e.g. NSC19630, crizotinib, NVP-BSK805; 1% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| nilotinib | KYSE180 | oesophagus | 14.0760 | 1.0000 |
| nilotinib | OV56 | ovary | 15.5670 | 1.0000 |
| nilotinib | SNU213 | pancreas | 15.7400 | 1.0000 |
| nilotinib | WM1799 | skin | 14.3070 | 1.0000 |
| nilotinib | NCIH441 | lung | 15.3490 | 1.0000 |

### Scope and Constraints
- [EV-000001] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000001] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0008 — pitstop2 on SNU886
*Evidence: EV-000009*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **pitstop2** (master_cpd_id=660985) |
| Gene Target | CLTA;CLTB;CLTC;CLTCL1 |
| Mechanism / Activity | inhibitor of clathrin and clathrin-independent endocytosis |
| Cell Line | **SNU886** (master_ccl_id=1128) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- [EV-000009] **pitstop2** on **SNU886**: observed AUC = **23.1410**
- [EV-000009] Kernel neighborhood weighted AUC = **14.8600** (median=14.8240, q10=13.9060, q90=15.9143)
- [EV-000009] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000009] **Interpretation**: exceptionally resistant (AUC far above both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0398** (higher; z=24.24, neighborhood=1.000 vs global=0.002)  
  _[SMARTS: `[#6]-[#7](-[#6]-[#6]-[#6])-[#6]`; e.g. pifithrin-alpha, IU1, SNX-2112; 3% of drugs]_
2. **fp_0347** (higher; z=18.61, neighborhood=1.000 vs global=0.003)  
  _[SMARTS: `[#7]-[#6@H](-[#6@@H])-[#6]-[#7](-[#6@])-[#6]`; e.g. mitomycin, TPCA-1, TG-101348; 2% of drugs]_
3. **fp_0985** (higher; z=12.33, neighborhood=1.000 vs global=0.007)  
  _[SMARTS: `[#6]-[#7](-[#6])-[#6]`; e.g. sitagliptin, BRD-K71935468, erastin; 5% of drugs]_
4. **fp_0601** (higher; z=10.10, neighborhood=1.000 vs global=0.010)  
  _[SMARTS: `[#6]:[#7]:[#6](:[#6](:[#6])-[#17])-[#7]-[#6]`; e.g. dacarbazine, decitabine, NVP-TAE684; 1% of drugs]_
5. **fp_0562** (higher; z=9.41, neighborhood=1.000 vs global=0.011)  
  _[SMARTS: `[#6]:[#6]:[#7]:[#6]:[#6]`; e.g. betulinic acid, paclitaxel, entinostat; 8% of drugs]_
6. **fp_0154** (higher; z=9.19, neighborhood=1.000 vs global=0.012)  
  _[SMARTS: `[#6]-[#6](:[#6]):[#7]:[#6](:[#6]):[#6]`; e.g. SRT-1720, SNS-032, GDC-0941; 1% of drugs]_
7. **fp_0206** (higher; z=8.52, neighborhood=1.000 vs global=0.014)  
  _[SMARTS: `[#6]-[#6@@H](-[#6])-[#8]`; e.g. ML050, Mdivi-1, brefeldin A; 2% of drugs]_
8. **fp_0733** (higher; z=6.15, neighborhood=1.000 vs global=0.026)  
  _[SMARTS: `[#6]:[#6](:[#6]:[#7]:[#6]):[#6]`; e.g. paclitaxel, BRD-K27224038, SID 26681509; 1% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| pitstop2 | LOUNH91 | lung | 14.5750 | 1.0000 |
| pitstop2 | NCIH2052 | pleura | 15.0000 | 1.0000 |
| pitstop2 | HUPT4 | pancreas | 14.7480 | 1.0000 |
| pitstop2 | PATU8902 | pancreas | 15.2890 | 1.0000 |
| pitstop2 | BECKER | central nervous system | 14.2610 | 1.0000 |

### Scope and Constraints
- [EV-000009] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000009] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0009 — AZD7762 on EOL1
*Evidence: EV-000005*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **AZD7762** (master_cpd_id=660777) |
| Gene Target | CHEK1;CHEK2 |
| Mechanism / Activity | inhibitor of checkpoint kinases 1 and 2 |
| Cell Line | **EOL1** (master_ccl_id=244) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- [EV-000005] **AZD7762** on **EOL1**: observed AUC = **0.1108**
- [EV-000005] Kernel neighborhood weighted AUC = **7.2569** (median=7.0634, q10=4.4558, q90=10.4526)
- [EV-000005] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000005] **Interpretation**: exceptionally sensitive (AUC far below both neighborhood and global baselines)

### Distinguishing Molecular Features
1. **fp_0354** (higher; z=6.65, neighborhood=0.945 vs global=0.020)  
  _[SMARTS: `[#6]:[#6](:[#6])-[#7+](-[#8-])=[#8]`; e.g. compound 1B, BRD-K92856060, omacetaxine mepesuccinate; 2% of drugs]_
2. **fp_0032** (higher; z=5.52, neighborhood=0.945 vs global=0.028)  
  _[SMARTS: `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; e.g. SB-431542, apicidin, MK-2206; 4% of drugs]_
3. **fp_0281** (higher; z=5.31, neighborhood=0.945 vs global=0.031)  
  _[SMARTS: `[#6]=[#6]-[#6]`; e.g. BRD4132, Bax channel blocker, staurosporine; 4% of drugs]_
4. **fp_0157** (higher; z=5.05, neighborhood=0.945 vs global=0.034)  
  _[SMARTS: `[#6]-[#6](-[#6])-[#7]`; e.g. CIL55, BRD4132, phloretin; 9% of drugs]_
5. **fp_0760** (higher; z=4.11, neighborhood=0.945 vs global=0.050)  
  _[SMARTS: `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](=[#8])-[#6]`; e.g. betulinic acid, paclitaxel, ouabain; 4% of drugs]_
6. **fp_0597** (higher; z=3.49, neighborhood=0.945 vs global=0.068)  
  _[SMARTS: `[#6](-[#6@@H])-[#6@@H](-[#6])-[#6]=[#6]`; e.g. simvastatin, lovastatin, tacrolimus; 1% of drugs]_
7. **fp_0966** (higher; z=3.26, neighborhood=0.945 vs global=0.077)  
  _[SMARTS: `[#7]-[#6](=[#8])-[#7]-[#6](:[#6]):[#6]`; e.g. LBH-589, PDMP, ML050; 5% of drugs]_
8. **fp_0208** (higher; z=2.94, neighborhood=0.945 vs global=0.093)  
  _[SMARTS: `[#6]-[#6]=[#6]`; e.g. NSC23766, topotecan, cerulenin; 2% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| AZD7762 | JM1 | haematopoietic and lymphoid tissue | 5.9094 | 0.9800 |
| AZD7762 | RCHACV | haematopoietic and lymphoid tissue | 4.3657 | 0.9800 |
| AZD7762 | RI1 | haematopoietic and lymphoid tissue | 4.1600 | 0.9800 |
| AZD7762 | HUNS1 | haematopoietic and lymphoid tissue | 7.0011 | 0.9800 |
| AZD7762 | NOMO1 | haematopoietic and lymphoid tissue | 6.4395 | 0.9800 |

### Scope and Constraints
- [EV-000005] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000005] Statements are grounded in this evidence entry only and do not imply causality.

---

## RPT-0010 — dinaciclib on EOL1
*Evidence: EV-000006*

### Sample Identity
| Property | Value |
|----------|-------|
| Drug | **dinaciclib** (master_cpd_id=687578) |
| Gene Target | CDK1;CDK2;CDK5;CDK9 |
| Mechanism / Activity | inhibitor of cyclin-dependent kinases |
| Cell Line | **EOL1** (master_ccl_id=244) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | haematopoietic neoplasm |
| Subtype | acute myeloid leukaemia |

### Response Summary
- [EV-000006] **dinaciclib** on **EOL1**: observed AUC = **0.1081**
- [EV-000006] Kernel neighborhood weighted AUC = **2.8318** (median=5.3134, q10=1.4906, q90=9.4927)
- [EV-000006] Global baseline AUC = 12.8613 (median=13.5430)
- [EV-000006] **Interpretation**: more sensitive than similar drug-cell pairs

### Distinguishing Molecular Features
1. **fp_0295** (higher; z=12.76, neighborhood=0.943 vs global=0.005)  
  _[SMARTS: `[#6]-[#6]-[#6]`; e.g. tretinoin, simvastatin, GSK-3 inhibitor IX; 2% of drugs]_
2. **fp_0259** (higher; z=12.23, neighborhood=0.943 vs global=0.006)  
  _[SMARTS: `[#6](-[#6@H])-[#6]-[#6]-[#6]`; e.g. tretinoin, BRD-A94377914, Ki8751; 3% of drugs]_
3. **fp_0051** (higher; z=12.02, neighborhood=0.943 vs global=0.006)  
  _[SMARTS: `[#6]-[#8]-[#6](-[#7])=[#8]`; e.g. mitomycin, vincristine, BRD-K33199242; 1% of drugs]_
4. **fp_0727** (higher; z=8.96, neighborhood=0.943 vs global=0.011)  
  _[SMARTS: `[#8]-[#6@@H](-[#6])-[#8]-[#6@H](-[#6@H])-[#6@H]`; e.g. etoposide, LY-2157299, BRD-M00053801; 1% of drugs]_
5. **fp_0842** (higher; z=7.50, neighborhood=0.943 vs global=0.016)  
  _[SMARTS: `[#6]:[#6]:[#7]`; e.g. gossypol, doxorubicin, SB-431542; 17% of drugs]_
6. **fp_0388** (higher; z=5.91, neighborhood=0.943 vs global=0.025)  
  _[SMARTS: `[#6]=[#6](-[#6](=[#8])-[#7]-[#6])-[#6]`; e.g. sunitinib, omacetaxine mepesuccinate, Ko-143; 1% of drugs]_
7. **fp_0992** (higher; z=4.99, neighborhood=0.943 vs global=0.034)  
  _[SMARTS: `[#16]-[#6](:[#6]:[#6]:[#6]):[#6]`; e.g. MG-132, L-685458, avrainvillamide; 2% of drugs]_
8. **fp_0462** (higher; z=4.70, neighborhood=0.943 vs global=0.039)  
  _[SMARTS: `[#7]-[#6](-[#6])-[#6](:[#6]:[#6]):[#6](:[#6])-[#8]`; e.g. ML311, nutlin-3, CAY10594; 1% of drugs]_

### Nearest Neighbors
| Drug | Cell Line | Tissue | AUC | Kernel Score |
|------|-----------|--------|-----|-------------|
| dinaciclib | MINO | haematopoietic and lymphoid tissue | 0.7869 | 0.8700 |
| dinaciclib | GA10 | haematopoietic and lymphoid tissue | 0.3272 | 0.8500 |
| dinaciclib | SIGM5 | haematopoietic and lymphoid tissue | 1.6543 | 0.8300 |
| dinaciclib | JEKO1 | haematopoietic and lymphoid tissue | 0.9389 | 0.8200 |
| dinaciclib | NUDHL1 | haematopoietic and lymphoid tissue | 2.0722 | 0.8200 |

### Scope and Constraints
- [EV-000006] Interpretation constrained to leaf-agreement neighbors (top_k=200).
- [EV-000006] Statements are grounded in this evidence entry only and do not imply causality.

---
