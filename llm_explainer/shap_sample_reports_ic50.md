# SHAP-Grounded Sample Reports (log10(IC50))

## RPT-0001 - SN-38 on PANC0504
*Evidence: SHAP-0001*

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
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

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

## RPT-0002 - zebularine on MEC1
*Evidence: SHAP-0002*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **zebularine** (master_cpd_id=411739) |
| Gene Target | DNMT1 |
| Mechanism / Activity | inhibitor of DNA methyltransferases |
| Cell Line | **MEC1** (master_ccl_id=663) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | chronic lymphocytic leukaemia; small lymphocytic lymphoma |

### Response Summary
- Observed log10(IC50): **-3.7750**
- RF-predicted log10(IC50): **1.4681**
- Prediction error (observed - predicted): **-5.2430**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (375 pairs): mean=2.1849, q10=1.0384, median=2.5497, q90=3.1175, sample percentile=0.3
- Cell cohort (313 pairs): mean=0.4142, q10=-1.4237, median=0.5479, q90=1.7474, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0876** (fingerprint_bit; SHAP=+0.1201, |SHAP|=0.1201)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.1107, |SHAP|=0.1107)  
  _value=0.2522, z=-1.62; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0535** (fingerprint_bit; SHAP=+0.1085, |SHAP|=0.1085)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
4. **fp_0994** (fingerprint_bit; SHAP=+0.0851, |SHAP|=0.0851)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0582** (fingerprint_bit; SHAP=+0.0783, |SHAP|=0.0783)  
  _absent; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
6. **fp_0518** (fingerprint_bit; SHAP=+0.0738, |SHAP|=0.0738)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
7. **fp_0141** (fingerprint_bit; SHAP=-0.0692, |SHAP|=0.0692)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
8. **fp_0157** (fingerprint_bit; SHAP=+0.0666, |SHAP|=0.0666)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| PSN1 | pancreas | -2.8214907748348432 | more sensitive |
| COLO320 | large intestine | -2.79258502089662 | more sensitive |
| HPAC | pancreas | 3.8832869440653575 | more resistant |
| KALS1 | central nervous system | 3.922420843501675 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.738665431539617 | more sensitive |
| GSK461364 | PLK1 | -3.1047054894487824 | more sensitive |
| MK-0752 | APH1A;NCSTN;PSEN1;PSENEN | 2.5999960725498057 | more resistant |
| BRD-K55116708 |  | 3.103619255295646 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0003 - oligomycin A on GRANTA519
*Evidence: SHAP-0003*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **oligomycin A** (master_cpd_id=411869) |
| Gene Target | ATP5L2 |
| Mechanism / Activity | inhibitor of mitochondrial ATP synthase |
| Cell Line | **GRANTA519** (master_ccl_id=283) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | mantle cell lymphoma |

### Response Summary
- Observed log10(IC50): **3.6485**
- RF-predicted log10(IC50): **-1.0538**
- Prediction error (observed - predicted): **+4.7023**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (418 pairs): mean=-0.6645, q10=-3.4501, median=-0.3418, q90=1.8571, sample percentile=99.5
- Cell cohort (288 pairs): mean=0.3738, q10=-1.7903, median=0.5490, q90=2.0555, sample percentile=99.7
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-1.0804, |SHAP|=1.0804)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0688** (fingerprint_bit; SHAP=-0.3105, |SHAP|=0.3105)  
  _present; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
3. **fp_0673** (fingerprint_bit; SHAP=-0.2234, |SHAP|=0.2234)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.1008, |SHAP|=0.1008)  
  _value=0.6197, z=-1.50; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0141** (fingerprint_bit; SHAP=-0.0878, |SHAP|=0.0878)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **CD79A (973)** (gene_expression; SHAP=+0.0307, |SHAP|=0.0307)  
  _value=9.8629, z=+3.70; markedly above the cross-cell-line mean; recurs in 14 predictable-drug RF signatures_
7. **NQO1 (1728)** (gene_expression; SHAP=-0.0176, |SHAP|=0.0176)  
  _value=2.4788, z=-1.99; below the cross-cell-line mean; recurs in 58 predictable-drug RF signatures_
8. **ANXA2 (302)** (gene_expression; SHAP=-0.0174, |SHAP|=0.0174)  
  _value=6.4457, z=-1.37; below the cross-cell-line mean; recurs in 32 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NALM6 | haematopoietic and lymphoid tissue | -3.995085306094607 | more sensitive |
| C32 | skin | -3.9852933655468 | more sensitive |
| KALS1 | central nervous system | 3.856194244455599 | more resistant |
| COV644 | ovary | 3.8802766441087178 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| NVP-BEZ235 | MTOR;PIK3CA;PIK3CB;PIK3CD;PIK3CG | -3.615060704489269 | more sensitive |
| vincristine |  | -3.479813981055834 | more sensitive |
| RO4929097 | APH1A;NCSTN;PSEN1;PSENEN | 3.639452647577533 | more resistant |
| regorafenib | BRAF;KDR;KIT;RET | 3.826091244889201 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0004 - cerulenin on SNUC2A
*Evidence: SHAP-0004*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **cerulenin** (master_cpd_id=52430) |
| Gene Target | FASN;HMGCS1 |
| Mechanism / Activity | inhibitor of fatty acid synthase; inhibitor of HMG-CoA synthase |
| Cell Line | **SNUC2A** (master_ccl_id=1131) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9657**
- RF-predicted log10(IC50): **1.2466**
- Prediction error (observed - predicted): **-5.2123**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (736 pairs): mean=1.4483, q10=0.8618, median=1.5713, q90=2.0162, sample percentile=0.1
- Cell cohort (198 pairs): mean=0.7010, q10=-1.2917, median=0.9370, q90=2.1852, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.1489, |SHAP|=0.1489)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=-0.1063, |SHAP|=0.1063)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0876** (fingerprint_bit; SHAP=+0.0821, |SHAP|=0.0821)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
4. **fp_0994** (fingerprint_bit; SHAP=+0.0788, |SHAP|=0.0788)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0071** (fingerprint_bit; SHAP=+0.0579, |SHAP|=0.0579)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0575, |SHAP|=0.0575)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0518** (fingerprint_bit; SHAP=+0.0570, |SHAP|=0.0570)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
8. **fp_0157** (fingerprint_bit; SHAP=+0.0547, |SHAP|=0.0547)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| 5637 | urinary tract | -3.846969760068848 | more sensitive |
| NCIH1734 | lung | -3.837980785551416 | more sensitive |
| T98G | central nervous system | 2.7396739905378933 | more resistant |
| TOLEDO | haematopoietic and lymphoid tissue | 2.763756390191011 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| Mdivi-1 | DNM1 | -2.557121586232295 | more sensitive |
| bortezomib | PSMB1;PSMB2;PSMB5;PSMD1;PSMD2 | -2.3611764332299194 | more sensitive |
| BRD-K13999467 |  | 3.877266344152078 | more resistant |
| barasertib | AURKB | 3.934462043328234 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0005 - vincristine on EN
*Evidence: SHAP-0005*

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
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

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

