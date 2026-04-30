# Generated Reports - Llama-3.3-70B-Instruct IC50 Explainable50

## RPT-0001 - BI-2536 on REC1
_Source evidence: SHAP-0001_

## Executive Summary
The case of BI-2536 on REC1 shows a higher observed log10(IC50) value (3.7237) compared to the model-predicted value (0.2231), indicating that the cell line is more resistant to the drug than predicted. The prediction error is +3.5006, and the absolute error is 3.5006.

## Evidence-Based Interpretation
The observed response of BI-2536 on REC1 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -1.1707, with the sample at the 100th percentile. The cell cohort context shows a mean log10(IC50) of 1.4160, with the sample also at the 100th percentile. This suggests that the cell line REC1 is more resistant to BI-2536 compared to other cell lines and drugs.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7083.
2. fp_0876: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3586.
3. PLEK (5341): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1355.
4. CD70 (970): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1337.
5. TNFRSF12A (51330): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1026.
6. TRIP6 (7205): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1010.
These features provide insight into the factors contributing to the predicted log10(IC50) value.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for BI-2536 is R2=0.2724. The top global fingerprint features and most common genes across predictable per-drug models are also available, but are not directly relevant to this specific case. The cell subtype metadata is available, indicating that REC1 is a mantle cell lymphoma.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the SHAP explanation of the RF prediction, rather than the underlying biology. The local case evidence is separate from the global training diagnostics, and the results should be interpreted in the context of the specific case. The per-drug R2 value of 0.2724 indicates moderate predictability for BI-2536, but the prediction error and absolute error suggest that there may be other factors at play that are not

---

## RPT-0002 - topotecan on GOS3
_Source evidence: SHAP-0002_

## Executive Summary
The case of topotecan on GOS3 cell line is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.6393, which is lower than the model-predicted log10(IC50) of 1.0604. This discrepancy suggests that the model predicts a more resistant response than what is actually observed.

## Evidence-Based Interpretation
The observed response of topotecan on GOS3 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.3539, with the sample percentile being 0.1, indicating that the observed response is more sensitive than the average response of the drug cohort. The cell cohort context shows a mean log10(IC50) of 0.9655, with the sample percentile being 0.5, indicating that the observed response is more sensitive than the average response of the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features that contribute to the prediction of topotecan on GOS3 are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1032.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0691.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0475.
4. fp_0059 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0400.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0185.
These features are present in various compounds and have specific SMARTS annotations, but their presence in topotecan contributes to the model's prediction of a more resistant response.

## Model-Level Context
The global model context shows that the model was trained on a large dataset with 181811 samples and 2024 features, achieving a training R2 of 0.4042 and a training RMSE of 1.0264. The per-drug cross-validated predictability for topotecan is 0.4014, indicating that the model is able to predict the response of topotecan on different cell lines with moderate accuracy. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this case.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and only explain the model's prediction rather than the underlying biology. The SHAP values provide insight into the features that contribute to the model's prediction, but do not necessarily reflect the actual mechanisms of action. The local case evidence should be separated from the global training diagnostics, and the results should be interpreted in the context of the specific cell line and drug being studied

---

## RPT-0003 - SN-38 on PANC0504
_Source evidence: SHAP-0003_

## Executive Summary
The case of SN-38 on PANC0504 exhibits an exceptionally resistant response, with an observed log10(IC50) of 3.9917, which is higher than the model-predicted log10(IC50) of -0.8168. This discrepancy suggests that the model underestimates the resistance of PANC0504 to SN-38.

## Evidence-Based Interpretation
The observed response of SN-38 on PANC0504 can be understood by examining the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -1.4223, with the sample at the 100th percentile. The cell cohort context has a mean log10(IC50) of 0.8651, with the sample also at the 100th percentile. This indicates that PANC0504 is more resistant to SN-38 compared to other cell lines and that SN-38 is generally more effective against other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are primarily fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). These include fp_0329, fp_0059, fp_0240, fp_0065, and fp_0667. However, the gene expression feature CCN1 (3491) pushes the prediction toward higher log10(IC50) (relative resistance). The presence of these features in the compound and their associated SHAP values contribute to the model's prediction. The features are described in local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, and same-drug/same-cell cohort examples.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for SN-38 has an R2 of 0.3278, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these are not directly relevant to the local case interpretation. It is essential to note that SHAP explains the RF prediction rather than the biological mechanisms directly, and conclusions should be kept non-causal. The local case evidence should be separated from global training diagnostics to avoid overgeneralization.

---

## RPT-0004 - selumetinib on MINO
_Source evidence: SHAP-0004_

## Executive Summary
The case RPT-0004 involves the analysis of selumetinib's effect on the MINO cell line. The observed log10(IC50) is -3.4912, indicating high sensitivity, whereas the model-predicted log10(IC50) is 0.6342, suggesting a discrepancy between the actual and predicted response. This report aims to explain this discrepancy using TreeSHAP features and provide context for the prediction.

## Evidence-Based Interpretation
The observed response of selumetinib on MINO is exceptionally sensitive, with an observed log10(IC50) of -3.4912, which is lower than the model-predicted log10(IC50) of 0.6342. The local drug/cell cohort baselines also indicate that the MINO cell line is more sensitive to selumetinib compared to other cell lines. The prediction error is -4.1254, indicating that the model underestimates the sensitivity of selumetinib on MINO.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2307.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0616.
3. fp_0538 (fingerprint bit): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0433.
4. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0258.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0187.
These features provide insight into the factors contributing to the predicted response of selumetinib on MINO.

## Model-Level Context
The global model context indicates that the training fit has an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. However, these metrics are only relevant for training diagnostics and not for held-out generalization. The per-drug cross-validated predictability for selumetinib has an R2 of 0.2203, indicating moderate predictability. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this case.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and only explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the factors contributing to the predicted response, but the relationships between these factors and the actual response are complex and require further investigation. The local case evidence should be separated from global training diagnostics to avoid overgeneralization. Additionally, the analysis is limited to the available data and may not capture all relevant factors influencing the response of selumetinib on MIN

---

## RPT-0005 - GSK461364 on MDAMB468
_Source evidence: SHAP-0005_

## Executive Summary
The case of GSK461364 on MDAMB468 is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.9435, which is significantly lower than the model-predicted log10(IC50) of 0.0698. This discrepancy suggests that the model underestimated the sensitivity of MDAMB468 to GSK461364.

## Evidence-Based Interpretation
The observed response of GSK461364 on MDAMB468 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -1.1247, with the sample percentile at 0.5, indicating that MDAMB468 is more sensitive than the average cell line in the cohort. The cell cohort context shows a mean log10(IC50) of 0.5478, with the sample percentile at 0.4, indicating that GSK461364 is more effective than the average drug in the cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include fingerprint bits and gene expression values. The top features pushing the prediction toward lower log10(IC50) (relative sensitivity) are:
* fp_0059: a fingerprint bit with a SHAP value of -0.4314, representing a SMARTS pattern `[#6]=[#6]-[#6@H]` present in 6.0% of CTRPv2 compounds.
* fp_0065: a fingerprint bit with a SHAP value of -0.1724, representing a SMARTS pattern `[#8]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]-[#6]` present in 2.5% of CTRPv2 compounds.
* fp_0227: a fingerprint bit with a SHAP value of -0.1081, representing a SMARTS pattern `[#8]-[#6@H]` present in 6.7% of CTRPv2 compounds.
* fp_0402: a fingerprint bit with a SHAP value of -0.0262, representing a SMARTS pattern `[#7]-[#15](=[#8])(-[#8])-[#7]` present in 1.2% of CTRPv2 compounds.
The top feature pushing the prediction toward higher log10(IC50) (relative resistance) is:
* CCN1 (3491): a gene expression value with a SHAP value of +0.0924, near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for GSK461364 shows an R2 of 0.2482, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to this specific case.
The same-drug cohort examples

---

## RPT-0006 - barasertib on MDAMB468
_Source evidence: SHAP-0006_

## Executive Summary
The case of barasertib on MDAMB468 is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.5277, which is lower than the model-predicted log10(IC50) of 1.0653. This discrepancy suggests that the model predicts a more resistant response than what is actually observed.

