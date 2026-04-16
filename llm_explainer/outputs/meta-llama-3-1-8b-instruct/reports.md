# Generated Reports - Meta-Llama-3.1-8B-Instruct

## RPT-0001 - cytarabine hydrochloride on SKMEL2
_Source evidence: SHAP-0001_

## Executive Summary
The observed AUC for cytarabine hydrochloride on SKMEL2 is 27.1820, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.5949, indicating a large positive prediction error of +13.5871.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

*   fp_0443: pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.7098.
*   fp_0504: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3425.
*   fp_0767: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2681.
*   fp_0450: pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1741.
*   fp_0864: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1686.
*   fp_1009: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1228.

These features are all fingerprint bits, which are binary descriptors of molecular structure. The presence of fp_0443 and fp_0450 suggests that the compound's molecular structure may be contributing to its lower sensitivity, while the presence of fp_0504, fp_0767, fp_0864, and fp_1009 suggests that it may be contributing to its higher resistance.

## Feature and Neighborhood Analysis
The fingerprint bits driving the prediction are all present in less than 11% of CTRPv2 compounds, indicating that they are relatively rare features. The SMARTS patterns associated with these features are:

*   fp_0443: `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`
*   fp_0504: `[#6]:[#6](=[#8]):[#7]`
*   fp_0767: `[#6]-[#7](-[#6])-[#6]`
*   fp_0450: `[#7]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]`
*   fp_0864: `[#7]=[#6]-[#6]`
*   fp_1009: `[#6]-[#6](:[#6]):[#6]`

These SMARTS patterns are representative of various molecular structures, including aromatic rings, alkyl chains, and functional groups. The example compounds provided for each feature are nilotinib, bleomycin A2, topotecan, IC-87114, erastin, Bax channel blocker, trifluoperazine, parbendazole, Repligen 136, BRD-K29313308, COL-3, mitomycin, omacetaxine mepesuccinate, PAC-1, betulinic acid

---

## RPT-0002 - birinapant on KYM1
_Source evidence: SHAP-0002_

## Executive Summary
The observed response of birinapant on KYM1 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed AUC of 0.6877 and a model-predicted AUC of 13.8762. The large negative prediction error (-13.1885) indicates that the model overestimated the sensitivity of birinapant on KYM1.

## Evidence-Based Interpretation
The top TreeSHAP features driving the prediction for birinapant on KYM1 are fingerprint bits that push the prediction toward higher AUC (relative resistance). The top features are:

* fp_0767: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3164
* fp_0504: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2344
* fp_0864: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2089
* fp_1009: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1965
* fp_0925: pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1182

In contrast, the fingerprint bit fp_0443 pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.5166.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0443 is representative of SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` and is present in 0.4% of CTRPv2 compounds. Example compounds include nilotinib and bleomycin A2. This feature is associated with a lower AUC (relative sensitivity) and may indicate a potential mechanism of resistance.

The fingerprint bit fp_0767 is representative of SMARTS `[#6]-[#7](-[#6])-[#6]` and is present in 11.0% of CTRPv2 compounds. Example compounds include Bax channel blocker, trifluoperazine, and parbendazole. This feature is associated with a higher AUC (relative resistance) and may indicate a potential mechanism of resistance.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.6648
* N-estimator tuning best row: max_depth=10, n_estimators=85, mean_r2=0.4752, std_r2=0.0113
* Top global fingerprint features: fp_0443, fp_0767, fp_0925, fp_0504, fp_0864
* Most common genes across predictable per-drug models: TNFR

---

## RPT-0003 - nilotinib on BT549
_Source evidence: SHAP-0003_

## Executive Summary
Nilotinib's observed AUC on BT549 is 23.7050, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model predicted an AUC of 13.4663, resulting in a positive prediction error of +10.2387.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2006.
* fp_0367, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1002.
* fp_0443, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0993.
* fp_0204, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0815.
* fp_0538, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0727.
* fp_0811, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0573.

## Feature and Neighborhood Analysis
The top TreeSHAP feature, TNFRSF12A (51330), is a gene expression feature that is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. This suggests that TNFRSF12A may be a relevant gene in the context of nilotinib's mechanism of action.

The fingerprint bits fp_0367, fp_0443, fp_0204, fp_0538, and fp_0811 are all representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. These patterns are associated with different types of compounds, including betulinic acid, gossypol, simvastatin, nilotinib, and bleomycin A2.

## Model-Level Context
The global model context indicates that the DEM training fit has a high R-squared value of 0.4928 and a low root mean squared error of 1.8342. However, these metrics should be treated as training diagnostics, not held-out generalization. The top global fingerprint features are fp_0443, fp_0767, and fp_0925, which are associated with resistance to various compounds.

The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), and SDC4 (6385), which are all associated with resistance to multiple compounds. The per-drug cross-validated predictability for nilotinib is relatively low, with an R2 value of 0.0227.

