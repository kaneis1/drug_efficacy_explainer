# SHAP-Grounded Sample Reports

## RPT-0001 - cytarabine hydrochloride on SKMEL2
*Evidence: SHAP-0001*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **cytarabine hydrochloride** (master_cpd_id=62690) |
| Gene Target | n/a |
| Mechanism / Activity | inducer of DNA damage |
| Cell Line | **SKMEL2** (master_ccl_id=1041) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **27.1820**
- RF-predicted AUC: **13.5949**
- Prediction error (observed - predicted): **+13.5871**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (786 pairs): mean=11.6275, q10=6.8893, median=12.4295, q90=14.5745, sample percentile=100.0
- Cell cohort (375 pairs): mean=14.2236, q10=11.7612, median=14.4630, q90=16.0996, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=-0.7098, |SHAP|=0.7098)  
  _present; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **fp_0504** (fingerprint_bit; SHAP=+0.3425, |SHAP|=0.3425)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
3. **fp_0767** (fingerprint_bit; SHAP=+0.2681, |SHAP|=0.2681)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
4. **fp_0450** (fingerprint_bit; SHAP=-0.1741, |SHAP|=0.1741)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]`; present in 0.8% of CTRPv2 compounds; example compounds: Repligen 136, BRD-K29313308, COL-3_
5. **fp_0864** (fingerprint_bit; SHAP=+0.1686, |SHAP|=0.1686)  
  _absent; representative SMARTS `[#7]=[#6]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: mitomycin, omacetaxine mepesuccinate, PAC-1_
6. **fp_1009** (fingerprint_bit; SHAP=+0.1228, |SHAP|=0.1228)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
7. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1132, |SHAP|=0.1132)  
  _value=7.8670, z=+0.64; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
8. **fp_0925** (fingerprint_bit; SHAP=+0.1036, |SHAP|=0.1036)  
  _absent; representative SMARTS `[#6]:[#6](:[#6](-[#6]):[#6]:[#6])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: gossypol, isoliquiritigenin, mitomycin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| BV173 | haematopoietic and lymphoid tissue | 0.3812 | more sensitive |
| REH | haematopoietic and lymphoid tissue | 0.3967 | more sensitive |
| HS688AT | skin | 18.548 | more resistant |
| RERFLCAD1 | lung | 19.187 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 2.1139 | more sensitive |
| LBH-589 | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 | 5.3553 | more sensitive |
| KU-0063794 | MTOR | 21.232 | more resistant |
| alisertib | AURKA;AURKB | 21.265 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0002 - birinapant on KYM1
*Evidence: SHAP-0002*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **birinapant** (master_cpd_id=660778) |
| Gene Target | DIABLO;XIAP |
| Mechanism / Activity | SMAC mimetic; inhibitor of inhibitor of apoptosis proteins (IAPs) |
| Cell Line | **KYM1** (master_ccl_id=578) |
| Tissue | soft tissue |
| Histology | rhabdomyosarcoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **0.6877**
- RF-predicted AUC: **13.8762**
- Prediction error (observed - predicted): **-13.1885**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (785 pairs): mean=13.9678, q10=10.8908, median=14.5760, q90=16.1450, sample percentile=0.1
- Cell cohort (409 pairs): mean=12.2157, q10=8.6169, median=12.7840, q90=14.7692, sample percentile=0.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=-0.5166, |SHAP|=0.5166)  
  _present; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **fp_0767** (fingerprint_bit; SHAP=+0.3164, |SHAP|=0.3164)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 11.0% of CTRPv2 compounds; example compounds: Bax channel blocker, trifluoperazine, parbendazole_
3. **fp_0504** (fingerprint_bit; SHAP=+0.2344, |SHAP|=0.2344)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
4. **fp_0864** (fingerprint_bit; SHAP=+0.2089, |SHAP|=0.2089)  
  _absent; representative SMARTS `[#7]=[#6]-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: mitomycin, omacetaxine mepesuccinate, PAC-1_
5. **fp_1009** (fingerprint_bit; SHAP=+0.1965, |SHAP|=0.1965)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
6. **fp_0925** (fingerprint_bit; SHAP=+0.1182, |SHAP|=0.1182)  
  _absent; representative SMARTS `[#6]:[#6](:[#6](-[#6]):[#6]:[#6])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: gossypol, isoliquiritigenin, mitomycin_
7. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1082, |SHAP|=0.1082)  
  _value=7.4180, z=+0.46; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
8. **fp_1001** (fingerprint_bit; SHAP=+0.0814, |SHAP|=0.0814)  
  _present; representative SMARTS `[#6]-[#6](-[#7])(-[#6])-[#6]`; present in 1.9% of CTRPv2 compounds; example compounds: nutlin-3, austocystin D, HLI 373_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| WSUDLCL2 | haematopoietic and lymphoid tissue | 0.9335 | more sensitive |
| ESS1 | endometrium | 3.5244 | more sensitive |
| BL70 | haematopoietic and lymphoid tissue | 18.364 | more resistant |
| NAMALWA | haematopoietic and lymphoid tissue | 18.381 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 0.9267 | more sensitive |
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | 1.85 | more sensitive |
| compound 1B |  | 18.39 | more resistant |
| ML320 | GSK3B | 20.237 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0003 - nilotinib on BT549
*Evidence: SHAP-0003*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **nilotinib** (master_cpd_id=374749) |
| Gene Target | ABL1;BCR;KIT |
| Mechanism / Activity | inhibitor of ABL1, BCR, and c-KIT |
| Cell Line | **BT549** (master_ccl_id=99) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed AUC: **23.7050**
- RF-predicted AUC: **13.4663**
- Prediction error (observed - predicted): **+10.2387**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (773 pairs): mean=13.9591, q10=12.0654, median=14.4330, q90=15.6900, sample percentile=100.0
- Cell cohort (403 pairs): mean=13.3170, q10=10.3396, median=13.8010, q90=15.3618, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2006, |SHAP|=0.2006)  
  _value=7.7769, z=+0.60; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0367** (fingerprint_bit; SHAP=-0.1002, |SHAP|=0.1002)  
  _present; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
3. **fp_0443** (fingerprint_bit; SHAP=+0.0993, |SHAP|=0.0993)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
4. **fp_0204** (fingerprint_bit; SHAP=+0.0815, |SHAP|=0.0815)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
5. **fp_0538** (fingerprint_bit; SHAP=-0.0727, |SHAP|=0.0727)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_
6. **fp_0811** (fingerprint_bit; SHAP=+0.0573, |SHAP|=0.0573)  
  _present; representative SMARTS `[#16]-[#6](:[#6]):[#6]`; present in 2.1% of CTRPv2 compounds; example compounds: VX-680, axitinib, navitoclax_
7. **fp_0504** (fingerprint_bit; SHAP=+0.0367, |SHAP|=0.0367)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
8. **fp_0994** (fingerprint_bit; SHAP=+0.0350, |SHAP|=0.0350)  
  _absent; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | 0.1918 | more sensitive |
| KYO1 | haematopoietic and lymphoid tissue | 0.7071 | more sensitive |
| SNU475 | liver | 18.744 | more resistant |
| SNU245 | biliary tract | 18.795 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 2.9978 | more sensitive |
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | 4.6538 | more sensitive |
| sildenafil | PDE5A | 18.476 | more resistant |
| daporinad | NAMPT | 18.637 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0004 - N9-isopropylolomoucine on CADOES1
*Evidence: SHAP-0004*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **N9-isopropylolomoucine** (master_cpd_id=45093) |
| Gene Target | CCNB1;CDK1;CDK5;CDK5R1 |
| Mechanism / Activity | inhibitor of CDK1/cyclin B and CDK5/p35 complexes |
| Cell Line | **CADOES1** (master_ccl_id=108) |
| Tissue | bone |
| Histology | Ewings sarcoma peripheral primitive neuroectodermal tumor |
| Subtype | n/a |

### Response Summary
- Observed AUC: **0.0835**
- RF-predicted AUC: **12.5703**
- Prediction error (observed - predicted): **-12.4868**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (755 pairs): mean=12.9659, q10=11.8228, median=13.0280, q90=14.0808, sample percentile=0.1
- Cell cohort (53 pairs): mean=11.3701, q10=5.9144, median=12.2070, q90=16.6946, sample percentile=1.9
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.6577, |SHAP|=0.6577)  
  _value=1.6410, z=-1.83; below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0227** (fingerprint_bit; SHAP=+0.0985, |SHAP|=0.0985)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