## Evidence-Based Interpretation
The observed response of barasertib on MDAMB468 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.8872, with the sample percentile being 1.0, indicating that the observed response is more sensitive than the average response in the drug cohort. Similarly, the cell cohort context shows a mean log10(IC50) of 0.5478, with the sample percentile being 1.5, indicating that the observed response is more sensitive than the average response in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features that contribute to the prediction are:
1. CCN1 (gene_expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0932.
2. fp_0141 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0813.
3. fp_0017 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0769.
4. fp_0513 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0187.
5. fp_0723 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0171.
6. fp_0284 (fingerprint_bit): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0159.
These features are grounded in local metadata, with CCN1 being a gene that recurs in 71 predictable-drug RF signatures, and the fingerprint bits having specific SMARTS annotations and being present in a certain percentage of CTRPv2 compounds.

## Model-Level Context
The global model context shows a training fit with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. However, these metrics are only relevant for training diagnostics and not for held-out generalization. The per-drug cross-validated predictability for barasertib shows an R2 of 0.3417, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but do not directly explain the observed response in this specific case.
## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and only explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features that

---

## RPT-0007 - dabrafenib on SIGM5
_Source evidence: SHAP-0007_

## Executive Summary
The case RPT-0007 involves the analysis of dabrafenib's effect on the SIGM5 cell line. The observed log10(IC50) is -3.8228, indicating exceptional sensitivity, while the model-predicted log10(IC50) is 0.7137, suggesting a discrepancy between the actual and predicted response. This report aims to provide an evidence-based interpretation of this discrepancy using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed log10(IC50) of -3.8228 for dabrafenib on SIGM5 is significantly lower than the model-predicted value of 0.7137, indicating that the cell line is more sensitive to the drug than expected. The prediction error is -4.5365, and the absolute error is 4.5365. The global mean log10(IC50) for dabrafenib is 0.6392, and the per-drug cross-validated predictability (R2) is 0.5336.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2107.
2. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0288.
3. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0220.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0191.
5. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0170.
These features provide insight into the local factors influencing the predicted response of SIGM5 to dabrafenib.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The max-depth tuning and N-estimator tuning results indicate optimal hyperparameters for the model. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these diagnostics are based on training data and should not be considered as held-out generalization.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the TreeSHAP explanation of the RF prediction, rather than direct biological mechanisms. The local case evidence is separated from global training diagnostics to avoid overgeneralization. The analysis is grounded in local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, and same-drug/same-cell cohort examples. The per-drug cross-validated predictability for dabrafenib (R2=0.533

---

## RPT-0008 - alisertib on T84
_Source evidence: SHAP-0008_

## Executive Summary
The case of alisertib on T84 cells shows an observed log10(IC50) of -3.6782, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0653, suggesting a discrepancy between the predicted and actual response. The top TreeSHAP features pushing the prediction toward higher log10(IC50) (relative resistance) include gene expression CCN1 and several fingerprint bits (fp_0141, fp_0017, fp_0723, fp_0513, fp_0535).

## Evidence-Based Interpretation
The observed response of alisertib on T84 cells is exceptionally sensitive, with an observed log10(IC50) of -3.6782. In contrast, the RF-predicted log10(IC50) is 1.0653, indicating a predicted response that is more resistant than the actual response. The local drug/cell cohort baselines also suggest that the observed response is sensitive, with a sample percentile of 0.4 in the drug cohort and 1.1 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include CCN1 (gene expression), which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1125. Other contributing features are fingerprint bits fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, all of which push the prediction toward higher log10(IC50) (relative resistance). These features are present in a subset of CTRPv2 compounds, with example compounds including dexamethasone, austocystin D, and bexarotene.

## Model-Level Context
The global model context indicates a training fit with an R2 of 0.4042 and RMSE of 1.0264. The per-drug cross-validated predictability for alisertib is 0.3285, suggesting moderate predictability. The top global fingerprint features include fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are also present in the local feature analysis. The most common genes across predictable per-drug models include CCN1, which is also a top feature in the local analysis. It is essential to note that SHAP values explain the RF prediction rather than the biological mechanism directly, and conclusions should be non-causal. The local case evidence should be separated from global training diagnostics to avoid overgeneralization.

---

## RPT-0009 - GSK461364 on TE4
_Source evidence: SHAP-0009_

## Executive Summary
The case of GSK461364 on TE4 cell line is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.9022, which is significantly lower than the model-predicted log10(IC50) of 0.0506. This discrepancy suggests that the model underestimates the sensitivity of GSK461364 on TE4 cells.

## Evidence-Based Interpretation
The observed response of GSK461364 on TE4 cells can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -1.1247, with the sample percentile being 1.1, indicating that TE4 cells are more sensitive to GSK461364 compared to other cell lines. The cell cohort context also shows a mean log10(IC50) of 0.5912, with the sample percentile being 0.8, indicating that GSK461364 is more effective on TE4 cells compared to other drugs.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0059: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4360.
2. fp_0065: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1724.
3. fp_0227: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1081.
4. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0903.
These features are present in various compounds, with representative SMARTS annotations and example drugs provided. The presence of these features in the compound's fingerprint contributes to the predicted sensitivity or resistance of GSK461364 on TE4 cells.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for GSK461364 shows an R2 of 0.2482, indicating moderate predictability. The most common genes across predictable per-drug models include CCN1, which is also present in the top TreeSHAP features for this case. The cell subtype metadata confirms that TE4 cells are of squamous cell carcinoma type.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features contributing to the predicted response, but do not imply a direct biological relationship. The local case evidence is separated from the global training diagnostics, and the analysis is limited to the provided data and metadata. The per-drug cross-validated predictability and global model context provide additional context for the results, but do not affect the local interpretation of the case.

---

## RPT-0010 - barasertib on LCLC97TM1
_Source evidence: SHAP-0010_

## Executive Summary
The case of barasertib on LCLC97TM1 is characterized by an observed log10(IC50) of -3.2033, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0653, suggesting a discrepancy between the predicted and actual response. The top TreeSHAP features, including CCN1 and several fingerprint bits, push the prediction toward higher log10(IC50) values, indicating relative resistance.

## Evidence-Based Interpretation
The observed response of barasertib on LCLC97TM1 is exceptionally sensitive, with an observed log10(IC50) of -3.2033. In contrast, the RF-predicted log10(IC50) is 1.0653, resulting in a prediction error of -4.2685. The local drug/cell cohort baselines also indicate that the observed response is sensitive, with a sample percentile of 2.9 in the drug cohort and 1.5 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include CCN1, fp_0141, fp_0017, fp_0513, fp_0723, and fp_0284. CCN1, a gene expression feature, pushes the prediction toward higher log10(IC50) values, indicating relative resistance. The fingerprint bits fp_0141, fp_0017, fp_0513, and fp_0723 also push the prediction toward higher log10(IC50) values, while fp_0284 pushes the prediction toward lower log10(IC50) values, indicating relative sensitivity. These features are supported by local metadata, including gene recurrence counts, target matches, and fingerprint SMARTS annotations.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for barasertib is 0.3417, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should not be directly interpreted as causal factors in this specific case. The cell subtype metadata is available, indicating that LCLC97TM1 is a large cell carcinoma. It is essential to note that SHAP values explain the RF prediction rather than the underlying biology, and conclusions should be kept non-causal. Local case evidence should be separated from global training diagnostics to avoid overgeneralization.

---

## RPT-0011 - alisertib on CAOV3
_Source evidence: SHAP-0011_

## Executive Summary
The case of alisertib on CAOV3 cells shows an observed log10(IC50) of -3.1799, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0653, suggesting a discrepancy between the predicted and actual response. The top TreeSHAP features pushing the prediction toward higher log10(IC50) (relative resistance) include CCN1 gene expression and several fingerprint bits (fp_0141, fp_0017, fp_0723, fp_0513, fp_0535).

## Evidence-Based Interpretation
The observed response of alisertib on CAOV3 cells is exceptionally sensitive, with an observed log10(IC50) of -3.1799. In contrast, the RF-predicted log10(IC50) is 1.0653, indicating a predicted response that is more resistant than the actual response. The local drug/cell cohort baselines also suggest that the observed response is sensitive, with a sample percentile of 1.3 in both the drug and cell cohorts.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include CCN1 gene expression, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1129. Other contributing features are fingerprint bits fp_0141, fp_0017, fp_0723, fp_0513, and fp_0535, all of which push the prediction toward higher log10(IC50) (relative resistance). These features are present in a subset of CTRPv2 compounds, with example compounds including dexamethasone, austocystin D, and bexarotene.

## Model-Level Context
The global model context indicates a training fit with an R2 of 0.4042 and an RMSE of 1.0264. The per-drug cross-validated predictability for alisertib is 0.3285, suggesting moderate predictability. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and CCN1, which is also a top feature in this case. The cell subtype metadata is available and indicates that the CAOV3 cells are adenocarcinoma. It is essential to note that the SHAP values explain the RF prediction rather than the biological mechanism directly, and the conclusions should be kept non-causal. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization.

---

## RPT-0012 - crizotinib on CAPAN2
_Source evidence: SHAP-0012_

## Executive Summary
The case of crizotinib on CAPAN2 cells shows an observed log10(IC50) of -3.0708, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0604, suggesting a discrepancy between the predicted and actual response. The top TreeSHAP features contributing to this prediction include fingerprint bits and gene expression values, which push the prediction toward higher log10(IC50) (relative resistance) or lower log10(IC50) (relative sensitivity).

## Evidence-Based Interpretation
The observed response of crizotinib on CAPAN2 cells is exceptionally sensitive, with an observed log10(IC50) of -3.0708. In contrast, the RF-predicted log10(IC50) is 1.0604, indicating a potential underestimation of the drug's efficacy. The local drug/cell cohort baselines show that the sample percentile for the drug cohort is 0.1 and 0.4 for the cell cohort, suggesting that CAPAN2 cells are more sensitive to crizotinib compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include:
1. fp_0017: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1361.
2. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1019.
3. fp_0673: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0696.
These features are grounded in local metadata, with fp_0017 present in 2.3% of CTRPv2 compounds and CCN1 recurring in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context shows a DEM training fit with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for crizotinib has an R2 of 0.2541. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and CCN1. The top global fingerprint features include fp_0141, fp_0513, and fp_0535. These metrics provide context for the model's performance but do not directly explain the biology of the crizotinib-CAPAN2 interaction.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The local case evidence is separate from global training diagnostics, and the results should be interpreted in the context of the specific drug-cell pair. The analysis is limited to the available data and may not generalize to other contexts.

---

## RPT-0013 - indisulam on NCIH2081
_Source evidence: SHAP-0013_

## Executive Summary
The case of indisulam on NCIH2081 cell line shows an observed log10(IC50) of -3.4710, indicating exceptional sensitivity. The RF-predicted log10(IC50) is 0.7137, resulting in a prediction error of -4.1846. This discrepancy suggests that the model predicts a higher log10(IC50) (more resistance) than observed.

## Evidence-Based Interpretation
The observed response of indisulam on NCIH2081 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.7254, with the sample at the 0.2 percentile. The cell cohort context has a mean log10(IC50) of 0.3004, with the sample at the 0.8 percentile. This indicates that NCIH2081 is more sensitive to indisulam compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2055.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0646.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0292.
4. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0182.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0168.
These features are grounded in local metadata, with CCN1 being below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bits have representative SMARTS annotations and are present in a subset of CTRPv2 compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for indisulam is R2=0.3312. The top global fingerprint features and most common genes across predictable per-drug models are available, but their relevance to this specific case is limited. The cell subtype metadata is available, indicating that NCIH2081 is a small cell carcinoma.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features contributing to the prediction, but do not directly imply biological mechanisms. The local case evidence is separated from global training diagnostics, and the analysis is grounded in available metadata. The results should be interpreted with caution, considering the limitations of the

---

## RPT-0014 - LBH-589 on MKN45
_Source evidence: SHAP-0014_

## Executive Summary
The case of LBH-589 on MKN45 shows an observed log10(IC50) of 3.8231, which is higher than the model-predicted log10(IC50) of 1.6866, indicating that MKN45 is more resistant to LBH-589 than predicted. The top TreeSHAP features suggest that certain fingerprint bits and gene expressions contribute to this resistance.

## Evidence-Based Interpretation
The observed response of LBH-589 on MKN45 can be explained by the difference between the observed log10(IC50) and the model-predicted log10(IC50). The model predicted a lower log10(IC50) value, indicating that the cell line should be more sensitive to the drug. However, the observed log10(IC50) value is higher, indicating resistance. This discrepancy can be attributed to the top TreeSHAP features, which include fingerprint bits and gene expressions that push the prediction toward higher log10(IC50) values.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include:
1. fp_0017: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3434.
2. MYLK (4638): a gene expression that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.3335.
3. fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.2212.
4. fp_0071: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1500.
5. TES (26136): a gene expression that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1418.
6. GLB1L2 (89944): a gene expression that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1089.
These features can be grounded in local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, and prevalence across compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for LBH-589 has an R2 of 0.2691. The top global fingerprint features and most common genes across predictable per-drug models are also available. However, it is essential to note that these metrics are training diagnostics and should not be used for held-out generalization. The model's performance on this specific case should be evaluated separately, considering the local evidence and TreeSHAP features.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the local evidence provided by the TreeSHAP features. The SHAP values explain the RF prediction rather

---

## RPT-0015 - topotecan on SNU886
_Source evidence: SHAP-0015_

## Executive Summary
The case of topotecan on SNU886 cell line is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.1800, which is lower than the model-predicted log10(IC50) of 1.0604. This discrepancy suggests that the model predicts a more resistant response than what is actually observed.

## Evidence-Based Interpretation
The observed response of topotecan on SNU886 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.3539, with the sample percentile being 0.4, indicating that the observed response is more sensitive than the average response in the drug cohort. Similarly, the cell cohort context shows a mean log10(IC50) of 0.3872, with the sample percentile being 2.8, indicating that the observed response is more sensitive than the average response in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features that contribute to the prediction of topotecan on SNU886 are:
1. CCN1 (gene_expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1032.
2. fp_0141 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0682.
3. fp_0017 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0475.
4. fp_0059 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0401.
5. fp_0513 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0180.
These features are present in various compounds and have specific SMARTS annotations, which provide insight into their chemical structure.

## Model-Level Context
The global model context provides training diagnostics, including a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. The per-drug cross-validated predictability for topotecan has an R2 of 0.4014, indicating moderate predictability. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this case. The cell subtype metadata is available, indicating that SNU886 is a hepatocellular carcinoma cell line. It is essential to note that the SHAP values explain the RF prediction rather than the biology directly, and the conclusions should be kept non-causal. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization.

---

## RPT-0016 - SN-38 on ISTMES1
_Source evidence: SHAP-0016_

## Executive Summary
The case of SN-38 on ISTMES1 cell line shows an observed log10(IC50) of 2.6421, which is higher than the model-predicted log10(IC50) of -1.0252, indicating that the cell line is more resistant to SN-38 than predicted. The prediction error is +3.6673, and the absolute error is 3.6673.

## Evidence-Based Interpretation
The observed response of SN-38 on ISTMES1 can be explained by the local drug/cell cohort baselines. The cell line ISTMES1 has a higher mean log10(IC50) of 0.9001 compared to the drug cohort mean of -1.4223. The sample percentile of 95.7 for ISTMES1 and 99.8 for SN-38 suggests that the cell line is relatively more resistant to SN-38 compared to other cell lines and drugs.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. fp_0329: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.5058.
2. fp_0059: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4387.
3. fp_0667: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1960.
4. fp_0240: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1855.
5. fp_0065: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1724.
6. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1229.
These features are present in various percentages of CTRPv2 compounds and have example compounds associated with them.

## Model-Level Context
The global model context shows a training fit with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for SN-38 has an R2 of 0.3278. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these are training diagnostics and not held-out generalization. The SHAP values explain the RF prediction rather than the biology directly, and conclusions should be kept non-causal. Local case evidence should be separated from global training diagnostics.

---

## RPT-0017 - dabrafenib on SCC4
_Source evidence: SHAP-0017_

## Executive Summary
The case of dabrafenib on SCC4 (RPT-0017) shows an observed log10(IC50) of -2.6407, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0653, suggesting a discrepancy between the predicted and actual response. The top TreeSHAP features pushing the prediction toward higher log10(IC50) (relative resistance) include CCN1 gene expression and several fingerprint bits (fp_0017, fp_0141, fp_0513, fp_0059, fp_0723).

## Evidence-Based Interpretation
The observed response of dabrafenib on SCC4 is exceptionally sensitive, with an observed log10(IC50) of -2.6407. In contrast, the RF-predicted log10(IC50) is 1.0653, indicating a predicted response that is more resistant than the actual response. The local drug/cell cohort baselines also suggest that the observed response is sensitive, with a sample percentile of 10.6 in the drug cohort and 2.7 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include CCN1 gene expression, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0903. Other contributing features are fingerprint bits fp_0017, fp_0141, fp_0513, fp_0059, and fp_0723, all of which push the prediction toward higher log10(IC50) (relative resistance). These features are present in a subset of CTRPv2 compounds, with example compounds including bexarotene, dexamethasone, and epigallocatechin-3-monogallate.

## Model-Level Context
The global model context includes a training fit with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for dabrafenib is R2=0.5336. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and CCN1. The top global fingerprint features include fp_0141, fp_0513, and fp_0535. It is essential to note that the SHAP values explain the RF prediction rather than the biological mechanisms directly, and the conclusions should be kept non-causal. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization.

---

## RPT-0018 - AZD7762 on MFE319
_Source evidence: SHAP-0018_

## Executive Summary
The case of AZD7762 on MFE319 exhibits an exceptionally sensitive response, with an observed log10(IC50) of -3.4999, which is lower than the model-predicted log10(IC50) of -0.3873. This discrepancy suggests that the model underestimates the sensitivity of AZD7762 on MFE319.

## Evidence-Based Interpretation
The observed response of AZD7762 on MFE319 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.3569, with the sample percentile at 0.3, indicating that AZD7762 is more sensitive than the average drug in the cohort. The cell cohort context shows a mean log10(IC50) of 0.8967, with the sample percentile at 1.2, indicating that MFE319 is more resistant than the average cell line in the cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. fp_0141, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7450.
2. fp_0157, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3086.
3. fp_0032, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1582.
4. fp_0994, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0701.
5. fp_0876, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0580.
6. fp_0071, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0469.
These features are present in various percentages of CTRPv2 compounds and have example compounds associated with them.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for AZD7762 is R2=0.2053, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to this specific case. The cell subtype metadata is available, confirming that MFE319 is an adenocarcinoma cell line.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the SHAP explanation of the RF prediction, rather than the underlying biology. The local case evidence is separated from the global training diagnostics, and the analysis is limited to the provided data and features. The results should be interpreted with caution, considering the complexity of the model and the potential for biases in the data.

---

## RPT-0019 - Ki8751 on A673
_Source evidence: SHAP-0019_

## Executive Summary
The case RPT-0019 involves the analysis of Ki8751 on A673 cells, where the observed log10(IC50) is -3.0652, indicating exceptional sensitivity. However, the RF-predicted log10(IC50) is 1.0543, suggesting a discrepancy between the predicted and observed responses. This report aims to provide an evidence-based interpretation of this discrepancy using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed log10(IC50) of -3.0652 for Ki8751 on A673 cells indicates that the cells are exceptionally sensitive to the drug. In contrast, the RF-predicted log10(IC50) of 1.0543 suggests that the model predicts a higher log10(IC50) value, indicating resistance. The large prediction error of -4.1195 and absolute error of 4.1195 highlight the need for further investigation. The drug cohort context shows that Ki8751 has a mean log10(IC50) of 0.6387, with the sample percentile being 0.9, indicating that the observed response is lower than expected.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0931.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0856.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0566.
4. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0189.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0189.
These features are present in various compounds and have specific SMARTS annotations, indicating their potential role in contributing to the predicted resistance.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for Ki8751 has an R2 of 0.2024, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, offering insight into the model's performance and feature importance.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The local case evidence is separated from global training diagnostics, and the report focuses on providing an evidence-based interpretation of the observed discrepancy between the predicted and observed responses. The results should be considered in the context of the available

---

## RPT-0020 - BI-2536 on OVCAR5
_Source evidence: SHAP-0020_

## Executive Summary
The case of BI-2536 on OVCAR5 is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.8048, which is lower than the model-predicted log10(IC50) of -0.8487. This discrepancy suggests that the model underestimates the sensitivity of BI-2536 on OVCAR5.

## Evidence-Based Interpretation
The observed response of BI-2536 on OVCAR5 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -1.1707, with the sample percentile at 0.9, indicating that BI-2536 is more sensitive than most drugs in the cohort. The cell cohort context shows a mean log10(IC50) of 0.7596, with the sample percentile at 0.4, indicating that OVCAR5 is more sensitive than most cell lines in the cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are all fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The top features are:
1. fp_0141: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.8879
2. fp_0876: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.4688
3. fp_0582: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0808
4. fp_0059: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0696
5. fp_0271: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0693
6. fp_0994: pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0402
These features are present in a small percentage of CTRPv2 compounds and are associated with example compounds such as dexamethasone, austocystin D, and triptolide.

## Model-Level Context
The global model context shows that the model was trained on a large dataset with 181,811 samples and 2,024 features, achieving a training R2 of 0.4042 and a training RMSE of 1.0264. The model was tuned using max-depth and n-estimator tuning, with the best parameters being max_depth=20 and n_estimators=100. The top global fingerprint features are different from the top features for this specific case, suggesting that the model is capturing different patterns in the data. The per-drug cross-validated predictability for BI-2536 shows an R2 of 0.2724, indicating moderate predictability.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and only explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features that drive the model's prediction, but do not necessarily reflect

---

## RPT-0021 - etoposide on CAL62
_Source evidence: SHAP-0021_

## Executive Summary
The case RPT-0021 involves the analysis of etoposide's effect on the CAL62 cell line. The observed log10(IC50) is -3.3349, indicating exceptional sensitivity, while the model-predicted log10(IC50) is 0.3324. This report aims to explain the discrepancy between the observed and predicted values using TreeSHAP features and provide context from the global model.

## Evidence-Based Interpretation
The observed log10(IC50) of -3.3349 for etoposide on CAL62 is significantly lower than the model-predicted value of 0.3324, suggesting that the cell line is more sensitive to the drug than expected. The prediction error is -3.6673, and the absolute error is 3.6673. The global mean log10(IC50) for etoposide is 0.6392, and the cell line's response is in the 0.2 percentile of the drug cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.6198.
2. fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.1918.
3. fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1199.
4. fp_0876: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0684.
5. fp_0582: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0559.
6. fp_0071: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0507.
These features are associated with specific SMARTS annotations and are present in a subset of compounds in the CTRPv2 dataset.

## Model-Level Context
The global model context provides information on the training fit, with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for etoposide is R2=0.3081. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these metrics are training diagnostics and not held-out generalization metrics.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features contributing to the prediction, but the relationships between these features and the biological mechanisms are not explicitly stated. The analysis is limited to the provided data and models, and the results should be interpreted in the context of the specific case and not generalized to other scenarios. Additionally, the cell subtype

---

## RPT-0022 - GDC-0879 on SKM1
_Source evidence: SHAP-0022_

## Executive Summary
The case of GDC-0879 on SKM1 is characterized by an observed log10(IC50) of -2.8138, indicating exceptional sensitivity. The RF-predicted log10(IC50) is 0.7137, resulting in a prediction error of -3.5275. This discrepancy suggests that the model predicts resistance, while the actual response is sensitive.

## Evidence-Based Interpretation
The observed response of GDC-0879 on SKM1 is exceptionally sensitive, with an observed log10(IC50) of -2.8138. In contrast, the RF-predicted log10(IC50) is 0.7137, indicating a predicted resistance. The local drug/cell cohort baselines also suggest that the observed response is sensitive, with a sample percentile of 0.5 in the drug cohort and 2.0 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. CCN1 (gene_expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2121.
2. fp_0141 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0424.
3. fp_0015 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0331.
4. fp_0017 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0290.
5. fp_0513 (fingerprint_bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0200.
These features provide insight into the factors contributing to the predicted resistance, despite the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. The per-drug cross-validated predictability for GDC-0879 is R2=0.2515, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific case is limited. The cell subtype metadata is available, confirming that SKM1 is an acute myeloid leukaemia cell line.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the SHAP explanation of the RF prediction, rather than the underlying biology. The analysis is limited to the local case evidence and does not generalize to other cases or the global model context. The prediction error and discrepancy between observed and predicted log10(IC50) values highlight the complexity of the relationship between GDC-0879 and SKM1, and further investigation is necessary to fully understand this interaction.

---

## RPT-0023 - teniposide on SNU878
_Source evidence: SHAP-0023_

## Executive Summary
The case of teniposide on SNU878 cell line is characterized by an exceptionally sensitive response, with an observed log10(IC50) of -3.7618, which is significantly lower than the model-predicted log10(IC50) of -0.0907. This discrepancy suggests that the model underestimates the sensitivity of teniposide on SNU878.

## Evidence-Based Interpretation
The observed response of teniposide on SNU878 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.3665, with the sample percentile at 0.5, indicating that teniposide is more sensitive than the average drug in the cohort. The cell cohort context shows a mean log10(IC50) of 0.3995, with the sample percentile at 1.0, indicating that SNU878 is more sensitive than the average cell line in the cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0141, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7211.
2. fp_0535, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1521.
3. fp_0994, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1204.
4. fp_0423, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0772.
5. fp_0110, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558.
6. CCN1 (3491), which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0440.
These features are grounded in local metadata, with representative SMARTS annotations and example compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for teniposide is R2=0.3841, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to this specific case.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features contributing to the prediction, but do not necessarily reflect the actual mechanisms of action. The local case evidence is separated from the global training diagnostics, and the analysis is grounded in structured evidence from the provided data sources. The cell subtype metadata is available and indicates that SNU878 is a hepatocellular carcinoma cell line.

---

## RPT-0024 - PD318088 on CHP212
_Source evidence: SHAP-0024_

## Executive Summary
The case of PD318088 on CHP212 cell line shows an exceptionally sensitive response with an observed log10(IC50) of -2.9343, which is lower than the model-predicted log10(IC50) of 0.9380. This discrepancy suggests that the model underestimated the sensitivity of PD318088 on CHP212.

## Evidence-Based Interpretation
The observed response of PD318088 on CHP212 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.4477, with the sample percentile of 0.2, indicating that PD318088 is more sensitive than most drugs in the cohort. The cell cohort context shows a mean log10(IC50) of 0.1812, with the sample percentile of 2.8, indicating that CHP212 is relatively sensitive to most drugs.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include fingerprint bits and gene expression features. The top feature, fp_0235, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1077. This feature is present in 4.0% of CTRPv2 compounds and is associated with example drugs such as blebbistatin and pifithrin-alpha. Other features, such as CCN1, fp_0141, fp_0017, and fp_0059, push the prediction toward higher log10(IC50) (relative resistance). The feature fp_0726 pushes the prediction toward lower log10(IC50) (relative sensitivity).

## Model-Level Context
The global model context shows a training fit with an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. However, these metrics are only relevant for training diagnostics and do not reflect held-out generalization. The per-drug cross-validated predictability for PD318088 shows an R2 of 0.2192, indicating moderate predictability. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and CCN1, which may be relevant for understanding the mechanisms of action for PD318088.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and only explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features that contribute to the predicted log10(IC50) value, but do not necessarily reflect the actual mechanisms of action. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization. Additionally, the analysis is limited to the available data and may not capture all relevant factors that influence the response of PD318088 on CHP212.

---

## RPT-0025 - 1S,3R-RSL-3 on LS1034
_Source evidence: SHAP-0025_

## Executive Summary
The case of 1S,3R-RSL-3 on LS1034 exhibits an exceptionally resistant response, with an observed log10(IC50) of 3.4227, significantly higher than the model-predicted log10(IC50) of 0.5075. This discrepancy suggests that the model underestimates the resistance of LS1034 to 1S,3R-RSL-3.

## Evidence-Based Interpretation
The observed response of 1S,3R-RSL-3 on LS1034 is higher than the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.7253, with the sample at the 99.9th percentile. The cell cohort context has a mean log10(IC50) of 0.6265, with the sample at the 100th percentile. The large difference between the observed and predicted log10(IC50) values indicates that the model predicts a more sensitive response than what is actually observed.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include fingerprint bits and gene expression values. The features pushing the prediction toward lower log10(IC50) (relative sensitivity) are: fp_0141 (SHAP = -0.7781), fp_0876 (SHAP = -0.1567), CCN1 (SHAP = -0.0985), and fp_0582 (SHAP = -0.0825). In contrast, features pushing the prediction toward higher log10(IC50) (relative resistance) are: fp_0518 (SHAP = 0.0942) and NQO1 (SHAP = 0.0733). These features provide insight into the factors contributing to the model's prediction, but their biological interpretation requires caution.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for 1S,3R-RSL-3 has an R2 of 0.2660, indicating moderate predictability. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and CCN1, which may be relevant for understanding the mechanisms underlying the response of LS1034 to 1S,3R-RSL-3. However, it is essential to note that these findings are based on training data and may not generalize to held-out data. Additionally, the SHAP values explain the RF prediction rather than the biological mechanisms directly, and conclusions should be drawn cautiously, avoiding causal interpretations.

---

## RPT-0026 - teniposide on CAL29
_Source evidence: SHAP-0026_

## Executive Summary
The case report RPT-0026 examines the response of teniposide on the CAL29 cell line. The observed log10(IC50) is -0.0258, and the model-predicted log10(IC50) is -0.0472, indicating that the model slightly underestimates the sensitivity of CAL29 to teniposide. The prediction error is +0.0214, and the absolute error is 0.0214.

## Evidence-Based Interpretation
The observed response of teniposide on CAL29 is close to the model prediction and cohort baselines. The drug target is TOP2A and TOP2B, and the cell lineage is bladder/urinary tract/bladder urothelial carcinoma. The per-drug R² on held-out cells is 0.38, indicating moderate predictability.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are:
1. fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7185.
2. fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1552.
3. fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1203.
4. fp_0423: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0767.
5. fp_0110: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558.
6. fp_0876: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0495.
These features are associated with specific SMARTS annotations and are present in a subset of CTRPv2 compounds.

## Model-Level Context
The global model context includes training diagnostics such as train_r2 (0.4042), train_rmse (1.0264), and train_corr (0.6385). The per-drug cross-validated predictability for teniposide is R2=0.3841. The top global fingerprint features and most common genes across predictable per-drug models are also available. However, these should be treated as training diagnostics and not held-out generalization.
The same-drug cohort examples show varying levels of sensitivity and resistance across different cell lines, and the same-cell cohort examples demonstrate different responses to various drugs. 
## Confidence and Caveats
The conclusions drawn from this report are non-causal, and the SHAP values explain the RF prediction rather than the underlying biology. The local case evidence should be separated from global training diagnostics. The report is based on the available data and should not be considered as clinical advice.

---

## RPT-0027 - KPT185 on SH4
_Source evidence: SHAP-0027_

## Executive Summary
The case of KPT185 on SH4 cell line is characterized by an observed log10(IC50) of 0.3890, which is close to the model-predicted value of 0.3960. The prediction error is -0.0070, indicating a slight underestimation by the model. The drug target is XPO1, an inhibitor of exportin 1, and the cell lineage is skin/melanoma.

## Evidence-Based Interpretation
The observed response of KPT185 on SH4 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.2379, with the sample percentile being 73.5. The cell cohort context has a mean log10(IC50) of 0.8095, with the sample percentile being 29.4. This suggests that KPT185 is relatively more effective on SH4 cells compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0017: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4674.
2. fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1894.
3. fp_0071: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1601.
4. fp_0284: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1335.
5. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0658.
These features are associated with specific SMARTS annotations and are present in various percentages of CTRPv2 compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for KPT185 has an R2 of 0.2550. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these are training diagnostics and should not be considered as held-out generalization.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features contributing to the prediction, but the relationships between these features and the biological mechanisms are not explicitly defined. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization. The analysis is based on the available data and should be considered in the context of the specific cell line and drug being studied.

---

## RPT-0028 - PRIMA-1 on SUDHL10
_Source evidence: SHAP-0028_

## Executive Summary
The case report RPT-0028 examines the response of PRIMA-1 on the SUDHL10 cell line, with an observed log10(IC50) of 0.7151 and a model-predicted log10(IC50) of 0.7137. The prediction error is +0.0014, indicating that the model prediction is close to the observed value. The cell line SUDHL10 is a lymphoid neoplasm, specifically diffuse large B cell lymphoma.

## Evidence-Based Interpretation
The observed response of PRIMA-1 on SUDHL10 is interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 1.5212, with the sample percentile of 8.1, indicating that PRIMA-1 is more effective on SUDHL10 compared to other cell lines. The cell cohort context shows a mean log10(IC50) of 0.3240, with the sample percentile of 60.1, indicating that SUDHL10 is relatively resistant to PRIMA-1 compared to other drugs.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2095.
2. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0307.
3. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0274.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0200.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0176.
6. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0152.
These features provide insight into the factors contributing to the predicted response of PRIMA-1 on SUDHL10.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for PRIMA-1 is R2=0.3234, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to this specific case. The cell subtype metadata is available, confirming that SUDHL10 is a diffuse large B cell lymphoma.
## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the SHAP explanation of the RF prediction,

---

## RPT-0029 - PRIMA-1 on A204
_Source evidence: SHAP-0029_

## Executive Summary
The case report RPT-0029 examines the response of PRIMA-1 on the A204 cell line, with an observed log10(IC50) of 1.0627 and a model-predicted log10(IC50) of 1.0653. The prediction error is -0.0026, indicating that the model slightly overestimates the sensitivity of the cell line to PRIMA-1. The report provides an evidence-based interpretation of the prediction, highlighting the top TreeSHAP features that contribute to the predicted log10(IC50) value.

## Evidence-Based Interpretation
The observed response of PRIMA-1 on A204 is close to the model prediction and cohort baselines. The drug target is TP53, and the cell lineage is Kidney/Rhabdoid Cancer. The per-drug R² on held-out cells is 0.32, indicating moderate predictability. The local drug/cell cohort baselines show that the sample is at the 23.5th percentile for the drug cohort and the 63.9th percentile for the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted log10(IC50) value are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0900.
2. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0501.
3. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0406.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0191.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0165.
6. fp_0059 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0152.
These features are associated with higher log10(IC50) values, indicating relative resistance to PRIMA-1.

## Model-Level Context
The global model context provides training diagnostics, including a train R² of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The max-depth tuning best row has a max depth of 20, 100 estimators, and an R² of 0.5459. The N-estimator tuning best row has a max depth of 10, 235 estimators, and a mean R² of 0.3803. The top global fingerprint features include fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723. The most common genes across predictable per-drug models include MYOF, TNFRSF12

---

## RPT-0030 - Compound 7d-cis on JVM3
_Source evidence: SHAP-0030_

## Executive Summary
The report analyzes the response of Compound 7d-cis on JVM3 cells, with an observed log10(IC50) of 0.7573 and a model-predicted log10(IC50) of 0.7676. The prediction error is -0.0103, indicating that the model slightly overestimates the sensitivity of the compound. The compound's target is XPO1, an inhibitor of CRM1-mediated nucleocytoplasmic transport.

## Evidence-Based Interpretation
The observed response of Compound 7d-cis on JVM3 cells is close to the model prediction and cohort baselines. The drug cohort context shows a mean log10(IC50) of 1.1250, with the sample at the 22.2 percentile. The cell cohort context has a mean log10(IC50) of 0.1542, with the sample at the 63.6 percentile. This suggests that JVM3 cells are relatively more sensitive to Compound 7d-cis compared to other cells.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are:
1. fp_0017 (fingerprint bit): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1787.
2. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1068.
3. fp_0673 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0810.
These features are present in various compounds and have specific SMARTS annotations. For example, fp_0017 is present in 2.3% of CTRPv2 compounds and has a representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for Compound 7d-cis has an R2 of 0.2832. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these should be treated as training diagnostics and not held-out generalization.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The local case evidence should be separated from global training diagnostics. The analysis is limited to the provided data and should not be used for clinical advice. The cell subtype metadata is available, and the compound's target is XPO1, but further research is needed to fully understand the mechanisms involved.

---

## RPT-0031 - NVP-BSK805 on FU97
_Source evidence: SHAP-0031_

## Executive Summary
The report analyzes the response of NVP-BSK805 on the FU97 cell line, with an observed log10(IC50) of 0.6578 and a model-predicted log10(IC50) of 0.6386. The prediction error is +0.0192, indicating that the model slightly underestimates the sensitivity of NVP-BSK805 on FU97. The observed log10(IC50) is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The observed response of NVP-BSK805 on FU97 is interpreted in the context of the drug and cell line cohorts. The drug cohort context shows a mean log10(IC50) of 1.0644, with the observed value for NVP-BSK805 on FU97 at the 13.1 percentile. The cell cohort context shows a mean log10(IC50) of 0.4157, with the observed value at the 51.5 percentile. This suggests that NVP-BSK805 is relatively more effective on FU97 compared to other cell lines, but less effective compared to other drugs on FU97.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are analyzed. The features and their effects on the prediction are:
1. CCN1 (gene expression): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2377.
2. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1367.
3. fp_0673 (fingerprint bit): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0823.
4. fp_0538 (fingerprint bit): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0409.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0177.
6. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0172.
These features provide insight into the factors influencing the predicted response of NVP-BSK805 on FU97.

## Model-Level Context
The global model context provides information on the training diagnostics, with a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. The per-drug cross-validated predictability for NVP-BSK805 is R2=0.2469, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to the interpretation of NVP-BSK805 on FU97.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather

---

## RPT-0032 - KW-2449 on F36P
_Source evidence: SHAP-0032_

## Executive Summary
The case RPT-0032 involves the drug KW-2449 and its effect on the cell line F36P. The observed log10(IC50) is 0.7418, which is close to the model-predicted value of 0.7676. The prediction error is -0.0258, indicating a slight underestimation by the model. The drug targets AURKA and FLT3, and the cell line is of haematopoietic and lymphoid tissue origin, specifically acute myeloid leukaemia.

## Evidence-Based Interpretation
The observed response of KW-2449 on F36P is interpreted based on the log10(IC50) values. The local drug/cell cohort baselines show that the sample percentile for the drug cohort is 28.0 and 57.6 for the cell cohort, indicating that the observed response is relatively sensitive compared to other drugs and cell lines. The model prediction is also close to the cohort baselines, suggesting that the model is able to capture the underlying patterns in the data.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. fp_0017: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1875.
2. CCN1: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1069.
3. fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0918.
4. fp_0673: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0885.
5. fp_0518: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0404.
6. fp_0688: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0296.
These features provide insight into the factors that contribute to the predicted response of KW-2449 on F36P.

## Model-Level Context
The global model context provides information on the training diagnostics, including the number of samples, features, and performance metrics such as R2, RMSE, and correlation. The per-drug cross-validated predictability for KW-2449 is 0.3149, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, offering a broader understanding of the model's behavior.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the SHAP values, which explain the RF prediction rather than the underlying biology. The local case evidence is separated from the global training diagnostics to avoid overgeneralization. The analysis is grounded in the provided metadata and does not invent pathways, biomarkers, or mechanisms not supported by the data. The results should be interpreted with caution, considering the limitations of the model and the complexity of the biological systems involved

---

## RPT-0033 - nutlin-3 on NCIH23
_Source evidence: SHAP-0033_

## Executive Summary
The report analyzes the response of nutlin-3 on NCIH23 cells, with an observed log10(IC50) of 1.0580 and a model-predicted log10(IC50) of 1.0653. The prediction error is -0.0073, indicating that the model slightly overestimates the sensitivity of NCIH23 cells to nutlin-3. The top TreeSHAP features suggest that several gene expression and fingerprint bits contribute to the prediction, pushing it toward higher log10(IC50) values (relative resistance).

## Evidence-Based Interpretation
The observed response of nutlin-3 on NCIH23 cells is close to the model prediction and cohort baselines. The drug target is MDM2, an inhibitor of the p53-MDM2 interaction. The per-drug cross-validated predictability for nutlin-3 is R2=0.2530, indicating moderate predictability. The cell lineage is Lung / Non-Small Cell Lung Cancer.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0955.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0621.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0567.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0169.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0163.
6. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0162.
These features are present in various compounds and have specific SMARTS annotations.

## Model-Level Context
The global model context includes training diagnostics such as train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385. The max-depth tuning best row has a max_depth of 20 and n_estimators of 100, with an r2 of 0.5459. The top global fingerprint features include fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, SDC4, CCN1, and PRSS23. The per-drug cross-validated predictability for nutlin-3 is R2=0.2530.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SH

---

## RPT-0034 - vorinostat on YAPC
_Source evidence: SHAP-0034_

## Executive Summary
The case RPT-0034 examines the response of vorinostat on the YAPC cell line, with an observed log10(IC50) of 1.0550 and a model-predicted log10(IC50) of 1.0653. The prediction error is -0.0103, indicating that the model slightly overestimates the sensitivity of YAPC to vorinostat. The observed log10(IC50) is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The observed response of vorinostat on YAPC can be interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.4576, with the sample percentile at 95.4. The cell cohort context has a mean log10(IC50) of 0.6910, with the sample percentile at 56.2. This suggests that YAPC is relatively resistant to vorinostat compared to other cell lines, but more sensitive than the average cell line in the drug cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0899.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0766.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0493.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0185.
5. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0155.
6. fp_0059 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0154.
These features are associated with higher log10(IC50) values, indicating relative resistance to vorinostat.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for vorinostat has an R2 of 0.2918. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should not be directly linked to the biology of vorinostat's action on YAPC without further evidence. It is essential to note that SHAP values explain the RF prediction rather than the underlying biology, and conclusions should be non-causal. Local case evidence should be separated from global training diagnostics to avoid overgeneralization.

---

## RPT-0035 - JQ-1 on SKMEL24
_Source evidence: SHAP-0035_

## Executive Summary
The case report RPT-0035 examines the response of JQ-1 on the SKMEL24 cell line, with an observed log10(IC50) of 1.0831 and a model-predicted log10(IC50) of 1.0653. The prediction error is +0.0178, indicating that the model slightly underestimates the resistance of SKMEL24 to JQ-1. The report aims to provide an evidence-based interpretation of this response using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed response of SKMEL24 to JQ-1 is close to the model prediction and cohort baselines. The drug target is BRDT, and the cell lineage is Skin/Melanoma. The per-drug R² on held-out cells is 0.25, indicating moderate predictability. The sample percentile is 72.2 in the drug cohort context and 46.0 in the cell cohort context.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0908.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0762.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0503.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0175.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0164.
6. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0148.
These features are associated with higher log10(IC50) values, indicating relative resistance to JQ-1.

## Model-Level Context
The global model context provides training diagnostics, including a train R² of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The max-depth tuning best row has a max depth of 20, 100 estimators, and an R² of 0.5459. The N-estimator tuning best row has a max depth of 10, 235 estimators, and a mean R² of 0.3803. The top global fingerprint features are similar to those found in the local analysis. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this analysis. The per-drug cross-validated predictability for JQ-1 is R² = 0.2458, indicating moderate predictability.

## Confidence and Caveats
The conclusions

---

## RPT-0036 - GDC-0879 on SNU61
_Source evidence: SHAP-0036_

## Executive Summary
The case report RPT-0036 examines the response of GDC-0879 on the SNU61 cell line. The observed log10(IC50) is 1.0741, and the model-predicted log10(IC50) is 1.0369, indicating a close prediction with a small error of +0.0371. The drug target is BRAF, an inhibitor of BRAF. The cell line SNU61 is of large intestine tissue and carcinoma histology.

## Evidence-Based Interpretation
The observed response of GDC-0879 on SNU61 is close to the model prediction and cohort baselines. The drug cohort context shows a mean log10(IC50) of 1.3279, with the sample at the 34.5th percentile. The cell cohort context has a mean log10(IC50) of 0.6059, with the sample at the 60th percentile. This suggests that SNU61 is relatively more resistant to GDC-0879 compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0662.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0561.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0471.
4. fp_0059 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0318.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0204.
These features are associated with higher log10(IC50) values, indicating relative resistance to GDC-0879.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The per-drug cross-validated predictability for GDC-0879 has an R2 of 0.2515. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these are not directly relevant to the local case evidence. It is essential to note that SHAP values explain the RF prediction rather than the biological mechanisms directly, and conclusions should be non-causal. The local case evidence should be separated from global training diagnostics to avoid overgeneralization.

---

## RPT-0037 - NVP-BSK805 on 253JBV
_Source evidence: SHAP-0037_

## Executive Summary
The case report RPT-0037 examines the response of NVP-BSK805 on the 253JBV cell line. The observed log10(IC50) is 1.0458, which is close to the model-predicted value of 1.0604. This report provides an evidence-based interpretation of the prediction, focusing on the top TreeSHAP features that contribute to the predicted log10(IC50) value.

## Evidence-Based Interpretation
The observed response of NVP-BSK805 on 253JBV is characterized by an observed log10(IC50) of 1.0458, which is close to the model-predicted value of 1.0604. The prediction error is -0.0147, indicating that the model slightly overestimates the log10(IC50) value. The drug cohort context shows a mean log10(IC50) of 1.0644, with the sample percentile at 45.4. The cell cohort context has a mean log10(IC50) of 0.7117, with the sample percentile at 51.2.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted log10(IC50) value are:
1. fp_0017: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1424.
2. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1023.
3. fp_0673: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0755.
4. fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0434.
5. fp_0513: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0187.
These features are grounded in local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, and prevalence across compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for NVP-BSK805 has an R2 of 0.2469. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these should be treated as training diagnostics and not held-out generalization.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the SHAP explanation of the RF prediction, rather than direct biological mechanisms. The local case evidence is separated from global training diagnostics to maintain the integrity of the analysis. The report is grounded in structured evidence and adheres to the rules of pharmacogenomics model explanation, avoiding invented pathways, biomarkers, or mechanisms not supported by the prompt.

---

## RPT-0038 - SN-38 on HCC1500
_Source evidence: SHAP-0038_

## Executive Summary
The case report RPT-0038 examines the response of SN-38 on the HCC1500 cell line. The observed log10(IC50) is -1.0253, and the RF-predicted log10(IC50) is -0.9158, indicating a prediction error of -0.1095. The report aims to provide an evidence-based interpretation of this response using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed response of SN-38 on HCC1500 is close to the model prediction and cohort baselines. The drug target is TOP1, and the cell lineage is breast ductal carcinoma. The per-drug R² on held-out cells is 0.33, indicating moderate predictability. The observed log10(IC50) is higher than the drug cohort mean (-1.4223) and lower than the cell cohort mean (0.8283).

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0329: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.5044.
2. fp_0059: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4343.
3. fp_0240: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1754.
4. fp_0065: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1725.
5. fp_0667: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1604.
6. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1185.
These features are present in various percentages of CTRPv2 compounds and have example compounds associated with them.

## Model-Level Context
The global model context provides training diagnostics, including a train R² of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for SN-38 is R²=0.3278. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these should be treated as training diagnostics and not held-out generalization.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The report separates local case evidence from global training diagnostics, and the results should be interpreted in the context of the specific cell line and drug combination. The cell subtype metadata is available, and the report is grounded in local metadata only, without inventing pathways, biomarkers, or mechanisms not supported by the prompt.

---

## RPT-0039 - apicidin on T84
_Source evidence: SHAP-0039_

## Executive Summary
The report analyzes the response of apicidin on T84 cells, with an observed log10(IC50) of 0.0286 and a model-predicted log10(IC50) of 0.0160. The prediction error is +0.0127, indicating that the model slightly underestimates the sensitivity of apicidin on T84 cells. The observed log10(IC50) is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The observed response of apicidin on T84 cells is interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.1742, with the sample percentile at 55.8. The cell cohort context shows a mean log10(IC50) of 0.3821, with the sample percentile at 31.7. This suggests that apicidin is relatively more effective on T84 cells compared to other cells, but less effective compared to other drugs on T84 cells.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are analyzed. The features pushing the prediction toward lower log10(IC50) (relative sensitivity) are:
* fp_0141 (SHAP = -0.7593): a fingerprint bit representing the SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, present in 1.5% of CTRPv2 compounds.
* fp_0876 (SHAP = -0.4527): a fingerprint bit representing the SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`, present in 1.5% of CTRPv2 compounds.
* fp_0582 (SHAP = -0.0471): a fingerprint bit representing the SMARTS `[#6](-[#6@H])-[#6@@H](-[#6]-[#6])-[#6]=[#6]`, present in 1.2% of CTRPv2 compounds.
The features pushing the prediction toward higher log10(IC50) (relative resistance) are:
* fp_0271 (SHAP = +0.0905): a fingerprint bit representing the SMARTS `[#7]-[#6](:[#6]):[#6]`, present in 5.0% of CTRPv2 compounds.
* fp_0617 (SHAP = +0.0455): a fingerprint bit representing the SMARTS `[#7]-[#6]-[#6](-[#7]-[#6])=[#8]`, present in 0.8% of CTRPv2 compounds.
* CCN1 (SHAP = +0.0448): a gene expression feature, near the cross-cell-line mean, recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context is provided, including training diagnostics (train_r2 = 0.4042

---

## RPT-0040 - indisulam on DANG
_Source evidence: SHAP-0040_

## Executive Summary
The report analyzes the response of indisulam on the DANG cell line, with an observed log10(IC50) of 1.0635 and a model-predicted log10(IC50) of 1.0653. The prediction error is -0.0017, indicating that the model slightly overestimates the sensitivity of the cell line to indisulam. The observed log10(IC50) is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The observed response of indisulam on DANG can be interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.7254, with the observed value at the 58.9th percentile. The cell cohort context shows a mean log10(IC50) of 0.9611, with the observed value at the 45.5th percentile. This suggests that the DANG cell line is relatively resistant to indisulam compared to other cell lines, but not extremely so.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0881.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0830.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0482.
4. fp_0059 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0353.
5. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0176.
These features are associated with higher log10(IC50) values, indicating relative resistance to indisulam.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for indisulam is R2=0.3312, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to the local interpretation of the DANG cell line response to indisulam.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, but do not directly imply biological relationships. The local case evidence is separated from global training diagnostics, and the analysis is limited to the available data. The results should not be considered as clinical advice, but rather as an interpretation of the observed response of the DANG cell line to indisulam in

---

## RPT-0041 - selumetinib on NCIH2009
_Source evidence: SHAP-0041_

## Executive Summary
The report analyzes the response of selumetinib on the NCIH2009 cell line, with an observed log10(IC50) of 1.0805 and a model-predicted log10(IC50) of 1.0604. The prediction error is +0.0201, indicating that the model slightly underestimates the actual log10(IC50) value. The observed log10(IC50) is close to the model prediction and cohort baselines.

## Evidence-Based Interpretation
The observed response of selumetinib on NCIH2009 can be interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 1.4319, with the observed value at the 32.2 percentile. The cell cohort context has a mean log10(IC50) of 0.5811, with the observed value at the 61.7 percentile. This suggests that NCIH2009 is relatively more resistant to selumetinib compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0992.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0766.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0486.
These features are associated with higher log10(IC50) values, indicating relative resistance to selumetinib. The presence of these features in the NCIH2009 cell line contributes to its predicted response.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for selumetinib is R2=0.2203, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to the specific case of selumetinib on NCIH2009 is limited. The cell subtype metadata is available, confirming that NCIH2009 is an adenocarcinoma. 
The report's conclusions are non-causal, and the SHAP values explain the RF prediction rather than the underlying biology. The local case evidence is separated from the global training diagnostics, providing a nuanced understanding of the selumetinib response on NCIH2009.

---

## RPT-0042 - teniposide on FUOV1
_Source evidence: SHAP-0042_

## Executive Summary
The case RPT-0042 involves the analysis of teniposide's effect on the FUOV1 cell line. The observed log10(IC50) is 0.0211, while the model-predicted log10(IC50) is -0.0472, indicating a prediction error of +0.0683. The drug target is TOP2A and TOP2B, and the cell lineage is ovary/Fallopian tube/ovarian epithelial tumor.

## Evidence-Based Interpretation
The observed response of teniposide on FUOV1 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of -0.3665, with the sample percentile being 56.4. The cell cohort context has a mean log10(IC50) of 0.7136, with the sample percentile being 24.1. This suggests that the observed response is close to the model prediction and cohort baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction are:
1. fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7254.
2. fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1617.
3. fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1205.
4. fp_0423: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0757.
5. fp_0876: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0587.
6. fp_0110: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0558.
These features are present in a small percentage of CTRPv2 compounds and have example compounds associated with them.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for teniposide is R2=0.3841. The top global fingerprint features and most common genes across predictable per-drug models are also available. However, these should be treated as training diagnostics and not held-out generalization.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than biology directly. The SHAP values provide insight into the features contributing to the prediction, but the relationships between these features and the biological mechanisms are not explicitly stated. The local case evidence is separated from global training diagnostics, and the analysis is grounded in the provided metadata and evidence. The cell subtype metadata is available, and the analysis is based on the provided data sources.

---

## RPT-0043 - etoposide on MOLM16
_Source evidence: SHAP-0043_

## Executive Summary
The case report RPT-0043 examines the response of etoposide on the MOLM16 cell line. The observed log10(IC50) is -0.0727, and the RF-predicted log10(IC50) is 0.1059, indicating a prediction error of -0.1786. The report aims to provide an evidence-based interpretation of this prediction using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed response of etoposide on MOLM16 is close to the model prediction and cohort baselines. The drug target is TOP2A, and the cell lineage is Myeloid/Acute Myeloid Leukemia. The per-drug R² on held-out cells is 0.31, indicating moderate predictability. The local drug cohort context shows a mean log10(IC50) of 0.4832, while the cell cohort context has a mean log10(IC50) of 0.0891.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are:
1. fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.5436.
2. fp_0535: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1951.
3. fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1195.
4. CCN1 (3491): pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1038.
These features are grounded in local metadata, including gene recurrence counts, target matches, fingerprint SMARTS annotations, and prevalence across compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R² of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The max-depth tuning best row has an R² of 0.5459, and the N-estimator tuning best row has a mean R² of 0.3803. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for etoposide is R²=0.3081.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The report separates local case evidence from global training diagnostics, and the results should be interpreted in the context of the specific cell line and drug combination. The cell subtype metadata is available, and the report is grounded in local metadata and evidence-based interpretations.

---

## RPT-0044 - PX-12 on RH18
_Source evidence: SHAP-0044_

## Executive Summary
The case of PX-12 on RH18 is characterized by an observed log10(IC50) of 1.4239, which is close to the model-predicted value of 1.4309. The prediction error is -0.0070, indicating a slight underestimation by the model. The sample falls within the 40.5th percentile of the drug cohort and the 73.1st percentile of the cell cohort.

## Evidence-Based Interpretation
The observed response of PX-12 on RH18 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 1.4466, with the sample falling below this value. The cell cohort context has a mean log10(IC50) of 0.7651, with the sample falling above this value. The model prediction is close to the observed value, suggesting that the model is able to capture the underlying patterns in the data.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case are:
1. fp_0777, which pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7414.
2. fp_0141, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.5402.
3. fp_0535, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.1124.
4. fp_0518, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0813.
5. fp_0876, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0804.
6. fp_0175, which pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of 0.0785.
These features are present in various percentages of CTRPv2 compounds and have example compounds associated with them.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for PX-12 is R2=0.2858, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but are not directly relevant to this specific case.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the SHAP explanation of the RF prediction, rather than the underlying biology. The local case evidence is separated from the global training diagnostics, and the analysis is limited to the provided data and features. The results should be interpreted with caution, considering the complexity of the model and the potential for overfitting or underfitting. Additionally, the availability of cell subtype metadata (alveolar) may provide further context, but

---

## RPT-0045 - PX-12 on ONCODG1
_Source evidence: SHAP-0045_

## Executive Summary
The report analyzes the response of PX-12 on ONCODG1, an ovarian adenocarcinoma cell line, using a random forest (RF) model. The observed log10(IC50) is 1.3392, close to the model-predicted value of 1.3879. The top TreeSHAP features influencing the prediction are fingerprint bits fp_0777, fp_0141, fp_0535, fp_0876, fp_0518, and fp_0994.

## Evidence-Based Interpretation
The observed response of PX-12 on ONCODG1 is interpreted based on the log10(IC50) values. The model-predicted log10(IC50) is slightly higher than the observed value, indicating a potential overestimation of resistance. The prediction error is -0.0487, and the absolute error is 0.0487. The global mean log10(IC50) is 0.6392, which is lower than the observed value.

## Feature and Neighborhood Analysis
The top TreeSHAP features are analyzed to understand their contribution to the prediction. 
1. fp_0777 pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7644.
2. fp_0141 pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.5757.
3. fp_0535, fp_0876, fp_0518, and fp_0994 also push the prediction toward higher log10(IC50) (relative resistance) with SHAP values of +0.1167, +0.0816, +0.0789, and +0.0776, respectively.
These features are fingerprint bits with specific SMARTS annotations, and their presence or absence in the compound influences the predicted log10(IC50) value.

## Model-Level Context
The global model context provides information about the training diagnostics, including the number of samples (181811), features (2024), train R2 (0.4042), train RMSE (1.0264), and train correlation (0.6385). The per-drug cross-validated predictability for PX-12 is R2=0.2858, indicating moderate predictability. The most common genes across predictable per-drug models include MYOF, TNFRSF12A, and SDC4. The cell subtype metadata is available, and the ONCODG1 cell line is classified as an adenocarcinoma.
The report is based on the analysis of the TreeSHAP values, fingerprint bits, and cell line metadata, providing insights into the predicted response of PX-12 on ONCODG1.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the RF model's prediction. The SHAP values explain the RF prediction rather than the underlying biology. The report is limited to the local case evidence and does not provide global generalization. The training diagnostics, such as train R2 and train RMSE, are only relevant to the training data and do not reflect the

---

## RPT-0046 - olaparib on SNU398
_Source evidence: SHAP-0046_

## Executive Summary
The case report RPT-0046 examines the response of olaparib on the SNU398 cell line. The observed log10(IC50) is 1.0785, which is close to the model-predicted value of 1.0653. This report provides an evidence-based interpretation of the prediction, focusing on the top TreeSHAP features that contribute to the predicted log10(IC50) value.

## Evidence-Based Interpretation
The observed response of olaparib on SNU398 is characterized by an observed log10(IC50) of 1.0785, which falls within the 21.1 percentile of the drug cohort and the 56.5 percentile of the cell cohort. The model-predicted log10(IC50) is 1.0653, indicating a slight underestimation of the observed value. The prediction error is +0.0132, suggesting that the model is reasonably accurate in predicting the response of olaparib on SNU398.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted log10(IC50) value are:
1. fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1927.
2. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0883.
3. fp_0017: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0509.
4. fp_0518: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0444.
5. fp_0876: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0374.
These features provide insight into the factors influencing the predicted response of olaparib on SNU398.

## Model-Level Context
The global model context indicates that the training fit has an R2 of 0.4042, RMSE of 1.0264, and correlation of 0.6385. However, these metrics are only relevant for training diagnostics and do not reflect held-out generalization. The per-drug cross-validated predictability for olaparib has an R2 of 0.2251, suggesting moderate predictability. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this case report.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, but do not directly imply biological relationships. The local case evidence should be separated from global training diagnostics to avoid overgeneralization. The report is grounded in the provided metadata and does not invent pathways, biomarkers, or mechanisms beyond the supported evidence.

---

## RPT-0047 - TG-101348 on JHH4
_Source evidence: SHAP-0047_

## Executive Summary
The case of TG-101348 on JHH4 is characterized by an observed log10(IC50) of 0.8964, which is close to the model-predicted value of 0.8849. The drug target is JAK2, an inhibitor of Janus kinase 2. The cell line JHH4 is of liver origin, specifically hepatocellular carcinoma. The per-drug cross-validated R² for TG-101348 is 0.2455, indicating moderate predictability.

## Evidence-Based Interpretation
The observed response of TG-101348 on JHH4 can be interpreted in the context of the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.6573, with the sample percentile at 68.1. The cell cohort context has a mean log10(IC50) of 0.7239, with the sample percentile at 50.0. This suggests that the observed response is relatively sensitive compared to the cell cohort but less sensitive compared to the drug cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this case include fingerprint bits and gene expression values. The features pushing the prediction toward lower log10(IC50) (relative sensitivity) are fp_0059, fp_0673, and fp_0227. These features have SHAP values of -0.1567, -0.0690, and -0.0404, respectively. On the other hand, features pushing the prediction toward higher log10(IC50) (relative resistance) are fp_0017, fp_0065, and CCN1, with SHAP values of 0.1150, 0.0846, and 0.0703, respectively. These features provide insight into the structural and genetic factors influencing the predicted response.

## Model-Level Context
The global model context provides training diagnostics, including a training R² of 0.4042, RMSE of 1.0264, and correlation of 0.6385. The max-depth tuning and N-estimator tuning results indicate optimal hyperparameters for the model. The top global fingerprint features and most common genes across predictable per-drug models offer a broader understanding of the model's behavior. However, it is essential to note that these diagnostics are based on training data and should not be considered as held-out generalization. The per-drug cross-validated predictability for TG-101348 is 0.2455, indicating moderate predictability. Cell subtype metadata is available, confirming the hepatocellular carcinoma origin of the JHH4 cell line.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and explain the RF prediction rather than the underlying biology. The SHAP values provide insight into the features driving the predicted response but should not be interpreted as direct biological mechanisms. The local case evidence should be separated from the global training diagnostics to avoid overgeneralization. The analysis is grounded in the provided data and metadata, without inventing unsupported pathways, biomarkers, or mechanisms. Clinical advice is not provided, and the report is limited to the interpretation

---

## RPT-0048 - BRD-K80183349 on KYSE70
_Source evidence: SHAP-0048_

## Executive Summary
The case report RPT-0048 examines the response of BRD-K80183349 on the KYSE70 cell line. The observed log10(IC50) is 0.9910, close to the model-predicted value of 1.0253. This report provides an evidence-based interpretation of the prediction, focusing on the top TreeSHAP features that influence the predicted log10(IC50) value.

## Evidence-Based Interpretation
The observed response of BRD-K80183349 on KYSE70 is characterized by an observed log10(IC50) of 0.9910, which is close to the model-predicted value of 1.0253. The prediction error is -0.0343, indicating a slight underestimation by the model. The global mean log10(IC50) is 0.6392, and the sample percentile is 55.0, suggesting that KYSE70 is relatively more resistant to BRD-K80183349 compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the predicted log10(IC50) value are:
1. fp_0141: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1296.
2. fp_0518: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0694.
3. CCN1 (3491): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0586.
4. fp_0017: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0489.
5. fp_0513: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0184.
These features provide insight into the molecular characteristics of BRD-K80183349 that contribute to its predicted response on KYSE70.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for BRD-K80183349 is R2=0.3317, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, offering a broader understanding of the model's performance and feature importance.

## Confidence and Caveats
The conclusions drawn from this report are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, not the underlying biology. The report is grounded in local case evidence, separate from global training diagnostics. The cell subtype metadata is available, and the report focuses on the specific case of BRD-K80183349 on KYSE70, without providing clinical advice or inventing unsupported pathways, biomarkers, or mechanisms.

---

## RPT-0049 - olaparib on RL952
_Source evidence: SHAP-0049_

## Executive Summary
The case report RPT-0049 examines the response of olaparib on the RL952 cell line. The observed log10(IC50) is 1.0778, which is close to the model-predicted value of 1.0653. The prediction error is +0.0125, indicating a slight overestimation of sensitivity. The report aims to provide an evidence-based interpretation of this response using TreeSHAP features and local metadata.

## Evidence-Based Interpretation
The observed response of olaparib on RL952 can be interpreted by analyzing the top TreeSHAP features. The features fp_0141, CCN1, fp_0017, and fp_0059 push the prediction toward higher log10(IC50) (relative resistance), while fp_0518 and fp_0876 push the prediction toward lower log10(IC50) (relative sensitivity). The presence of these features in the olaparib molecule and the RL952 cell line contributes to the predicted response.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:
1. fp_0141: a fingerprint bit with a SMARTS annotation `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, present in 1.5% of CTRPv2 compounds.
2. CCN1: a gene expression feature with a z-score of +0.69, recurs in 71 predictable-drug RF signatures.
3. fp_0017: a fingerprint bit with a SMARTS annotation `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`, present in 2.3% of CTRPv2 compounds.
4. fp_0518: a fingerprint bit with a SMARTS annotation `[#6]:[#7]:[#8]`, present in 4.0% of CTRPv2 compounds.
5. fp_0876: a fingerprint bit with a SMARTS annotation `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`, present in 1.5% of CTRPv2 compounds.
6. fp_0059: a fingerprint bit with a SMARTS annotation `[#6]=[#6]-[#6@H]`, present in 6.0% of CTRPv2 compounds.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for olaparib is R2=0.2251. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these should be treated as training diagnostics and not held-out generalization.

## Confidence

---

## RPT-0050 - JQ-1 on SF295
_Source evidence: SHAP-0050_

## Executive Summary
The case RPT-0050 involves the drug JQ-1 and its effect on the cell line SF295. The observed log10(IC50) is 1.0301, which is close to the model-predicted value of 1.0653. The prediction error is -0.0352, indicating that the model slightly overestimates the sensitivity of SF295 to JQ-1. The drug target is BRDT, and the cell lineage is CNS/Brain / Diffuse Glioma.

## Evidence-Based Interpretation
The observed response of JQ-1 on SF295 can be explained by the local drug/cell cohort baselines. The drug cohort context shows a mean log10(IC50) of 0.3443, with the sample percentile being 70.3. The cell cohort context has a mean log10(IC50) of 0.7466, with the sample percentile being 52.1. This suggests that SF295 is relatively more resistant to JQ-1 compared to other cell lines.

## Feature and Neighborhood Analysis
The top TreeSHAP features that contribute to the prediction are:
1. CCN1 (gene expression): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0910.
2. fp_0141 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0800.
3. fp_0017 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0505.
4. fp_0513 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0173.
5. fp_0535 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0168.
6. fp_0723 (fingerprint bit): pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0148.
These features are present in various compounds and are associated with specific SMARTS annotations.

## Model-Level Context
The global model context provides training diagnostics, including a train R2 of 0.4042, train RMSE of 1.0264, and train correlation of 0.6385. The per-drug cross-validated predictability for JQ-1 is R2=0.2458, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these are not directly relevant to the local case evidence.

## Confidence and Caveats
The conclusions drawn from this analysis are non-causal and based on the RF prediction rather than biological mechanisms. The SHAP values explain the RF prediction, but do not directly imply biological relationships. The local case evidence is separate from the global training diagnostics, and the results should be interpreted in the context of the specific drug-cell pair. The

---