## Confidence and Caveats
This analysis is based on the SHAP values of the top TreeSHAP features, which explain the RF prediction rather than the underlying biology directly. The conclusions drawn from this analysis

---

## RPT-0004 - N9-isopropylolomoucine on CADOES1
_Source evidence: SHAP-0004_

## Executive Summary
N9-isopropylolomoucine on CADOES1 cell line shows an observed AUC of 0.0835, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.5703, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.6577.
* fp_0227, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0985.
* fp_0204, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0901.
* fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0887.
* fp_0538, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0829.
* fp_0504, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0438.

These features suggest that the model is predicting a relatively resistant response to N9-isopropylolomoucine on CADOES1, but the observed AUC indicates a more sensitive response.

## Feature and Neighborhood Analysis
The feature TNFRSF12A (51330) is a gene expression feature that recurs in 166 predictable-drug RF signatures and is below the cross-cell-line mean. This suggests that TNFRSF12A may be a relevant gene for predicting sensitivity to N9-isopropylolomoucine.

The fingerprint bits fp_0227, fp_0204, fp_0062, fp_0538, and fp_0504 are all present in a small percentage of CTRPv2 compounds, ranging from 0.6% to 6.7%. These features are representative of specific molecular substructures, such as aromatic rings and heterocycles, which may be relevant for predicting resistance to N9-isopropylolomoucine.

## Model-Level Context
The global model context indicates that the model has a high R2 score of 0.4928 on the training data, with a mean RMSE of 1.8342 and a correlation coefficient of 0.7061. The model was tuned using a random forest algorithm with a maximum depth of 20 and 100 estimators, resulting in an R2 score of 0.6648. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204.

The per-drug cross-validated predictability for N9-is

---

## RPT-0005 - GSK461364 on MC116
_Source evidence: SHAP-0005_

## Executive Summary
GSK461364 was tested on MC116, a B cell lymphoma cell line from haematopoietic and lymphoid tissue. The observed AUC was 17.4070, which is higher than the model-predicted AUC of 7.3230, indicating that the compound is more resistant than expected. The prediction error is +10.0840, and the compound was selected for analysis due to its large positive prediction error.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are fingerprint bits and gene expressions. The fingerprint bits `fp_0504`, `fp_0443`, `fp_1001`, and `fp_0738` all push the prediction toward lower AUC (relative sensitivity), indicating that these features are associated with reduced sensitivity to GSK461364. Gene expressions of `TNFRSF12A` and `SYTL2` also contribute to the prediction, with `TNFRSF12A` pushing the prediction toward lower AUC (relative sensitivity) and `SYTL2` pushing it toward higher AUC (relative resistance).

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* `fp_0504`: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 4.4% of CTRPv2 compounds, and associated with compounds like topotecan, IC-87114, and erastin.
* `fp_0443`: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 0.4% of CTRPv2 compounds, and associated with compounds like nilotinib and bleomycin A2.
* `fp_1001`: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 1.9% of CTRPv2 compounds, and associated with compounds like nutlin-3, austocystin D, and HLI 373.
* `fp_0738`: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 4.6% of CTRPv2 compounds, and associated with compounds like teniposide, etoposide, and SB-431542.
* `TNFRSF12A`: a gene expression that pushes the prediction toward lower AUC (relative sensitivity), below the cross-cell-line mean, and recurs in 166 predictable-drug RF signatures.
* `SYTL2`: a gene expression that pushes the prediction toward higher AUC (relative resistance), near the cross-cell-line mean, and recurs in 84 predictable-drug RF signatures.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061 (treat these as training diagnostics, not held-out generalization).
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.6648.
* N

---

## RPT-0006 - niclosamide on IALM
_Source evidence: SHAP-0006_

## Executive Summary
The observed response of niclosamide on IALM shows an exceptionally sensitive profile with an AUC of 0.9043, which is lower than the model-predicted AUC of 13.3307. This indicates a significant prediction error of -12.4264, suggesting that the model overestimates the drug's effectiveness on this cell line.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2028.
* fp_0623, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1794.
* fp_0771, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1178.
* fp_0443, a fingerprint bit feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1124.
* fp_0204, a fingerprint bit feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0885.
* fp_0062, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0551.

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