3. **fp_0204** (fingerprint_bit; SHAP=+0.0901, |SHAP|=0.0901)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
4. **fp_0062** (fingerprint_bit; SHAP=-0.0887, |SHAP|=0.0887)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
5. **fp_0538** (fingerprint_bit; SHAP=-0.0829, |SHAP|=0.0829)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: NSC19630, crizotinib, NVP-BSK805_
6. **fp_0504** (fingerprint_bit; SHAP=+0.0438, |SHAP|=0.0438)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
7. **SDC4 (6385)** (gene_expression; SHAP=-0.0418, |SHAP|=0.0418)  
  _value=2.5523, z=-1.19; below the cross-cell-line mean; recurs in 154 predictable-drug RF signatures_
8. **fp_0443** (fingerprint_bit; SHAP=+0.0367, |SHAP|=0.0367)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CAL78 | bone | 9.7426 | more sensitive |
| SNU1079 | biliary tract | 10.342 | more sensitive |
| BEN | lung | 16.05 | more resistant |
| NCIH1184 | lung | 16.815 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 1.1661 | more sensitive |
| topotecan | TOP1 | 4.0491 | more sensitive |
| birinapant | DIABLO;XIAP | 17.126 | more resistant |
| GSK4112 | NR1D1 | 17.213 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0005 - GSK461364 on MC116
*Evidence: SHAP-0005*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GSK461364** (master_cpd_id=649862) |
| Gene Target | PLK1 |
| Mechanism / Activity | inhibitor of polo-like kinase 1 (PLK1) |
| Cell Line | **MC116** (master_ccl_id=643) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | B cell lymphoma |

### Response Summary
- Observed AUC: **17.4070**
- RF-predicted AUC: **7.3230**
- Prediction error (observed - predicted): **+10.0840**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (770 pairs): mean=7.3729, q10=2.7793, median=7.1394, q90=12.0872, sample percentile=100.0
- Cell cohort (395 pairs): mean=13.0759, q10=9.8849, median=13.8270, q90=15.4484, sample percentile=100.0
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0504** (fingerprint_bit; SHAP=-2.5354, |SHAP|=2.5354)  
  _present; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
2. **fp_0443** (fingerprint_bit; SHAP=-2.5230, |SHAP|=2.5230)  
  _present; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
3. **fp_1001** (fingerprint_bit; SHAP=-0.4914, |SHAP|=0.4914)  
  _absent; representative SMARTS `[#6]-[#6](-[#7])(-[#6])-[#6]`; present in 1.9% of CTRPv2 compounds; example compounds: nutlin-3, austocystin D, HLI 373_
4. **fp_0738** (fingerprint_bit; SHAP=-0.3354, |SHAP|=0.3354)  
  _absent; representative SMARTS `[#6]:[#6]:[#6](:[#6](:[#6])-[#8])-[#8]-[#6]`; present in 4.6% of CTRPv2 compounds; example compounds: teniposide, etoposide, SB-431542_
5. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.2506, |SHAP|=0.2506)  
  _value=1.5683, z=-1.85; below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
6. **SYTL2 (54843)** (gene_expression; SHAP=+0.1654, |SHAP|=0.1654)  
  _value=3.5290, z=+0.12; near the cross-cell-line mean; recurs in 84 predictable-drug RF signatures_
7. **MYLK (4638)** (gene_expression; SHAP=+0.1620, |SHAP|=0.1620)  
  _value=0.2243, z=-1.25; below the cross-cell-line mean; recurs in 46 predictable-drug RF signatures_
8. **fp_0059** (fingerprint_bit; SHAP=-0.0916, |SHAP|=0.0916)  
  _present; representative SMARTS `[#6]=[#6]-[#6@H]`; present in 6.0% of CTRPv2 compounds; example compounds: CIL55, simvastatin, lovastatin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NB4 | haematopoietic and lymphoid tissue | 0.2916 | more sensitive |
| SKM1 | haematopoietic and lymphoid tissue | 0.5588 | more sensitive |
| KARPAS620 | haematopoietic and lymphoid tissue | 14.517 | more resistant |
| ZR751 | breast | 14.567 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 1.5993 | more sensitive |
| SB-743921 | KIF11 | 1.9029 | more sensitive |
| Ch-55 | RARA;RARB;RARG | 17.092 | more resistant |
| BRD9876 |  | 17.306 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0006 - niclosamide on IALM
*Evidence: SHAP-0006*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **niclosamide** (master_cpd_id=32653) |
| Gene Target | STAT3 |
| Mechanism / Activity | inhibitor of STAT3 signaling |
| Cell Line | **IALM** (master_ccl_id=469) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | large cell carcinoma |

### Response Summary
- Observed AUC: **0.9043**
- RF-predicted AUC: **13.3307**
- Prediction error (observed - predicted): **-12.4264**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (782 pairs): mean=11.8062, q10=10.0244, median=11.7355, q90=13.7238, sample percentile=0.1
- Cell cohort (340 pairs): mean=13.8401, q10=11.3316, median=14.2360, q90=15.8798, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2028, |SHAP|=0.2028)  
  _value=7.6074, z=+0.54; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0623** (fingerprint_bit; SHAP=-0.1794, |SHAP|=0.1794)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
3. **fp_0771** (fingerprint_bit; SHAP=-0.1178, |SHAP|=0.1178)  
  _present; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
4. **fp_0443** (fingerprint_bit; SHAP=+0.1124, |SHAP|=0.1124)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0885, |SHAP|=0.0885)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0551, |SHAP|=0.0551)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0367** (fingerprint_bit; SHAP=+0.0400, |SHAP|=0.0400)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
8. **fp_0227** (fingerprint_bit; SHAP=+0.0370, |SHAP|=0.0370)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNU398 | liver | 2.741 | more sensitive |
| MINO | haematopoietic and lymphoid tissue | 5.572 | more sensitive |
| SNU308 | biliary tract | 16.805 | more resistant |
| MKN45 | stomach | 16.973 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| 1S,3R-RSL-3 | GPX4 | 3.8443 | more sensitive |
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | 3.8458 | more sensitive |
| procarbazine |  | 18.598 | more resistant |
| GDC-0879 | BRAF | 19.124 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0007 - pitstop2 on SNU886
*Evidence: SHAP-0007*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **pitstop2** (master_cpd_id=660985) |
| Gene Target | CLTA;CLTB;CLTC;CLTCL1 |
| Mechanism / Activity | inhibitor of clathrin and clathrin-independent endocytosis |
| Cell Line | **SNU886** (master_ccl_id=1128) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed AUC: **23.1410**
- RF-predicted AUC: **13.6419**
- Prediction error (observed - predicted): **+9.4991**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (542 pairs): mean=14.8376, q10=13.8893, median=14.8015, q90=16.0306, sample percentile=100.0
- Cell cohort (316 pairs): mean=12.7377, q10=9.1165, median=12.9715, q90=15.5240, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2107, |SHAP|=0.2107)  
  _value=7.8593, z=+0.64; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0204** (fingerprint_bit; SHAP=+0.0847, |SHAP|=0.0847)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
3. **fp_0443** (fingerprint_bit; SHAP=+0.0738, |SHAP|=0.0738)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
4. **fp_0367** (fingerprint_bit; SHAP=+0.0646, |SHAP|=0.0646)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
5. **fp_0062** (fingerprint_bit; SHAP=-0.0584, |SHAP|=0.0584)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
6. **fp_0227** (fingerprint_bit; SHAP=+0.0374, |SHAP|=0.0374)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
7. **fp_0504** (fingerprint_bit; SHAP=+0.0345, |SHAP|=0.0345)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
8. **fp_0142** (fingerprint_bit; SHAP=+0.0284, |SHAP|=0.0284)  
  _absent; representative SMARTS `[#6]-[#6](:[#6](-[#7]-[#6]):[#6]:[#6]):[#6]`; present in 1.5% of CTRPv2 compounds; example compounds: GSK-3 inhibitor IX, sunitinib, SU11274_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SKMM2 | haematopoietic and lymphoid tissue | 9.786 | more sensitive |