## RPT-0006 - cerulenin on NCIH1734
*Evidence: SHAP-0006*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **cerulenin** (master_cpd_id=52430) |
| Gene Target | FASN;HMGCS1 |
| Mechanism / Activity | inhibitor of fatty acid synthase; inhibitor of HMG-CoA synthase |
| Cell Line | **NCIH1734** (master_ccl_id=155445) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.8380**
- RF-predicted log10(IC50): **1.3462**
- Prediction error (observed - predicted): **-5.1841**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (736 pairs): mean=1.4483, q10=0.8618, median=1.5713, q90=2.0162, sample percentile=0.4
- Cell cohort (220 pairs): mean=0.1405, q10=-1.5979, median=0.3698, q90=1.6714, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.1494, |SHAP|=0.1494)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0141** (fingerprint_bit; SHAP=-0.0897, |SHAP|=0.0897)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0876** (fingerprint_bit; SHAP=+0.0819, |SHAP|=0.0819)  
  _absent; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26_
4. **fp_0994** (fingerprint_bit; SHAP=+0.0785, |SHAP|=0.0785)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
5. **fp_0518** (fingerprint_bit; SHAP=+0.0652, |SHAP|=0.0652)  
  _absent; representative SMARTS `[#6]:[#7]:[#8]`; present in 4.0% of CTRPv2 compounds; example compounds: valdecoxib, neuronal differentiation inducer III, BMS-754807_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0635, |SHAP|=0.0635)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0071** (fingerprint_bit; SHAP=+0.0607, |SHAP|=0.0607)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_
8. **fp_0157** (fingerprint_bit; SHAP=+0.0556, |SHAP|=0.0556)  
  _absent; representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNUC2A | large intestine | -3.965693246914807 | more sensitive |
| 5637 | urinary tract | -3.846969760068848 | more sensitive |
| T98G | central nervous system | 2.7396739905378933 | more resistant |
| TOLEDO | haematopoietic and lymphoid tissue | 2.763756390191011 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| pluripotin | MAPK1;RASAL1 | -2.9667316359800493 | more sensitive |
| paclitaxel |  | -2.887240996875649 | more sensitive |
| BRD-K96970199 |  | 3.031372056336291 | more resistant |
| BRD-A71883111 | IDH1 | 3.458834650179144 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0007 - oligomycin A on MOLP2
*Evidence: SHAP-0007*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **oligomycin A** (master_cpd_id=411869) |
| Gene Target | ATP5L2 |
| Mechanism / Activity | inhibitor of mitochondrial ATP synthase |
| Cell Line | **MOLP2** (master_ccl_id=695) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | plasma cell myeloma |

### Response Summary
- Observed log10(IC50): **3.2270**
- RF-predicted log10(IC50): **-1.0738**
- Prediction error (observed - predicted): **+4.3009**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (418 pairs): mean=-0.6645, q10=-3.4501, median=-0.3418, q90=1.8571, sample percentile=98.3
- Cell cohort (255 pairs): mean=0.6831, q10=-1.2970, median=0.9986, q90=1.9304, sample percentile=100.0
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-1.0808, |SHAP|=1.0808)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0688** (fingerprint_bit; SHAP=-0.3141, |SHAP|=0.3141)  
  _present; representative SMARTS `[#8]-[#6]-[#6]-[#6]-[#7]`; present in 3.1% of CTRPv2 compounds; example compounds: tamoxifen, gefitinib, O-6-benzylguanine_
3. **fp_0673** (fingerprint_bit; SHAP=-0.2108, |SHAP|=0.2108)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.0963, |SHAP|=0.0963)  
  _value=0.5939, z=-1.51; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0141** (fingerprint_bit; SHAP=-0.0895, |SHAP|=0.0895)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
6. **CLU (1191)** (gene_expression; SHAP=+0.0342, |SHAP|=0.0342)  
  _value=0.5236, z=-2.00; below the cross-cell-line mean; recurs in 17 predictable-drug RF signatures_
7. **NQO1 (1728)** (gene_expression; SHAP=-0.0179, |SHAP|=0.0179)  
  _value=2.1598, z=-2.11; markedly below the cross-cell-line mean; recurs in 58 predictable-drug RF signatures_
8. **MYOF (26509)** (gene_expression; SHAP=-0.0175, |SHAP|=0.0175)  
  _value=0.2910, z=-1.67; below the cross-cell-line mean; recurs in 92 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NALM6 | haematopoietic and lymphoid tissue | -3.995085306094607 | more sensitive |