* TNFRSF12A (51330) is a gene that is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
* fp_0623 is a representative SMARTS pattern `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]` that is present in 5.8% of CTRPv2 compounds and is associated with trifluoperazine, prochlorperazine, and pifithrin-alpha.
* fp_0771 is a representative SMARTS pattern `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]` that is present in 6.4% of CTRPv2 compounds and is associated with tacedinaline, AM-580, and entinostat.
* fp_0443 is a representative SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` that is present in 0.4% of CTRPv2 compounds and is associated with nilotinib and bleomycin A2.
* fp_0204 is a representative SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]` that is present in 2.9% of CTRPv2 compounds and is associated with BRD-K26531177, NVP-BEZ235, and CD-437.
* fp_0062 is a representative SMARTS pattern `[#

---

## RPT-0007 - pitstop2 on SNU886
_Source evidence: SHAP-0007_

## Executive Summary
The observed AUC for pitstop2 on SNU886 is 23.1410, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.6419, resulting in a prediction error of +9.4991.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction of higher AUC (relative resistance) for pitstop2 on SNU886 are:

* TNFRSF12A (51330) with a SHAP value of +0.2107, indicating that higher expression of this gene pushes the prediction toward higher AUC.
* fp_0204 with a SHAP value of +0.0847, indicating that the presence of this fingerprint bit pushes the prediction toward higher AUC.
* fp_0443 with a SHAP value of +0.0738, indicating that the presence of this fingerprint bit pushes the prediction toward higher AUC.
* fp_0367 with a SHAP value of +0.0646, indicating that the presence of this fingerprint bit pushes the prediction toward higher AUC.
* fp_0227 with a SHAP value of +0.0374, indicating that the presence of this fingerprint bit pushes the prediction toward higher AUC.

## Feature and Neighborhood Analysis
The top TreeSHAP features are supported by local metadata:

* TNFRSF12A (51330) is a gene that recurs in 166 predictable-drug RF signatures and is near the cross-cell-line mean.
* fp_0204 is a fingerprint bit that represents the SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]` and is present in 2.9% of CTRPv2 compounds, with example compounds including BRD-K26531177, NVP-BEZ235, and CD-437.
* fp_0443 is a fingerprint bit that represents the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` and is present in 0.4% of CTRPv2 compounds, with example compounds including nilotinib and bleomycin A2.
* fp_0367 is a fingerprint bit that represents the SMARTS pattern `[#6]:[#6](-[#6]):[#6]` and is present in 6.4% of CTRPv2 compounds, with example compounds including betulinic acid, gossypol, and simvastatin.
* fp_0227 is a fingerprint bit that represents the SMARTS pattern `[#8]-[#6@H]` and is present in 6.7% of CTRPv2 compounds, with example compounds including Bax channel blocker, paclitaxel, and teniposide.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.

---

## RPT-0008 - trametinib on DU4475
_Source evidence: SHAP-0008_

## Executive Summary
Trametinib's observed AUC on DU4475 is 0.1282, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.4028, indicating a large negative prediction error.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:
- fp_0367, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2979.
- TNFRSF12A (51330), a gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1562.
- fp_0204, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1206.
- fp_0409, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0868.
- fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0866.
- fp_1008, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0863.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0367 is representative of SMARTS `[#6]:[#6](-[#6]):[#6]`, present in 6.4% of CTRPv2 compounds, and is associated with example drugs betulinic acid, gossypol, and simvastatin. TNFRSF12A (51330) is a gene that recurs in 166 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bit fp_0204 is representative of SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, present in 2.9% of CTRPv2 compounds, and is associated with example drugs BRD-K26531177, NVP-BEZ235, and CD-437.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061. These metrics should be treated as training diagnostics, not held-out generalization. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204. The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), SDC4 (6385), PRSS23 (11098), LAMB2 (3913), GPRC5A (9052), IKZF1 (10320), and ITGA3 (3675).

---

## RPT-0009 - docetaxel on KPNYN
_Source evidence: SHAP-0009_

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

## RPT-0010 - RITA on TE441T
_Source evidence: SHAP-0010_

## Executive Summary
The observed AUC for RITA on TE441T is 1.3692, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.5331, indicating a large negative prediction error.

## Evidence-Based Interpretation
The top TreeSHAP features driving the prediction for RITA on TE441T are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2021.
* fp_0760, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0898.
* fp_0443, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0888.
* fp_0902, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0803.
* fp_0204, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0779.
* fp_0367, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0763.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily fingerprint bits, which are representative SMARTS patterns that are present in a small percentage of compounds in the CTRPv2 dataset. These features are associated with a range of compounds, including betulinic acid, paclitaxel, and nilotinib. The gene expression feature TNFRSF12A is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

## Model-Level Context
The global model context indicates that the top fingerprint features across all models are fp_0443, fp_0767, and fp_0925. The most common genes across predictable per-drug models are TNFRSF12A, MYOF, and SDC4. The per-drug cross-validated predictability for RITA is R2=0.2078. These metrics provide context for the local evidence but should be treated as training diagnostics rather than held-out generalization.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than biology directly, and the conclusions drawn from this analysis are non-causal. The local evidence for this sample should be separated from the global model context. The observed AUC is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, indicating a large negative prediction error.

---

## RPT-0011 - GSK2636771 on SUDHL10
_Source evidence: SHAP-0011_

## Executive Summary
The observed AUC for GSK2636771 on SUDHL10 is 21.9540, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.5439, indicating a significant positive prediction error of +9.4101.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.6573.
* fp_0623, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1025.
* fp_0062, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0969.
* fp_0806, a fingerprint bit feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0864.
* fp_0443, a fingerprint bit feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0712.
* fp_0760, a fingerprint bit feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0568.