| PFEIFFER | haematopoietic and lymphoid tissue | 10.176 | more sensitive |
| DKMG | central nervous system | 18.053 | more resistant |
| PK45H | pancreas | 18.267 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 2.305 | more sensitive |
| navitoclax | BCL2;BCL2L1;BCL2L2 | 2.6415 | more sensitive |
| I-BET151 | BRD2;BRD3;BRD4 | 20.533 | more resistant |
| KH-CB19 | CLK1;CLK4 | 20.918 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0008 - trametinib on DU4475
*Evidence: SHAP-0008*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **trametinib** (master_cpd_id=687418) |
| Gene Target | MAP2K1;MAP2K2 |
| Mechanism / Activity | inhibitor of MEK1 and MEK2 |
| Cell Line | **DU4475** (master_ccl_id=226) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed AUC: **0.1282**
- RF-predicted AUC: **12.4028**
- Prediction error (observed - predicted): **-12.2746**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (391 pairs): mean=10.4971, q10=5.7207, median=11.1740, q90=13.9710, sample percentile=0.3
- Cell cohort (363 pairs): mean=11.2338, q10=5.5261, median=11.7180, q90=14.7064, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0367** (fingerprint_bit; SHAP=-0.2979, |SHAP|=0.2979)  
  _present; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.1562, |SHAP|=0.1562)  
  _value=4.5098, z=-0.69; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_0204** (fingerprint_bit; SHAP=+0.1206, |SHAP|=0.1206)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
4. **fp_0409** (fingerprint_bit; SHAP=-0.0868, |SHAP|=0.0868)  
  _present; representative SMARTS `[#7]-[#6](:[#7]):[#7]`; present in 3.3% of CTRPv2 compounds; example compounds: azacitidine, methotrexate, apicidin_