| C32 | skin | -3.9852933655468 | more sensitive |
| KALS1 | central nervous system | 3.856194244455599 | more resistant |
| COV644 | ovary | 3.8802766441087178 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | -3.410217562573685 | more sensitive |
| BI-2536 | PLK1 | -3.0374424273735987 | more sensitive |
| necrostatin-1 | RIPK1 | 3.2059694538214 | more resistant |
| necrostatin-7 |  | 3.20897975377804 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0008 - BRD-K02492147 on KMM1
*Evidence: SHAP-0008*

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
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

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

## RPT-0009 - SNX-2112 on NCIH2291
*Evidence: SHAP-0009*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SNX-2112** (master_cpd_id=362338) |
| Gene Target | HSP90AA1;HSP90B1 |
| Mechanism / Activity | inhibitor of HSP90alpha and HSP90beta |
| Cell Line | **NCIH2291** (master_ccl_id=155511) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **3.7478**
- RF-predicted log10(IC50): **-0.5302**
- Prediction error (observed - predicted): **+4.2781**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (545 pairs): mean=-1.4757, q10=-2.1602, median=-1.4484, q90=-0.9560, sample percentile=100.0
- Cell cohort (124 pairs): mean=0.9657, q10=-0.5801, median=1.1854, q90=2.5387, sample percentile=99.2
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0064** (fingerprint_bit; SHAP=-0.6305, |SHAP|=0.6305)  
  _present; representative SMARTS `[#6]:[#6]:[#6]`; present in 52.8% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, ML006_
2. **fp_0059** (fingerprint_bit; SHAP=-0.4382, |SHAP|=0.4382)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
3. **CCN1 (3491)** (gene_expression; SHAP=+0.1615, |SHAP|=0.1615)  
  _value=7.9883, z=+0.87; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0065** (fingerprint_bit; SHAP=-0.1531, |SHAP|=0.1531)  
  _present; representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: BI-2536, PI-103, BRD1812_
5. **fp_0227** (fingerprint_bit; SHAP=-0.1110, |SHAP|=0.1110)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
6. **S100A6 (6277)** (gene_expression; SHAP=+0.0703, |SHAP|=0.0703)  
  _value=13.9315, z=+1.37; above the cross-cell-line mean; recurs in 33 predictable-drug RF signatures_
7. **fp_0017** (fingerprint_bit; SHAP=-0.0500, |SHAP|=0.0500)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
8. **KRT7 (3855)** (gene_expression; SHAP=+0.0499, |SHAP|=0.0499)  
  _value=12.5119, z=+2.13; markedly above the cross-cell-line mean; recurs in 8 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RCHACV | haematopoietic and lymphoid tissue | -3.8268611950734592 | more sensitive |
| COLO205 | large intestine | -3.780704233392226 | more sensitive |
| NCIH660 | prostate | 1.875416872986603 | more resistant |
| SNU475 | liver | 2.861892168777469 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -3.2267209686217915 | more sensitive |
| triptolide |  | -2.775182103417997 | more sensitive |
| necrostatin-1 | RIPK1 | 3.5100097494420206 | more resistant |
| cytarabine hydrochloride |  | 3.9133899436317554 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0010 - NSC95397 on AM38
*Evidence: SHAP-0010*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **NSC95397** (master_cpd_id=50715) |
| Gene Target | CDC25A;CDC25B;CDC25C |
| Mechanism / Activity | inhibitor of cell division cycle 25 phosphatase (CDC25) |
| Cell Line | **AM38** (master_ccl_id=47) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma Grade IV |

### Response Summary
- Observed log10(IC50): **-3.9927**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0579**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (592 pairs): mean=1.1187, q10=0.3858, median=1.1880, q90=1.7540, sample percentile=0.2
- Cell cohort (89 pairs): mean=-0.6903, q10=-3.0607, median=-0.6840, q90=1.4389, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0896, |SHAP|=0.0896)  
  _value=9.6762, z=+1.42; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0629, |SHAP|=0.0629)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0495, |SHAP|=0.0495)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0190, |SHAP|=0.0190)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0156, |SHAP|=0.0156)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0156, |SHAP|=0.0156)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0153, |SHAP|=0.0153)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0109, |SHAP|=0.0109)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| J82 | urinary tract | -3.895572486670497 | more sensitive |
| HT1080 | soft tissue | -2.502253872228975 | more sensitive |
| NCIH1792 | lung | 3.2631651529975563 | more resistant |
| LOUNH91 | lung | 3.624401147794333 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| NVP-BEZ235 | MTOR;PIK3CA;PIK3CB;PIK3CD;PIK3CG | -3.977343430235752 | more sensitive |
| cytarabine hydrochloride |  | -3.8231593360354506 | more sensitive |
| chlorambucil |  | 2.252818896794222 | more resistant |
| ML031 | S1PR2 | 2.5503261232652488 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0011 - pevonedistat on PATU8988S
*Evidence: SHAP-0011*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **pevonedistat** (master_cpd_id=411809) |
| Gene Target | NAE1 |
| Mechanism / Activity | inhibitor of Nedd-8 activating enzyme |
| Cell Line | **PATU8988S** (master_ccl_id=929) |
| Tissue | pancreas |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **3.9044**
- RF-predicted log10(IC50): **-0.2990**
- Prediction error (observed - predicted): **+4.2033**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (500 pairs): mean=-0.3639, q10=-1.2064, median=-0.3595, q90=0.3661, sample percentile=100.0
- Cell cohort (261 pairs): mean=0.7635, q10=-1.2691, median=0.9829, q90=2.2279, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.5739, |SHAP|=0.5739)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0032** (fingerprint_bit; SHAP=-0.1197, |SHAP|=0.1197)  
  _present; representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206_
3. **fp_0994** (fingerprint_bit; SHAP=-0.1109, |SHAP|=0.1109)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
4. **CCN1 (3491)** (gene_expression; SHAP=-0.1102, |SHAP|=0.1102)  
  _value=2.0839, z=-1.03; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
