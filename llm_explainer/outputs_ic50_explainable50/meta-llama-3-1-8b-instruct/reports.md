# Generated Reports - Meta-Llama-3.1-8B-Instruct IC50 Explainable50

## RPT-0001 - BI-2536 on REC1
_Source evidence: SHAP-0001_

## Executive Summary
The BI-2536 compound was tested on the REC1 cell line, resulting in an observed log10(IC50) of 3.7237. The random forest (RF) model predicted a log10(IC50) of 0.2231, indicating that the compound is more resistant than expected. The prediction error is +3.5006, and the absolute error is 3.5006.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are:

* fp_0141, a fingerprint bit, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7083.
* fp_0876, another fingerprint bit, which also pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3586.
* PLEK (gene expression), which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1355.
* CD70 (gene expression), which also pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1337.
* TNFRSF12A (gene expression), which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1026.
* TRIP6 (gene expression), which also pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1010.

## Feature and Neighborhood Analysis
The feature fp_0141 is a fingerprint bit that is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. The feature fp_0876 is also a fingerprint bit that is present in 1.5% of CTRPv2 compounds and is associated with compounds such as triptolide, cucurbitacin I, and NPC-26. The gene expression features PLEK, CD70, TNFRSF12A, and TRIP6 are all associated with higher log10(IC50) (relative resistance) and are marked by their z-scores and the number of supporting drugs.

## Model-Level Context
The global model context indicates that the RF model has a training fit of n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385. These metrics are used as training diagnostics and should not be taken as held-out generalization. The model was tuned using max-depth and N-estimator tuning, with the best row being max_depth=20, n_estimators=100, r2=0.5459. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable

---

## RPT-0002 - topotecan on GOS3
_Source evidence: SHAP-0002_

## Executive Summary
The observed response of topotecan on GOS3 is exceptionally sensitive, with an observed log10(IC50) of -3.6393, which is lower than the model-predicted log10(IC50) of 1.0604. This indicates that topotecan is more effective against GOS3 than expected based on the model's prediction.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are CCN1, fp_0141, fp_0017, fp_0059, fp_0513, and fp_0535. These features all push the prediction toward higher log10(IC50), indicating relative resistance. The SHAP values for these features are +0.1032, +0.0691, +0.0475, +0.0400, +0.0185, and +0.0152, respectively.

## Feature and Neighborhood Analysis
The feature CCN1 is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. It is also present in 71 drugs in the CTRPv2 dataset. The fingerprint features fp_0141, fp_0017, fp_0059, fp_0513, and fp_0535 are all representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. For example, fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with drugs such as dexamethasone, austocystin D, and daporinad.

## Model-Level Context
The global model context indicates that the model has a good fit on the training data, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The model's performance on the per-drug level is also good, with a per-drug R2 of 0.4014 for topotecan. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
The SHAP analysis provides a local explanation for the prediction, but it is essential to note that it does not explain the underlying biology directly. The model's performance on the training data is good, but it is essential to consider the model's limitations and potential biases. The per-drug R2 of 0.4014 indicates that the model's performance on topotecan is relatively good, but it is still a relatively low value. The same-drug and same-cell cohort examples provide additional context, but they should be interpreted with caution due to the small sample size.

---

## RPT-0003 - SN-38 on PANC0504
_Source evidence: SHAP-0003_

## Executive Summary
The observed response of SN-38 on PANC0504 is exceptionally resistant relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of 3.9917 and a model-predicted log10(IC50) of -0.8168. The prediction error is +4.8085, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0329, fp_0059, fp_0240, and fp_0065, all of which are fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity).
* CCN1 (3491), a gene expression feature, pushes the prediction toward higher log10(IC50) (relative resistance).

These features suggest that the presence of certain molecular patterns and the expression level of CCN1 contribute to the exceptional resistance of PANC0504 to SN-38.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that PANC0504 is more resistant than other cells treated with SN-38, with AUC values ranging from -3.8613 to 2.6421. The same-cell cohort examples show that PANC0504 is more resistant than other cells treated with drugs that target different genes, with AUC values ranging from -2.9153 to 3.1518.

The top fingerprint features are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. For example, fp_0329 is present in 5.0% of CTRPv2 compounds and is associated with NSC23766, PD 153035, and gefitinib.

## Model-Level Context
The global model context shows that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which are training diagnostics and not held-out generalization metrics. The per-drug cross-validated predictability for SN-38 is R2=0.3278.

The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518.

## Confidence and Caveats
This analysis is based on the SHAP explanation of the RF prediction, which does not directly explain the underlying biology. The conclusions are non-causal and should be interpreted with caution. The local case evidence is specific to this sample and may not generalize to other cells or compounds. The global model context provides training diagnostics and feature importance, but should not be used to make predictions or draw conclusions about the underlying biology.

---

## RPT-0004 - selumetinib on MINO
_Source evidence: SHAP-0004_

## Executive Summary
The observed response of selumetinib on MINO cell line is exceptionally sensitive, with an observed log10(IC50) of -3.4912, which is lower than the model-predicted log10(IC50) of 0.6342. This indicates that the model underestimates the sensitivity of selumetinib on MINO.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are:

* CCN1 (3491), a gene expression feature, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2307.
* fp_0141, a fingerprint bit feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0616.
* fp_0538, a fingerprint bit feature, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0433.
* fp_0017, a fingerprint bit feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0258.
* fp_0513, a fingerprint bit feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0187.
* fp_0535, a fingerprint bit feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0176.

## Feature and Neighborhood Analysis
The feature CCN1 (3491) is a gene expression feature that is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bit features fp_0141, fp_0538, fp_0017, fp_0513, and fp_0535 are all present in less than 3% of CTRPv2 compounds and have example compounds such as dexamethasone, crizotinib, bexarotene, epigallocatechin-3-monogallate, and BRD4132, respectively.

## Model-Level Context
The global model context shows that the training fit diagnostics are: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385. These should be treated as training diagnostics, not held-out generalization. The per-drug cross-validated predictability for selumetinib is R2=0.2203. The most common genes across predictable per-drug models are MYOF (26509), TNFRSF12A (51330), SDC4 (6385), CCN1 (3491), PRSS23 (11098), WWTR1 (25937), LAMB2 (3913), and GPX8 (493869).

## Confidence and Caveats
The SHAP analysis explains the RF prediction rather than the underlying biology directly. The conclusions drawn from this analysis are based on the observed data and

---

## RPT-0005 - GSK461364 on MDAMB468
_Source evidence: SHAP-0005_

## Executive Summary
GSK461364 exhibits an exceptionally sensitive response on MDAMB468, with an observed log10(IC50) of -3.9435, which is lower than the model-predicted log10(IC50) of 0.0698. This discrepancy indicates that the model underestimates the compound's effectiveness against this cell line.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this prediction are fingerprint bits and gene expression. Specifically, the presence of fp_0059, fp_0065, and fp_0227 push the prediction toward lower log10(IC50), indicating relative sensitivity. On the other hand, CCN1 (3491) and fp_0141 push the prediction toward higher log10(IC50), indicating relative resistance. These features are consistent with the observed response, suggesting that the model's underestimation of GSK461364's effectiveness may be due to the presence of these resistance-inducing features.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* fp_0059: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 6.0% of CTRPv2 compounds, and found in example drugs CIL55, simvastatin, and lovastatin.
* fp_0065: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 2.5% of CTRPv2 compounds, and found in example drugs BI-2536, PI-103, and BRD1812.
* fp_0227: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 6.7% of CTRPv2 compounds, and found in example drugs Bax channel blocker, paclitaxel, and teniposide.
* CCN1 (3491): a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance), near the cross-cell-line mean, and recurs in 71 predictable-drug RF signatures.
* fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), present in 1.5% of CTRPv2 compounds, and found in example drugs dexamethasone, austocystin D, and daporinad.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with a train_r2 of 0.4042 and train_rmse of 1.0264. The top global fingerprint features are fp_0141, fp_0513, and fp_0535. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4. The per-drug cross-validated predictability for GSK461364 is R2=0.2482.

## Confidence and Caveats
The SHAP analysis provides a local explanation for the model's prediction, but it is essential to note that SHAP explains the RF prediction rather than the underlying

---

## RPT-0006 - barasertib on MDAMB468
_Source evidence: SHAP-0006_

## Executive Summary
The observed response of barasertib on MDAMB468 is exceptionally sensitive, with an observed log10(IC50) of -3.5277. However, the RF-predicted log10(IC50) is 1.0653, indicating a significant discrepancy between the model's prediction and the actual response. This discrepancy is reflected in the high prediction error of -4.5930.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this discrepancy are CCN1, fp_0141, fp_0017, fp_0513, fp_0723, and fp_0284. CCN1, fp_0141, fp_0017, and fp_0723 all push the prediction toward higher log10(IC50), indicating relative resistance. In contrast, fp_0284 pushes the prediction toward lower log10(IC50), indicating relative sensitivity. These features are representative SMARTS patterns and are present in a small percentage of CTRPv2 compounds.

## Feature and Neighborhood Analysis
The feature CCN1 is a gene expression feature that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bits fp_0141, fp_0017, fp_0513, and fp_0723 are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. FP_0141 is present in 1.5% of compounds and is associated with drugs such as dexamethasone, austocystin D, and daporinad. FP_0017 is present in 2.3% of compounds and is associated with drugs such as bexarotene, SR-II-138A, and CR-1-31B. FP_0513 is present in 0.8% of compounds and is associated with drugs such as epigallocatechin-3-monogallate, CAY10594, and avrainvillamide. FP_0723 is present in 6.0% of compounds and is associated with drugs such as gossypol, teniposide, and valdecoxib.