5. **fp_0062** (fingerprint_bit; SHAP=-0.0866, |SHAP|=0.0866)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
6. **fp_1008** (fingerprint_bit; SHAP=-0.0863, |SHAP|=0.0863)  
  _present; representative SMARTS `[#7]-[#6](:[#7]:[#6]):[#7]:[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: fluorouracil, azacitidine, ouabain_
7. **fp_0227** (fingerprint_bit; SHAP=+0.0500, |SHAP|=0.0500)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
8. **fp_0728** (fingerprint_bit; SHAP=-0.0385, |SHAP|=0.0385)  
  _present; representative SMARTS `Br`; present in 5.2% of CTRPv2 compounds; example compounds: Bax channel blocker, manumycin A, SB-225002_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| OCIAML3 | haematopoietic and lymphoid tissue | 0.3553 | more sensitive |
| WM88 | skin | 1.4912 | more sensitive |
| ZR7530 | breast | 17.172 | more resistant |
| JHH6 | liver | 17.853 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 0.2409 | more sensitive |
| dabrafenib | BRAF | 0.6377 | more sensitive |
| BRD-A05715709 | IDH1 | 17.2 | more resistant |
| BRD-K02492147 |  | 17.426 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0009 - docetaxel on KPNYN
*Evidence: SHAP-0009*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **docetaxel** (master_cpd_id=660364) |
| Gene Target | n/a |
| Mechanism / Activity | inhibitor of microtubule assembly |
| Cell Line | **KPNYN** (master_ccl_id=572) |
| Tissue | autonomic ganglia |
| Histology | neuroblastoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **17.3740**
- RF-predicted AUC: **7.9419**
- Prediction error (observed - predicted): **+9.4321**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (374 pairs): mean=6.6365, q10=1.9261, median=6.6621, q90=11.3557, sample percentile=100.0
- Cell cohort (374 pairs): mean=13.7829, q10=11.9721, median=13.9665, q90=15.4320, sample percentile=98.7
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_1009** (fingerprint_bit; SHAP=-1.6916, |SHAP|=1.6916)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
2. **fp_0443** (fingerprint_bit; SHAP=-1.1463, |SHAP|=1.1463)  
  _present; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
3. **fp_0204** (fingerprint_bit; SHAP=-0.7446, |SHAP|=0.7446)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
4. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.4360, |SHAP|=0.4360)  
  _value=0.7524, z=-2.18; markedly below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
5. **fp_0741** (fingerprint_bit; SHAP=-0.2464, |SHAP|=0.2464)  
  _present; representative SMARTS `[#7]-[#6]-[#6]`; present in 6.7% of CTRPv2 compounds; example compounds: BIX-01294, IC-87114, ML031_
6. **fp_0271** (fingerprint_bit; SHAP=-0.2446, |SHAP|=0.2446)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, BRD-K94991378_
7. **SDC4 (6385)** (gene_expression; SHAP=-0.1550, |SHAP|=0.1550)  
  _value=1.9825, z=-1.44; below the cross-cell-line mean; recurs in 154 predictable-drug RF signatures_
8. **fp_0806** (fingerprint_bit; SHAP=-0.1096, |SHAP|=0.1096)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| 697 | haematopoietic and lymphoid tissue | 0.1864 | more sensitive |
| OCIAML3 | haematopoietic and lymphoid tissue | 0.2513 | more sensitive |
| TUHR14TKB | kidney | 14.56 | more resistant |
| MALME3M | skin | 14.573 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 6.9324 | more sensitive |
| 1S,3R-RSL-3 | GPX4 | 7.8236 | more sensitive |
| erlotinib | EGFR;ERBB2 | 19.163 | more resistant |
| pevonedistat | NAE1 | 19.572 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0010 - RITA on TE441T
*Evidence: SHAP-0010*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **RITA** (master_cpd_id=375492) |
| Gene Target | MDM2;TP53 |
| Mechanism / Activity | inhibitor of p53-MDM2 interaction |
| Cell Line | **TE441T** (master_ccl_id=1192) |
| Tissue | soft tissue |
| Histology | rhabdomyosarcoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **1.3692**
- RF-predicted AUC: **13.5331**
- Prediction error (observed - predicted): **-12.1639**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (768 pairs): mean=12.6550, q10=8.7796, median=13.3960, q90=14.9503, sample percentile=0.1
- Cell cohort (400 pairs): mean=12.4603, q10=8.3222, median=13.2110, q90=14.9732, sample percentile=0.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2021, |SHAP|=0.2021)  
  _value=6.2249, z=-0.01; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0760** (fingerprint_bit; SHAP=-0.0898, |SHAP|=0.0898)  
  _present; representative SMARTS `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](=[#8])-[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: betulinic acid, paclitaxel, ouabain_
3. **fp_0443** (fingerprint_bit; SHAP=+0.0888, |SHAP|=0.0888)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
4. **fp_0902** (fingerprint_bit; SHAP=+0.0803, |SHAP|=0.0803)  
  _absent; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0779, |SHAP|=0.0779)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0367** (fingerprint_bit; SHAP=+0.0763, |SHAP|=0.0763)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
7. **fp_0062** (fingerprint_bit; SHAP=-0.0588, |SHAP|=0.0588)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
8. **fp_0504** (fingerprint_bit; SHAP=+0.0412, |SHAP|=0.0412)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| BCP1 | haematopoietic and lymphoid tissue | 1.5251 | more sensitive |
| SET2 | haematopoietic and lymphoid tissue | 2.0638 | more sensitive |
| BFTC905 | urinary tract | 17.214 | more resistant |
| CAL120 | breast | 18.954 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | 0.8076 | more sensitive |
| leptomycin B | XPO1 | 1.0931 | more sensitive |
| procarbazine |  | 17.3 | more resistant |
| BRD-K16147474 |  | 17.667 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0011 - GSK2636771 on SUDHL10
*Evidence: SHAP-0011*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **GSK2636771** (master_cpd_id=668723) |
| Gene Target | PIK3CB |
| Mechanism / Activity | inhibitor of PI3K catalytic subunit beta |
| Cell Line | **SUDHL10** (master_ccl_id=1140) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | diffuse large B cell lymphoma |

### Response Summary
- Observed AUC: **21.9540**
- RF-predicted AUC: **12.5439**
- Prediction error (observed - predicted): **+9.4101**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (572 pairs): mean=14.2447, q10=12.8601, median=14.3780, q90=15.4192, sample percentile=100.0
- Cell cohort (352 pairs): mean=12.7645, q10=8.8718, median=13.4990, q90=15.6467, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.6573, |SHAP|=0.6573)  
  _value=1.9408, z=-1.71; below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0623** (fingerprint_bit; SHAP=-0.1025, |SHAP|=0.1025)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
3. **fp_0062** (fingerprint_bit; SHAP=-0.0969, |SHAP|=0.0969)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
4. **fp_0806** (fingerprint_bit; SHAP=+0.0864, |SHAP|=0.0864)  
  _present; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_
5. **fp_0443** (fingerprint_bit; SHAP=+0.0712, |SHAP|=0.0712)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
6. **fp_0760** (fingerprint_bit; SHAP=-0.0568, |SHAP|=0.0568)  
  _present; representative SMARTS `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](=[#8])-[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: betulinic acid, paclitaxel, ouabain_
7. **fp_0504** (fingerprint_bit; SHAP=+0.0482, |SHAP|=0.0482)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_
8. **SDC4 (6385)** (gene_expression; SHAP=-0.0388, |SHAP|=0.0388)  
  _value=0.5632, z=-2.04; markedly below the cross-cell-line mean; recurs in 154 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| UO31 |  | 9.2347 | more sensitive |
| WM115 | skin | 9.9355 | more sensitive |
| NCIH1573 | lung | 17.421 | more resistant |
| NCIH2444 | lung | 17.696 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| paclitaxel |  | 0.6975 | more sensitive |
| SB-743921 | KIF11 | 1.0623 | more sensitive |
| isonicotinohydroxamic acid | HDAC6 | 17.676 | more resistant |
| palmostatin B | LYPLA1 | 18.229 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0012 - dabrafenib on DU4475
*Evidence: SHAP-0012*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **dabrafenib** (master_cpd_id=687954) |
| Gene Target | BRAF |
| Mechanism / Activity | inhibitor of BRAF |
| Cell Line | **DU4475** (master_ccl_id=226) |
| Tissue | breast |
| Histology | carcinoma |
| Subtype | ductal carcinoma |

### Response Summary
- Observed AUC: **0.6377**
- RF-predicted AUC: **12.7509**
- Prediction error (observed - predicted): **-12.1132**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (387 pairs): mean=13.4354, q10=11.2278, median=14.0730, q90=14.9602, sample percentile=0.3
- Cell cohort (363 pairs): mean=11.2338, q10=5.5261, median=11.7180, q90=14.7064, sample percentile=0.8
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.5127, |SHAP|=0.5127)  
  _value=4.5098, z=-0.69; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0204** (fingerprint_bit; SHAP=+0.1150, |SHAP|=0.1150)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
3. **fp_0443** (fingerprint_bit; SHAP=+0.0805, |SHAP|=0.0805)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
4. **fp_0760** (fingerprint_bit; SHAP=-0.0698, |SHAP|=0.0698)  
  _present; representative SMARTS `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](=[#8])-[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: betulinic acid, paclitaxel, ouabain_
5. **fp_0227** (fingerprint_bit; SHAP=+0.0556, |SHAP|=0.0556)  
  _absent; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0544, |SHAP|=0.0544)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0902** (fingerprint_bit; SHAP=+0.0537, |SHAP|=0.0537)  
  _absent; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
8. **fp_0504** (fingerprint_bit; SHAP=+0.0420, |SHAP|=0.0420)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SIGM5 | haematopoietic and lymphoid tissue | 2.4951 | more sensitive |
| WM88 | skin | 2.5202 | more sensitive |
| NCIH2196 | lung | 16.729 | more resistant |
| SKMEL2 | skin | 19.85 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| trametinib | MAP2K1;MAP2K2 | 0.1282 | more sensitive |
| leptomycin B | XPO1 | 0.2409 | more sensitive |
| BRD-A05715709 | IDH1 | 17.2 | more resistant |
| BRD-K02492147 |  | 17.426 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0013 - MLN2238 on KARPAS620
*Evidence: SHAP-0013*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **MLN2238** (master_cpd_id=632873) |
| Gene Target | PSMB5 |
| Mechanism / Activity | inhibitor of 20S proteasome at the chymotrypsin-like proteolytic (beta-5) site |
| Cell Line | **KARPAS620** (master_ccl_id=517) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | plasma cell myeloma |

### Response Summary
- Observed AUC: **18.6540**
- RF-predicted AUC: **9.2450**
- Prediction error (observed - predicted): **+9.4090**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (799 pairs): mean=9.1400, q10=7.0639, median=8.9598, q90=11.4934, sample percentile=100.0
- Cell cohort (399 pairs): mean=14.4543, q10=13.0386, median=14.6440, q90=15.7248, sample percentile=100.0
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0204** (fingerprint_bit; SHAP=-1.9080, |SHAP|=1.9080)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
2. **fp_0271** (fingerprint_bit; SHAP=-0.7280, |SHAP|=0.7280)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, BRD-K94991378_
3. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.5841, |SHAP|=0.5841)  
  _value=1.9553, z=-1.70; below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
4. **fp_0806** (fingerprint_bit; SHAP=-0.3630, |SHAP|=0.3630)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_
5. **fp_0062** (fingerprint_bit; SHAP=-0.1713, |SHAP|=0.1713)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
6. **fp_0623** (fingerprint_bit; SHAP=-0.1084, |SHAP|=0.1084)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
7. **fp_0600** (fingerprint_bit; SHAP=+0.1070, |SHAP|=0.1070)  
  _present; representative SMARTS `[#6]:[#6](:[#7]):[#7]`; present in 5.0% of CTRPv2 compounds; example compounds: methotrexate, C6-ceramide, cerulenin_
8. **fp_0131** (fingerprint_bit; SHAP=+0.1033, |SHAP|=0.1033)  
  _present; representative SMARTS `[#6]:[#6]:[#6]:[#6]:[#7]`; present in 2.7% of CTRPv2 compounds; example compounds: paclitaxel, SB-431542, axitinib_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| RS411 | haematopoietic and lymphoid tissue | 3.3318 | more sensitive |
| JM1 | haematopoietic and lymphoid tissue | 4.1435 | more sensitive |
| HS934T | skin | 16.136 | more resistant |
| HS688AT | skin | 17.592 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| 1S,3R-RSL-3 | GPX4 | 6.8549 | more sensitive |
| doxorubicin | TOP2A | 7.6793 | more sensitive |
| brefeldin A | ARF1 | 17.858 | more resistant |
| bortezomib | PSMB1;PSMB2;PSMB5;PSMD1;PSMD2 | 18.476 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0014 - AZD4547 on NCIH716
*Evidence: SHAP-0014*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **AZD4547** (master_cpd_id=660325) |
| Gene Target | FGFR1;FGFR2;FGFR3 |
| Mechanism / Activity | inhibitor of fibroblast growth factor receptors |
| Cell Line | **NCIH716** (master_ccl_id=155348) |
| Tissue | large intestine |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed AUC: **1.1299**
- RF-predicted AUC: **13.2363**
- Prediction error (observed - predicted): **-12.1064**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (713 pairs): mean=12.5713, q10=10.7448, median=12.8880, q90=14.1954, sample percentile=0.1
- Cell cohort (415 pairs): mean=12.9378, q10=9.0513, median=13.7170, q90=15.3282, sample percentile=0.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2038, |SHAP|=0.2038)  
  _value=4.7051, z=-0.61; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0227** (fingerprint_bit; SHAP=-0.1489, |SHAP|=0.1489)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
3. **fp_0468** (fingerprint_bit; SHAP=-0.1446, |SHAP|=0.1446)  
  _present; representative SMARTS `[#6]:[#6](:[#6](-[#6]-[#7]):[#6](-[#6]):[#6]):[#6]`; present in 0.6% of CTRPv2 compounds; example compounds: staurosporine, StemRegenin 1, leptomycin B_
4. **fp_0443** (fingerprint_bit; SHAP=+0.0964, |SHAP|=0.0964)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0720, |SHAP|=0.0720)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0705, |SHAP|=0.0705)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0902** (fingerprint_bit; SHAP=+0.0644, |SHAP|=0.0644)  
  _absent; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