5. **fp_0582** (fingerprint_bit; SHAP=-0.0896, |SHAP|=0.0896)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
6. **fp_0423** (fingerprint_bit; SHAP=-0.0780, |SHAP|=0.0780)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: chlorambucil, CIL70, axitinib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0504, |SHAP|=0.0504)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0017** (fingerprint_bit; SHAP=+0.0457, |SHAP|=0.0457)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH1869 | lung | -3.7939594310000095 | more sensitive |
| NCIH1693 | lung | -3.5403297855821347 | more sensitive |
| NCIH69 | lung | 3.266175452954196 | more resistant |
| LS1034 | large intestine | 3.395618351089708 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BMS-345541 | IKBKB | -3.4558514991106906 | more sensitive |
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -3.241307461564701 | more sensitive |
| ML320 | GSK3B | 3.473886149962343 | more resistant |
| dabrafenib | BRAF | 3.808029445149362 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0012 - tretinoin on RT112
*Evidence: SHAP-0012*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **tretinoin** (master_cpd_id=23151) |
| Gene Target | RARA;RARB;RARG |
| Mechanism / Activity | agonist of retinoid acid receptors |
| Cell Line | **RT112** (master_ccl_id=997) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.9920**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0573**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (265 pairs): mean=1.7166, q10=0.4007, median=1.9492, q90=2.9104, sample percentile=0.4
- Cell cohort (208 pairs): mean=0.6241, q10=-0.9826, median=0.8296, q90=1.9398, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0903, |SHAP|=0.0903)  
  _value=4.8726, z=-0.13; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0661, |SHAP|=0.0661)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0498, |SHAP|=0.0498)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0191, |SHAP|=0.0191)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0535** (fingerprint_bit; SHAP=+0.0161, |SHAP|=0.0161)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
7. **fp_0059** (fingerprint_bit; SHAP=+0.0154, |SHAP|=0.0154)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0105, |SHAP|=0.0105)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| AM38 | central nervous system | -2.714660645276391 | more sensitive |
| OCIAML3 | haematopoietic and lymphoid tissue | -2.3512168567446707 | more sensitive |
| MKN45 | stomach | 3.9585444429813528 | more resistant |
| HCC1395 | breast | 3.961554742937993 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | -3.6128780338130273 | more sensitive |
| SB-743921 | KIF11 | -2.968059078305081 | more sensitive |
| neratinib | EGFR;ERBB2 | 3.1277016549487646 | more resistant |
| JQ-1 | BRDT | 3.3745462513932294 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0013 - paclitaxel on GB1
*Evidence: SHAP-0013*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **paclitaxel** (master_cpd_id=26956) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **GB1** (master_ccl_id=269) |
| Tissue | central nervous system |
| Histology | glioma |
| Subtype | astrocytoma Grade IV |

### Response Summary
- Observed log10(IC50): **2.6608**
- RF-predicted log10(IC50): **-1.5110**
- Prediction error (observed - predicted): **+4.1718**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (316 pairs): mean=-2.2562, q10=-3.6252, median=-2.8177, q90=1.1135, sample percentile=97.8
- Cell cohort (261 pairs): mean=0.8836, q10=-0.8005, median=1.0169, q90=2.1551, sample percentile=94.6
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-1.2796, |SHAP|=1.2796)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0997** (fingerprint_bit; SHAP=-0.7904, |SHAP|=0.7904)  
  _present; representative SMARTS `[#7]:[#6](:[#6]):[#6]:[#6]:[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: Bax channel blocker, teniposide, methotrexate_
3. **fp_0963** (fingerprint_bit; SHAP=-0.0789, |SHAP|=0.0789)  
  _present; representative SMARTS `[#6]-[#7]-[#7]-[#6]-[#6]`; present in 0.8% of CTRPv2 compounds; example compounds: procarbazine, KU 0060648, vorapaxar_
4. **PTN (5764)** (gene_expression; SHAP=+0.0701, |SHAP|=0.0701)  
  _value=7.7716, z=+2.91; markedly above the cross-cell-line mean; recurs in 2 predictable-drug RF signatures_
5. **CCN1 (3491)** (gene_expression; SHAP=+0.0472, |SHAP|=0.0472)  
  _value=8.5876, z=+1.06; above the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
6. **fp_0994** (fingerprint_bit; SHAP=-0.0375, |SHAP|=0.0375)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_
7. **fp_0654** (fingerprint_bit; SHAP=-0.0353, |SHAP|=0.0353)  
  _present; representative SMARTS `[#7]-[#16](-[#6](:[#6](-[#8]):[#6]):[#6]:[#6])(=[#8])=[#8]`; present in 3.3% of CTRPv2 compounds; example compounds: KU-55933, FQI-1, NSC30930_
8. **fp_0071** (fingerprint_bit; SHAP=+0.0293, |SHAP|=0.0293)  
  _absent; representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HT1080 | soft tissue | -3.99055223825201 | more sensitive |
| PANC1005 | pancreas | -3.985570834111101 | more sensitive |
| CAPAN1 | pancreas | 3.771905845669684 | more resistant |
| HCC1171 | lung | 3.829101544845841 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K97651142 |  | -3.2706629398596765 | more sensitive |
| leptomycin B | XPO1 | -3.04451973094906 | more sensitive |
| SKI-II | SPHK1 | 3.657514447317372 | more resistant |
| pifithrin-alpha |  | 3.961554742937993 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0014 - PD 153035 on EFE184
*Evidence: SHAP-0014*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PD 153035** (master_cpd_id=52133) |
| Gene Target | EGFR |
| Mechanism / Activity | inhibitor of EGFR |
| Cell Line | **EFE184** (master_ccl_id=234) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.9910**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0563**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (367 pairs): mean=1.2230, q10=0.3163, median=1.3489, q90=1.9677, sample percentile=0.3
- Cell cohort (196 pairs): mean=1.0093, q10=-0.5085, median=1.2858, q90=2.0548, sample percentile=0.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=+0.1138, |SHAP|=0.1138)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0906, |SHAP|=0.0906)  
  _value=7.3266, z=+0.66; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0777, |SHAP|=0.0777)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0187, |SHAP|=0.0187)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0284** (fingerprint_bit; SHAP=-0.0163, |SHAP|=0.0163)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 7.7% of CTRPv2 compounds; example compounds: Bax channel blocker, isoliquiritigenin, curcumin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0132, |SHAP|=0.0132)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0994** (fingerprint_bit; SHAP=-0.0109, |SHAP|=0.0109)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| PC14 | lung | -1.8114401946249727 | more sensitive |