## Model-Level Context
The global model context indicates that the DEM training fit has a high train_r2 of 0.4042 and a train_rmse of 1.0264. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for barasertib is R2=0.3417.

## Confidence and Caveats
This report is based on the analysis of a single case and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local evidence presented here should

---

## RPT-0007 - dabrafenib on SIGM5
_Source evidence: SHAP-0007_

## Executive Summary
The observed response of dabrafenib on SIGM5 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.8228 and a model-predicted log10(IC50) of 0.7137. The prediction error is -4.5365, indicating that the model underestimates the sensitivity of dabrafenib on SIGM5.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2107.
* fp_0017, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0288.
* fp_0141, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0220.
* fp_0513, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0191.
* fp_0723, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0170.
* fp_0535, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0164.

These features suggest that the presence of certain molecular patterns in dabrafenib may contribute to its exceptional sensitivity on SIGM5.

## Feature and Neighborhood Analysis
The feature CCN1 (3491) is a gene expression feature that is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. This suggests that CCN1 may be a relevant biomarker for predicting sensitivity to dabrafenib.

The fingerprint bit features fp_0017, fp_0141, fp_0513, fp_0723, and fp_0535 are all present in a small percentage of CTRPv2 compounds (2.3%, 1.5%, 0.8%, 6.0%, and 1.7%, respectively). These features are representative of specific molecular patterns that may contribute to resistance to dabrafenib.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. These metrics are used as training diagnostics and should not be taken as held-out generalization metrics. The per-drug cross-validated predictability for dabrafenib is R2=0.5336.

The most common genes across predictable per-drug models are MYOF (26509), TNFRSF12A (51330), SDC4 (6385), CCN1 (3491), PRSS23 (11098), WWTR

---

## RPT-0008 - alisertib on T84
_Source evidence: SHAP-0008_

## Executive Summary
The observed response of alisertib on T84 cells is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.6782 and a model-predicted log10(IC50) of 1.0653, resulting in a prediction error of -4.7435.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, all of which push the prediction toward higher log10(IC50) or relative resistance. These features are associated with gene expression and fingerprint bits, with CCN1 being near the cross-cell-line mean and recursing in 71 predictable-drug RF signatures. The fingerprint bits are representative SMARTS patterns present in a small percentage of CTRPv2 compounds, with example compounds including dexamethasone, austocystin D, and bexarotene.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that alisertib is more sensitive in Jeko1 and OCILY3 cells, but more resistant in UACC257 and SNU869 cells. The same-cell cohort examples show that T84 cells are more sensitive to quizartinib and BRD-K28456706, but more resistant to BRD-M00053801 and AZD7545. This suggests that the response of alisertib on T84 cells is not representative of the broader cell cohort.

## Model-Level Context
The global model context shows that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which should be treated as training diagnostics rather than held-out generalization. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are also among the top features for alisertib. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly. The local evidence for this sample should be kept separate from the global model context. The conclusions drawn from this report are non-causal and based on the observed data. The per-drug cross-validated predictability for alisertib is R2=0.3285, indicating that the model's performance on this drug is moderate.

---

## RPT-0009 - GSK461364 on TE4
_Source evidence: SHAP-0009_

## Executive Summary
The observed response of GSK461364 on TE4 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.9022 and a model-predicted log10(IC50) of 0.0506. The prediction error is -3.9528, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0059, fp_0065, and fp_0227, which push the prediction toward lower log10(IC50) (relative sensitivity)
* CCN1 (3491), which pushes the prediction toward higher log10(IC50) (relative resistance)
* fp_0141, which pushes the prediction toward higher log10(IC50) (relative resistance)
* fp_0402, which pushes the prediction toward lower log10(IC50) (relative sensitivity)

These features suggest that the presence of certain molecular patterns in GSK461364 contributes to its exceptional sensitivity on TE4 cells.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which represent molecular substructures. Specifically:

* fp_0059 represents a benzene ring with a hydrogen atom attached to a carbon atom, present in 6.0% of CTRPv2 compounds.
* fp_0065 represents a larger molecular pattern involving a benzene ring and a nitrogen atom, present in 2.5% of CTRPv2 compounds.
* fp_0227 represents a benzene ring with a hydrogen atom attached to a carbon atom, present in 6.7% of CTRPv2 compounds.
* fp_0141 represents a molecular pattern involving a nitrogen atom and a benzene ring, present in 1.5% of CTRPv2 compounds.
* fp_0402 represents a molecular pattern involving a sulfur atom and a benzene ring, present in 1.2% of CTRPv2 compounds.

These features are all relatively rare in the CTRPv2 dataset, suggesting that they may be unique to GSK461364 or a small subset of compounds.

## Model-Level Context
The global model context provides additional information about the training data and model performance. The DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. The per-drug cross-validated predictability for GSK461364 is R2=0.2482. The most common genes across predictable per-drug models include CCN1 (3491), which is also a top feature in this case.

## Confidence and Caveats
This analysis is based on a single case and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local evidence presented here should be considered in the context of the global model diagnostics, which indicate a moderate level of training fit.

---

## RPT-0010 - barasertib on LCLC97TM1
_Source evidence: SHAP-0010_

## Executive Summary
The observed response of barasertib on LCLC97TM1 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.2033 and a model-predicted log10(IC50) of 1.0653. The prediction error is -4.2685, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0723, and fp_0284. CCN1, fp_0141, fp_0017, and fp_0723 all push the prediction toward higher log10(IC50), indicating relative resistance, while fp_0284 pushes the prediction toward lower log10(IC50), indicating relative sensitivity. These features are supported by local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, and prevalence across compounds.

## Feature and Neighborhood Analysis
The feature CCN1 is a gene expression feature that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. It is associated with a positive SHAP value of 0.0933, indicating that it pushes the prediction toward higher log10(IC50). The fingerprint bit features fp_0141, fp_0017, fp_0513, and fp_0723 are all representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. They are associated with positive SHAP values, indicating that they also push the prediction toward higher log10(IC50). The fingerprint bit feature fp_0284 is associated with a negative SHAP value, indicating that it pushes the prediction toward lower log10(IC50).

## Model-Level Context
The global model context includes training diagnostics, such as train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385, which should be treated as training diagnostics rather than held-out generalization. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for barasertib is R2=0.3417.

## Confidence and Caveats
This report is based on local evidence from the SHAP values and metadata, and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The conclusions drawn from this report are non-causal and should not be used to make clinical decisions.

---

## RPT-0011 - alisertib on CAOV3
_Source evidence: SHAP-0011_

## Executive Summary
The observed response of alisertib on CAOV3 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.1799 and a model-predicted log10(IC50) of 1.0653, resulting in a prediction error of -4.2452.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1129.
* fp_0141, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0817.
* fp_0017, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0547.
* fp_0723, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0183.
* fp_0513, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0170.
* fp_0535, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0128.

These features are all associated with relative resistance, indicating that the model predicts alisertib to be less effective against CAOV3 cells.