8. **fp_0504** (fingerprint_bit; SHAP=+0.0362, |SHAP|=0.0362)  
  _absent; representative SMARTS `[#6]:[#6](=[#8]):[#7]`; present in 4.4% of CTRPv2 compounds; example compounds: topotecan, IC-87114, erastin_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SNU16 | stomach | 2.9571 | more sensitive |
| UMUC1 | urinary tract | 4.3505 | more sensitive |
| NCIH2444 | lung | 16.097 | more resistant |
| SW1573 | lung | 19.226 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| cediranib | FLT1;FLT4;KDR | 3.5276 | more sensitive |
| pluripotin | MAPK1;RASAL1 | 3.6143 | more sensitive |
| ML320 | GSK3B | 18.45 | more resistant |
| elocalcitol | VDR | 18.716 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0015 - LBH-589 on KARPAS620
*Evidence: SHAP-0015*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **LBH-589** (master_cpd_id=54210) |
| Gene Target | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8 |
| Cell Line | **KARPAS620** (master_ccl_id=517) |
| Tissue | haematopoietic and lymphoid tissue |
| Histology | lymphoid neoplasm |
| Subtype | plasma cell myeloma |

### Response Summary
- Observed AUC: **14.7440**
- RF-predicted AUC: **5.4171**
- Prediction error (observed - predicted): **+9.3269**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (794 pairs): mean=5.3007, q10=2.3740, median=5.3373, q90=7.9625, sample percentile=99.5
- Cell cohort (399 pairs): mean=14.4543, q10=13.0386, median=14.6440, q90=15.7248, sample percentile=55.4
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0223** (fingerprint_bit; SHAP=-2.4886, |SHAP|=2.4886)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: gossypol, cytochalasin B, erastin_
2. **fp_0623** (fingerprint_bit; SHAP=-0.7250, |SHAP|=0.7250)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
3. **TNFRSF12A (51330)** (gene_expression; SHAP=-0.6997, |SHAP|=0.6997)  
  _value=1.9553, z=-1.70; below the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
4. **fp_0362** (fingerprint_bit; SHAP=-0.5959, |SHAP|=0.5959)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: staurosporine, vincristine, omacetaxine mepesuccinate_
5. **fp_0053** (fingerprint_bit; SHAP=-0.5671, |SHAP|=0.5671)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 10.0% of CTRPv2 compounds; example compounds: chlorambucil, tanespimycin, mitomycin_
6. **fp_0799** (fingerprint_bit; SHAP=-0.3937, |SHAP|=0.3937)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 4.4% of CTRPv2 compounds; example compounds: ciclopirox, blebbistatin, pifithrin-alpha_
7. **fp_0091** (fingerprint_bit; SHAP=-0.3443, |SHAP|=0.3443)  
  _present; representative SMARTS `[#16]-[#8]-[#6]`; present in 1.7% of CTRPv2 compounds; example compounds: CIL55, NSC 74859, pevonedistat_
8. **fp_0242** (fingerprint_bit; SHAP=-0.2823, |SHAP|=0.2823)  
  _present; representative SMARTS `[#6]:[#7]:[#6](:[#6]:[#16])-[#6](:[#6]):[#6]`; present in 4.0% of CTRPv2 compounds; example compounds: BRD4132, BRD-A94377914, SKI-II_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KMS26 | haematopoietic and lymphoid tissue | 0.4297 | more sensitive |
| SEM | haematopoietic and lymphoid tissue | 0.4308 | more sensitive |
| HUCCT1 | biliary tract | 18.374 | more resistant |
| 253JBV | urinary tract | 20.449 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| 1S,3R-RSL-3 | GPX4 | 6.8549 | more sensitive |
| doxorubicin | TOP2A | 7.6793 | more sensitive |
| bortezomib | PSMB1;PSMB2;PSMB5;PSMD1;PSMD2 | 18.476 | more resistant |
| MLN2238 | PSMB5 | 18.654 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0016 - ceranib-2 on SNU398
*Evidence: SHAP-0016*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **ceranib-2** (master_cpd_id=660078) |
| Gene Target | ACER1;ACER2;ACER3;ASAH1;ASAH2;ASAH2B |
| Mechanism / Activity | inhibitor of ceramidase activity |
| Cell Line | **SNU398** (master_ccl_id=1101) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed AUC: **0.9898**
- RF-predicted AUC: **13.0950**
- Prediction error (observed - predicted): **-12.1052**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (802 pairs): mean=11.1811, q10=9.0483, median=11.2180, q90=13.2789, sample percentile=0.1
- Cell cohort (376 pairs): mean=12.6859, q10=9.3419, median=13.3605, q90=14.8910, sample percentile=0.3
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=+0.3525, |SHAP|=0.3525)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2492, |SHAP|=0.2492)  
  _value=6.1374, z=-0.05; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_0227** (fingerprint_bit; SHAP=-0.1804, |SHAP|=0.1804)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
4. **fp_0362** (fingerprint_bit; SHAP=-0.1707, |SHAP|=0.1707)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: staurosporine, vincristine, omacetaxine mepesuccinate_
5. **fp_1009** (fingerprint_bit; SHAP=-0.1700, |SHAP|=0.1700)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
6. **fp_0204** (fingerprint_bit; SHAP=+0.0762, |SHAP|=0.0762)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
7. **fp_0062** (fingerprint_bit; SHAP=-0.0675, |SHAP|=0.0675)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
8. **fp_0623** (fingerprint_bit; SHAP=+0.0599, |SHAP|=0.0599)  
  _absent; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH510 | lung | 4.5546 | more sensitive |
| DND41 | haematopoietic and lymphoid tissue | 4.9285 | more sensitive |
| KARPAS620 | haematopoietic and lymphoid tissue | 16.087 | more resistant |
| MKN45 | stomach | 16.756 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| tosedostat | ANPEP;LAP3;NPEPPS | 1.025 | more sensitive |
| lenvatinib | FLT1;FLT3;KDR;KIT;PDGFRA;PDGFRB | 1.3195 | more sensitive |
| erlotinib | EGFR;ERBB2 | 17.1 | more resistant |
| abiraterone | CYP17A1 | 17.336 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0017 - LBH-589 on 253JBV
*Evidence: SHAP-0017*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **LBH-589** (master_cpd_id=54210) |
| Gene Target | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 |
| Mechanism / Activity | inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8 |
| Cell Line | **253JBV** (master_ccl_id=9) |
| Tissue | urinary tract |
| Histology | carcinoma |
| Subtype | transitional cell carcinoma |

### Response Summary
- Observed AUC: **20.4490**
- RF-predicted AUC: **11.2021**
- Prediction error (observed - predicted): **+9.2469**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (794 pairs): mean=5.3007, q10=2.3740, median=5.3373, q90=7.9625, sample percentile=100.0
- Cell cohort (331 pairs): mean=13.6723, q10=10.3790, median=13.9550, q90=16.5890, sample percentile=99.4
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0223** (fingerprint_bit; SHAP=-1.5843, |SHAP|=1.5843)  
  _present; representative SMARTS `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`; present in 1.2% of CTRPv2 compounds; example compounds: gossypol, cytochalasin B, erastin_
2. **PLK2 (10769)** (gene_expression; SHAP=+0.8630, |SHAP|=0.8630)  
  _value=10.5297, z=+1.69; above the cross-cell-line mean; recurs in 102 predictable-drug RF signatures_
3. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.5953, |SHAP|=0.5953)  
  _value=7.8195, z=+0.62; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
4. **fp_0362** (fingerprint_bit; SHAP=-0.3505, |SHAP|=0.3505)  
  _present; representative SMARTS `[#8]-[#6](=[#8])-[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: staurosporine, vincristine, omacetaxine mepesuccinate_
5. **fp_0623** (fingerprint_bit; SHAP=-0.3048, |SHAP|=0.3048)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
6. **fp_0902** (fingerprint_bit; SHAP=-0.2993, |SHAP|=0.2993)  
  _present; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
7. **fp_0053** (fingerprint_bit; SHAP=-0.2767, |SHAP|=0.2767)  
  _present; representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 10.0% of CTRPv2 compounds; example compounds: chlorambucil, tanespimycin, mitomycin_
8. **PLBD1 (79887)** (gene_expression; SHAP=+0.2708, |SHAP|=0.2708)  
  _value=0.0000, z=-1.02; below the cross-cell-line mean; recurs in 16 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KMS26 | haematopoietic and lymphoid tissue | 0.4297 | more sensitive |
| SEM | haematopoietic and lymphoid tissue | 0.4308 | more sensitive |
| TE441T | soft tissue | 16.315 | more resistant |
| HUCCT1 | biliary tract | 18.374 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | 2.6835 | more sensitive |
| leptomycin B | XPO1 | 3.6618 | more sensitive |
| triazolothiadiazine | PDE4A;PDE4B;PDE4D | 21.219 | more resistant |
| ML203 | PKM | 21.542 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0018 - foretinib on EBC1
*Evidence: SHAP-0018*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **foretinib** (master_cpd_id=628607) |
| Gene Target | KDR;MET |
| Mechanism / Activity | inhibitor of MET and VEGFR2 |
| Cell Line | **EBC1** (master_ccl_id=230) |
| Tissue | lung |
| Histology | carcinoma |
| Subtype | squamous cell carcinoma |

### Response Summary
- Observed AUC: **0.8572**
- RF-predicted AUC: **12.9169**
- Prediction error (observed - predicted): **-12.0597**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (779 pairs): mean=10.1968, q10=7.9914, median=10.5290, q90=12.1368, sample percentile=0.5
- Cell cohort (404 pairs): mean=12.7372, q10=9.1351, median=13.2355, q90=15.3490, sample percentile=0.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1686, |SHAP|=0.1686)  
  _value=9.0505, z=+1.11; above the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0227** (fingerprint_bit; SHAP=-0.1640, |SHAP|=0.1640)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
3. **fp_0728** (fingerprint_bit; SHAP=-0.0929, |SHAP|=0.0929)  
  _present; representative SMARTS `Br`; present in 5.2% of CTRPv2 compounds; example compounds: Bax channel blocker, manumycin A, SB-225002_
4. **fp_0521** (fingerprint_bit; SHAP=-0.0710, |SHAP|=0.0710)  
  _present; representative SMARTS `[#6]-[#6](=[#8])-[#8]-[#6@H]`; present in 1.5% of CTRPv2 compounds; example compounds: paclitaxel, staurosporine, cerulenin_
5. **fp_0806** (fingerprint_bit; SHAP=+0.0704, |SHAP|=0.0704)  
  _present; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0651, |SHAP|=0.0651)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0443** (fingerprint_bit; SHAP=+0.0564, |SHAP|=0.0564)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
8. **fp_0902** (fingerprint_bit; SHAP=-0.0551, |SHAP|=0.0551)  
  _present; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | 0.0691 | more sensitive |
| MOLM13 | haematopoietic and lymphoid tissue | 0.2374 | more sensitive |
| L1236 | haematopoietic and lymphoid tissue | 15.179 | more resistant |
| BEN | lung | 15.806 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SGX-523 | MET | 3.8224 | more sensitive |
| SB-743921 | KIF11 | 4.0831 | more sensitive |
| isonicotinohydroxamic acid | HDAC6 | 16.908 | more resistant |
| Ki8751 | KDR;KIT;PDGFRA | 17.13 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0019 - 1S,3R-RSL-3 on CAL62
*Evidence: SHAP-0019*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **1S,3R-RSL-3** (master_cpd_id=609060) |
| Gene Target | GPX4 |
| Mechanism / Activity | synthetic lethal with HRAS in engineered cells; inhibitor of GPX4 |
| Cell Line | **CAL62** (master_ccl_id=119) |
| Tissue | thyroid |
| Histology | carcinoma |
| Subtype | anaplastic carcinoma |

### Response Summary
- Observed AUC: **18.6380**
- RF-predicted AUC: **9.6448**
- Prediction error (observed - predicted): **+8.9932**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (808 pairs): mean=8.0446, q10=4.1912, median=7.9968, q90=12.3435, sample percentile=100.0
- Cell cohort (354 pairs): mean=13.6896, q10=10.2066, median=14.0290, q90=16.9564, sample percentile=98.3
- Interpretation: **more resistant than the model predicted**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0204** (fingerprint_bit; SHAP=-1.7674, |SHAP|=1.7674)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
2. **fp_0271** (fingerprint_bit; SHAP=-0.8043, |SHAP|=0.8043)  
  _present; representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 5.0% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, BRD-K94991378_
3. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.3501, |SHAP|=0.3501)  
  _value=8.1221, z=+0.74; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
4. **fp_1017** (fingerprint_bit; SHAP=-0.3293, |SHAP|=0.3293)  
  _present; representative SMARTS `[#6]-[#6]`; present in 8.1% of CTRPv2 compounds; example compounds: tretinoin, betulinic acid, paclitaxel_
5. **fp_0806** (fingerprint_bit; SHAP=-0.2953, |SHAP|=0.2953)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_
6. **fp_0062** (fingerprint_bit; SHAP=-0.1521, |SHAP|=0.1521)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0261** (fingerprint_bit; SHAP=-0.1379, |SHAP|=0.1379)  
  _present; representative SMARTS `[#7]:[#6](:[#6]:[#6]:[#6]):[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: BRD6340, gossypol, staurosporine_
8. **fp_0395** (fingerprint_bit; SHAP=-0.0753, |SHAP|=0.0753)  
  _present; representative SMARTS `[#6]-[#6@H](-[#6])-[#7](-[#6]-[#6@H])-[#6](-[#6])=[#8]`; present in 4.8% of CTRPv2 compounds; example compounds: cytochalasin B, MI-1, NSC632839_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| SW948 | large intestine | 0.7235 | more sensitive |
| DOHH2 | haematopoietic and lymphoid tissue | 1.0629 | more sensitive |
| 253JBV | urinary tract | 15.0 | more resistant |
| BEN | lung | 15.397 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| SB-743921 | KIF11 | 4.5453 | more sensitive |
| GSK461364 | PLK1 | 5.0099 | more sensitive |
| RG-108 | DNMT1 | 20.715 | more resistant |
| BRD-K29086754 |  | 20.784 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0020 - PHA-793887 on SNU398
*Evidence: SHAP-0020*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **PHA-793887** (master_cpd_id=640007) |
| Gene Target | CDK1;CDK2;CDK4;CDK5;CDK7;CDK9 |
| Mechanism / Activity | inhibitor of cyclin-dependent kinases |
| Cell Line | **SNU398** (master_ccl_id=1101) |
| Tissue | liver |
| Histology | carcinoma |
| Subtype | hepatocellular carcinoma |

### Response Summary
- Observed AUC: **1.5525**
- RF-predicted AUC: **13.5394**
- Prediction error (observed - predicted): **-11.9869**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (797 pairs): mean=11.4834, q10=8.5192, median=11.8740, q90=13.7878, sample percentile=0.1
- Cell cohort (376 pairs): mean=12.6859, q10=9.3419, median=13.3605, q90=14.8910, sample percentile=1.1
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=+0.3779, |SHAP|=0.3779)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2414, |SHAP|=0.2414)  
  _value=6.1374, z=-0.05; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_1009** (fingerprint_bit; SHAP=-0.1604, |SHAP|=0.1604)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