## Feature and Neighborhood Analysis
The feature TNFRSF12A (51330) is a gene expression feature that recurs in 166 predictable-drug RF signatures and is below the cross-cell-line mean. It is associated with a SHAP value of -0.6573, indicating that it pushes the prediction toward lower AUC (relative sensitivity). The fingerprint bit features fp_0623, fp_0062, fp_0806, fp_0443, and fp_0760 are all representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. They are associated with SHAP values that push the prediction toward lower AUC (relative sensitivity) or higher AUC (relative resistance).

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061, which should be treated as training diagnostics only. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204. The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), SDC4 (6385), PRSS23 (11098), LAMB2 (3913), GPRC5A (9052), IKZF1 (10320), and ITGA3 (3675). The per-drug cross-validated predictability for GSK2636771 is R2=-0.0163.

## Confidence and Caveats
This report is

---

## RPT-0012 - dabrafenib on DU4475
_Source evidence: SHAP-0012_

## Executive Summary
The observed response of dabrafenib on DU4475 cell line shows an AUC of 0.6377, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.7509, indicating a significant discrepancy between the observed and predicted response.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* TNFRSF12A (51330), a gene expression feature, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.5127.
* fp_0204, a fingerprint bit feature, pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1150.
* fp_0443, a fingerprint bit feature, pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0805.
* fp_0760, a fingerprint bit feature, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0698.
* fp_0227, a fingerprint bit feature, pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0556.
* fp_0062, a fingerprint bit feature, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0544.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily fingerprint bit features, which represent molecular substructures. These features are present in a small percentage of compounds in the CTRPv2 dataset, indicating that they may be indicative of specific molecular properties that contribute to the predicted response. The gene expression feature, TNFRSF12A, is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, suggesting its importance in predicting drug responses.

## Model-Level Context
The global model context indicates that the model has a high training R-squared value (0.4928) and a moderate training RMSE (1.8342). The top global fingerprint features are fp_0443, fp_0767, and fp_0925, which are also present in the top TreeSHAP features for this case. The most common genes across predictable per-drug models are TNFRSF12A, MYOF, and SDC4, which are also present in the top TreeSHAP features. The per-drug cross-validated predictability for dabrafenib is 0.3967, indicating a moderate level of predictability for this drug.

## Confidence and Caveats
The SHAP values provide a local explanation for the predicted response, but do not directly explain the underlying biology. The observed response of dabrafenib on DU4475 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, indicating a significant discrepancy between the observed and predicted response. The top TreeSHAP features provide insight into the molecular properties that contribute to this prediction, but the local evidence should be considered in the context of the global model diagnostics and metadata.

---

## RPT-0013 - MLN2238 on KARPAS620
_Source evidence: SHAP-0013_

## Executive Summary
MLN2238 on KARPAS620 shows an observed AUC of 18.6540, which is higher than the model-predicted AUC of 9.2450. This indicates that the compound is more resistant than the model predicted. The prediction error is +9.4090, indicating a significant discrepancy between the observed and predicted AUC.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are fingerprint bits and gene expression levels. Specifically, the presence of fp_0204, fp_0271, TNFRSF12A, fp_0806, fp_0062, and fp_0623 push the prediction toward lower AUC (relative sensitivity). These features are present in a small percentage of compounds in the CTRPv2 dataset and are associated with more sensitive profiles in other compounds.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* fp_0204: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 2.9% of CTRPv2 compounds, and associated with compounds like BRD-K26531177, NVP-BEZ235, and CD-437.
* fp_0271: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 5.0% of CTRPv2 compounds, and associated with compounds like trifluoperazine, prochlorperazine, and BRD-K94991378.
* TNFRSF12A: a gene expression level that pushes the prediction toward lower AUC (relative sensitivity), below the cross-cell-line mean, and recurs in 166 predictable-drug RF signatures.
* fp_0806: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 6.0% of CTRPv2 compounds, and associated with compounds like fluorouracil, cimetidine, and dacarbazine.
* fp_0062: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 3.7% of CTRPv2 compounds, and associated with compounds like Merck60, cytarabine hydrochloride, and VX-680.
* fp_0623: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity), present in 5.8% of CTRPv2 compounds, and associated with compounds like trifluoperazine, prochlorperazine, and pifithrin-alpha.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.6648.
* N-estimator tuning best row: max_depth=10, n_estimators=85, mean_r2=0.4752, std_r2=0.0113.
* Top global fingerprint features: fp_0443,

---

## RPT-0014 - AZD4547 on NCIH716
_Source evidence: SHAP-0014_

## Executive Summary
The observed response of AZD4547 on NCIH716 shows an exceptionally sensitive profile relative to the SHAP-predicted response and cohort baselines, with an observed AUC of 1.1299 and a model-predicted AUC of 13.2363. This indicates a significant discrepancy between the actual and predicted response, with the model overestimating the sensitivity of AZD4547 on NCIH716.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* TNFRSF12A (51330), which pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2038.
* fp_0227, fp_0468, fp_0443, fp_0204, and fp_0062, which all push the prediction toward lower AUC (relative sensitivity) with SHAP values ranging from -0.1489 to -0.0705.