## Feature and Neighborhood Analysis
The local metadata for these features is as follows:
* CCN1 (3491) is a gene expression feature that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean.
* fp_0141 is a fingerprint bit feature that is present in 1.5% of CTRPv2 compounds and is associated with the SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, which is representative of compounds such as dexamethasone, austocystin D, and daporinad.
* fp_0017 is a fingerprint bit feature that is present in 2.3% of CTRPv2 compounds and is associated with the SMARTS pattern `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`, which is representative of compounds such as bexarotene, SR-II-138A, and CR-1-31B.
* fp_0723 is a fingerprint bit feature that is present in 6.0% of CTRPv2 compounds and is associated with the SMARTS pattern `[#6]:[#6

---

## RPT-0012 - crizotinib on CAPAN2
_Source evidence: SHAP-0012_

## Executive Summary
The crizotinib response on CAPAN2 was exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.0708 and a model-predicted log10(IC50) of 1.0604. The prediction error was -4.1312, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1361.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1019.
* fp_0673, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0696.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0387.
* fp_0059, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0362.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0170.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0017 is present in 2.3% of CTRPv2 compounds and is associated with compounds such as bexarotene, SR-II-138A, and CR-1-31B. CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bit fp_0673 is present in 17.5% of CTRPv2 compounds and is associated with compounds such as tamoxifen, procarbazine, and methotrexate.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF (26509), TNFRSF12A (51330), SDC4 (6385), CCN1 (

---

## RPT-0013 - indisulam on NCIH2081
_Source evidence: SHAP-0013_

## Executive Summary
Indisulam's response on NCIH2081 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.4710 and a model-predicted log10(IC50) of 0.7137. This discrepancy is reflected in a prediction error of -4.1846 and an absolute error of 4.1846.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2055.
* Fingerprint bits fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, which all push the prediction toward higher log10(IC50) (relative resistance) with SHAP values ranging from 0.0146 to 0.0646.

These features suggest that the model is predicting a relatively resistant response to indisulam on NCIH2081, but the observed data indicates a highly sensitive response.

## Feature and Neighborhood Analysis
The feature CCN1 (3491) is a gene expression feature that is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. This suggests that CCN1 may be a relevant biomarker for predicting sensitivity to indisulam.

The fingerprint bits fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535 are all present in a small percentage of CTRPv2 compounds (1.5%, 2.3%, 6.0%, 0.8%, and 1.7%, respectively). These features are representative of specific molecular substructures and are associated with a range of compounds, including dexamethasone, austocystin D, and gossypol.

## Model-Level Context
The global model context provides some insights into the overall performance of the model. The DEM training fit diagnostics indicate a moderate level of fit (R² = 0.4042, RMSE = 1.0264, and correlation coefficient = 0.6385). The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are all associated with a range of compounds and may be relevant for predicting sensitivity to indisulam.

The per-drug cross-validated predictability for indisulam is R² = 0.3312, indicating a moderate level of predictability for this compound. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, SDC4, CCN1, and PRSS23, which may be relevant for predicting sensitivity to indisulam.

## Confidence and Caveats
This analysis is based on a single case and should be interpreted with caution. The SHAP values provide insight into the local features driving the prediction, but do not necessarily reflect the underlying biology. The model's performance on

---

## RPT-0014 - LBH-589 on MKN45
_Source evidence: SHAP-0014_

## Executive Summary
LBH-589 was tested on MKN45 cells, resulting in an observed log10(IC50) of 3.8231. The model predicted a log10(IC50) of 1.6866, indicating that the cells were more resistant than expected. The prediction error was +2.1365, and the absolute error was 2.1365.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0017, a fingerprint bit, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3434.
* MYLK, a gene expression feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.3335.
* fp_0141, a fingerprint bit, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.2212.
* fp_0071, a fingerprint bit, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1500.
* TES, a gene expression feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1418.
* GLB1L2, a gene expression feature, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1089.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0017 is present in 2.3% of CTRPv2 compounds and is associated with compounds such as bexarotene, SR-II-138A, and CR-1-31B. This feature pushes the prediction toward lower log10(IC50), indicating that it is associated with increased sensitivity. The gene expression feature MYLK is below the cross-cell-line mean and recurs in 20 predictable-drug RF signatures, pushing the prediction toward higher log10(IC50) and indicating relative resistance. The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad, also pushing the prediction toward higher log10(IC50) and indicating relative resistance.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385. These metrics are used as training diagnostics and not held-out generalization.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp

---

## RPT-0015 - topotecan on SNU886
_Source evidence: SHAP-0015_

## Executive Summary
The observed response of topotecan on SNU886 is exceptionally sensitive, with an observed log10(IC50) of -3.1800. The model-predicted log10(IC50) is 1.0604, indicating a significant prediction error of -4.2405. This discrepancy suggests that the model underestimates the sensitivity of SNU886 to topotecan.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0059, fp_0513, fp_0723, which all push the prediction toward higher log10(IC50)/resistance. These features are associated with above-average expression levels of CCN1, presence of specific fingerprint bits, and low prevalence in the CTRPv2 compound set. The SHAP values indicate that these features contribute positively to the prediction, suggesting that they are associated with increased resistance to topotecan.

## Feature and Neighborhood Analysis
The feature CCN1 is a gene expression feature that is above the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. It has a SHAP value of +0.1032, indicating that it contributes to the prediction of higher log10(IC50)/resistance. The fingerprint bits fp_0141, fp_0017, fp_0059, fp_0513, and fp_0723 are all present in a small percentage of CTRPv2 compounds and are associated with specific SMARTS patterns. These features have SHAP values ranging from +0.0180 to +0.1032, indicating their contribution to the prediction of higher log10(IC50)/resistance.

## Model-Level Context
The global model context indicates that the model has a good fit on the training data, with a train_r2 of 0.4042 and a train_corr of 0.6385. However, these metrics should be treated as training diagnostics only. The per-drug cross-validated predictability for topotecan is R2=0.4014, indicating a moderate level of predictability. The most common genes across predictable per-drug models include CCN1, which is associated with the top TreeSHAP feature. The cell subtype metadata indicates that SNU886 is a hepatocellular carcinoma cell line.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other cell lines or compounds. The global model diagnostics provide some confidence in the model's performance, but the prediction error for this specific case is significant. Further investigation is needed to understand the underlying mechanisms driving the exceptional sensitivity of SNU886 to topotecan.

---

## RPT-0016 - SN-38 on ISTMES1
_Source evidence: SHAP-0016_

## Executive Summary
The observed log10(IC50) of SN-38 on ISTMES1 is 2.6421, which is more resistant than the model predicted (-1.0252). The prediction error is +3.6673, indicating a significant discrepancy between the observed and predicted values.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this discrepancy are fingerprint bits fp_0329, fp_0059, fp_0667, fp_0240, and fp_0065, all of which push the prediction toward lower log10(IC50) (relative sensitivity). This suggests that the presence of these features in SN-38 contributes to its observed resistance on ISTMES1.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* fp_0329: a fingerprint bit that is present in 5.0% of CTRPv2 compounds, pushing the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.5058.
* fp_0059: a fingerprint bit that is present in 6.0% of CTRPv2 compounds, pushing the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4387.
* fp_0667: a fingerprint bit that is present in 9.6% of CTRPv2 compounds, pushing the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1960.
* fp_0240: a fingerprint bit that is present in 4.0% of CTRPv2 compounds, pushing the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1855.
* fp_0065: a fingerprint bit that is present in 2.5% of CTRPv2 compounds, pushing the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1724.

Additionally, the gene expression feature CCN1 (3491) pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1229.

## Model-Level Context
The global model context indicates that the training fit has a high R2 of 0.4042 and a low RMSE of 1.0264, suggesting good fit to the training data. However, this should be treated as a training diagnostic, not a held-out generalization. The per-drug cross-validated predictability for SN-38 is R2=0.3278, indicating moderate predictability.

The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8, but none of these are directly related to the observed resistance of SN-38 on ISTMES1.

## Confidence and Caveats
This report is based on the local evidence for this sample and should not be extrapolated to other samples or contexts. The

---

## RPT-0017 - dabrafenib on SCC4
_Source evidence: SHAP-0017_

## Executive Summary
The observed response of dabrafenib on SCC4 is exceptionally sensitive, with an observed log10(IC50) of -2.6407. However, the RF-predicted log10(IC50) is 1.0653, indicating a significant discrepancy between the observed and predicted responses. The prediction error is -3.7060, suggesting that the model underestimates the sensitivity of SCC4 to dabrafenib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0017, fp_0141, fp_0513, fp_0059, fp_0723, and fp_0723. These features all push the prediction toward higher log10(IC50), indicating relative resistance. Specifically:

* CCN1 (gene_expression) has a SHAP value of +0.0903, indicating that higher expression of CCN1 contributes to increased resistance.
* fp_0017, fp_0141, fp_0513, fp_0059, and fp_0723 (fingerprint_bits) all have SHAP values between +0.0161 and +0.0903, indicating that these fingerprint features contribute to increased resistance.

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

* CCN1 is a gene that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean.
* fp_0017, fp_0141, fp_0513, fp_0059, and fp_0723 are fingerprint bits that are present in 2.3%, 1.5%, 0.8%, 6.0%, and 6.0% of CTRPv2 compounds, respectively. These features are representative of specific molecular structures and are associated with increased resistance.

## Model-Level Context
The global model context provides additional information about the training data and model performance:

* The DEM training fit has a train_r2 of 0.4042 and train_rmse of 1.0264, indicating moderate fit to the training data.
* The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518.
* The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.
* The per-drug cross-validated predictability for dabrafenib is R2=0.5336.

## Confidence and Caveats
This analysis is based on the SHAP values and local metadata, which explain the RF prediction rather than the underlying biology. The conclusions are non-causal and should not be interpreted as direct evidence of biological mechanisms. The local case evidence should be separated from the global training diagnostics, which are provided for context only.

---

## RPT-0018 - AZD7762 on MFE319
_Source evidence: SHAP-0018_

## Executive Summary
The observed response of AZD7762 on MFE319 cell line shows exceptional sensitivity, with an observed log10(IC50) of -3.4999, which is significantly lower than the model-predicted log10(IC50) of -0.3873. This discrepancy suggests that the model underestimates the actual sensitivity of AZD7762 on MFE319.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this prediction are fingerprint bits fp_0141, fp_0157, fp_0032, fp_0994, fp_0876, and fp_0071. These features all push the prediction toward lower log10(IC50), indicating that they contribute to the exceptional sensitivity of AZD7762 on MFE319. Specifically:

* fp_0141 is a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]` present in 1.5% of CTRPv2 compounds, with example drugs dexamethasone, austocystin D, and daporinad.
* fp_0157 is a representative SMARTS pattern `[#6]-[#6](-[#6])-[#7]` present in 8.9% of CTRPv2 compounds, with example drugs CIL55, BRD4132, and phloretin.
* fp_0032 is a representative SMARTS pattern `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]` present in 3.5% of CTRPv2 compounds, with example drugs SB-431542, apicidin, and MK-2206.
* fp_0994 is a representative SMARTS pattern `[#7]-[#6](:[#6]):[#6]` present in 2.3% of CTRPv2 compounds, with example drugs NSC23766, compound 1B, and BRD-K92856060.
* fp_0876 is a representative SMARTS pattern `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]` present in 1.5% of CTRPv2 compounds, with example drugs triptolide, cucurbitacin I, and NPC-26, pushing the prediction toward higher log10(IC50).
* fp_0071 is a representative SMARTS pattern `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]` present in 5.2% of CTRPv2 compounds, with example drugs N9-isopropylolomoucine, purmorphamine, and IC-87114, also pushing the prediction toward higher log10(IC50).

## Feature and Neighborhood Analysis
The same-drug cohort examples show that AZD7762 is more sensitive on MOLM13 and MDAMB453 cell lines, but more resistant on MALME3M and

---