| KMS11 | haematopoietic and lymphoid tissue | -1.7734590916104174 | more sensitive |
| REH | haematopoietic and lymphoid tissue | 3.811039745106002 | more resistant |
| RCC10RGB | kidney | 3.859204544412239 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| triptolide |  | -2.595335975830824 | more sensitive |
| SR-II-138A | EIF4A2;EIF4E;EIF4G1 | -2.4780898756449967 | more sensitive |
| necrostatin-1 | RIPK1 | 3.284237252694035 | more resistant |
| erlotinib | EGFR;ERBB2 | 3.314340252260433 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0015 - cucurbitacin I on LS411N
*Evidence: SHAP-0015*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **cucurbitacin I** (master_cpd_id=595102) |
| Gene Target | n/a |
| Mechanism / Activity | natural product; modulator of NFKB1 and STAT3 signaling |
| Cell Line | **LS411N** (master_ccl_id=631) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **3.7057**
- RF-predicted log10(IC50): **-0.4513**
- Prediction error (observed - predicted): **+4.1570**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (715 pairs): mean=-0.9390, q10=-2.0708, median=-1.0937, q90=0.4465, sample percentile=100.0
- Cell cohort (168 pairs): mean=0.7504, q10=-1.0107, median=1.0648, q90=2.0174, sample percentile=98.8
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=-0.7066, |SHAP|=0.7066)  
  _present; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **fp_0673** (fingerprint_bit; SHAP=-0.6346, |SHAP|=0.6346)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
3. **CCN1 (3491)** (gene_expression; SHAP=-0.1030, |SHAP|=0.1030)  
  _value=1.6730, z=-1.16; below the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
4. **fp_0141** (fingerprint_bit; SHAP=-0.0545, |SHAP|=0.0545)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0535** (fingerprint_bit; SHAP=-0.0265, |SHAP|=0.0265)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
6. **fp_0761** (fingerprint_bit; SHAP=+0.0255, |SHAP|=0.0255)  
  _present; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_
7. **NQO1 (1728)** (gene_expression; SHAP=+0.0250, |SHAP|=0.0250)  
  _value=9.2559, z=+0.77; near the cross-cell-line mean; recurs in 58 predictable-drug RF signatures_
8. **GPRC5B (51704)** (gene_expression; SHAP=+0.0236, |SHAP|=0.0236)  
  _value=0.0456, z=-1.22; below the cross-cell-line mean; recurs in 25 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CAOV3 | ovary | -3.919785320228274 | more sensitive |