These features suggest that the model is overestimating the sensitivity of AZD4547 on NCIH716 due to the presence of certain fingerprint bits and gene expression levels.

## Feature and Neighborhood Analysis
The top TreeSHAP feature, TNFRSF12A (51330), is a gene expression feature that is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. This suggests that TNFRSF12A is a common feature across many drug-cell pairs and may be a key driver of the model's prediction.

The fingerprint bits (fp_0227, fp_0468, fp_0443, fp_0204, and fp_0062) all have low prevalence across the CTRPv2 compounds, ranging from 0.4% to 6.7%. These features are representative of specific molecular substructures and are present in example compounds such as Bax channel blocker, paclitaxel, teniposide, staurosporine, StemRegenin 1, leptomycin B, nilotinib, bleomycin A2, BRD-K26531177, NVP-BEZ235, CD-437, Merck60, cytarabine hydrochloride, and VX-680.

## Model-Level Context
The global model context indicates that the DEM training fit has a high train_r2 of 0.4928 and a train_rmse of 1.8342, suggesting good fit to the training data. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204, which are all related to molecular substructures. The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), SDC4 (6385), PRSS23 (11098), LAMB2 (3913), GPRC5A (9052), IKZF1 (10320), and ITGA3 (3675).

## Confidence and Caveats
The SHAP values explain the RF

---

## RPT-0015 - LBH-589 on KARPAS620
_Source evidence: SHAP-0015_

## Executive Summary
LBH-589 on KARPAS620 shows a higher observed AUC (14.7440) compared to the model's prediction (5.4171), indicating more resistance than expected. This discrepancy is reflected in a large positive prediction error (+9.3269). The drug cohort context suggests that LBH-589 is generally less effective, with a mean AUC of 5.3007 and a sample percentile of 99.5. In contrast, the cell cohort context indicates that KARPAS620 is more resistant, with a mean AUC of 14.4543 and a sample percentile of 55.4.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_0223: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -2.4886.
*   fp_0623: another fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.7250.
*   TNFRSF12A (51330): a gene expression feature that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.6997.
*   fp_0362: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.5959.
*   fp_0053: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.5671.
*   fp_0799: a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.3937.

These features are all fingerprint bits or gene expression levels that contribute to the model's prediction of lower AUC (relative sensitivity) for LBH-589 on KARPAS620.

## Feature and Neighborhood Analysis
The fingerprint bits (fp_0223, fp_0623, fp_0362, fp_0053, and fp_0799) are all present in a small percentage of CTRPv2 compounds (1.2%, 5.8%, 3.1%, 10.0%, and 4.4%, respectively). These features are representative of specific molecular structures, as indicated by their SMARTS annotations. For example, fp_0223 is associated with the structure `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`, which is present in compounds like gossypol, cytochalasin B, and erastin.

The gene expression feature, TNFRSF12A (51330), is below the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. This suggests that TNFRSF12A may be a relevant biomarker for predicting resistance to LBH-589.

## Model-Level Context
The global model context provides some insights into the overall performance of the model. The DEM training fit diagnostics indicate a moderate level of fit (R

---

## RPT-0016 - ceranib-2 on SNU398
_Source evidence: SHAP-0016_

## Executive Summary
The observed AUC for ceranib-2 on SNU398 is 0.9898, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.0950, indicating a large negative prediction error.

## Evidence-Based Interpretation
The SHAP values indicate that the top features contributing to the prediction are:

* fp_0443, a fingerprint bit, pushing the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3525.
* TNFRSF12A (51330), a gene expression feature, pushing the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2492.
* fp_0227, a fingerprint bit, pushing the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1804.
* fp_0362, a fingerprint bit, pushing the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1707.
* fp_1009, a fingerprint bit, pushing the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1700.
* fp_0204, a fingerprint bit, pushing the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0762.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily fingerprint bits, which are representative SMARTS patterns. The SMARTS patterns for these features are:

* fp_0443: `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`
* fp_0227: `[#8]-[#6@H]`
* fp_0362: `[#8]-[#6](=[#8])-[#6]`
* fp_1009: `[#6]-[#6](:[#6]):[#6]`
* fp_0204: `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`

These SMARTS patterns are present in a small percentage of CTRPv2 compounds, indicating that they are relatively rare. The example drugs for these features are nilotinib, bleomycin A2, Bax channel blocker, paclitaxel, teniposide, staurosporine, vincristine, omacetaxine mepesuccinate, betulinic acid, isoliquiritigenin, curcumin, BRD-K26531177, NVP-BEZ235, and CD-437.

## Model-Level Context
The global model context indicates that the top fingerprint features across all models are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204. The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), SDC4 (6385), PRSS23 (11098),

---

## RPT-0017 - LBH-589 on 253JBV
_Source evidence: SHAP-0017_