## RPT-0019 - Ki8751 on A673
_Source evidence: SHAP-0019_

## Executive Summary
Ki8751 on A673 shows an exceptionally sensitive response with an observed log10(IC50) of -3.0652, which is significantly lower than the model-predicted log10(IC50) of 1.0543. This discrepancy is reflected in the high prediction error of -4.1195. The SHAP analysis reveals that the top features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, all of which push the prediction toward higher log10(IC50) or relative resistance.

## Evidence-Based Interpretation
The observed response of Ki8751 on A673 is characterized by a low log10(IC50) of -3.0652, indicating exceptional sensitivity. In contrast, the model-predicted log10(IC50) is 1.0543, suggesting a more resistant profile. The prediction error of -4.1195 highlights the discrepancy between the observed and predicted responses. The SHAP analysis identifies CCN1 as the top feature, pushing the prediction toward higher log10(IC50) or relative resistance. Other significant features include fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, all of which contribute to the prediction of relative resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features for Ki8751 on A673 are:

* CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0931.
* fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0856.
* fp_0017: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0566.
* fp_0723: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0189.
* fp_0513: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0189.
* fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0143.

These features are all fingerprint bits, indicating that the molecular structure of Ki8751 contributes to its predicted resistance profile. CCN1 is a gene expression feature, suggesting that the expression level of this gene may also play a role in the predicted response.

## Model-Level Context
The global model context provides insights into the overall performance of the model. The DEM training fit diagnostics indicate a moderate level of fit, with an R² of 0.4042 and a correlation coefficient of 0.6385. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are all present in the top features for Ki8751 on A673. The most common genes across predictable

---

## RPT-0020 - BI-2536 on OVCAR5
_Source evidence: SHAP-0020_

## Executive Summary
The BI-2536 compound exhibits an exceptionally sensitive response on the OVCAR5 cell line, with an observed log10(IC50) of -3.8048. The Random Forest (RF) model predicts a log10(IC50) of -0.8487, indicating a significant discrepancy between the observed and predicted responses. This discrepancy is reflected in the high prediction error of -2.9561.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are all fingerprint bits that push the prediction toward lower log10(IC50) or relative sensitivity. The top features are:

* fp_0141, fp_0876, fp_0582, fp_0059, fp_0271, and fp_0994, all of which are present in less than 6% of the CTRPv2 compounds.
These features are representative SMARTS patterns, including aromatic rings and functional groups, and are associated with sensitive responses in other compounds.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that BI-2536 is more sensitive in some cell lines (LUDLU1, F36P) and more resistant in others (JHH6, REC1). The same-cell cohort examples reveal that BI-2536 is more sensitive than triptolide and niclosamide in OVCAR5, but more resistant than BRD-K42260513 and lapatinib.

## Model-Level Context
The global model context indicates that the RF model has a moderate training fit, with an R2 of 0.4042 and a correlation coefficient of 0.6385. The per-drug cross-validated predictability for BI-2536 is R2=0.2724, indicating a moderate level of predictability. The top global fingerprint features are fp_0141, fp_0513, and fp_0535, which are associated with sensitive responses in other compounds.

## Confidence and Caveats
This analysis is based on the RF model's prediction and TreeSHAP feature importance, which explains the prediction rather than the underlying biology. The SHAP values indicate the contribution of each feature to the prediction, but do not imply causality. The local evidence for this sample should be considered in the context of the global model diagnostics, which indicate a moderate level of training fit and predictability.

---

## RPT-0021 - etoposide on CAL62
_Source evidence: SHAP-0021_

## Executive Summary
Etoposide's observed log10(IC50) on CAL62 is -3.3349, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted log10(IC50) is 0.3324, indicating a significant prediction error of -3.6673.

## Evidence-Based Interpretation
The top TreeSHAP features driving this prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.6198.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1918.
* fp_0994, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1199.
* fp_0876, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0684.
* fp_0582, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0559.
* fp_0071, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0507.

## Feature and Neighborhood Analysis
The fingerprint bits driving the prediction are mostly related to molecular structure, with SMARTS patterns indicating aromatic rings and functional groups. The presence of fp_0141, a fingerprint bit present in 1.5% of CTRPv2 compounds, suggests that etoposide's molecular structure may be contributing to its sensitivity on CAL62. In contrast, the presence of fp_0535, a fingerprint bit present in 1.7% of CTRPv2 compounds, suggests that etoposide's molecular structure may also be contributing to its resistance on CAL62.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The top global fingerprint features are fp_0141, fp_0513, and fp_0535, which are all related to molecular structure. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4, which are not directly related to the target gene TOP2A. The per-drug cross-validated predictability for etoposide is R2=0.3081, indicating a moderate level of predictability.

## Confidence and Caveats
This analysis is based on the SHAP values of the top TreeSHAP features driving the prediction, which explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other cells or drugs. The global model context provides some insight into the model's performance, but should not be taken as

---

## RPT-0022 - GDC-0879 on SKM1
_Source evidence: SHAP-0022_

## Executive Summary
GDC-0879 on SKM1 shows an exceptionally sensitive response relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -2.8138 and a model-predicted log10(IC50) of 0.7137. The prediction error is -3.5275, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2121.
* fp_0141, fp_0015, fp_0017, fp_0513, fp_0723, which all push the prediction toward higher log10(IC50) (relative resistance) with SHAP values of 0.0424, 0.0331, 0.0290, 0.0200, and 0.0172, respectively.

These features suggest that the presence of CCN1 and the absence of the fingerprint bits fp_0141, fp_0015, fp_0017, fp_0513, and fp_0723 contribute to the exceptionally sensitive response of GDC-0879 on SKM1.

## Feature and Neighborhood Analysis
Metadata-backed support for these features includes:

* CCN1 is a gene that recurs in 71 predictable-drug RF signatures and has a below-average expression level in SKM1.
* The fingerprint bits fp_0141, fp_0015, fp_0017, fp_0513, and fp_0723 are present in 1.5%, 18.9%, 2.3%, 0.8%, and 6.0% of CTRPv2 compounds, respectively, and have been associated with resistance to various compounds in the same-drug and same-cell cohorts.

## Model-Level Context
The global model context includes:

* A DEM training fit with n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385, which should be treated as training diagnostics only.
* The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518.
* The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.
* Per-drug cross-validated predictability for GDC-0879 is R2=0.2515.

## Confidence and Caveats
This analysis is based on the SHAP explanation of the RF prediction, which should not be taken as a direct explanation of the biological mechanisms underlying the response of GDC-0879 on SKM1. The conclusions drawn from this analysis are specific to this particular case and

---

## RPT-0023 - teniposide on SNU878
_Source evidence: SHAP-0023_

## Executive Summary
The observed response of teniposide on SNU878 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.7618 and a model-predicted log10(IC50) of -0.0907. The prediction error is -3.6711, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7211
*   fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1521
*   fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1204
*   fp_0423: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0772
*   fp_0110: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558
*   CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0440

These features indicate that the presence of certain molecular patterns in teniposide contributes to its exceptional sensitivity on SNU878.

## Feature and Neighborhood Analysis
The fingerprint bit features (fp_0141, fp_0535, fp_0994, fp_0423, and fp_0110) are all present in less than 3.2% of CTRPv2 compounds, suggesting that they are relatively rare molecular patterns. The SMARTS annotations for these features provide insight into their chemical structure:

*   fp_0141: representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`
*   fp_0535: representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`
*   fp_0994: representative SMARTS `[#7]-[#6](:[#6]):[#6]`
*   fp_0423: representative SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`
*   fp_0110: representative SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`

The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures, indicating its potential importance in predicting drug responses.

## Model-Level Context
The global model context provides information on the training fit and tuning:

*   DEM training fit: n_samples=181811

---

## RPT-0024 - PD318088 on CHP212
_Source evidence: SHAP-0024_

## Executive Summary
The observed response of PD318088 on CHP212 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -2.9343 and a model-predicted log10(IC50) of 0.9380. The prediction error is -3.8723, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0235, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1077.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0805.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0595.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0407.
* fp_0726, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0236.
* fp_0059, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0188.

## Feature and Neighborhood Analysis
The feature fp_0235 is a representative SMARTS pattern `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]` present in 4.0% of CTRPv2 compounds, with example compounds including blebbistatin, pifithrin-alpha, and ML162. CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bits fp_0141, fp_0017, fp_0726, and fp_0059 are representative SMARTS patterns present in 1.5%, 2.3%, 84.2%, and 6.0% of CTRPv2 compounds, respectively, with example compounds including dexamethasone, austocystin D, daporinad, bexarotene, SR-II-138A, CR-1-31B, CIL55, simvastatin, and lovastatin.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=

---

## RPT-0025 - 1S,3R-RSL-3 on LS1034
_Source evidence: SHAP-0025_

## Executive Summary
The observed response of 1S,3R-RSL-3 on LS1034 is exceptionally resistant relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of 3.4227 and a model-predicted log10(IC50) of 0.5075. The prediction error is +2.9152, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7781.
* fp_0876, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1567.
* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0985.
* fp_0518, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0942.
* fp_0582, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0825.
* NQO1 (1728), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0733.

These features suggest that the combination of fingerprint bits and gene expression levels in 1S,3R-RSL-3 contributes to its exceptionally resistant response on LS1034.

## Feature and Neighborhood Analysis
The same-drug cohort examples show varying responses across different cell lines, with some cells being more sensitive (e.g., MHHCALL3, NOMO1) and others being more resistant (e.g., A2058, COLO800). The same-cell cohort examples also show varying responses across different drugs, with some drugs being more sensitive (e.g., CD-1530, LY-2183240) and others being more resistant (e.g., sirolimus, pevonedistat).