| SNU201 | central nervous system | -3.833706334742816 | more sensitive |
| FUOV1 | ovary | 1.7242998151632842 | more resistant |
| REC1 | haematopoietic and lymphoid tissue | 2.062356500293935 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SR-II-138A | EIF4A2;EIF4E;EIF4G1 | -3.862962396491048 | more sensitive |
| leptomycin B | XPO1 | -3.66095013373106 | more sensitive |
| CIL55 |  | 3.823080944932561 | more resistant |
| BRD-K09587429 |  | 3.985637142591111 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0016 - SMER-3 on HCC2108
*Evidence: SHAP-0016*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SMER-3** (master_cpd_id=660286) |
| Gene Target | CUL1;SKP1 |
| Mechanism / Activity | inhibitor of E3-ubiquitin ligase |
| Cell Line | **HCC2108** (master_ccl_id=316) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed log10(IC50): **-3.9895**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0548**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (514 pairs): mean=-0.0973, q10=-0.7217, median=-0.0176, q90=0.5923, sample percentile=0.2
- Cell cohort (174 pairs): mean=0.7874, q10=-1.1365, median=1.0384, q90=2.4050, sample percentile=0.6
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0017** (fingerprint_bit; SHAP=+0.1310, |SHAP|=0.1310)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
2. **CCN1 (3491)** (gene_expression; SHAP=+0.0893, |SHAP|=0.0893)  
  _value=7.2242, z=+0.62; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0673** (fingerprint_bit; SHAP=-0.0706, |SHAP|=0.0706)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`; present in 17.5% of CTRPv2 compounds; example compounds: tamoxifen, procarbazine, methotrexate_
4. **fp_0141** (fingerprint_bit; SHAP=+0.0647, |SHAP|=0.0647)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0179, |SHAP|=0.0179)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0179, |SHAP|=0.0179)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0168, |SHAP|=0.0168)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0723** (fingerprint_bit; SHAP=+0.0160, |SHAP|=0.0160)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RL952 | endometrium | -3.81686271254478 | more sensitive |
| MDST8 | large intestine | -3.5701550635854358 | more sensitive |
| A101D | skin | 3.076526555685888 | more resistant |
| JHOC5 | ovary | 3.5160303493553005 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| oligomycin A | ATP5L2 | -3.137538756572957 | more sensitive |
| SB-743921 | KIF11 | -2.979099305038164 | more sensitive |
| BRD-K88742110 | HDAC8 | 3.83813244471576 | more resistant |
| BMS-195614 | RARA;RARB;RARG | 3.9194105435450353 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0017 - navitoclax on MELHO
*Evidence: SHAP-0017*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **navitoclax** (master_cpd_id=362342) |
| Gene Target | BCL2;BCL2L1;BCL2L2 |
| Mechanism / Activity | inhibitor of BCL2, BCL-xL, and BCL-W |
| Cell Line | **MELHO** (master_ccl_id=666) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **3.8803**
- RF-predicted log10(IC50): **-0.0688**
- Prediction error (observed - predicted): **+3.9490**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (333 pairs): mean=-0.0562, q10=-1.5856, median=-0.1511, q90=1.4067, sample percentile=99.7
- Cell cohort (204 pairs): mean=0.5980, q10=-1.2446, median=0.7368, q90=2.0708, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0691** (fingerprint_bit; SHAP=-0.5106, |SHAP|=0.5106)  
  _present; representative SMARTS `[#6]-[#8]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: sirolimus, QW-BI-011, AGK-2_
2. **CCN1 (3491)** (gene_expression; SHAP=-0.2983, |SHAP|=0.2983)  
  _value=2.2872, z=-0.96; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
3. **fp_0059** (fingerprint_bit; SHAP=-0.0980, |SHAP|=0.0980)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
4. **fp_0015** (fingerprint_bit; SHAP=-0.0880, |SHAP|=0.0880)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
5. **fp_0642** (fingerprint_bit; SHAP=-0.0612, |SHAP|=0.0612)  
  _present; representative SMARTS `[#6]=[#6]-[#6](=[#8])-[#8]`; present in 1.2% of CTRPv2 compounds; example compounds: tretinoin, AGK-2, BRD8958_
6. **fp_0497** (fingerprint_bit; SHAP=-0.0419, |SHAP|=0.0419)  
  _present; representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#7]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: cyclophosphamide, topotecan, manumycin A_
7. **fp_0141** (fingerprint_bit; SHAP=-0.0402, |SHAP|=0.0402)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
8. **SPINT2 (10653)** (gene_expression; SHAP=+0.0387, |SHAP|=0.0387)  
  _value=0.6568, z=-1.62; below the cross-cell-line mean; recurs in 8 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HUG1N | stomach | -3.986382142714768 | more sensitive |
| NCIH1975 | lung | -3.798084348397786 | more sensitive |
| T47D | breast | 3.84716334458568 | more resistant |
| BICR31 | upper aerodigestive tract | 3.943492943198154 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -2.6167243817989654 | more sensitive |
| NVP-TAE684 | ALK | -2.5019315711958896 | more sensitive |
| Ch-55 | RARA;RARB;RARG | 3.696648346753689 | more resistant |
| bleomycin A2 |  | 3.808029445149362 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0018 - Mdivi-1 on JHOS2
*Evidence: SHAP-0018*

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
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

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

## RPT-0019 - paclitaxel on HCC1171
*Evidence: SHAP-0019*

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
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

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

## RPT-0020 - KX2-391 on HUG1N
*Evidence: SHAP-0020*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KX2-391** (master_cpd_id=660779) |
| Gene Target | SRC |
| Mechanism / Activity | peptide mimetic; inhibitor of SRC activity in cells |
| Cell Line | **HUG1N** (master_ccl_id=456) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **-3.9788**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0440**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (495 pairs): mean=-1.3463, q10=-2.5250, median=-1.6261, q90=1.1914, sample percentile=0.4
- Cell cohort (244 pairs): mean=0.6023, q10=-1.2481, median=0.8768, q90=1.9781, sample percentile=0.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.1345, |SHAP|=0.1345)  
  _value=2.9464, z=-0.75; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0474, |SHAP|=0.0474)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0423, |SHAP|=0.0423)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0015** (fingerprint_bit; SHAP=-0.0212, |SHAP|=0.0212)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#6]`; present in 18.9% of CTRPv2 compounds; example compounds: doxorubicin, pyrazolanthrone, PD 153035_
5. **fp_0513** (fingerprint_bit; SHAP=+0.0210, |SHAP|=0.0210)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
6. **fp_0792** (fingerprint_bit; SHAP=+0.0186, |SHAP|=0.0186)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 23.3% of CTRPv2 compounds; example compounds: parbendazole, niclosamide, ouabain_
7. **fp_0723** (fingerprint_bit; SHAP=+0.0173, |SHAP|=0.0173)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
8. **fp_0059** (fingerprint_bit; SHAP=+0.0159, |SHAP|=0.0159)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH661 | lung | -3.9889711910219177 | more sensitive |
| TE9 | oesophagus | -3.9535145796322175 | more sensitive |
| 8MGBA | central nervous system | 3.762874945799765 | more resistant |
| CAS1 | central nervous system | 3.780936745539604 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| navitoclax | BCL2;BCL2L1;BCL2L2 | -3.986382142714768 | more sensitive |
| paclitaxel |  | -3.364609319711318 | more sensitive |
| bleomycin A2 |  | 2.8308860792240798 | more resistant |
| ML203 | PKM | 2.8880817784002355 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0021 - vincristine on SNU46
*Evidence: SHAP-0021*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **vincristine** (master_cpd_id=62602) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of mictrotubule assembly |
| Cell Line | **SNU46** (master_ccl_id=1106) |
| Tissue | upper aerodigestive tract |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **3.2872**
- RF-predicted log10(IC50): **-0.6018**
- Prediction error (observed - predicted): **+3.8891**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (589 pairs): mean=-1.3333, q10=-2.9338, median=-1.6033, q90=1.3216, sample percentile=99.7
- Cell cohort (157 pairs): mean=0.9577, q10=-0.8817, median=1.1364, q90=2.4121, sample percentile=96.2
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-1.0175, |SHAP|=1.0175)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.4042, |SHAP|=0.4042)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0767** (fingerprint_bit; SHAP=+0.1434, |SHAP|=0.1434)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **fp_0204** (fingerprint_bit; SHAP=-0.1104, |SHAP|=0.1104)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
5. **fp_0974** (fingerprint_bit; SHAP=-0.0661, |SHAP|=0.0661)  
  _present; representative SMARTS `[#7]-[#6]-[#6]-[#6]-[#6]`; present in 7.5% of CTRPv2 compounds; example compounds: parbendazole, importazole, tacrolimus_