## Executive Summary
LBH-589 on 253JBV was observed to be exceptionally resistant with an AUC of 20.4490, which is higher than the model-predicted AUC of 11.2021. This indicates a significant positive prediction error of +9.2469. The drug cohort baseline for LBH-589 has a mean AUC of 5.3007, and the cell cohort baseline for 253JBV has a mean AUC of 13.6723.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0223, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -1.5843.
* PLK2 (10769), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.8630.
* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.5953.
* fp_0362, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.3505.
* fp_0623, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.3048.
* fp_0902, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.2993.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0223, fp_0362, fp_0623, and fp_0902 are all representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. These patterns are associated with more sensitive compounds, indicating that their presence may contribute to reduced AUC. On the other hand, the gene expression features PLK2 and TNFRSF12A are associated with higher AUC, indicating that their presence may contribute to increased resistance.

## Model-Level Context
The global model context includes training diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061. These metrics are not held-out generalization metrics but rather training diagnostics. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204. The most common genes across predictable per-drug models are TNFRSF12A, MYOF, SDC4, PRSS23, LAMB2, GPRC5A, IKZF1, and ITGA3.

## Confidence and Caveats
This analysis is based on the SHAP explanation of the RF prediction, which explains the prediction rather than the underlying biology directly. The conclusions drawn from this analysis are non-causal and should be interpreted with caution. The local evidence for this sample should be separated

---

## RPT-0018 - foretinib on EBC1
_Source evidence: SHAP-0018_

## Executive Summary
Foretinib's observed AUC on EBC1 is 0.8572, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.9169, indicating a significant prediction error (-12.0597). This discrepancy suggests that the model may not accurately capture the underlying biology of foretinib's interaction with EBC1.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1686.
* fp_0227, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1640.
* fp_0728, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0929.
* fp_0521, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0710.
* fp_0806, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0704.
* fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0651.

These features are supported by local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, and same-drug/same-cell cohort examples.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily composed of fingerprint bits, which are representative SMARTS patterns that describe the molecular structure of compounds. These features are present in a small percentage of CTRPv2 compounds, suggesting that they may be indicative of specific molecular properties that contribute to the prediction. The gene expression feature, TNFRSF12A, is above the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, indicating its importance in predicting drug responses.

## Model-Level Context
The global model context provides insight into the overall performance of the random forest model. The DEM training fit diagnostics indicate a moderate level of fit (R2=0.4928, RMSE=1.8342, Corr=0.7061), which should be interpreted as training diagnostics rather than held-out generalization. The top global fingerprint features are primarily composed of fingerprint bits, similar to the top TreeSHAP features. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4, which are also present in the top TreeSHAP features.

## Confidence and Caveats
While the SHAP analysis provides insight into the features contributing to the prediction, it is essential to note that SHAP explains the RF prediction rather than biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other contexts. The global model diagnostics provide a general sense of the model's performance but should not be

---

## RPT-0019 - 1S,3R-RSL-3 on CAL62
_Source evidence: SHAP-0019_

## Executive Summary
The observed AUC for 1S,3R-RSL-3 on CAL62 is 18.6380, which is higher than the model-predicted AUC of 9.6448. This indicates that the compound is more resistant than the model predicted. The prediction error is +8.9932, which is a large positive value indicating a significant discrepancy between the observed and predicted AUC.

## Evidence-Based Interpretation
The top TreeSHAP features for this prediction are:

* fp_0204: pushes the prediction toward lower AUC (relative sensitivity)
* fp_0271: pushes the prediction toward lower AUC (relative sensitivity)
* TNFRSF12A (51330): pushes the prediction toward higher AUC (relative resistance)
* fp_1017: pushes the prediction toward lower AUC (relative sensitivity)
* fp_0806: pushes the prediction toward lower AUC (relative sensitivity)
* fp_0062: pushes the prediction toward lower AUC (relative sensitivity)

These features are all fingerprint bits, which are binary features that represent the presence or absence of specific substructures in the compound's molecular fingerprint. The presence of these features in the compound's fingerprint is associated with lower AUC (relative sensitivity).

## Feature and Neighborhood Analysis
The feature TNFRSF12A (51330) is a gene expression feature that pushes the prediction toward higher AUC (relative resistance). This gene is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. The other top features are fingerprint bits that are present in a small percentage of CTRPv2 compounds. These features are representative of specific substructures that are associated with lower AUC (relative sensitivity).

The same-drug cohort examples show that 1S,3R-RSL-3 is more sensitive in some cell lines (e.g. SW948, DOHH2) and more resistant in others (e.g. 253JBV, BEN). The same-cell cohort examples show that other compounds are more sensitive or resistant in CAL62, but the specific mechanisms are not clear.

## Model-Level Context
The global model context shows that the DEM training fit has a high train_r2 of 0.4928 and a low train_rmse of 1.8342. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204. The most common genes across predictable per-drug models are TNFRSF12A (51330), MYOF (26509), SDC4 (6385), PRSS23 (11098), LAMB2 (3913), GPRC5A (9052), IKZF1 (10320), and ITGA3 (3675).