## Model-Level Context
The global model context shows that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which are training diagnostics and not held-out generalization metrics. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly. The local

---

## RPT-0026 - teniposide on CAL29
_Source evidence: SHAP-0026_

## Executive Summary
The observed response of teniposide on CAL29 is characterized by an observed log10(IC50) of -0.0258, which is close to the model-predicted log10(IC50) of -0.0472 and the local drug/cell cohort baselines. The prediction error is +0.0214, indicating that the model underestimates the actual sensitivity of teniposide on CAL29.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7185.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1552.
* fp_0994, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1203.
* fp_0423, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0767.
* fp_0110, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558.
* fp_0876, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0495.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which are binary features that represent the presence or absence of specific substructures in the molecular fingerprint of the compound. These features are:

* fp_0141: represents the presence of a specific substructure, present in 1.5% of CTRPv2 compounds, and is associated with lower log10(IC50) (relative sensitivity).
* fp_0535: represents the presence of a specific substructure, present in 1.7% of CTRPv2 compounds, and is associated with higher log10(IC50) (relative resistance).
* fp_0994: represents the presence of a specific substructure, present in 2.3% of CTRPv2 compounds, and is associated with lower log10(IC50) (relative sensitivity).
* fp_0423: represents the presence of a specific substructure, present in 3.1% of CTRPv2 compounds, and is associated with lower log10(IC50) (relative sensitivity).
* fp_0110: represents the presence of a specific substructure, present in 1.7% of CTRPv2 compounds, and is associated with lower log10(IC50) (relative sensitivity).
* fp_0876: represents the presence of a specific substructure, present in 1.5% of CTRPv2 compounds, and is associated with higher log10(IC50) (relative resistance).

## Model-Level Context
The global model context is characterized by:

* DEM training fit diagnostics

---

## RPT-0027 - KPT185 on SH4
_Source evidence: SHAP-0027_

## Executive Summary
KPT185, an inhibitor of exportin 1, was tested on cell line SH4. The observed log10(IC50) was 0.3890, close to the model-predicted log10(IC50) of 0.3960 and the cohort baselines. The prediction error was -0.0070, indicating that the model slightly underestimated the compound's potency.

## Evidence-Based Interpretation
The top TreeSHAP features for KPT185 on SH4 include:

* fp_0017, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.4674.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.1894.
* fp_0071, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.1601.
* fp_0284, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.1335.
* CCN1, a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0658.
* fp_0673, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0548.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0017 and fp_0141 have the largest absolute SHAP values, indicating that they have the most influence on the prediction. Fingerprint bit fp_0017 is present in 2.3% of CTRPv2 compounds and is associated with compounds such as bexarotene, SR-II-138A, and CR-1-31B. Fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. Gene expression feature CCN1 is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models

---

## RPT-0028 - PRIMA-1 on SUDHL10
_Source evidence: SHAP-0028_

## Executive Summary
PRIMA-1, a re-activator of the pro-apoptotic activity of mutant p53, was tested on SUDHL10, a diffuse large B cell lymphoma cell line. The observed log10(IC50) was 0.7151, close to the model-predicted log10(IC50) of 0.7137. The prediction error was +0.0014, indicating a slight overestimation by the model.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are CCN1 (gene_expression), which pushes the prediction toward lower log10(IC50) (relative sensitivity), and several fingerprint bits (fp_0017, fp_0141, fp_0513, fp_0535, fp_0723), which push the prediction toward higher log10(IC50) (relative resistance). These features suggest that CCN1's expression level may contribute to PRIMA-1's sensitivity in SUDHL10, while the fingerprint bits may indicate resistance mechanisms.

## Feature and Neighborhood Analysis
CCN1 is a gene involved in cell adhesion and migration, and its expression is below the cross-cell-line mean. It recurs in 71 predictable-drug RF signatures, indicating its potential role in drug response. The fingerprint bits (fp_0017, fp_0141, fp_0513, fp_0535, fp_0723) are present in a small percentage of CTRPv2 compounds (2.3%, 1.5%, 0.8%, 1.7%, and 6.0%, respectively) and are associated with various compounds, including bexarotene, dexamethasone, epigallocatechin-3-monogallate, BRD4132, and gossypol.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which should be treated as training diagnostics. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for PRIMA-1 is R2=0.3234.

## Confidence and Caveats
This analysis is based on the TreeSHAP feature importance and should not be taken as a causal explanation of the biological mechanisms underlying PRIMA-1's activity. The SHAP values explain the RF prediction rather than the underlying biology. The local evidence for this sample should be separated from the global model context. The conclusions drawn from this analysis are specific to this case and may not generalize to other cell lines or compounds.

---

## RPT-0029 - PRIMA-1 on A204
_Source evidence: SHAP-0029_

## Executive Summary
PRIMA-1 was tested on A204 cells, resulting in an observed log10(IC50) of 1.0627. The Random Forest (RF) model predicted a log10(IC50) of 1.0653, indicating that the compound is close to the model's prediction and cohort baselines.

## Evidence-Based Interpretation
The TreeSHAP analysis identified six top features that contributed to the prediction. All six features are fingerprint bits that push the prediction toward higher log10(IC50), indicating relative resistance. These features are:
- CCN1 (3491), a gene expression feature, with a SHAP value of +0.0900
- fp_0017, a fingerprint bit, with a SHAP value of +0.0501
- fp_0141, a fingerprint bit, with a SHAP value of +0.0406
- fp_0513, a fingerprint bit, with a SHAP value of +0.0191
- fp_0535, a fingerprint bit, with a SHAP value of +0.0165
- fp_0059, a fingerprint bit, with a SHAP value of +0.0152

## Feature and Neighborhood Analysis
The top features are all fingerprint bits, which are representative SMARTS patterns. The SMARTS patterns are:
- fp_0017: `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`
- fp_0141: `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`
- fp_0513: `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`
- fp_0535: `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`
- fp_0059: `[#6]=[#6]-[#6@H]`

These SMARTS patterns are present in a small percentage of compounds in the CTRPv2 dataset, ranging from 0.8% to 6.0%. The example compounds for each SMARTS pattern include:
- fp_0017: bexarotene, SR-II-138A, CR-1-31B
- fp_0141: dexamethasone, austocystin D, daporinad
- fp_0513: epigallocatechin-3-monogallate, CAY10594, avrainvillamide
- fp_0535: BRD4132, BRD6340, parbendazole
- fp_0059: CIL55, simvastatin, lovastatin

## Model-Level Context
The global model context includes training diagnostics, which should be treated as training diagnostics only.

---

## RPT-0030 - Compound 7d-cis on JVM3
_Source evidence: SHAP-0030_

## Executive Summary
Compound 7d-cis was tested on JVM3, a cell line from the haematopoietic and lymphoid tissue, with a subtype of chronic lymphocytic leukaemia; small lymphocytic lymphoma. The observed log10(IC50) was 0.7573, which is close to the model-predicted log10(IC50) of 0.7676 and the local drug/cell cohort baselines.

