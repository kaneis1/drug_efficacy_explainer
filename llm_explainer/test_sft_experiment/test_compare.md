# SFT vs Base Comparison

Base remains competitive on the held-out split.

## Summary

| Run | Reports | Avg Words | Heading Coverage | Unique-Line Ratio | Heuristic Score | Teacher Token-F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Base | 2/2 | 371.0 | 0.70 | 1.00 | 70.0 | 0.000 |
| SFT | 2/2 | 371.0 | 0.70 | 1.00 | 70.0 | 0.000 |

## RPT-0009 - docetaxel on KPNYN

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0009
- observed_auc: 17.3740
- interpretation: more resistant than the model predicted
- tissue / histology: autonomic ganglia / neuroblastoma
- model_predicted_auc: 7.9419
- prediction_error: +9.4321
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### Base (score=60.0, words=359)
## Executive Summary
Docetaxel on KPNYN cell line shows a higher observed AUC of 17.3740 compared to the model-predicted AUC of 7.9419, indicating more resistance than expected. The prediction error is +9.4321, which is a large positive deviation from the model's prediction.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_1009: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -1.6916.
*   fp_0443: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -1.1463.
*   fp_0204: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.7446.
*   TNFRSF12A (51330): A gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.4360.
*   fp_0741: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2464.
*   fp_0271: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2446.

These features are all associated with lower AUC (relative sensitivity), indicating that the model predicts docetaxel to be less effective on KPNYN cells than it actually is.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which are binary features representing the presence or absence of specific substructures in the compound's molecular structure. These features are:

*   fp_1009: Represented by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]`, present in 9.1% of CTRPv2 compounds, and associated with example compounds like betulinic acid, isoliquiritigenin, and curcumin.
*   fp_0443: Represented by the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, present in 0.4% of CTRPv2 compounds, and associated with example compounds like nilotinib and bleomycin A2.
*   fp_0204: Represented by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, present in 2.9% of CTRPv2 compounds, and associated with example compounds like BRD-K26531177, NVP-BEZ235, and CD-437.
*   fp_0741: Represented by the SMARTS pattern `[#7]-[#6]-[#6]`, present in 6.7% of CTRPv2 compounds, and associated with example compounds like BIX-01294, IC-87114, and ML031.
*   fp

### SFT (score=60.0, words=359)
## Executive Summary
Docetaxel on KPNYN cell line shows a higher observed AUC of 17.3740 compared to the model-predicted AUC of 7.9419, indicating more resistance than expected. The prediction error is +9.4321, which is a large positive deviation from the model's prediction.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_1009: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -1.6916.
*   fp_0443: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -1.1463.
*   fp_0204: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.7446.
*   TNFRSF12A (51330): A gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.4360.
*   fp_0741: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2464.
*   fp_0271: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2446.

These features are all associated with lower AUC (relative sensitivity), indicating that the model predicts docetaxel to be less effective on KPNYN cells than it actually is.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which are binary features representing the presence or absence of specific substructures in the compound's molecular structure. These features are:

*   fp_1009: Represented by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]`, present in 9.1% of CTRPv2 compounds, and associated with example compounds like betulinic acid, isoliquiritigenin, and curcumin.
*   fp_0443: Represented by the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, present in 0.4% of CTRPv2 compounds, and associated with example compounds like nilotinib and bleomycin A2.
*   fp_0204: Represented by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, present in 2.9% of CTRPv2 compounds, and associated with example compounds like BRD-K26531177, NVP-BEZ235, and CD-437.
*   fp_0741: Represented by the SMARTS pattern `[#7]-[#6]-[#6]`, present in 6.7% of CTRPv2 compounds, and associated with example compounds like BIX-01294, IC-87114, and ML031.
*   fp

---

## RPT-0024 - KX2-391 on SNU16

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0024
- observed_auc: 1.4980
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: stomach / carcinoma
- model_predicted_auc: 13.1396
- prediction_error: -11.6416
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### Base (score=80.0, words=383)
## Executive Summary
The observed AUC for KX2-391 on SNU16 is 1.4980, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.1396, indicating a large negative prediction error. This suggests that the model overestimates the sensitivity of KX2-391 on SNU16.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0443, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.2984.
* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.2193.
* fp_0706, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.2036.
* fp_1009, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.1539.
* fp_0806, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.0667.
* fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.0608.

These features indicate that the model's prediction of high sensitivity for KX2-391 on SNU16 is driven by the presence of specific fingerprint bits and gene expression levels.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0443 and fp_0806 are present in 0.4% and 6.0% of CTRPv2 compounds, respectively. These features are representative of SMARTS patterns `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` and `[#6]:[#7]:[#6]`, respectively. The gene expression feature TNFRSF12A (51330) is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

The same-drug cohort examples for KX2-391 show varying levels of sensitivity, with some cells being more sensitive (IMR32, DB) and others being more resistant (SKMEL2, TUHR14TKB). The same-cell cohort examples for SNU16 show that other drugs (vincristine, dinaciclib) are more sensitive, while some drugs (IC-87114, BRD-K48477130) are more resistant.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061. These metrics are used as training diagnostics and not held-out generalization. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp

### SFT (score=80.0, words=383)
## Executive Summary
The observed AUC for KX2-391 on SNU16 is 1.4980, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.1396, indicating a large negative prediction error. This suggests that the model overestimates the sensitivity of KX2-391 on SNU16.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0443, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.2984.
* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.2193.
* fp_0706, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.2036.
* fp_1009, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.1539.
* fp_0806, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance), with a SHAP value of +0.0667.
* fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), with a SHAP value of -0.0608.

These features indicate that the model's prediction of high sensitivity for KX2-391 on SNU16 is driven by the presence of specific fingerprint bits and gene expression levels.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0443 and fp_0806 are present in 0.4% and 6.0% of CTRPv2 compounds, respectively. These features are representative of SMARTS patterns `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` and `[#6]:[#7]:[#6]`, respectively. The gene expression feature TNFRSF12A (51330) is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

The same-drug cohort examples for KX2-391 show varying levels of sensitivity, with some cells being more sensitive (IMR32, DB) and others being more resistant (SKMEL2, TUHR14TKB). The same-cell cohort examples for SNU16 show that other drugs (vincristine, dinaciclib) are more sensitive, while some drugs (IC-87114, BRD-K48477130) are more resistant.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061. These metrics are used as training diagnostics and not held-out generalization. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp

---