6. **fp_0582** (fingerprint_bit; SHAP=-0.0651, |SHAP|=0.0651)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
7. **fp_0761** (fingerprint_bit; SHAP=-0.0485, |SHAP|=0.0485)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_
8. **fp_0654** (fingerprint_bit; SHAP=-0.0454, |SHAP|=0.0454)  
  _present; representative SMARTS `[#7]-[#16](-[#6](:[#6](-[#8]):[#6]):[#6]:[#6])(=[#8])=[#8]`; present in 3.3% of CTRPv2 compounds; example compounds: KU-55933, FQI-1, NSC30930_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HCC1954 | breast | -3.9905585726829234 | more sensitive |
| DB | haematopoietic and lymphoid tissue | -3.987471614892891 | more sensitive |
| PATU8902 | pancreas | 3.413680150829547 | more resistant |
| EN | endometrium | 3.52205094926858 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BRD-K71935468 |  | -3.976198733688067 | more sensitive |
| leptomycin B | XPO1 | -2.864008354342205 | more sensitive |
| selumetinib | MAP2K1;MAP2K2 | 3.618380547881054 | more resistant |
| 3-Cl-AHPC | NR0B2 | 3.759864645843125 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0022 - linsitinib on ZR7530
*Evidence: SHAP-0022*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **linsitinib** (master_cpd_id=705300) |
| Gene Target | IGF1R;INSR |
| Mechanism / Activity | inhibitor of insulin-like growth factor 1 receptor and insulin receptor |
| Cell Line | **ZR7530** (master_ccl_id=1286) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed log10(IC50): **-3.9686**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0339**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (459 pairs): mean=1.1411, q10=0.0649, median=1.3284, q90=1.8589, sample percentile=0.2
- Cell cohort (224 pairs): mean=1.0273, q10=-0.8872, median=1.3122, q90=2.3833, sample percentile=0.4
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0924, |SHAP|=0.0924)  
  _value=6.3270, z=+0.34; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0141** (fingerprint_bit; SHAP=+0.0847, |SHAP|=0.0847)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