## Evidence-Based Interpretation
The TreeSHAP analysis identified six key features that contributed to the prediction. The top feature, fp_0017, is a fingerprint bit that pushes the prediction toward lower log10(IC50), indicating relative sensitivity. CCN1 (3491) is another gene expression feature that also pushes the prediction toward lower log10(IC50). In contrast, four fingerprint bits (fp_0673, fp_0688, fp_0141, and fp_0771) push the prediction toward higher log10(IC50), indicating relative resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP feature, fp_0017, is a fingerprint bit present in 2.3% of CTRPv2 compounds. It is representative of SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]` and has example compounds such as bexarotene, SR-II-138A, and CR-1-31B. CCN1 (3491) is a gene expression feature that recurs in 71 predictable-drug RF signatures and is below the cross-cell-line mean. The other fingerprint bits (fp_0673, fp_0688, fp_0141, and fp_0771) are present in 17.5%, 3.1%, 1.5%, and 6.4% of CTRPv2 compounds, respectively, and have example compounds such as tamoxifen, gefitinib, and tacedinaline.

## Model-Level Context
The global model context shows that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which are training diagnostics and not held-out generalization metrics. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for Compound 7d-cis is R2=0.2832.

## Confidence and Caveats
The SHAP analysis explains the RF prediction rather than the underlying biology directly. The conclusions drawn from this report

---

## RPT-0031 - NVP-BSK805 on FU97
_Source evidence: SHAP-0031_

## Executive Summary
The observed response of NVP-BSK805 on FU97 cell line shows a log10(IC50) of 0.6578, which is close to the model's predicted log10(IC50) of 0.6386 and the local drug/cell cohort baselines. The prediction error is +0.0192, indicating that the model slightly overestimated the compound's potency.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), a gene expression feature, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2377.
* fp_0017, a fingerprint bit feature, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1367.
* fp_0673, a fingerprint bit feature, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0823.
* fp_0538, a fingerprint bit feature, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0409.
* fp_0535, a fingerprint bit feature, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0177.
* fp_0513, a fingerprint bit feature, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0172.

## Feature and Neighborhood Analysis
The feature CCN1 (3491) is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bit features fp_0017, fp_0673, fp_0538, fp_0535, and fp_0513 are all present in a small percentage of CTRPv2 compounds, with example compounds including bexarotene, tamoxifen, and epigallocatechin-3-monogallate.

## Model-Level Context
The global model context shows that the model has a high train_r2 of 0.4042 and a train_corr of 0.6385, indicating good fit to the training data. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, and PRSS23. The per-drug cross-validated predictability for NVP-BSK805 is R2=0.2469.

## Confidence and Caveats
This report is based on the local evidence for this sample and should be interpreted with caution. SHAP explains the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The model's performance on held-out data is not evaluated here, and the results should be validated with additional experiments.

---

## RPT-0032 - KW-2449 on F36P
_Source evidence: SHAP-0032_

## Executive Summary
KW-2449 on F36P has an observed log10(IC50) of 0.7418, which is close to the model's predicted log10(IC50) of 0.7676 and the cohort baselines. The prediction error is -0.0258, indicating that the model underestimates the compound's IC50.

## Evidence-Based Interpretation
The top TreeSHAP features for KW-2449 on F36P are:

* fp_0017: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1875.
* CCN1 (3491): a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1069.
* fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0918.
* fp_0673: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0885.
* fp_0518: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0404.
* fp_0688: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0296.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily fingerprint bits, which are indicative of the compound's molecular structure. The presence of fp_0017 and fp_0518 suggests that KW-2449 may have a sensitive profile on F36P, while the presence of fp_0141, fp_0673, and fp_0688 suggests that it may have a resistant profile. CCN1 (3491) is a gene expression feature that is below the cross-cell-line mean, suggesting that it may also contribute to the compound's sensitive profile.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The per-drug cross-validated predictability for KW-2449 is 0.3149, indicating that the model has a moderate level of predictability for this compound. The most common genes across predictable per-drug models include CCN1 (3491), which is also present in the top TreeSHAP features for KW-2449 on F36P.

## Confidence and Caveats
The SHAP values provide a local explanation for the model's prediction, but it is essential to note that they do not explain the underlying biology directly. The model's performance on held-out data is not evaluated here, and the training diagnostics should be treated as such. The same-drug and same-cell cohort examples provide additional context, but they should be interpreted with caution. The conclusions drawn from this report are based on the available data and should be validated through

---

## RPT-0033 - nutlin-3 on NCIH23
_Source evidence: SHAP-0033_

## Executive Summary
The nutlin-3 compound was tested on the NCIH23 cell line, resulting in an observed log10(IC50) of 1.0580. The random forest (RF) model predicted a log10(IC50) of 1.0653, indicating that the compound is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The RF model's prediction for nutlin-3 on NCIH23 is influenced by several features, as revealed by TreeSHAP analysis. The top features pushing the prediction toward higher log10(IC50) (relative resistance) are:

* CCN1 (3491) with a SHAP value of +0.0955, indicating that higher expression of CCN1 is associated with increased resistance to nutlin-3.
* fp_0141, fp_0017, fp_0513, fp_0535, fp_0723, which are all fingerprint bits with SHAP values ranging from +0.0162 to +0.0621, indicating that these molecular features are associated with increased resistance to nutlin-3.

These features are supported by local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, and same-drug/same-cell cohort examples.

## Feature and Neighborhood Analysis
The top TreeSHAP features for nutlin-3 on NCIH23 are primarily fingerprint bits, which are molecular features that describe the chemical structure of the compound. These features are associated with increased resistance to nutlin-3. The CCN1 gene is also a significant feature, indicating that higher expression of this gene is associated with increased resistance to nutlin-3.

The same-drug cohort examples show that nutlin-3 is more resistant in some cell lines (e.g., SKMEL28, SNB75) and more sensitive in others (e.g., MELHO, NCIH1581). The same-cell cohort examples show that other compounds (e.g., docetaxel, methotrexate) are more sensitive in NCIH23, while others (e.g., RAF265, bendamustine) are more resistant.

## Model-Level Context
The global model context provides information on the training fit, tuning, and feature importance. The DEM training fit shows a moderate R-squared value of 0.4042 and a correlation coefficient of 0.6385. The max-depth and N-estimator tuning results indicate that the optimal model parameters are max_depth=20 and n_estimators=100. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are all associated with increased resistance to nutlin-3. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
The SHAP analysis provides a local explanation of the RF model's prediction for nutlin-3 on NCIH23, but it is

---

## RPT-0034 - vorinostat on YAPC
_Source evidence: SHAP-0034_

## Executive Summary
The observed response of vorinostat on YAPC shows a log10(IC50) of 1.0550, which is close to the model-predicted log10(IC50) of 1.0653. The prediction error is -0.0103, indicating that the model slightly overestimated the IC50. The per-drug cross-validated R2 for vorinostat is 0.2918, indicating moderate predictability.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0723, and fp_0059. These features all push the prediction toward higher log10(IC50) or relative resistance. CCN1 has the largest SHAP value at +0.0899, indicating that it has the greatest impact on the prediction. The presence of these features suggests that the model is using a combination of gene expression and fingerprint information to predict the IC50 of vorinostat on YAPC.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* CCN1 (3491): gene_expression, pushes the prediction toward higher log10(IC50), SHAP=+0.0899, abs_SHAP=0.0899, value=5.5028, z=+0.07, supporting_drugs=71, note=near the cross-cell-line mean; recurs in 71 predictable-drug RF signatures
* fp_0141: fingerprint_bit, pushes the prediction toward higher log10(IC50), SHAP=+0.0766, abs_SHAP=0.0766, value=0.0000, pct_drugs=1.5, SMARTS=[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7], example_drugs=dexamethasone, austocystin D, daporinad
* fp_0017: fingerprint_bit, pushes the prediction toward higher log10(IC50), SHAP=+0.0493, abs_SHAP=0.0493, value=0.0000, pct_drugs=2.3, SMARTS=[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6], example_drugs=bexarotene, SR-II-138A, CR-1-31B
* fp_0513: fingerprint_bit, pushes the prediction toward higher log10(IC50), SHAP=+0.0185, abs_SHAP=0.0185, value=0.0000, pct_drugs=0.8, SMARTS=[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8], example_drugs=epigallocatechin-3-monogallate, C

---

## RPT-0035 - JQ-1 on SKMEL24
_Source evidence: SHAP-0035_

## Executive Summary
The observed log10(IC50) of JQ-1 on SKMEL24 is 1.0831, which is close to the model-predicted log10(IC50) of 1.0653 and the local drug/cell cohort baselines. The prediction error is +0.0178, indicating that the model's prediction is slightly higher than the observed value.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0535, fp_0723, which all push the prediction toward higher log10(IC50)/resistance. These features are associated with gene expression and fingerprint bits, and are present in a significant number of compounds in the CTRPv2 dataset.

## Feature and Neighborhood Analysis
The top TreeSHAP feature, CCN1, is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bits fp_0141, fp_0017, fp_0513, fp_0535, and fp_0723 are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds. These features are associated with a range of compounds, including dexamethasone, austocystin D, and gossypol.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with an R² of 0.4042 and a correlation coefficient of 0.6385. The per-drug cross-validated predictability for JQ-1 is 0.2458, indicating that the model is moderately predictable for this compound. The most common genes across predictable per-drug models include CCN1, which is associated with 71 drugs.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other contexts. The global model diagnostics, such as train_r2 and train_rmse, should be treated as training diagnostics rather than held-out generalization metrics.

---

## RPT-0036 - GDC-0879 on SNU61
_Source evidence: SHAP-0036_

## Executive Summary
GDC-0879 was tested on SNU61 cells, resulting in an observed log10(IC50) of 1.0741. The random forest model predicted a log10(IC50) of 1.0369, indicating that the observed response is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0059, fp_0513, fp_0723, and their positive SHAP values indicate that they push the prediction toward higher log10(IC50) or relative resistance. These features are associated with gene expression and fingerprint bits, and are present in a significant number of compounds in the CTRPv2 dataset.

## Feature and Neighborhood Analysis
CCN1 is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. It has a SHAP value of +0.0662, indicating that it contributes to the prediction of higher log10(IC50). Fingerprint bits fp_0141, fp_0017, fp_0059, fp_0513, and fp_0723 are also significant features, with SHAP values ranging from +0.0188 to +0.0662. These features are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds, including dexamethasone, austocystin D, daporinad, bexarotene, SR-II-138A, CR-1-31B, CIL55, simvastatin, lovastatin, epigallocatechin-3-monogallate, CAY10594, avrainvillamide, gossypol, teniposide, and valdecoxib.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. These metrics are used as training diagnostics and should not be taken as held-out generalization. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for GDC-0879 is R2=0.2515.

## Confidence and Caveats
This report is based on the analysis of a single case and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The conclusions drawn from this report are non-causal and should not be taken as evidence of a causal relationship between the features and the response.

---

## RPT-0037 - NVP-BSK805 on 253JBV
_Source evidence: SHAP-0037_

## Executive Summary
NVP-BSK805, an inhibitor of Janus kinase 2 (JAK2), was tested on the 253JBV cell line. The observed log10(IC50) was 1.0458, which is close to the model's predicted log10(IC50) of 1.0604 and the cohort baselines. The prediction error is -0.0147, indicating that the model slightly underpredicted the observed IC50.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are fingerprint bits and gene expression levels. Fingerprint bit fp_0017 pushes the prediction toward higher log10(IC50) (relative resistance), while fp_0673 pushes the prediction toward lower log10(IC50) (relative sensitivity). Gene expression levels of CCN1 also contribute to higher log10(IC50) (relative resistance). These features are consistent with the observed behavior of NVP-BSK805 on the 253JBV cell line.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* fp_0017: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1424. This feature is present in 2.3% of CTRPv2 compounds and is representative of SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`. Example compounds include bexarotene, SR-II-138A, and CR-1-31B.
* CCN1 (3491): a gene expression level that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1023. This gene is above the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.
* fp_0673: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0755. This feature is present in 17.5% of CTRPv2 compounds and is representative of SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`. Example compounds include tamoxifen, procarbazine, and methotrexate.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385. These metrics are used as training diagnostics and not held-out generalization metrics.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.003

---

## RPT-0038 - SN-38 on HCC1500
_Source evidence: SHAP-0038_

## Executive Summary
The observed response of SN-38 on HCC1500 shows a predicted log10(IC50) of -0.9158, which is close to the model prediction and cohort baselines. The observed log10(IC50) is -1.0253, indicating a relatively sensitive response. The prediction error is -0.1095, and the absolute error is 0.1095.

## Evidence-Based Interpretation
The top TreeSHAP features pushing the prediction toward lower log10(IC50) (relative sensitivity) are:

* fp_0329: a fingerprint bit with a value of 1.0000, present in 5.0% of CTRPv2 compounds, and representative SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`, found in example drugs NSC23766, PD 153035, and gefitinib.
* fp_0059: a fingerprint bit with a value of 1.0000, present in 6.0% of CTRPv2 compounds, and representative SMARTS `[#6]=[#6]-[#6@H]`, found in example drugs CIL55, simvastatin, and lovastatin.
* fp_0240: a fingerprint bit with a value of 1.0000, present in 4.0% of CTRPv2 compounds, and representative SMARTS `[#6]:[#6](-[#8]-[#6](:[#6]):[#6]):[#6]`, found in example drugs cytochalasin B, BRD-A94377914, and CIL41.
* fp_0065: a fingerprint bit with a value of 1.0000, present in 2.5% of CTRPv2 compounds, and representative SMARTS `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]`, found in example drugs BI-2536, PI-103, and BRD1812.
* fp_0667: a fingerprint bit with a value of 1.0000, present in 9.6% of CTRPv2 compounds, and representative SMARTS `[#7]-[#6]-[#6]`, found in example drugs CIL55, BRD4132, and cimetidine.