4. **fp_0367** (fingerprint_bit; SHAP=+0.0897, |SHAP|=0.0897)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
5. **fp_0623** (fingerprint_bit; SHAP=-0.0847, |SHAP|=0.0847)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0645, |SHAP|=0.0645)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0141** (fingerprint_bit; SHAP=+0.0500, |SHAP|=0.0500)  
  _absent; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_
8. **fp_0771** (fingerprint_bit; SHAP=+0.0486, |SHAP|=0.0486)  
  _absent; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| EOL1 | haematopoietic and lymphoid tissue | 4.6997 | more sensitive |
| OCIAML3 | haematopoietic and lymphoid tissue | 4.9334 | more sensitive |
| DMS454 | lung | 17.514 | more resistant |
| KPL1 | breast | 17.693 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ceranib-2 | ACER1;ACER2;ACER3;ASAH1;ASAH2;ASAH2B | 0.9898 | more sensitive |
| tosedostat | ANPEP;LAP3;NPEPPS | 1.025 | more sensitive |
| erlotinib | EGFR;ERBB2 | 17.1 | more resistant |
| abiraterone | CYP17A1 | 17.336 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0021 - KU-0063794 on SKMEL2
*Evidence: SHAP-0021*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KU-0063794** (master_cpd_id=606363) |
| Gene Target | MTOR |
| Mechanism / Activity | inhibitor of mTOR |
| Cell Line | **SKMEL2** (master_ccl_id=1041) |
| Tissue | skin |
| Histology | malignant melanoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **21.2320**
- RF-predicted AUC: **12.2996**
- Prediction error (observed - predicted): **+8.9324**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (791 pairs): mean=11.8501, q10=9.6862, median=12.0360, q90=13.6900, sample percentile=100.0
- Cell cohort (375 pairs): mean=14.2236, q10=11.7612, median=14.4630, q90=16.0996, sample percentile=99.5
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0202** (fingerprint_bit; SHAP=-0.4209, |SHAP|=0.4209)  
  _present; representative SMARTS `[#6]:[#6](-[#8]):[#6]`; present in 7.3% of CTRPv2 compounds; example compounds: gossypol, teniposide, epigallocatechin-3-monogallate_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1665, |SHAP|=0.1665)  
  _value=7.8670, z=+0.64; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_0623** (fingerprint_bit; SHAP=-0.1642, |SHAP|=0.1642)  
  _present; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
4. **fp_0227** (fingerprint_bit; SHAP=-0.1639, |SHAP|=0.1639)  
  _present; representative SMARTS `[#8]-[#6@H]`; present in 6.7% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, teniposide_
5. **fp_0771** (fingerprint_bit; SHAP=-0.1116, |SHAP|=0.1116)  
  _present; representative SMARTS `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: tacedinaline, AM-580, entinostat_
6. **fp_0722** (fingerprint_bit; SHAP=-0.0890, |SHAP|=0.0890)  
  _present; representative SMARTS `[#6]:[#6](:[#16])-[#6](=[#8])-[#7]-[#6]`; present in 3.1% of CTRPv2 compounds; example compounds: simvastatin, lovastatin, doxorubicin_
7. **fp_0062** (fingerprint_bit; SHAP=-0.0889, |SHAP|=0.0889)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
8. **fp_0806** (fingerprint_bit; SHAP=+0.0624, |SHAP|=0.0624)  
  _present; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| KMS34 | haematopoietic and lymphoid tissue | 5.7813 | more sensitive |
| PFEIFFER | haematopoietic and lymphoid tissue | 6.0865 | more sensitive |
| SU8686 | pancreas | 17.003 | more resistant |
| NB4 | haematopoietic and lymphoid tissue | 17.395 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 2.1139 | more sensitive |
| LBH-589 | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 | 5.3553 | more sensitive |
| alisertib | AURKA;AURKB | 21.265 | more resistant |
| cytarabine hydrochloride |  | 27.182 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0022 - BRD-K99006945 on JHUEM1
*Evidence: SHAP-0022*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **BRD-K99006945** (master_cpd_id=687395) |
| Gene Target | n/a |
| Mechanism / Activity | screening hit |
| Cell Line | **JHUEM1** (master_ccl_id=497) |
| Tissue | endometrium |
| Histology | carcinoma |
| Subtype | adenocarcinoma |

### Response Summary
- Observed AUC: **1.5813**
- RF-predicted AUC: **13.5611**
- Prediction error (observed - predicted): **-11.9798**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (391 pairs): mean=14.0290, q10=12.3540, median=14.5820, q90=15.2840, sample percentile=0.5
- Cell cohort (411 pairs): mean=12.2365, q10=8.3711, median=12.7280, q90=14.8290, sample percentile=0.2
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1896, |SHAP|=0.1896)  
  _value=7.5636, z=+0.52; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
2. **fp_0367** (fingerprint_bit; SHAP=+0.1308, |SHAP|=0.1308)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
3. **fp_0204** (fingerprint_bit; SHAP=+0.1090, |SHAP|=0.1090)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
4. **fp_0623** (fingerprint_bit; SHAP=+0.0909, |SHAP|=0.0909)  
  _absent; representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`; present in 5.8% of CTRPv2 compounds; example compounds: trifluoperazine, prochlorperazine, pifithrin-alpha_
5. **fp_0443** (fingerprint_bit; SHAP=+0.0719, |SHAP|=0.0719)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0642, |SHAP|=0.0642)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0902** (fingerprint_bit; SHAP=-0.0553, |SHAP|=0.0553)  
  _present; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
8. **fp_0141** (fingerprint_bit; SHAP=-0.0418, |SHAP|=0.0418)  
  _present; representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| CORL51 | lung | 0.7138 | more sensitive |
| HEL9217 | haematopoietic and lymphoid tissue | 2.7437 | more sensitive |
| GRANTA519 | haematopoietic and lymphoid tissue | 17.246 | more resistant |
| CORL88 | lung | 17.958 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| ouabain | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 | 2.3956 | more sensitive |
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | 2.5153 | more sensitive |
| SJ-172550 | MDM2;TP53 | 15.632 | more resistant |
| BRD-K51831558 | EZH2 | 16.167 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0023 - SCH-529074 on MESSA
*Evidence: SHAP-0023*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **SCH-529074** (master_cpd_id=609062) |
| Gene Target | TP53 |
| Mechanism / Activity | activator of mutant p53 |
| Cell Line | **MESSA** (master_ccl_id=668) |
| Tissue | soft tissue |
| Histology | sarcoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **22.3390**
- RF-predicted AUC: **13.4876**
- Prediction error (observed - predicted): **+8.8514**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (728 pairs): mean=12.7564, q10=11.8330, median=12.6080, q90=13.7739, sample percentile=100.0
- Cell cohort (384 pairs): mean=13.4964, q10=10.2458, median=14.2045, q90=15.3131, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=+0.3470, |SHAP|=0.3470)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2027, |SHAP|=0.2027)  
  _value=5.7781, z=-0.19; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_1009** (fingerprint_bit; SHAP=-0.1453, |SHAP|=0.1453)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
4. **fp_0367** (fingerprint_bit; SHAP=+0.1125, |SHAP|=0.1125)  
  _absent; representative SMARTS `[#6]:[#6](-[#6]):[#6]`; present in 6.4% of CTRPv2 compounds; example compounds: betulinic acid, gossypol, simvastatin_
5. **fp_0204** (fingerprint_bit; SHAP=+0.0686, |SHAP|=0.0686)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0489, |SHAP|=0.0489)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0902** (fingerprint_bit; SHAP=-0.0473, |SHAP|=0.0473)  
  _present; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_
8. **SDC4 (6385)** (gene_expression; SHAP=-0.0388, |SHAP|=0.0388)  
  _value=0.4017, z=-2.11; markedly below the cross-cell-line mean; recurs in 154 predictable-drug RF signatures_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| NCIH146 | lung | 9.9315 | more sensitive |