3. **fp_0017** (fingerprint_bit; SHAP=+0.0498, |SHAP|=0.0498)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
4. **fp_0513** (fingerprint_bit; SHAP=+0.0195, |SHAP|=0.0195)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
5. **fp_0059** (fingerprint_bit; SHAP=+0.0175, |SHAP|=0.0175)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
6. **fp_0723** (fingerprint_bit; SHAP=+0.0172, |SHAP|=0.0172)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
7. **fp_0535** (fingerprint_bit; SHAP=+0.0128, |SHAP|=0.0128)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
8. **fp_0777** (fingerprint_bit; SHAP=+0.0099, |SHAP|=0.0099)  
  _absent; representative SMARTS `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: NSC95397, Mdivi-1, cyanoquinoline 11_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| YD15 | salivary gland | -3.400713419386802 | more sensitive |
| HDMYZ | haematopoietic and lymphoid tissue | -2.103914329948007 | more sensitive |
| PANC0403 | pancreas | 3.302299052433874 | more resistant |
| HEC6 | endometrium | 3.534092149095139 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| RAF265 | BRAF;KDR | -3.631771526985402 | more sensitive |
| ibrutinib | BTK | -2.453427409829219 | more sensitive |
| zebularine | DNMT1 | 3.4317419505693856 | more resistant |
| COL-3 |  | 3.437762550482665 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0023 - GMX-1778 on KYSE140
*Evidence: SHAP-0023*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GMX-1778** (master_cpd_id=411843) |
| Gene Target | NAMPT |
| Mechanism / Activity | inhibitor of nicotinamide phosphoribosyltransferase |
| Cell Line | **KYSE140** (master_ccl_id=580) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **2.6430**
- RF-predicted log10(IC50): **-1.1579**
- Prediction error (observed - predicted): **+3.8009**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (547 pairs): mean=-1.8215, q10=-2.7235, median=-1.8837, q90=-1.1413, sample percentile=99.1
- Cell cohort (232 pairs): mean=1.0695, q10=-0.8045, median=1.2206, q90=2.5472, sample percentile=92.2
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0691** (fingerprint_bit; SHAP=-0.6908, |SHAP|=0.6908)  
  _present; representative SMARTS `[#6]-[#8]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: sirolimus, QW-BI-011, AGK-2_
2. **fp_0925** (fingerprint_bit; SHAP=-0.5944, |SHAP|=0.5944)  
  _present; representative SMARTS `[#6]:[#6](:[#6](-[#6]):[#6]:[#6])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: gossypol, isoliquiritigenin, mitomycin_
3. **fp_0769** (fingerprint_bit; SHAP=-0.5281, |SHAP|=0.5281)  
  _present; representative SMARTS `[#7](-[#6@H])(-[#6])-[#6](-[#6](:[#6]):[#6])=[#8]`; present in 4.4% of CTRPv2 compounds; example compounds: BRD-K27224038, Compound 1541A, BRD-K48334597_
4. **fp_0017** (fingerprint_bit; SHAP=-0.0970, |SHAP|=0.0970)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
5. **APOBEC3B (9582)** (gene_expression; SHAP=+0.0695, |SHAP|=0.0695)  
  _value=0.0470, z=-1.98; below the cross-cell-line mean; recurs in 11 predictable-drug RF signatures_
6. **fp_0141** (fingerprint_bit; SHAP=-0.0671, |SHAP|=0.0671)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
7. **CCN1 (3491)** (gene_expression; SHAP=+0.0645, |SHAP|=0.0645)  
  _value=6.5030, z=+0.39; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
8. **SLC7A8 (23428)** (gene_expression; SHAP=+0.0504, |SHAP|=0.0504)  
  _value=7.8923, z=+3.09; markedly above the cross-cell-line mean; recurs in 12 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SKNDZ | autonomic ganglia | -3.672954881363247 | more sensitive |
| DAUDI | haematopoietic and lymphoid tissue | -3.626515466331264 | more sensitive |
| NCIH2052 | pleura | 3.410669850872907 | more resistant |
| DLD1 | large intestine | 3.777926445582964 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | -2.935854993960265 | more sensitive |
| CR-1-31B | EIF4A2;EIF4E;EIF4G1 | -1.92038767742768 | more sensitive |
| SKI-II | SPHK1 | 3.922420843501675 | more resistant |
| BRD-K34485477 |  | 3.9404826432415136 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0024 - MLN2480 on OE21
*Evidence: SHAP-0024*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **MLN2480** (master_cpd_id=687579) |
| Gene Target | ARAF;BRAF;RAF1 |
| Mechanism / Activity | inhibitor of RAF kinases |
| Cell Line | **OE21** (master_ccl_id=895) |
| Tissue | oesophagus |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed log10(IC50): **-3.9663**
- RF-predicted log10(IC50): **1.0653**
- Prediction error (observed - predicted): **-5.0315**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (198 pairs): mean=1.6824, q10=0.7072, median=1.7517, q90=2.4650, sample percentile=0.5
- Cell cohort (289 pairs): mean=0.5505, q10=-1.3788, median=0.6558, q90=2.0115, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **CCN1 (3491)** (gene_expression; SHAP=+0.0867, |SHAP|=0.0867)  
  _value=4.1637, z=-0.36; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
2. **fp_0017** (fingerprint_bit; SHAP=+0.0694, |SHAP|=0.0694)  
  _absent; representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: bexarotene, SR-II-138A, CR-1-31B_
3. **fp_0141** (fingerprint_bit; SHAP=+0.0545, |SHAP|=0.0545)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
4. **fp_0059** (fingerprint_bit; SHAP=+0.0387, |SHAP|=0.0387)  
  _absent; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_
5. **fp_0723** (fingerprint_bit; SHAP=+0.0178, |SHAP|=0.0178)  
  _absent; representative SMARTS `[#6]:[#6](:[#6])-[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: gossypol, teniposide, valdecoxib_
6. **fp_0513** (fingerprint_bit; SHAP=+0.0175, |SHAP|=0.0175)  
  _absent; representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`; present in 0.8% of CTRPv2 compounds; example compounds: epigallocatechin-3-monogallate, CAY10594, avrainvillamide_
7. **fp_0284** (fingerprint_bit; SHAP=-0.0167, |SHAP|=0.0167)  
  _present; representative SMARTS `[#6]-[#7]-[#6]`; present in 7.7% of CTRPv2 compounds; example compounds: Bax channel blocker, isoliquiritigenin, curcumin_
8. **fp_0535** (fingerprint_bit; SHAP=+0.0157, |SHAP|=0.0157)  
  _absent; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | -2.6768138399941277 | more sensitive |
| OVCAR5 |  | -0.8517378155921729 | more sensitive |
| HCC4006 | lung | 3.6364423476208927 | more resistant |
| NCIH2029 | lung | 3.6725659471005705 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SID 26681509 | CTSL1 | -3.532396502031166 | more sensitive |
| erlotinib | EGFR;ERBB2 | -2.996818123034092 | more sensitive |
| olaparib | PARP1;PARP2 | 3.473886149962343 | more resistant |
| navitoclax | BCL2;BCL2L1;BCL2L2 | 3.7869573454528833 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0025 - docetaxel on K029AX
*Evidence: SHAP-0025*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **docetaxel** (master_cpd_id=660364) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **K029AX** (master_ccl_id=512) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed log10(IC50): **3.8803**
- RF-predicted log10(IC50): **0.0950**
- Prediction error (observed - predicted): **+3.7853**
- Global mean log10(IC50) across all pairs: **0.6392**
- Drug cohort (232 pairs): mean=-1.5609, q10=-3.4473, median=-2.4625, q90=1.6247, sample percentile=99.6
- Cell cohort (178 pairs): mean=0.7570, q10=-1.2718, median=1.1091, q90=2.3076, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0141** (fingerprint_bit; SHAP=-0.8692, |SHAP|=0.8692)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
2. **fp_0535** (fingerprint_bit; SHAP=-0.4386, |SHAP|=0.4386)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: BRD4132, BRD6340, parbendazole_
3. **fp_0767** (fingerprint_bit; SHAP=+0.1666, |SHAP|=0.1666)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **fp_0204** (fingerprint_bit; SHAP=-0.0864, |SHAP|=0.0864)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
5. **PHLDA3 (23612)** (gene_expression; SHAP=+0.0514, |SHAP|=0.0514)  
  _value=6.5855, z=+1.22; above the cross-cell-line mean; recurs in 23 predictable-drug RF signatures_
6. **CCN1 (3491)** (gene_expression; SHAP=+0.0458, |SHAP|=0.0458)  
  _value=3.8624, z=-0.46; near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures_
7. **fp_0582** (fingerprint_bit; SHAP=-0.0427, |SHAP|=0.0427)  
  _present; representative SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: tacrolimus, BRD-K90370028, SR-II-138A_
8. **fp_0761** (fingerprint_bit; SHAP=-0.0355, |SHAP|=0.0355)  
  _absent; representative SMARTS `[#6]-[#6@@H](-[#6@H])-[#6]`; present in 1.0% of CTRPv2 compounds; example compounds: ciclosporin, apicidin, BRD-K88742110_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| HS683 | central nervous system | -3.990623517601181 | more sensitive |
| PECAPJ49 | upper aerodigestive tract | -3.9768469903133754 | more sensitive |
| BL41 | haematopoietic and lymphoid tissue | 3.52205094926858 | more resistant |
| CAKI1 | kidney | 3.8832869440653575 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| BI-2536 | PLK1 | -3.2559052238170327 | more sensitive |
| leptomycin B | XPO1 | -2.5132490446822384 | more sensitive |
| SKI-II | SPHK1 | 3.4979685496154613 | more resistant |
| MK-0752 | APH1A;NCSTN;PSEN1;PSENEN | 3.877266344152078 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---