The top TreeSHAP feature pushing the prediction toward higher log10(IC50) (relative resistance) is:

* CCN1 (3491): a gene expression feature with a value of 4.8499, near the cross-cell-line mean, and recurs in 71 predictable-drug RF signatures.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that SN-38 is more sensitive in cell lines SNUC1 and HEC50B, and more resistant in cell lines ISTMES1 and PANC0504. The same-cell cohort examples show that SN-38 is more sensitive in combination with oligomycin A, dinaciclib, and more resistant in combination with Ki8751 and tamoxifen.

##

---

## RPT-0039 - apicidin on T84
_Source evidence: SHAP-0039_

## Executive Summary
Apicidin, an inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8, was tested on T84 cells. The observed log10(IC50) was 0.0286, which is close to the model prediction of 0.0160 and the cohort baselines. The prediction error is +0.0127, indicating that the model slightly overestimated the sensitivity of apicidin on T84 cells.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7593.
* fp_0876, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4527.
* fp_0271, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0905.
* fp_0582, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0471.
* fp_0617, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0455.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0448.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0141 and fp_0876 are present in 1.5% of CTRPv2 compounds and are associated with relative sensitivity. The fingerprint bits fp_0271 and fp_0617 are present in 5.0% and 0.8% of CTRPv2 compounds, respectively, and are associated with relative resistance. The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context shows that the training fit diagnostics are train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385. The per-drug cross-validated predictability for apicidin is R2=0.3700. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
This report is based on the SHAP values of the top features contributing to the prediction. However, SHAP explains the RF prediction rather than the underlying biology directly. The local

---

## RPT-0040 - indisulam on DANG
_Source evidence: SHAP-0040_

## Executive Summary
Indisulam's effect on DANG cells is predicted to be close to the model's prediction and cohort baselines, with an observed log10(IC50) of 1.0635 and a model-predicted log10(IC50) of 1.0653. The prediction error is -0.0017, indicating a slight underestimation by the model.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0059, fp_0513, fp_0723, and their positive SHAP values indicate that they push the prediction toward higher log10(IC50) or relative resistance. These features are associated with gene expression and fingerprint bits, which are representative SMARTS patterns present in a small percentage of compounds in the CTRPv2 dataset.

## Feature and Neighborhood Analysis
CCN1 is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. It has a SHAP value of +0.0881, indicating that it contributes to the prediction of higher log10(IC50) or relative resistance. Fingerprint bits fp_0141, fp_0017, fp_0059, fp_0513, and fp_0723 are representative SMARTS patterns present in a small percentage of compounds in the CTRPv2 dataset. They have SHAP values ranging from +0.0171 to +0.0881, indicating that they also contribute to the prediction of higher log10(IC50) or relative resistance.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, which should be treated as training diagnostics rather than held-out generalization. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for indisulam is R2=0.3312.

## Confidence and Caveats
This report is based on the analysis of a single case, RPT-0040, and should not be generalized to other cases without further evidence. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The conclusions drawn from this report are non-causal and should not be used to make clinical decisions.

---

## RPT-0041 - selumetinib on NCIH2009
_Source evidence: SHAP-0041_

## Executive Summary
The observed response of selumetinib on NCIH2009 is characterized by an observed log10(IC50) of 1.0805, which is close to the model-predicted log10(IC50) of 1.0604 and the local drug/cell cohort baselines. The prediction error is +0.0201, indicating that the model slightly overestimates the sensitivity of NCIH2009 to selumetinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0992.
* fp_0141, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0766.
* fp_0017, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0486.
* fp_0059, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0188.
* fp_0513, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0183.
* fp_0723, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0174.

These features suggest that the model is predicting relative resistance to selumetinib in NCIH2009 due to the presence of these molecular characteristics.

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

* CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and has a near-average expression level across cell lines.
* fp_0141 is a fingerprint bit feature present in 1.5% of CTRPv2 compounds, with example compounds including dexamethasone, austocystin D, and daporinad.
* fp_0017 is a fingerprint bit feature present in 2.3% of CTRPv2 compounds, with example compounds including bexarotene, SR-II-138A, and CR-1-31B.
* fp_0059 is a fingerprint bit feature present in 6.0% of CTRPv2 compounds, with example compounds including CIL55, simvastatin, and lovastatin.
* fp_0513 is a fingerprint bit feature present in 0.8% of CTRPv2 compounds, with example compounds including epigallocatechin-3-monogallate, CAY10594, and avrainvillamide.
* fp_0723 is a fingerprint bit feature present in 6.0% of CTRPv2 compounds, with example compounds including gossypol, teniposide, and valde

---

## RPT-0042 - teniposide on FUOV1
_Source evidence: SHAP-0042_

## Executive Summary
The observed response of teniposide on FUOV1 cell line is characterized by an observed log10(IC50) of 0.0211, which is close to the model prediction of -0.0472 and the local drug/cell cohort baselines. The prediction error is +0.0683, indicating that the model underestimates the actual IC50 value.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7254.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1617.
* fp_0994, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1205.
* fp_0423, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0757.
* fp_0876, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0587.
* fp_0110, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which are binary features that represent the presence or absence of specific substructures in the molecular fingerprint of the compound. The features that push the prediction toward lower log10(IC50) (relative sensitivity) are present in 1.5-3.1% of CTRPv2 compounds, while the feature that pushes the prediction toward higher log10(IC50) (relative resistance) is present in 1.7% of CTRPv2 compounds.

The same-drug cohort examples show that teniposide is more sensitive in some cell lines (e.g., KARPAS620, SNU878) and more resistant in others (e.g., TUHR10TKB, KPL1). The same-cell cohort examples show that other drugs are more sensitive (e.g., leptomycin B, ouabain) or more resistant (e.g., temozolomide, procarbazine) in the FUOV1 cell line.

## Model-Level Context
The global model context shows that the model has a good fit on the training data (R2=0.4042, RMSE=1.0264, Corr=0.6385), but these metrics should be treated as training diagnostics only. The per-drug cross-validated predictability for teniposide is R2=0.3841. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX

---

## RPT-0043 - etoposide on MOLM16
_Source evidence: SHAP-0043_

## Executive Summary
Etoposide, an inhibitor of topoisomerase II, was tested on the MOLM16 cell line. The observed log10(IC50) was -0.0727, which is close to the model's predicted log10(IC50) of 0.1059 and the cohort baselines. The prediction error is -0.1786, indicating that the model underpredicted the observed log10(IC50).

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.5436.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.1951.
* fp_0994, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.1195.
* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.1038.
* fp_0876, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0938.
* fp_0110, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.0780.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. This feature pushes the prediction toward lower log10(IC50) (relative sensitivity). The fingerprint bit fp_0535 is present in 1.7% of CTRPv2 compounds and is associated with compounds such as BRD4132, BRD6340, and parbendazole. This feature pushes the prediction toward higher log10(IC50) (relative resistance). The gene expression feature CCN1 (3491) is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures, pushing the prediction toward lower log10(IC50) (relative sensitivity).

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385. These metrics are used as training diagnostics, not held-out generalization.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_

---

## RPT-0044 - PX-12 on RH18
_Source evidence: SHAP-0044_

## Executive Summary
PX-12 on RH18 has an observed log10(IC50) of 1.4239, which is close to the model-predicted log10(IC50) of 1.4309. The prediction error is -0.0070, indicating that the model slightly overestimates the compound's activity. The per-drug cross-validated R2 for PX-12 is 0.2858, suggesting moderate predictability.