| LXF289 | lung | 10.131 | more sensitive |
| KMS34 | haematopoietic and lymphoid tissue | 16.203 | more resistant |
| KMS28BM | haematopoietic and lymphoid tissue | 16.835 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | 2.8442 | more sensitive |
| leptomycin B | XPO1 | 3.0203 | more sensitive |
| BRD-K52037352 |  | 22.02 | more resistant |
| BRD-K02251932 |  | 22.116 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0024 - KX2-391 on SNU16
*Evidence: SHAP-0024*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **KX2-391** (master_cpd_id=660779) |
| Gene Target | SRC |
| Mechanism / Activity | peptide mimetic; inhibitor of SRC activity in cells |
| Cell Line | **SNU16** (master_ccl_id=1089) |
| Tissue | stomach |
| Histology | carcinoma |
| Subtype | undifferentiated adenocarcinoma |

### Response Summary
- Observed AUC: **1.4980**
- RF-predicted AUC: **13.1396**
- Prediction error (observed - predicted): **-11.6416**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (771 pairs): mean=8.9221, q10=4.6224, median=9.1032, q90=12.8370, sample percentile=0.3
- Cell cohort (400 pairs): mean=11.2748, q10=6.2427, median=11.8720, q90=14.7997, sample percentile=2.5
- Interpretation: **exceptionally sensitive relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Top TreeSHAP Features
1. **fp_0443** (fingerprint_bit; SHAP=+0.2984, |SHAP|=0.2984)  
  _absent; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
2. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.2193, |SHAP|=0.2193)  
  _value=5.3644, z=-0.35; near the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
3. **fp_0706** (fingerprint_bit; SHAP=-0.2036, |SHAP|=0.2036)  
  _present; representative SMARTS `[#8]-[#6@@H](-[#6@@])-[#6]`; present in 2.5% of CTRPv2 compounds; example compounds: Bax channel blocker, paclitaxel, topotecan_
4. **fp_1009** (fingerprint_bit; SHAP=-0.1539, |SHAP|=0.1539)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]`; present in 9.1% of CTRPv2 compounds; example compounds: betulinic acid, isoliquiritigenin, curcumin_
5. **fp_0806** (fingerprint_bit; SHAP=+0.0667, |SHAP|=0.0667)  
  _present; representative SMARTS `[#6]:[#7]:[#6]`; present in 6.0% of CTRPv2 compounds; example compounds: fluorouracil, cimetidine, dacarbazine_
6. **fp_0062** (fingerprint_bit; SHAP=-0.0608, |SHAP|=0.0608)  
  _absent; representative SMARTS `[#6]-[#6](:[#6]):[#16]`; present in 3.7% of CTRPv2 compounds; example compounds: Merck60, cytarabine hydrochloride, VX-680_
7. **fp_0830** (fingerprint_bit; SHAP=-0.0608, |SHAP|=0.0608)  
  _absent; representative SMARTS `[#6]-[#7](-[#6])-[#6]`; present in 2.1% of CTRPv2 compounds; example compounds: vincristine, BI-2536, YM-155_
8. **fp_0902** (fingerprint_bit; SHAP=-0.0525, |SHAP|=0.0525)  
  _present; representative SMARTS `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]`; present in 1.0% of CTRPv2 compounds; example compounds: teniposide, NSC23766, etoposide_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| IMR32 | autonomic ganglia | 1.1789 | more sensitive |
| DB | haematopoietic and lymphoid tissue | 1.7067 | more sensitive |
| SKMEL2 | skin | 17.445 | more resistant |
| TUHR14TKB | kidney | 17.696 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| vincristine |  | 0.3588 | more sensitive |
| dinaciclib | CDK1;CDK2;CDK5;CDK9 | 0.3862 | more sensitive |
| IC-87114 | PIK3CD | 16.222 | more resistant |
| BRD-K48477130 |  | 16.314 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---

## RPT-0025 - ouabain on TUHR10TKB
*Evidence: SHAP-0025*

### Sample Identity
| Property | Value |
|---|---|
| Drug | **ouabain** (master_cpd_id=37190) |
| Gene Target | ATP1A1;ATP1A2;ATP1A3;ATP1A4;ATP1B1;ATP1B2;ATP1B3;ATP1B4 |
| Mechanism / Activity | cardiac glycoside; inhibitor of the Na+/K+-ATPase |
| Cell Line | **TUHR10TKB** (master_ccl_id=1213) |
| Tissue | kidney |
| Histology | carcinoma |
| Subtype | n/a |

### Response Summary
- Observed AUC: **29.3500**
- RF-predicted AUC: **20.6181**
- Prediction error (observed - predicted): **+8.7319**
- Global mean AUC across all pairs: **12.8580**
- Drug cohort (808 pairs): mean=5.8459, q10=2.8572, median=5.4318, q90=9.3618, sample percentile=100.0
- Cell cohort (394 pairs): mean=13.7497, q10=11.1287, median=13.9475, q90=16.1392, sample percentile=100.0
- Interpretation: **exceptionally resistant relative to the SHAP-predicted response and cohort baselines**
- Selection reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Top TreeSHAP Features
1. **CSF1 (1435)** (gene_expression; SHAP=+1.0870, |SHAP|=1.0870)  
  _value=7.8048, z=+2.69; markedly above the cross-cell-line mean; recurs in 13 predictable-drug RF signatures_
2. **fp_0009** (fingerprint_bit; SHAP=+0.9989, |SHAP|=0.9989)  
  _absent; representative SMARTS `[#6]-[#6](=[#8])-[#6]`; present in 3.3% of CTRPv2 compounds; example compounds: IC-87114, sorafenib, SNX-2112_
3. **fp_0443** (fingerprint_bit; SHAP=+0.5723, |SHAP|=0.5723)  
  _present; representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`; present in 0.4% of CTRPv2 compounds; example compounds: nilotinib, bleomycin A2_
4. **SDC4 (6385)** (gene_expression; SHAP=+0.4625, |SHAP|=0.4625)  
  _value=7.7349, z=+1.02; above the cross-cell-line mean; recurs in 154 predictable-drug RF signatures_
5. **COL18A1 (80781)** (gene_expression; SHAP=+0.3655, |SHAP|=0.3655)  
  _value=8.1162, z=+2.18; markedly above the cross-cell-line mean; recurs in 15 predictable-drug RF signatures_
6. **TNFRSF12A (51330)** (gene_expression; SHAP=+0.1918, |SHAP|=0.1918)  
  _value=9.5256, z=+1.30; above the cross-cell-line mean; recurs in 166 predictable-drug RF signatures_
7. **fp_0204** (fingerprint_bit; SHAP=-0.1742, |SHAP|=0.1742)  
  _present; representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`; present in 2.9% of CTRPv2 compounds; example compounds: BRD-K26531177, NVP-BEZ235, CD-437_
8. **fp_0630** (fingerprint_bit; SHAP=-0.1674, |SHAP|=0.1674)  
  _present; representative SMARTS `[#7](-[#6@@H])(-[#6@@H])-[#6](=[#8])-[#6]-[#17]`; present in 0.4% of CTRPv2 compounds; example compounds: 1S,3R-RSL-3, bleomycin A2_

### Same-Drug Cohort Examples
| Cell Line | Tissue | AUC | Profile |
|---|---|---|---|
| JEKO1 | haematopoietic and lymphoid tissue | 0.7869 | more sensitive |
| MINO | haematopoietic and lymphoid tissue | 0.8414 | more sensitive |
| NCIH2291 | lung | 16.16 | more resistant |
| NCIH2228 | lung | 16.285 | more resistant |

### Same-Cell Cohort Examples
| Drug | Gene Target | AUC | Profile |
|---|---|---|---|
| leptomycin B | XPO1 | 2.3645 | more sensitive |
| LBH-589 | HDAC1;HDAC2;HDAC3;HDAC6;HDAC8 | 6.0701 | more sensitive |
| PRIMA-1 | TP53 | 18.38 | more resistant |
| CID-5951923 | KLF5 | 18.702 | more resistant |

### Scope and Constraints
- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.
- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.
- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.

---