Per-drug cross-validated predictability for 1S,3R-RSL-3 is R2=0.2548. Cell subtype metadata is available for anaplastic carcinoma.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly.

---

## RPT-0020 - PHA-793887 on SNU398
_Source evidence: SHAP-0020_

## Executive Summary
PHA-793887 on SNU398 shows an exceptionally sensitive response with an observed AUC of 1.5525, which is significantly lower than the model-predicted AUC of 13.5394. This large negative prediction error indicates that the model overestimates the compound's effectiveness on this cell line.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this prediction are:

*   **fp_0443**: A fingerprint bit that pushes the prediction toward higher AUC (relative resistance). This feature is present in 0.4% of CTRPv2 compounds and is representative of SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, found in compounds like nilotinib and bleomycin A2.
*   **TNFRSF12A (51330)**: A gene expression feature that pushes the prediction toward higher AUC (relative resistance). This gene is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
*   **fp_1009**: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity). This feature is present in 9.1% of CTRPv2 compounds and is representative of SMARTS `[#6]-[#6](:[#6]):[#6]`, found in compounds like betulinic acid, isoliquiritigenin, and curcumin.
*   **fp_0367**: A fingerprint bit that pushes the prediction toward higher AUC (relative resistance). This feature is present in 6.4% of CTRPv2 compounds and is representative of SMARTS `[#6]:[#6](-[#6]):[#6]`, found in compounds like betulinic acid, gossypol, and simvastatin.
*   **fp_0623**: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity). This feature is present in 5.8% of CTRPv2 compounds and is representative of SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, found in compounds like trifluoperazine, prochlorperazine, and pifithrin-alpha.
*   **fp_0062**: A fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity). This feature is present in 3.7% of CTRPv2 compounds and is representative of SMARTS `[#6]-[#6](:[#6]):[#16]`, found in compounds like Merck60, cytarabine hydrochloride, and VX-680.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that PHA-793887 is more sensitive on cell lines EOL1 and OCIAML3, but more resistant on cell lines DMS454 and KPL1. The same-cell cohort examples reveal that PHA-793887 is more sensitive compared to ceranib-2 and tosedostat, but more resistant compared to erlotinib and abiraterone

---

## RPT-0021 - KU-0063794 on SKMEL2
_Source evidence: SHAP-0021_

## Executive Summary
The observed AUC for KU-0063794 on SKMEL2 is 21.2320, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 12.2996, indicating a significant positive prediction error of +8.9324.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* fp_0202, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.4209.
* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1665.
* fp_0623, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1642.
* fp_0227, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1639.
* fp_0771, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1116.
* fp_0722, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0890.

## Feature and Neighborhood Analysis
The fingerprint bits (fp_0202, fp_0623, fp_0227, fp_0771, and fp_0722) are all present in less than 10% of CTRPv2 compounds, suggesting that they may be unique or rare features in the dataset. TNFRSF12A (51330) is a gene that recurs in 166 predictable-drug RF signatures, indicating its potential importance in the model's predictions.

The SMARTS annotations for these features suggest that they may be related to specific molecular structures or functional groups. For example, fp_0202 is associated with a representative SMARTS pattern of `[#6]:[#6](-[#8]):[#6]`, which may indicate the presence of a specific type of aromatic ring or functional group.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with an R-squared value of 0.4928 and a root mean squared error of 1.8342. The model's performance on the per-drug level is also moderate, with an R-squared value of 0.1121 for KU-0063794. The top global fingerprint features are fp_0443, fp_0767, fp_0925, fp_0504, fp_0864, fp_0723, fp_0806, and fp_0204.

## Confidence and Caveats
While the SHAP values provide insight into the features driving the prediction, it is essential to note that SHAP explains the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, and conclusions should be non-causal. Additionally, the global training diagnostics should

---

## RPT-0022 - BRD-K99006945 on JHUEM1
_Source evidence: SHAP-0022_

## Executive Summary
The observed AUC for BRD-K99006945 on JHUEM1 is 1.5813, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.5611, indicating a large negative prediction error.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

*   TNFRSF12A (51330) with a SHAP value of +0.1896, pushing the prediction toward higher AUC (relative resistance)
*   fp_0367 with a SHAP value of +0.1308, pushing the prediction toward higher AUC (relative resistance)
*   fp_0204 with a SHAP value of +0.1090, pushing the prediction toward higher AUC (relative resistance)
*   fp_0623 with a SHAP value of +0.0909, pushing the prediction toward higher AUC (relative resistance)
*   fp_0443 with a SHAP value of +0.0719, pushing the prediction toward higher AUC (relative resistance)
*   fp_0062 with a SHAP value of -0.0642, pushing the prediction toward lower AUC (relative sensitivity)

## Feature and Neighborhood Analysis
The feature descriptions are grounded in local metadata:

*   TNFRSF12A (51330) is a gene that recurs in 166 predictable-drug RF signatures and is near the cross-cell-line mean.
*   fp_0367 is a fingerprint bit representative SMARTS `[#6]:[#6](-[#6]):[#6]`, present in 6.4% of CTRPv2 compounds, and is associated with example compounds like betulinic acid, gossypol, and simvastatin.
*   fp_0204 is a fingerprint bit representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, present in 2.9% of CTRPv2 compounds, and is associated with example compounds like BRD-K26531177, NVP-BEZ235, and CD-437.
*   fp_0623 is a fingerprint bit representative SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, present in 5.8% of CTRPv2 compounds, and is associated with example compounds like trifluoperazine, prochlorperazine, and pifithrin-alpha.
*   fp_0443 is a fingerprint bit representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, present in 0.4% of CTRPv2 compounds, and is associated with example compounds like nilotinib and bleomycin A2.
*   fp_0062 is a fingerprint bit representative SMARTS `[#6]-[#6](:[#6]):[#16]`, present in 3.7% of CTRPv2 compounds, and is associated with

---

## RPT-0023 - SCH-529074 on MESSA
_Source evidence: SHAP-0023_

## Executive Summary
SCH-529074 on MESSA cell line shows an observed AUC of 22.3390, which is exceptionally resistant relative to the SHAP-predicted response and cohort baselines. The model-predicted AUC is 13.4876, indicating a significant positive prediction error of +8.8514.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this exceptional resistance include:

* fp_0443, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3470.
* TNFRSF12A (51330), a gene expression feature that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2027.
* fp_1009, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1453.
* fp_0367, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1125.
* fp_0204, a fingerprint bit that pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0686.
* fp_0062, a fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0489.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0443 is present in 0.4% of CTRPv2 compounds and is associated with representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`. It is also present in example compounds nilotinib and bleomycin A2. TNFRSF12A (51330) is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. The fingerprint bit fp_1009 is present in 9.1% of CTRPv2 compounds and is associated with representative SMARTS `[#6]-[#6](:[#6]):[#6]`. It is also present in example compounds betulinic acid, isoliquiritigenin, and curcumin.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=311258, n_features=2024, train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.6648.
* N-estimator tuning best row: max_depth=10, n_estimators=85, mean_r2=0.4752, std_r2=0.0113.
* Top global fingerprint features: fp_0443 (0.07739), fp_0767 (0.05026), fp_0925 (0.04976), fp_0504 (0.04522), fp_0864 (0.04060), fp_0723 (0.02951), fp_0806

---

## RPT-0024 - KX2-391 on SNU16
_Source evidence: SHAP-0024_

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

## RPT-0025 - ouabain on TUHR10TKB
_Source evidence: SHAP-0025_

## Executive Summary
The observed response of ouabain on TUHR10TKB shows exceptionally high resistance, with an observed AUC of 29.3500, exceeding the model-predicted AUC of 20.6181 by 8.7319. This result is significantly higher than the global mean AUC of 12.8580.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features driving this prediction toward higher AUC (relative resistance) are:

* CSF1 (gene expression), with a SHAP value of +1.0870, indicating a marked increase in resistance.
* fp_0009 (fingerprint bit), with a SHAP value of +0.9989, suggesting a representative SMARTS pattern associated with resistance.
* fp_0443 (fingerprint bit), with a SHAP value of +0.5723, indicating another representative SMARTS pattern linked to resistance.
* SDC4 (gene expression), with a SHAP value of +0.4625, showing above-average expression levels.
* COL18A1 (gene expression), with a SHAP value of +0.3655, indicating markedly above-average expression levels.
* TNFRSF12A (gene expression), with a SHAP value of +0.1918, showing above-average expression levels.

These features are all pushing the prediction toward higher AUC (relative resistance).

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

* CSF1 is a gene involved in macrophage differentiation and has been implicated in various cancers. It is markedly above the cross-cell-line mean and recurs in 13 predictable-drug RF signatures.
* fp_0009 is a fingerprint bit representing a SMARTS pattern associated with resistance. It is present in 3.3% of CTRPv2 compounds and has been observed in example compounds like IC-87114, sorafenib, and SNX-2112.
* fp_0443 is another fingerprint bit representing a SMARTS pattern linked to resistance. It is present in 0.4% of CTRPv2 compounds and has been observed in example compounds like nilotinib and bleomycin A2.
* SDC4 is a gene involved in cell adhesion and has been implicated in various cancers. It is above the cross-cell-line mean and recurs in 154 predictable-drug RF signatures.
* COL18A1 is a gene involved in collagen synthesis and has been implicated in various cancers. It is markedly above the cross-cell-line mean and recurs in 15 predictable-drug RF signatures.
* TNFRSF12A is a gene involved in cell signaling and has been implicated in various cancers. It is above the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

## Model-Level Context
The global model context provides additional information about the training fit and hyperparameter tuning:

* The DEM training fit has a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061, which are training diagnostics only.
* The max-depth tuning best row has a

---