## Evidence-Based Interpretation
The top TreeSHAP features for this prediction are:

* fp_0777: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7414
* fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.5402
* fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1124
* fp_0518: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0813
* fp_0876: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0804
* fp_0175: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0785

These features are all fingerprint bits, which are binary features that represent the presence or absence of specific substructures in the compound.

## Feature and Neighborhood Analysis
The feature fp_0777 is a fingerprint bit that represents the presence of a specific substructure, which is present in 1.2% of CTRPv2 compounds. This feature pushes the prediction toward lower log10(IC50), indicating that the presence of this substructure is associated with increased sensitivity to PX-12. The example compounds that contain this substructure are NSC95397, Mdivi-1, and cyanoquinoline 11.

The feature fp_0141 is a fingerprint bit that represents the presence of a different substructure, which is present in 1.5% of CTRPv2 compounds. This feature pushes the prediction toward higher log10(IC50), indicating that the presence of this substructure is associated with increased resistance to PX-12. The example compounds that contain this substructure are dexamethasone, austocystin D, and daporinad.

## Model-Level Context
The global model context is as follows:

* The model was trained on 181,811 samples with 2024 features.
* The training diagnostics are: train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* The max-depth tuning best row is: max_depth=20, n_estimators=100, r2=0.5459.
* The N-estimator tuning best row is: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031

---

## RPT-0045 - PX-12 on ONCODG1
_Source evidence: SHAP-0045_

## Executive Summary
PX-12's performance on ONCODG1 is close to the model prediction and cohort baselines, with an observed log10(IC50) of 1.3392 and a model-predicted log10(IC50) of 1.3879. The prediction error is -0.0487, indicating that the observed IC50 is slightly lower than the predicted value.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0777, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.7644.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.5757.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.1167.
* fp_0876, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0816.
* fp_0518, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0789.
* fp_0994, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0776.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0777 is present in 1.2% of CTRPv2 compounds and is associated with a representative SMARTS pattern `[#6]=[#6](-[#16])-[#6](=[#8])-[#6](:[#6]):[#6]`. This SMARTS pattern is present in example compounds such as NSC95397, Mdivi-1, and cyanoquinoline 11. The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`. This SMARTS pattern is present in example compounds such as dexamethasone, austocystin D, and daporinad.

## Model-Level Context
The global model context is as follows:
* DEM training fit only: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141 (0.11630), fp_0513 (

---

## RPT-0046 - olaparib on SNU398
_Source evidence: SHAP-0046_

## Executive Summary
The observed log10(IC50) of olaparib on SNU398 is 1.0785, which is close to the model-predicted log10(IC50) of 1.0653 and the cohort baselines. The prediction error is +0.0132, indicating that the model's prediction is slightly higher than the observed value.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1927.
* CCN1 (3491): a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0883.
* fp_0017: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0509.
* fp_0518: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0444.
* fp_0876: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0374.
* fp_0059: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0330.

These features are representative of the compound's fingerprint SMARTS patterns and gene expression levels, and are present in a small percentage of compounds in the CTRPv2 dataset.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bits fp_0518 and fp_0876 are present in 4.0% and 1.5% of CTRPv2 compounds, respectively, and are associated with compounds such as valdecoxib, neuronal differentiation inducer III, and BMS-754807, and triptolide, cucurbitacin I, and NPC-26, respectively. The fingerprint bit fp_0059 is present in 6.0% of CTRPv2 compounds and is associated with compounds such as CIL55, simvastatin, and lovastatin.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators

---

## RPT-0047 - TG-101348 on JHH4
_Source evidence: SHAP-0047_

## Executive Summary
TG-101348, an inhibitor of Janus kinase 2, was tested on JHH4 cells. The observed log10(IC50) was 0.8964, which is close to the model's predicted log10(IC50) of 0.8849 and the cohort baselines. The prediction error was +0.0114.

## Evidence-Based Interpretation
The top TreeSHAP features for this case are:

* fp_0059, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1567.
* fp_0017, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1150.
* fp_0065, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0846.
* CCN1, a gene expression feature, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0703.
* fp_0673, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0690.
* fp_0227, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0404.

## Feature and Neighborhood Analysis
The top fingerprint bits (fp_0059, fp_0017, fp_0065, fp_0673, and fp_0227) are all present in less than 17.5% of the CTRPv2 compounds. These features are representative of specific substructures, such as aromatic rings and heteroatoms. The gene expression feature, CCN1, is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context shows that the top fingerprint features across all compounds are fp_0141, fp_0513, and fp_0535. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4. The per-drug cross-validated predictability for TG-101348 is R2=0.2455. The cell subtype metadata is available, indicating that the cell line JHH4 is a hepatocellular carcinoma.

## Confidence and Caveats
This report is based on the observed response of TG-101348 on JHH4 cells and the local model predictions. The SHAP values explain the RF prediction rather than the underlying biology directly. The conclusions are non-causal and should be interpreted with caution. The local case evidence should be separated from the global training diagnostics.

---

## RPT-0048 - BRD-K80183349 on KYSE70
_Source evidence: SHAP-0048_

## Executive Summary
BRD-K80183349, an inhibitor of HDAC1 and HDAC2, was tested on KYSE70 cells. The observed log10(IC50) was 0.9910, which is close to the model's predicted log10(IC50) of 1.0253 and the cohort baselines. The prediction error is -0.0343, indicating that the model slightly overestimated the compound's potency.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1296.
* fp_0518, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0694.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0586.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0489.
* fp_0513 and fp_0723, fingerprint bits that push the prediction toward higher log10(IC50) (relative resistance) with SHAP values of +0.0184.

These features suggest that BRD-K80183349's structure and expression profile contribute to its relative resistance in KYSE70 cells.

## Feature and Neighborhood Analysis
The top fingerprint bit features are:

* fp_0141, present in 1.5% of CTRPv2 compounds, with example drugs dexamethasone, austocystin D, and daporinad.
* fp_0518, present in 4.0% of CTRPv2 compounds, with example drugs valdecoxib, neuronal differentiation inducer III, and BMS-754807.
* fp_0017, present in 2.3% of CTRPv2 compounds, with example drugs bexarotene, SR-II-138A, and CR-1-31B.
* fp_0513 and fp_0723, present in 0.8% and 6.0% of CTRPv2 compounds, respectively, with example drugs epigallocatechin-3-monogallate, CAY10594, avrainvillamide, gossypol, teniposide, and valdecoxib.

The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-est

---

## RPT-0049 - olaparib on RL952
_Source evidence: SHAP-0049_

## Executive Summary
The observed response of olaparib on RL952 is characterized by an observed log10(IC50) of 1.0778, which is close to the model-predicted log10(IC50) of 1.0653. The prediction error is +0.0125, indicating that the model slightly overestimated the sensitivity of RL952 to olaparib. The local drug and cell cohort baselines are also close to the observed response, suggesting that RL952 is not an outlier in terms of its sensitivity to olaparib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.1726.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0884.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0503.
* fp_0518, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.0433.
* fp_0876, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), with a SHAP value of -0.0342.
* fp_0059, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance), with a SHAP value of +0.0330.

These features suggest that the model is predicting a relatively resistant response to olaparib in RL952, with the fingerprint bits and gene expression feature contributing to this prediction.

## Feature and Neighborhood Analysis
The fingerprint bits fp_0141, fp_0017, and fp_0059 are present in 1.5%, 2.3%, and 6.0% of CTRPv2 compounds, respectively. These features are representative of SMARTS patterns `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`, and `[#6]=[#6]-[#6@H]`, respectively. The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. These metrics should be treated as training diagnostics only. The top global fingerprint features

---

## RPT-0050 - JQ-1 on SF295
_Source evidence: SHAP-0050_

## Executive Summary
JQ-1 on SF295 has an observed log10(IC50) of 1.0301, which is close to the model-predicted log10(IC50) of 1.0653 and the local drug and cell cohort baselines. The prediction error is -0.0352, indicating that the model underestimates the compound's potency. The per-drug cross-validated R2 is 0.2458, suggesting moderate predictability.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0535, fp_0723, which all push the prediction toward higher log10(IC50) or relative resistance. These features are associated with gene expression and fingerprint bits, with CCN1 being a gene that recurs in 71 predictable-drug RF signatures. The fingerprint bits are representative SMARTS patterns present in a small percentage of CTRPv2 compounds, with example drugs including dexamethasone, austocystin D, and bexarotene.

## Feature and Neighborhood Analysis
The same-drug cohort examples show varying levels of sensitivity and resistance, with some cells being more sensitive (e.g., AMO1, SCC25) and others more resistant (e.g., OV56, MJ). The same-cell cohort examples also demonstrate different profiles, with some drugs being more sensitive (e.g., daporinad, leptomycin B) and others more resistant (e.g., necrostatin-1, PRL-3 inhibitor I). The local metadata provides information on gene recurrence counts, target matches, fingerprint SMARTS annotations, and prevalence across compounds.

## Model-Level Context
The global model context includes training diagnostics, such as train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385, which should be treated as training diagnostics rather than held-out generalization. The model was tuned using max-depth and N-estimator hyperparameters, with the best-performing combination being max_depth=20, n_estimators=100, and r2=0.5459. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, and fp_0071. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
This analysis is based on the local evidence for this sample and should not be extrapolated to the broader population. The SHAP values explain the RF prediction rather than the underlying biology directly. The model's performance on this sample is moderate, with a per-drug cross-validated R2 of 0.2458. The same-drug and same-cell cohort examples provide additional context, but their profiles may not generalize to other compounds or cells.

---
