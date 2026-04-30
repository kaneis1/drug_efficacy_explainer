# Teacher Pairs - Llama-3.3-70B-Instruct - test

## RPT-0009 - linifanib on EOL1
_Split: test_

## Executive Summary
The sample EOL1 treated with linifanib exhibits an exceptionally sensitive response with an observed AUC of 0.2525, which is significantly lower than the predicted AUC of 12.5787. This discrepancy suggests that the model underestimated the sensitivity of EOL1 to linifanib.

## Evidence-Based Interpretation
The observed AUC of 0.2525 indicates a high sensitivity of EOL1 to linifanib, which is consistent with the cell line's subtype, acute myeloid leukaemia. The large negative prediction error (-12.3262) suggests that the model did not accurately capture the underlying factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression; SHAP=-0.7195), which has a negative SHAP value, indicating that it pushes the prediction towards lower AUC (higher sensitivity). The absence of certain fingerprint features (fp_0204, fp_0443, fp_0062, and fp_0227) also contributes to the predicted AUC, with positive SHAP values indicating that their presence would increase the predicted AUC (decrease sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The model was trained on a dataset with 311258 samples and 2024 features. The per-drug cross-validated predictability for linifanib has an R2 of 0.1316, indicating moderate predictability. The most common genes across predictable per-drug models include TNFRSF12A, which is also a top feature in this sample's TreeSHAP analysis.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values are not direct causal evidence and should be treated as explanations of the fitted Random Forest prediction for this sample. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results may not generalize to other cell lines or drugs, and further experimentation is needed to confirm the findings.

---

## RPT-0017 - dasatinib on EOL1
_Split: test_

## Executive Summary
The sample in question involves the drug dasatinib and the cell line EOL1, with an observed AUC of 0.1834, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of EOL1 to dasatinib.

## Evidence-Based Interpretation
The observed AUC of 0.1834 is significantly lower than the global mean AUC across all pairs (12.8580), indicating greater sensitivity. The drug cohort and cell cohort summaries also suggest that EOL1 is more sensitive to dasatinib compared to other cell lines and drugs. The top TreeSHAP features, including fp_0367 and fp_0760, have negative SHAP values, pushing the prediction towards lower AUC/sensitivity, while features like fp_0204 and fp_0443 have positive SHAP values, pushing the prediction towards higher AUC/resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the molecular characteristics contributing to the observed sensitivity. Fingerprint bits fp_0367 and fp_0760 are present in dasatinib and have negative SHAP values, suggesting that these features contribute to the drug's sensitivity in EOL1. In contrast, fingerprint bits fp_0204 and fp_0443 are absent in dasatinib and have positive SHAP values, indicating that their absence may also contribute to the observed sensitivity. The same-drug and same-cell cohort examples provide additional context, with other cell lines (KYO1 and LAMA84) showing similar sensitivity to dasatinib, and other drugs (foretinib and dinaciclib) showing similar sensitivity in EOL1.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). While these metrics are not directly applicable to this sample, they suggest that the model has a moderate level of fit to the training data. The per-drug cross-validated predictability for dasatinib (R2=0.2203) indicates some level of predictability, but the model's performance may be limited by the complexity of the data. The availability of cell subtype metadata (acute myeloid leukaemia) provides additional context for the sample, but does not directly influence the interpretation of the results.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the molecular characteristics of dasatinib. However, the model's performance is limited by its training data and may not generalize to other contexts. The absence of direct causal evidence and the reliance on training diagnostics rather than held-out performance metrics are important caveats to consider when interpreting the results. Additionally, the complexity of the data and the limited predictability of the model for dasatinib suggest that the results should be treated with caution and considered in the context of additional evidence.

---

## RPT-0045 - tandutinib on EOL1
_Split: test_

## Executive Summary
The sample EOL1 treated with tandutinib exhibits an observed AUC of 0.7004, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of EOL1 to tandutinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a SHAP value of -0.6376, indicating that lower expression of TNFRSF12A pushes the prediction towards lower AUC (greater sensitivity). Fingerprint features such as fp_0227, fp_0062, fp_0806, and fp_0443 also contribute to the prediction, with positive SHAP values indicating that their presence or absence pushes the prediction towards higher AUC (greater resistance).

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that EOL1 is more sensitive to tandutinib compared to other cell lines in the same-drug cohort, such as MOLM13 and MV411. Similarly, EOL1 is more sensitive to other drugs in the same-cell cohort, such as foretinib and dinaciclib. The top global fingerprint features and most common genes across predictable per-drug models provide additional context for the prediction, with TNFRSF12A being a prominent gene in 166 predictable per-drug models.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was tuned for max-depth and n-estimators, with the best parameters being max_depth=20 and n_estimators=100. The per-drug cross-validated predictability for tandutinib is relatively low, with an R2 of 0.0849. The cell subtype metadata confirms that EOL1 is an acute myeloid leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the per-drug cross-validated predictability for tandutinib is relatively low, which may impact the confidence in the prediction.

---

## RPT-0062 - dasatinib on JK1
_Split: test_

## Executive Summary
The sample JK1 treated with dasatinib exhibits an observed AUC of 1.2201, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of JK1 to dasatinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction error are fp_0367, fp_0760, fp_0204, fp_0062, and TNFRSF12A (51330). The presence of fp_0367 and fp_0760, and the absence of fp_0204 and fp_0062, push the prediction towards lower AUC (greater sensitivity). The gene expression of TNFRSF12A (51330) has a positive SHAP value, indicating that it contributes to higher AUC (lower sensitivity), but its effect is outweighed by the other features.

## Feature and Neighborhood Analysis
The local neighborhood analysis reveals that the cell lines KYO1 and EOL1, which are also of haematopoietic and lymphoid tissue origin, exhibit higher sensitivity to dasatinib (AUC values of 0.1676 and 0.1834, respectively). In contrast, the drugs leptomycin B and oligomycin A, which target different genes, exhibit higher AUC values (1.4886 and 1.5326, respectively) when treated with the JK1 cell line.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for dasatinib is 0.2203, indicating moderate predictability. The cell subtype metadata is available, which may be useful for further analysis.

## Confidence and Caveats
The interpretation of the results is grounded in the local SHAP values and feature analysis. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and any conclusions drawn from these metrics should be interpreted with caution.

---

## RPT-0066 - RITA on BCP1
_Split: test_

## Executive Summary
The sample RPT-0066, involving the drug RITA and cell line BCP1, exhibits an observed AUC of 1.5251, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on the local SHAP values and global model context.

## Evidence-Based Interpretation
The observed AUC of 1.5251 is significantly lower than the predicted AUC of 12.6318, indicating a large negative prediction error. This suggests that the sample is more sensitive to RITA than expected. The top TreeSHAP features contributing to this prediction error include TNFRSF12A (gene_expression; SHAP=-0.6659), fp_0204 (fingerprint_bit; SHAP=+0.1650), and fp_0062 (fingerprint_bit; SHAP=-0.0878). These features push the prediction towards lower AUC (greater sensitivity) or higher AUC (greater resistance).

## Feature and Neighborhood Analysis
The top TreeSHAP feature, TNFRSF12A, has a negative SHAP value, indicating that its low expression level (below the cross-cell-line mean) contributes to the increased sensitivity of the sample to RITA. The fingerprint bits fp_0204 and fp_0062 also have positive and negative SHAP values, respectively, influencing the prediction. The presence or absence of these fingerprint bits in the drug's molecular structure may affect its interaction with the cell line. The neighborhood analysis reveals that similar cell lines, such as TE441T and SET2, also exhibit sensitivity to RITA, while other drugs, like leptomycin B and oligomycin A, show sensitivity in the same cell line BCP1.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The top global fingerprint features and most common genes across predictable per-drug models are also provided, offering insight into the broader patterns in the data. The per-drug cross-validated predictability for RITA is relatively low (R2=0.2078), suggesting that the model's performance may vary for this specific drug.

## Confidence and Caveats
The interpretation of the results is grounded in the local SHAP values and global model context. However, it is essential to acknowledge the limitations of the analysis. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated with caution, as they are training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, but its impact on the results is not explicitly explored in this analysis.

---

## RPT-0073 - compound 1B on JHUEM1
_Split: test_

## Executive Summary
The sample in question involves compound 1B and cell line JHUEM1, with an observed AUC of 2.5603, indicating exceptional sensitivity relative to the predicted response and cohort baselines. The prediction error is -11.0008, suggesting that the model overestimated the AUC.

## Evidence-Based Interpretation
The observed AUC of 2.5603 is lower than the predicted AUC of 13.5611, indicating that compound 1B is more sensitive than expected against the JHUEM1 cell line. This sensitivity is also evident when compared to the drug cohort (754 pairs) and cell cohort (411 pairs), where the sample percentile is 0.3 and 1.0, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include TNFRSF12A (gene_expression; SHAP=+0.2007), fp_0443 (fingerprint_bit; SHAP=+0.1201), fp_0204 (fingerprint_bit; SHAP=+0.1053), fp_0367 (fingerprint_bit; SHAP=+0.0960), and fp_0062 (fingerprint_bit; SHAP=-0.0624). These features suggest that the absence of certain fingerprint bits and the expression of TNFRSF12A contribute to the predicted AUC. However, the negative SHAP value for fp_0062 indicates that its absence pushes the prediction towards lower AUC/sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. The per-drug cross-validated predictability for compound 1B is R2=0.0545, indicating limited predictability. Cell subtype metadata is available, confirming that the JHUEM1 cell line is an adenocarcinoma. It is essential to note that these metrics are training diagnostics and should not be treated as held-out performance. The model's limitations and potential biases should be considered when interpreting the results.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated with caution, as they are training diagnostics rather than held-out performance. Additionally, the per-drug cross-validated predictability for compound 1B is limited, which may impact the accuracy of the predictions.

---

## RPT-0077 - barasertib on EOL1
_Split: test_

## Executive Summary
The sample RPT-0077, involving the drug barasertib on the EOL1 cell line, exhibits an observed AUC of 1.0544, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.0544 is significantly lower than the predicted AUC of 12.0153, suggesting that the EOL1 cell line is more sensitive to barasertib than expected. The top TreeSHAP features contributing to this sensitivity include TNFRSF12A (gene_expression; SHAP=-0.4578), fp_0227 (fingerprint_bit; SHAP=-0.2357), fp_0367 (fingerprint_bit; SHAP=-0.1668), fp_0131 (fingerprint_bit; SHAP=-0.1091), and fp_0204 (fingerprint_bit; SHAP=+0.0991). These features push the prediction towards lower AUC (greater sensitivity) or higher AUC (lower sensitivity) based on their SHAP values.

## Feature and Neighborhood Analysis
The top TreeSHAP features suggest that the expression of TNFRSF12A and the presence of specific fingerprint bits (fp_0227, fp_0367, fp_0131) contribute to the increased sensitivity of the EOL1 cell line to barasertib. The absence of fp_0204 also contributes to the sensitivity. The same-drug cohort examples (MOLT16 and OCILY19) and same-cell cohort examples (foretinib and dinaciclib) provide additional context, indicating that the EOL1 cell line is more sensitive to barasertib compared to other cell lines and drugs.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for barasertib is R2=0.3743. While this information provides context, it is essential to note that these metrics are training diagnostics and not held-out performance.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to recognize that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions and feature importance should be treated with caution, and any global model metrics referenced should be considered as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, but its relevance to the observed sensitivity is not explicitly stated.

---

## RPT-0121 - daporinad on A673
_Split: test_

## Executive Summary
The sample RPT-0121, involving the drug daporinad on the A673 cell line, exhibits an observed AUC of 1.3954, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.3954 is significantly lower than the predicted AUC of 11.8994, indicating a large negative prediction error. This suggests that the model underestimated the sensitivity of the A673 cell line to daporinad. The top TreeSHAP features, including TNFRSF12A, fp_0706, fp_0062, fp_0443, and fp_0830, contribute to this prediction error. Notably, TNFRSF12A has a SHAP value of -0.7232, indicating that its low expression level in the A673 cell line pushes the prediction towards lower AUC (greater sensitivity).

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the factors contributing to the sensitivity of the A673 cell line to daporinad. TNFRSF12A, a gene with low expression in the A673 cell line, is a key contributor to this sensitivity. The fingerprint features, such as fp_0706, fp_0062, fp_0443, and fp_0830, also play a role in shaping the predicted response. The presence or absence of these features in the daporinad molecule and their frequency in the CTRPv2 compound library provide context for their contribution to the predicted response.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics indicate the model's performance on the training data but should not be interpreted as held-out generalization. The top global fingerprint features and most common genes across predictable per-drug models provide additional context for the model's behavior. The per-drug cross-validated predictability for daporinad, with an R2 of 0.1876, suggests that the model has limited ability to predict the response of daporinad across different cell lines.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to recognize that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The model's performance on the training data should not be extrapolated to held-out data, and the results should be treated with caution. Additionally, the molecular descriptions and feature analysis are limited to the local data and should not be generalized to other contexts without further validation.

---

## RPT-0133 - birinapant on SKOV3
_Split: test_

## Executive Summary
The sample RPT-0133, involving the drug birinapant on the SKOV3 cell line, exhibits an observed AUC of 3.6946, which is exceptionally sensitive compared to the predicted AUC of 14.0506 and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on the SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (-10.3560) suggests that the model underestimated the sensitivity of birinapant on SKOV3 cells. The observed AUC is lower than the global mean AUC across all pairs (12.8580), indicating greater sensitivity. The drug and cell cohorts also show that this sample is more sensitive than expected, with a sample percentile of 0.5 in the drug cohort and 0.2 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error are fp_0443 (SHAP=-0.3551), fp_0767 (SHAP=+0.2438), fp_0504 (SHAP=+0.1826), fp_1009 (SHAP=+0.1696), and fp_0864 (SHAP=+0.1533). The presence of fp_0443 and absence of fp_0767, fp_0504, fp_1009, and fp_0864 in birinapant contribute to the observed sensitivity. The same-drug cohort examples (KYM1 and WSUDLCL2) and same-cell cohort examples (GSK461364 and LBH-589) also exhibit more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for birinapant (R2=0.0192) is relatively low, indicating that the model may not capture the underlying mechanisms well for this specific drug.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge the limitations of the model and the potential biases in the data. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. Additionally, the cell subtype metadata is available, but its impact on the prediction is not explicitly evaluated in this analysis. Therefore, the results should be considered in the context of these limitations and caveats.

---

## RPT-0136 - AT13387 on SUPM2
_Split: test_

## Executive Summary
The sample RPT-0136, involving the drug AT13387 on the SUPM2 cell line, exhibits an exceptionally sensitive response with an observed AUC of 2.8574, which is significantly lower than the predicted AUC of 13.1962. This discrepancy suggests that the model underestimated the sensitivity of AT13387 in this specific context.

## Evidence-Based Interpretation
The observed AUC of 2.8574 indicates a higher sensitivity of the SUPM2 cell line to AT13387 compared to the predicted response. The large negative prediction error of -10.3388 further emphasizes the model's underestimation of the drug's efficacy in this case. The sample's percentile rank of 1.0 within the drug cohort and 3.8 within the cell cohort reinforces its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include fingerprint bits (fp_0443, fp_1009, fp_0367, and fp_0017) and gene expression (TNFRSF12A). Positive SHAP values for fp_0443, fp_0367, and TNFRSF12A suggest that these features would increase the predicted AUC (i.e., decrease sensitivity) if present or highly expressed. In contrast, the negative SHAP value for fp_1009 and fp_0017 indicates that their presence would decrease the predicted AUC (i.e., increase sensitivity). The absence of fp_0443 and fp_0367, and the presence of fp_1009 and fp_0017 in the sample, may contribute to the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics indicate a reasonable fit, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for AT13387 (R2=0.2709) suggests moderate predictability. The most common genes across predictable per-drug models, including TNFRSF12A, may be relevant for understanding the drug's mechanism of action. However, it is essential to consider the limitations of the model and the specific context of the sample when interpreting these results.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values provide insights into the features contributing to the predicted response but do not constitute direct causal evidence. The global model metrics, such as train_r2, train_rmse, and train_corr, are training diagnostics and should not be used to evaluate the model's performance on unseen data. Additionally, the absence of certain information, such as clinical advice, is intentional, as it is outside the scope of this analysis.

---

## RPT-0143 - cytarabine hydrochloride on KE37
_Split: test_

## Executive Summary
The KE37 cell line exhibits exceptional sensitivity to cytarabine hydrochloride, with an observed AUC of 2.8796, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of KE37 to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 2.8796 indicates that KE37 is more sensitive to cytarabine hydrochloride than expected. The large negative prediction error (-10.3048) and low sample percentile (1.4) in the drug cohort further support this interpretation. The presence of certain fingerprint features, such as fp_0443, and the low expression of TNFRSF12A (51330) may contribute to this increased sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include fp_0443 (SHAP=-0.7287), fp_0504 (SHAP=+0.5512), and fp_0767 (SHAP=+0.4276). The presence of fp_0443 and the absence of fp_0504 and fp_0767 may push the prediction towards lower AUC (greater sensitivity). The low expression of TNFRSF12A (51330) (SHAP=-0.3748) also contributes to the increased sensitivity. The same-drug cohort examples (e.g., BV173 and REH) and same-cell cohort examples (e.g., SB-743921 and leptomycin B) provide additional context, suggesting that KE37 is more sensitive to cytarabine hydrochloride than other cell lines.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The cell subtype metadata (acute lymphoblastic T cell leukaemia) is available, but its impact on the model's prediction is not directly assessed.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the absence of certain information, such as the gene target for cytarabine hydrochloride, may limit the interpretation of the results.

---

## RPT-0153 - daporinad on IMR32
_Split: test_

## Executive Summary
The observed AUC of daporinad on the IMR32 cell line is 1.7024, which is exceptionally sensitive compared to the predicted AUC of 11.8994. This sample was selected due to its large negative prediction error, indicating that the actual response is more sensitive than expected.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are TNFRSF12A, fp_0706, fp_0062, fp_0443, and fp_0830. The negative SHAP values for TNFRSF12A, fp_0706, fp_0062, and fp_0830 suggest that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP value for fp_0443 pushes the prediction towards higher AUC (greater resistance).

## Feature and Neighborhood Analysis
The local analysis reveals that the IMR32 cell line has a low expression of TNFRSF12A, which is below the cross-cell-line mean. The presence of fp_0706 and absence of fp_0062, fp_0443, and fp_0830 in the molecular structure of daporinad also contribute to the observed sensitivity. The same-drug cohort examples show that daporinad is more sensitive on other cell lines, such as GA10 and 697. The same-cell cohort examples show that other drugs, such as SB-743921 and paclitaxel, are also more sensitive on the IMR32 cell line.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for daporinad is relatively low (R2=0.1876), indicating that the model may not capture all the underlying mechanisms of action for this drug.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance.

---

## RPT-0163 - methotrexate on SUPM2
_Split: test_

## Executive Summary
The sample SUPM2 treated with methotrexate exhibits an exceptionally sensitive response, with an observed AUC of 1.9983, which is significantly lower than the predicted AUC of 12.1192. This discrepancy suggests that the model underestimated the sensitivity of SUPM2 to methotrexate.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top contributing features to the predicted AUC are fingerprint bits fp_0538 and fp_0694, which have negative SHAP values, indicating that their presence pushes the prediction towards lower AUC (greater sensitivity). Additionally, the gene expression of TNFRSF12A has a positive SHAP value, suggesting that its high expression level contributes to the predicted resistance. However, the overall effect of these features is overridden by the strong negative prediction error, resulting in an observed sensitive response.

## Feature and Neighborhood Analysis
The top TreeSHAP features, including fp_0538 and fp_0694, are present in a small percentage of CTRPv2 compounds, suggesting that these fingerprint bits may be unique to certain compounds. The presence of these features in methotrexate may contribute to its exceptional sensitivity in SUPM2 cells. The gene expression of TNFRSF12A is near the cross-cell-line mean, but its positive SHAP value indicates that it may play a role in the predicted resistance. The same-drug cohort examples, such as EOL1 and TF1, also exhibit sensitive responses, suggesting that methotrexate may be generally effective against haematopoietic and lymphoid tissue cells.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models provide insight into the overall structure of the data. The per-drug cross-validated predictability for methotrexate is relatively low (R2=0.1418), indicating that the model may not capture the full complexity of methotrexate's response. The availability of cell subtype metadata, such as anaplastic large cell lymphoma, may provide additional context for understanding the response of SUPM2 cells to methotrexate.

## Confidence and Caveats
The interpretation of the results is limited by the availability of data and the constraints of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and further investigation is necessary to fully understand the mechanisms underlying the response of SUPM2 cells to methotrexate.

---

## RPT-0181 - AT13387 on GA10
_Split: test_

## Executive Summary
The sample GA10 treated with AT13387 exhibits an observed AUC of 2.4924, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a SHAP value of -0.5999, indicating that the low expression of TNFRSF12A in this sample pushes the prediction towards lower AUC (greater sensitivity). The presence of fingerprint feature fp_1009 and the absence of fp_0443, fp_0204, and fp_0062 also contribute to the predicted AUC.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the sample GA10 has a low expression of TNFRSF12A, which is markedly below the cross-cell-line mean. The absence of certain fingerprint features, such as fp_0443 and fp_0204, also contributes to the predicted AUC. The presence of fp_1009, which is present in 9.1% of CTRPv2 compounds, also plays a role in the predicted AUC.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features include fp_0443, fp_0767, and fp_0925. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4. The per-drug cross-validated predictability for AT13387 is R2=0.2709.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. The cell subtype metadata is available, and the sample GA10 is classified as Burkitt lymphoma.

---

## RPT-0186 - dasatinib on JURLMK1
_Split: test_

## Executive Summary
The sample RPT-0186, involving the drug dasatinib on the JURLMK1 cell line, exhibits an exceptionally sensitive response with an observed AUC of 0.2495, which is significantly lower than the RF-predicted AUC of 10.2678. This discrepancy suggests that the model underestimated the sensitivity of dasatinib in this specific context.

## Evidence-Based Interpretation
The observed AUC of 0.2495 indicates a high sensitivity of the JURLMK1 cell line to dasatinib, which is consistent with the drug's mechanism as an inhibitor of SRC, YES1, EPHA2, c-KIT, and LCK. The large negative prediction error (-10.0183) implies that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0367, fp_0760, fp_0902, fp_1019, and fp_0062, with negative SHAP values indicating that their presence or absence pushes the prediction towards lower AUC (higher sensitivity). These features are associated with specific molecular structures, such as the presence of certain functional groups or rings. The same-drug cohort examples (KYO1 and EOL1) and same-cell cohort examples (leptomycin B and paclitaxel) provide additional context, suggesting that dasatinib's sensitivity in JURLMK1 is consistent with its behavior in other similar cell lines and that other drugs may also exhibit sensitivity in this cell line.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics indicate a reasonable fit to the training data, they should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models offer insight into the broader patterns in the data but do not directly inform the interpretation of the RPT-0186 sample. The per-drug cross-validated predictability for dasatinib (R2=0.2203) suggests that the model has some capacity to predict dasatinib's behavior, but the large prediction error in this case highlights the limitations of the model.

## Confidence and Caveats
The interpretation of the RPT-0186 sample is grounded in the local evidence and should be considered in the context of the model's limitations. The large prediction error and the specific molecular features contributing to the predicted AUC suggest that there may be additional factors at play that are not fully captured by the model. Therefore, caution should be exercised when extrapolating these findings to other contexts or using them to inform clinical decisions.

---

## RPT-0190 - decitabine on SUDHL8
_Split: test_

## Executive Summary
The sample RPT-0190, which involves the drug decitabine on the SUDHL8 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.6528. This is significantly lower than the RF-predicted AUC of 13.6451, indicating a large negative prediction error. The response is also notably sensitive compared to the drug and cell cohorts, ranking at the 0.6 percentile for the drug cohort and the 3.5 percentile for the cell cohort.

## Evidence-Based Interpretation
The observed sensitivity of the SUDHL8 cell line to decitabine is unexpected given the model's prediction. The top TreeSHAP features contributing to this discrepancy include fingerprint bits fp_0504, fp_0767, fp_0204, and the gene expression of TNFRSF12A. The absence of fp_0504 and fp_0767, which are present in a small percentage of CTRPv2 compounds, pushes the prediction towards higher AUC (resistance), while the presence of fp_0204 and the low expression of TNFRSF12A push the prediction towards lower AUC (sensitivity).

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the absence of certain fingerprint bits (fp_0504, fp_0767, and fp_0864) and the presence of fp_0204 contribute to the observed sensitivity. Additionally, the low expression of TNFRSF12A, which is a gene that recurs in 166 predictable-drug RF signatures, also contributes to the sensitivity. The same-drug and same-cell cohort examples show that other cell lines (BV173 and JURLMK1) are also sensitive to decitabine, and other drugs (leptomycin B and GSK461364) exhibit similar sensitivity on the SUDHL8 cell line.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for decitabine is 0.5143, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated with caution, and the results should not be used for clinical advice.

---

## RPT-0223 - RITA on SH10TC
_Split: test_

## Executive Summary
The sample RPT-0223, involving the drug RITA and cell line SH10TC, exhibits an observed AUC of 3.8331, which is lower than the RF-predicted AUC of 13.5650. This indicates that the sample is exceptionally sensitive relative to the predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of RITA in the SH10TC cell line.

## Evidence-Based Interpretation
The observed AUC of 3.8331 is significantly lower than the global mean AUC across all pairs (12.8580), indicating higher sensitivity. The sample's percentile rank within the drug cohort (0.9) and cell cohort (0.5) further supports this interpretation. The top TreeSHAP features, including TNFRSF12A and various fingerprint bits (fp_0902, fp_0760, fp_0204, and fp_0367), contribute to the predicted AUC value. Positive SHAP values for TNFRSF12A, fp_0902, fp_0204, and fp_0367 push the prediction toward higher AUC/resistance, while the negative SHAP value for fp_0760 pushes toward lower AUC/sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. TNFRSF12A, a gene with a positive SHAP value, is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures. The fingerprint bits, such as fp_0902 and fp_0204, are absent in the sample but present in a small percentage of CTRPv2 compounds. In contrast, fp_0760 is present in the sample and has a negative SHAP value, contributing to the lower observed AUC. The same-drug cohort examples (TE441T and BCP1) and same-cell cohort examples (dinaciclib and SB-743921) provide additional context, showing that RITA tends to be more sensitive in certain cell lines, while other drugs exhibit similar sensitivity profiles in the SH10TC cell line.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). These metrics should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models offer a broader understanding of the model's behavior. The per-drug cross-validated predictability for RITA (R2=0.2078) indicates moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any

---

## RPT-0224 - PRIMA-1-Met on NCIH2291
_Split: test_

## Executive Summary
The NCIH2291 cell line exhibits exceptional sensitivity to PRIMA-1-Met, with an observed AUC of 3.9753, which is significantly lower than the predicted AUC of 13.6951. This discrepancy suggests that the model underestimated the sensitivity of NCIH2291 to PRIMA-1-Met.

## Evidence-Based Interpretation
The observed AUC of 3.9753 indicates that NCIH2291 is more sensitive to PRIMA-1-Met than expected. The large negative prediction error of -9.7198 further supports this conclusion. The cell line's sensitivity is also evident when compared to other cell lines treated with PRIMA-1-Met, such as SW1710 and AM38, which have higher AUC values.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A, fp_0443, fp_0062, fp_0367, and fp_0204. The presence of TNFRSF12A, a gene involved in apoptosis, may contribute to the cell line's sensitivity to PRIMA-1-Met. The absence of certain fingerprint features, such as fp_0443 and fp_0062, may also play a role in the cell line's sensitivity. The neighborhood analysis reveals that other cell lines, such as SW1710 and AM38, exhibit similar sensitivity to PRIMA-1-Met.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The model's performance on the training data is moderate, but it is essential to note that these metrics do not reflect the model's held-out performance. The per-drug cross-validated predictability for PRIMA-1-Met is low, with an R2 of 0.0141, indicating that the model may not capture the underlying relationships between PRIMA-1-Met and the cell lines. The availability of cell subtype metadata, such as adenocarcinoma, may provide additional context for understanding the cell line's sensitivity to PRIMA-1-Met.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, the conclusions drawn from this analysis should be considered with caution and in the context of the available evidence.

---

## RPT-0227 - trametinib on WM88
_Split: test_

## Executive Summary
The WM88 cell line exhibits exceptional sensitivity to trametinib, with an observed AUC of 1.4912, which is significantly lower than the predicted AUC of 11.1998. This discrepancy suggests that the model underestimated the sensitivity of WM88 to trametinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC value are fp_0367, fp_1008, fp_0409, fp_1001, and fp_0728, all of which have negative SHAP values. These features are associated with specific molecular substructures, such as `[#6]:[#6](-[#6]):[#6]` and `[#7]-[#6](:[#7]:[#6]):[#7]:[#6]`. The presence of these features in trametinib pushes the predicted AUC towards a lower value, indicating increased sensitivity.

## Feature and Neighborhood Analysis
The same-drug cohort examples, such as DU4475 and OCIAML3, also exhibit high sensitivity to trametinib, with AUC values of 0.1282 and 0.3553, respectively. Similarly, the same-cell cohort examples, such as dabrafenib and leptomycin B, show increased sensitivity in the WM88 cell line, with AUC values of 2.5202 and 3.1017, respectively. These examples suggest that the WM88 cell line is generally more sensitive to certain drugs, including trametinib.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features, such as fp_0443 and fp_0767, are associated with specific molecular substructures. However, these features are not directly relevant to the interpretation of the WM88 cell line's sensitivity to trametinib. The per-drug cross-validated predictability for trametinib has an R2 of 0.3821, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results may be limited by the availability of data and the specific features used in the model. Therefore, the interpretation should be considered in the context of these limitations and caveats.

---

## RPT-0234 - cytarabine hydrochloride on P12ICHIKAWA
_Split: test_

## Executive Summary
The sample **P12ICHIKAWA** treated with **cytarabine hydrochloride** exhibits an observed AUC of **3.5152**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the drug's mechanism as an inducer of DNA damage.

## Evidence-Based Interpretation
The observed AUC is significantly lower than the predicted AUC, indicating a higher sensitivity than expected. The top TreeSHAP features contributing to this prediction error include **fp_0443** (present, SHAP=-0.7283), **fp_0504** (absent, SHAP=+0.5429), **fp_0767** (absent, SHAP=+0.4244), **TNFRSF12A (51330)** (gene expression, SHAP=-0.3712), and **fp_0864** (absent, SHAP=+0.2674). These features suggest that the presence of certain molecular structures and the expression of specific genes contribute to the increased sensitivity of **P12ICHIKAWA** to **cytarabine hydrochloride**.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. The presence of **fp_0443** and the absence of **fp_0504**, **fp_0767**, and **fp_0864** contribute to the increased sensitivity. Additionally, the low expression of **TNFRSF12A (51330)** also contributes to this sensitivity. The same-drug cohort examples, such as **BV173** and **REH**, exhibit similar sensitivity profiles, while the same-cell cohort examples, such as **SB-743921** and **paclitaxel**, also demonstrate increased sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for **cytarabine hydrochloride** is 0.5313, indicating moderate predictability. The cell subtype metadata is available, confirming that **P12ICHIKAWA** is an acute lymphoblastic T cell leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the training diagnostics. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and any clinical implications or applications are outside the scope of this report.

---

## RPT-0253 - cytarabine hydrochloride on MINO
_Split: test_

## Executive Summary
The sample **MINO** treated with **cytarabine hydrochloride** exhibits an observed AUC of **3.6165**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the drug's mechanism as an inducer of DNA damage.

## Evidence-Based Interpretation
The observed AUC is significantly lower than the predicted AUC, indicating a larger than expected sensitivity of the **MINO** cell line to **cytarabine hydrochloride**. The top TreeSHAP features contributing to this prediction error include **fp_0443**, **fp_0504**, **fp_0767**, **TNFRSF12A (51330)**, and **fp_0864**. The presence of **fp_0443** and the absence of **fp_0504**, **fp_0767**, and **fp_0864** in the compound's fingerprint, along with the low expression of **TNFRSF12A**, push the prediction towards a lower AUC, suggesting increased sensitivity.

## Feature and Neighborhood Analysis
The local SHAP values indicate that the presence of **fp_0443** and the low expression of **TNFRSF12A** contribute to the increased sensitivity of **MINO** to **cytarabine hydrochloride**. In contrast, the absence of **fp_0504**, **fp_0767**, and **fp_0864** also contributes to this sensitivity. The same-drug cohort examples, such as **BV173** and **REH**, and the same-cell cohort examples, such as **SB-743921** and **docetaxel**, further support the notion that **MINO** is exceptionally sensitive to **cytarabine hydrochloride**.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The top global fingerprint features and the most common genes across predictable per-drug models are also provided. However, these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for **cytarabine hydrochloride** is 0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local SHAP values and the provided metadata. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to the local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated with caution, as they are based on training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice.

---

## RPT-0284 - docetaxel on KPNYN
_Split: test_

## Executive Summary
The KPNYN cell line showed a higher resistance to docetaxel than predicted by the model, with an observed AUC of 17.3740 compared to a predicted AUC of 7.9419. This discrepancy suggests that the model underestimated the resistance of KPNYN cells to docetaxel.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction error are primarily fingerprint bits (fp_1009, fp_0443, fp_0204, and fp_0741) and a gene expression feature (TNFRSF12A). These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). However, the observed AUC is higher than predicted, suggesting that other factors not captured by the model contribute to the resistance of KPNYN cells to docetaxel.

## Feature and Neighborhood Analysis
The fingerprint bits identified as top features are present in a relatively small percentage of CTRPv2 compounds, ranging from 0.4% (fp_0443) to 9.1% (fp_1009). The gene expression feature, TNFRSF12A, has a value markedly below the cross-cell-line mean, which may contribute to the resistance of KPNYN cells to docetaxel. The same-drug cohort examples show that other cell lines (697 and OCIAML3) are more sensitive to docetaxel, while the same-cell cohort examples show that KPNYN cells are more resistant to docetaxel compared to other drugs (leptomycin B and 1S,3R-RSL-3).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for docetaxel has an R2 of 0.2934, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is limited by the availability of data and the complexity of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. Therefore, the results should be treated with caution and considered in the context of the available data and model limitations.

---

## RPT-0287 - PF-3758309 on OCIAML5
_Split: test_

## Executive Summary
The sample RPT-0287, treated with PF-3758309 on the OCIAML5 cell line, exhibited an observed AUC of 2.4675, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include fingerprint bits fp_0367, fp_0091, fp_1001, and fp_0760, as well as the gene expression of TNFRSF12A. These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). The presence of these features in the sample contributes to its observed sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features are associated with specific molecular structures and gene expressions. For example, fp_0367 is represented by the SMARTS `[#6]:[#6](-[#6]):[#6]` and is present in 6.4% of CTRPv2 compounds. The gene expression of TNFRSF12A is below the cross-cell-line mean, which may also contribute to the sample's sensitivity. The same-drug cohort examples, such as EOL1 and SIGM5, also exhibit sensitivity, suggesting that PF-3758309 may be effective against certain cell lines.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for PF-3758309 is 0.3602, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to the local context and should not be extrapolated to other datasets or models. Additionally, the global model metrics should be treated with caution, as they are based on training diagnostics rather than held-out performance.

---

## RPT-0296 - cytarabine hydrochloride on SUDHL8
_Split: test_

## Executive Summary
The sample RPT-0296, involving cytarabine hydrochloride on the SUDHL8 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.8360, which is significantly lower than the RF-predicted AUC of 13.1844. This discrepancy indicates that the model underestimated the sensitivity of the SUDHL8 cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 3.8360 suggests that the SUDHL8 cell line is more sensitive to cytarabine hydrochloride than predicted by the model. The large negative prediction error of -9.3484 further supports this interpretation. The sample's sensitivity is also evident when compared to the drug cohort and cell cohort baselines, with the sample percentile being 3.1 and 4.1, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443, fp_0504, fp_0767, TNFRSF12A, and fp_0864. The presence of fp_0443 (SHAP=-0.7386) and the absence of fp_0504 (SHAP=+0.5580), fp_0767 (SHAP=+0.4455), and fp_0864 (SHAP=+0.2661) push the prediction towards lower AUC/sensitivity. The low expression of TNFRSF12A (SHAP=-0.3682) also contributes to the increased sensitivity. The same-drug cohort examples, such as BV173 and REH, and same-cell cohort examples, such as leptomycin B and GSK461364, further support the sensitive response of the SUDHL8 cell line.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is R2=0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to the provided data and should not be extrapolated to other contexts. Additionally, the global model metrics should be treated with caution, as they are based on training diagnostics rather than held-out performance.

---

## RPT-0313 - ML210 on NCIH446
_Split: test_

## Executive Summary
The sample RPT-0313, involving the drug ML210 and the cell line NCIH446, exhibits an observed AUC of 4.2146, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of this observation, focusing on the local SHAP values and global model context.

## Evidence-Based Interpretation
The observed AUC of 4.2146 is significantly lower than the predicted AUC of 13.4714, indicating a large negative prediction error. This suggests that the model underestimated the sensitivity of the NCIH446 cell line to ML210. The top TreeSHAP features contributing to this prediction error include fp_0443, TNFRSF12A, fp_1009, fp_0367, and fp_0204. Positive SHAP values for fp_0443, TNFRSF12A, fp_0367, and fp_0204 push the prediction toward higher AUC/resistance, while the negative SHAP value for fp_1009 pushes the prediction toward lower AUC/sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. The presence of fp_1009 and the absence of fp_0443, fp_0367, and fp_0204 contribute to the observed sensitivity. The gene expression level of TNFRSF12A is near the cross-cell-line mean, but its positive SHAP value suggests that it contributes to the predicted resistance. The same-drug cohort examples, such as DOHH2 and SKNDZ, exhibit more sensitive profiles, while the same-cell cohort examples, such as leptomycin B and SB-743921, also exhibit more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The max-depth tuning and N-estimator tuning results indicate that the model is optimized for a max depth of 20 and 100 estimators. The top global fingerprint features and most common genes across predictable per-drug models provide additional context for the model's performance. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local SHAP values and global model context. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, but its impact on the model's performance is not explicitly evaluated.

---

## RPT-0321 - mitomycin on IMR32
_Split: test_

## Executive Summary
The IMR32 cell line exhibits exceptional sensitivity to mitomycin, with an observed AUC of 3.2914, which is significantly lower than the predicted AUC of 12.5119. This discrepancy suggests that the model underestimated the sensitivity of IMR32 to mitomycin.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include TNFRSF12A gene expression, which has a negative SHAP value of -0.6876, indicating that its low expression in IMR32 pushes the prediction towards lower AUC (greater sensitivity). In contrast, the absence of certain fingerprint features (fp_0204, fp_0443) has a positive SHAP value, suggesting that their presence would increase the predicted AUC (resistance).

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that IMR32 is more sensitive to mitomycin compared to other cell lines, such as KASUMI2 and MV411, which also exhibit low AUC values. Similarly, within the same cell line cohort, IMR32 is more sensitive to other drugs like SB-743921 and paclitaxel. The presence of certain fingerprint features, such as fp_0741, may contribute to this sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The top global fingerprint features, such as fp_0443 and fp_0767, are not directly relevant to this specific sample. However, the per-drug cross-validated predictability for mitomycin (R2=0.3579) suggests that the model has some capacity to predict the response of cell lines to this drug.

## Confidence and Caveats
The interpretation of these results is limited by the availability of data and the constraints of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata and feature tables, and any global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, these findings should be considered in the context of the available data and model limitations.

---

## RPT-0334 - ML210 on NCO2
_Split: test_

## Executive Summary
The sample **NCO2** treated with **ML210** shows an exceptionally sensitive response with an observed AUC of **3.3964**, which is significantly lower than the predicted AUC of **12.5487**. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of **3.3964** indicates a high sensitivity of the **NCO2** cell line to **ML210**, which is consistent with the mechanism of action of **ML210** as a selective killer of engineered cells expressing mutant HRAS. The large negative prediction error (**-9.1523**) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include **TNFRSF12A** (SHAP=-0.6706), **fp_0443** (SHAP=+0.4031), **fp_1009** (SHAP=-0.1715), **fp_0204** (SHAP=+0.1396), and **fp_0367** (SHAP=+0.0440). The negative SHAP value for **TNFRSF12A** suggests that its expression level pushes the prediction towards lower AUC (higher sensitivity), while the positive SHAP values for the fingerprint features **fp_0443**, **fp_0204**, and **fp_0367** indicate that their presence or absence pushes the prediction towards higher AUC (lower sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of **0.4928** and a training RMSE of **1.8342**. The model was trained on a dataset with **311258** samples and **2024** features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for **ML210** is **0.3111**, indicating moderate predictability. The cell subtype metadata confirms that **NCO2** is a chronic myeloid leukaemia cell line. 

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance.

---

## RPT-0336 - KX2-391 on LC1F
_Split: test_

## Executive Summary
The sample RPT-0336, involving the drug KX2-391 on the LC1F cell line, exhibits an observed AUC of 4.0116, which is more sensitive than the model's prediction of 13.1396. This discrepancy suggests that the model underestimated the sensitivity of KX2-391 on LC1F cells.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include fingerprint bits fp_0443, TNFRSF12A gene expression, fp_0706, fp_1009, and fp_0806. Positive SHAP values for fp_0443 and TNFRSF12A indicate that these features push the prediction towards higher AUC (resistance), while negative SHAP values for fp_0706, fp_1009 suggest that these features contribute to lower AUC (sensitivity). The presence of fp_0806 has a minor positive effect on the prediction.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the absence of fp_0443 and the near-average expression of TNFRSF12A are notable. The presence of fp_0706 and fp_1009, which are associated with lower AUC, may contribute to the observed sensitivity. The same-drug cohort examples, such as IMR32 and SNU16, also exhibit higher sensitivity, suggesting that KX2-391 may be more effective against certain cell lines. The same-cell cohort examples, including SB-743921 and LBH-589, demonstrate that LC1F cells can be sensitive to various drugs.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for KX2-391 is 0.4019, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata and feature tables, and any global model metrics should be treated with caution. The results should not be used for clinical advice, and further investigation is necessary to fully understand the mechanisms underlying the observed sensitivity of KX2-391 on LC1F cells.

---

## RPT-0345 - ML210 on PEER
_Split: test_

## Executive Summary
The sample RPT-0345, involving the drug ML210 and cell line PEER, exhibits an observed AUC of 3.4663, which is exceptionally sensitive compared to the predicted AUC of 12.5487 and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on the SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (-9.0824) suggests that the actual response of the PEER cell line to ML210 is more sensitive than expected. The global mean AUC across all pairs is 12.8580, and the sample percentile for both the drug and cell cohorts is around 2%, indicating that this sample is an outlier in terms of sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to this prediction include TNFRSF12A (gene_expression) with a SHAP value of -0.6682, indicating that lower expression of this gene pushes the prediction towards higher sensitivity. Fingerprint features such as fp_0443, fp_1009, fp_0204, and fp_0062 also contribute to the prediction, with positive SHAP values indicating the presence or absence of specific molecular structures. The presence of fp_1009 and the absence of fp_0443, fp_0204, and fp_0062 push the prediction towards higher sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311258 samples with 2024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance metrics. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability.

## Confidence and Caveats
The interpretation of this report is grounded in the local SHAP values and feature analysis. However, it is essential to consider the limitations of the model, including the potential for overfitting and the use of training diagnostics as evaluation metrics. Additionally, the molecular descriptions are based on local CTRPv2 metadata and feature tables, which may not capture the full complexity of the biological system. Therefore, the results should be treated with caution and considered in the context of additional experimental validation and clinical expertise.

---

## RPT-0353 - cytarabine hydrochloride on RPMI8402
_Split: test_

## Executive Summary
The sample RPMI8402 treated with cytarabine hydrochloride exhibits an exceptionally sensitive response, with an observed AUC of 4.1214, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of this particular cell line to the drug.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the presence of fingerprint feature **fp_0443** and the low expression of gene **TNFRSF12A (51330)** are the primary contributors to the observed sensitivity. The absence of features **fp_0504**, **fp_0767**, and **fp_0864** also plays a role in the sensitive response. These findings are grounded in the local CTRPv2 metadata and feature tables.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include **fp_0443** (SHAP=-0.7202), **fp_0504** (SHAP=+0.5370), **fp_0767** (SHAP=+0.4164), **TNFRSF12A (51330)** (SHAP=-0.3708), and **fp_0864** (SHAP=+0.2683). The presence of **fp_0443** and the low expression of **TNFRSF12A (51330)** push the prediction towards a lower AUC (greater sensitivity), while the absence of **fp_0504**, **fp_0767**, and **fp_0864** contributes to the sensitive response. The same-drug cohort examples (e.g., BV173 and REH) and same-cell cohort examples (e.g., leptomycin B and SB-743921) also exhibit sensitive responses.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated with caution, as they are training diagnostics rather than held-out performance.

---

## RPT-0360 - birinapant on HEC265
_Split: test_

## Executive Summary
The sample HEC265 treated with birinapant shows an exceptionally sensitive response with an observed AUC of 5.0118, which is significantly lower than the RF-predicted AUC of 14.0621. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of 5.0118 indicates a high sensitivity of the HEC265 cell line to birinapant. In contrast, the predicted AUC of 14.0621 suggests a lower sensitivity. The large negative prediction error of -9.0503 highlights the discrepancy between the observed and predicted responses. The sample percentile of 1.1 in the drug cohort and 1.6 in the cell cohort further emphasizes the exceptional sensitivity of this combination.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443, fp_0767, fp_0864, fp_0504, and fp_1009. The presence of fp_0443 (SHAP=-0.3698) pushes the prediction towards lower AUC (higher sensitivity), while the absence of fp_0767, fp_0864, fp_0504, and fp_1009 (SHAP=+0.2403, +0.1776, +0.1704, and +0.1598, respectively) pushes the prediction towards higher AUC (lower sensitivity). The neighborhood analysis reveals that other cell lines, such as KYM1 and WSUDLCL2, also exhibit high sensitivity to birinapant, while other drugs, such as leptomycin B and oligomycin A, show high sensitivity in the HEC265 cell line.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. The top global fingerprint features, such as fp_0443, fp_0767, and fp_0925, are consistent with the local feature analysis. The per-drug cross-validated predictability for birinapant is relatively low (R2=0.0192), indicating that the model may not capture the underlying mechanisms of this specific drug-cell line combination. The availability of cell subtype metadata (adenocarcinoma) provides additional context for the analysis.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, the results should be interpreted with caution, and further investigation is necessary to fully understand the underlying mechanisms of the observed sensitivity.

---

## RPT-0393 - BRD-K61166597 on GSS
_Split: test_

## Executive Summary
The sample RPT-0393, involving the drug BRD-K61166597 on the GSS cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.6444, which is significantly lower than the RF-predicted AUC of 13.5650. This discrepancy suggests that the model underestimated the sensitivity of this drug-cell line pair.

## Evidence-Based Interpretation
The observed AUC of 4.6444 indicates a higher sensitivity of the GSS cell line to BRD-K61166597 compared to the model's prediction. The large negative prediction error of -8.9206 further supports this interpretation. The sample's percentile rank of 0.1 in the drug cohort and 3.8 in the cell cohort also indicates that this response is unusually sensitive.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a positive SHAP value of +0.2158, and several fingerprint bits (fp_0443, fp_0204, fp_0367) with positive SHAP values, indicating that their presence or absence pushes the prediction towards higher AUC (resistance). In contrast, fp_0062 has a negative SHAP value of -0.0575, suggesting that its absence contributes to the predicted sensitivity. The local neighborhood analysis shows that similar cell lines (EOL1, SEM) and drugs (paclitaxel, SB-743921) exhibit more sensitive responses.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for BRD-K61166597 has an R2 of 0.3454, indicating moderate predictability. The availability of cell subtype metadata (adenocarcinoma) provides additional context for this sample.

## Confidence and Caveats
The interpretation of this sample's response is grounded in the local TreeSHAP values and cohort summaries. However, the global model metrics should be treated with caution, as they represent training diagnostics rather than held-out performance. The absence of direct causal evidence and the reliance on local metadata and feature tables are additional limitations of this analysis. Furthermore, the results should not be used for clinical advice, and any conclusions drawn from this analysis should be carefully considered in the context of the available data and limitations.

---

## RPT-0398 - cytarabine hydrochloride on CHP212
_Split: test_

## Executive Summary
The sample RPT-0398, involving cytarabine hydrochloride on the CHP212 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.6951, which is significantly lower than the RF-predicted AUC of 13.5949. This discrepancy indicates that the model underestimated the sensitivity of cytarabine hydrochloride on CHP212 cells.

## Evidence-Based Interpretation
The observed AUC of 4.6951 suggests that cytarabine hydrochloride is highly effective against the CHP212 cell line, with a large negative prediction error of -8.8998. This error indicates that the model predicted a higher AUC (lower sensitivity) than what was actually observed. The sample's percentile ranks within the drug and cell cohorts (4.6 and 4.1, respectively) further emphasize its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443 (SHAP = -0.7612), fp_0504 (SHAP = 0.4053), fp_0767 (SHAP = 0.3200), fp_0864 (SHAP = 0.1892), and fp_0450 (SHAP = -0.1741). The presence of fp_0443 and fp_0450, and the absence of fp_0504, fp_0767, and fp_0864, are associated with the observed sensitivity. These features are represented by specific molecular substructures, such as `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` for fp_0443.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features, such as fp_0443 and fp_0767, are also identified. However, it is essential to note that these metrics are based on training data and should not be considered as held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride has an R2 of 0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to recognize that TreeSHAP values explain the fitted Random Forest prediction for this sample and do not provide direct causal evidence. The model's performance and feature importance should be considered in the context of the training data and may not generalize to unseen data. Additionally, the absence of certain information, such as gene targets and mechanisms, may limit the depth of the analysis.

---

## RPT-0418 - selumetinib on OCUM1
_Split: test_

## Executive Summary
The OCUM1 cell line exhibits exceptional sensitivity to selumetinib, with an observed AUC of 3.8209, which is lower than the RF-predicted AUC of 12.6775. This discrepancy suggests that the model underestimated the sensitivity of OCUM1 to selumetinib. The top TreeSHAP features contributing to this prediction error include fingerprint bits fp_0367, fp_1001, and gene expression of TNFRSF12A.

## Evidence-Based Interpretation
The observed AUC of 3.8209 indicates that OCUM1 is more sensitive to selumetinib than predicted by the model. The large negative prediction error of -8.8566 suggests that the model overestimated the resistance of OCUM1 to selumetinib. The top TreeSHAP features, including fp_0367 and fp_1001, have negative SHAP values, indicating that they contribute to the lower observed AUC and increased sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features include fingerprint bits fp_0367, fp_1001, fp_0053, and fp_1019, as well as gene expression of TNFRSF12A. The presence of fp_0367 and fp_1001 contributes to the increased sensitivity of OCUM1 to selumetinib, while the gene expression of TNFRSF12A has a positive SHAP value, indicating that it contributes to the predicted resistance. The neighborhood analysis reveals that other cell lines, such as NUDUL1 and HUT78, also exhibit sensitivity to selumetinib.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The model was trained on a large dataset with 311258 samples and 2024 features, and the top global fingerprint features are distinct from the top TreeSHAP features for this sample. The per-drug cross-validated predictability for selumetinib is relatively low, with an R2 of 0.2298, indicating that the model may not capture all the relevant factors influencing the response to selumetinib.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The model is not causal, and the TreeSHAP values explain the fitted Random Forest prediction for this sample only. The molecular descriptions are based on local CTRPv2 metadata and feature tables, and any global model metrics should be treated with caution. Additionally, the cell subtype metadata is available, but its relevance to the prediction error is unclear.

---

## RPT-0421 - ML210 on RH18
_Split: test_

## Executive Summary
The sample RPT-0421, involving drug ML210 and cell line RH18, exhibits an exceptionally sensitive response with an observed AUC of 4.6495, which is significantly lower than the RF-predicted AUC of 13.4979. This discrepancy suggests that the model underestimated the sensitivity of ML210 in RH18 cells.

## Evidence-Based Interpretation
The Top TreeSHAP features for this sample indicate that the presence or absence of specific molecular fingerprints (fp_0443, fp_0367, fp_1009, and fp_0204) and the expression level of the gene TNFRSF12A contribute to the predicted AUC. Notably, the presence of fp_1009 has a negative SHAP value, pushing the prediction towards lower AUC (greater sensitivity), while the absence of fp_0443, fp_0367, and fp_0204 have positive SHAP values, pushing the prediction towards higher AUC (lower sensitivity).

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the molecular fingerprints fp_0443, fp_0367, and fp_0204 are absent in ML210, which may contribute to its sensitivity in RH18 cells. In contrast, the presence of fp_1009 in ML210 may enhance its sensitivity. The expression level of TNFRSF12A is near the cross-cell-line mean, which may not significantly impact the predicted AUC. The same-drug cohort examples (DOHH2 and SKNDZ) and same-cell cohort examples (1S,3R-RSL-3 and LBH-589) also exhibit sensitive responses, suggesting that ML210 may be generally effective against certain cell lines.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models are listed, but their relevance to this specific sample is unclear. The per-drug cross-validated predictability for ML210 (R2=0.3111) suggests moderate predictability. The availability of cell subtype metadata (alveolar) may be useful for further analysis.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Further analysis and validation are necessary to confirm the findings and establish the underlying mechanisms.

---

## RPT-0425 - decitabine on JM1
_Split: test_

## Executive Summary
The sample in question involves the drug decitabine and the cell line JM1, with an observed AUC of 4.7976, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The prediction error is -8.8475, indicating that the actual response is more sensitive than predicted.

## Evidence-Based Interpretation
The observed AUC of 4.7976 is lower than the predicted AUC of 13.6451, suggesting that the cell line JM1 is more sensitive to decitabine than expected. This is further supported by the fact that the sample percentile for the drug cohort is 2.1, indicating that the observed AUC is lower than 97.9% of the AUC values in the cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include fp_0504, fp_0767, fp_0204, TNFRSF12A, and fp_0864. The presence of fp_0204 and the absence of fp_0504, fp_0767, and fp_0864 contribute to the lower predicted AUC, while the low expression of TNFRSF12A also pushes the prediction towards a lower AUC. The same-drug cohort examples, such as BV173 and JURLMK1, also exhibit more sensitive profiles, with AUC values of 2.0894 and 2.2041, respectively.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features include fp_0443, fp_0767, and fp_0925, among others. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4. The per-drug cross-validated predictability for decitabine is 0.5143, indicating moderate predictability. The cell subtype metadata is available and indicates that the cell line JM1 is a B cell lymphoma. 

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any conclusions drawn from this analysis should be carefully considered in the context of the available data and limitations of the model.

---

## RPT-0427 - salermide on SCC25
_Split: test_

## Executive Summary
The sample RPT-0427, involving the drug salermide on the SCC25 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.7206, which is significantly lower than the RF-predicted AUC of 13.5650. This discrepancy suggests that the model underestimated the sensitivity of salermide on SCC25 cells.

## Evidence-Based Interpretation
The observed AUC of 4.7206 indicates a higher sensitivity of the SCC25 cell line to salermide compared to the predicted response. The large negative prediction error of -8.8444 further supports this interpretation. The sample's sensitivity is also notable when compared to the drug cohort and cell cohort baselines, with the sample percentile being 0.2 for the drug cohort and 2.4 for the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include TNFRSF12A, fp_0443, fp_0204, fp_0062, and fp_0367. Positive SHAP values for TNFRSF12A, fp_0443, fp_0204, and fp_0367 suggest that these features push the prediction toward higher AUC/resistance, while the negative SHAP value for fp_0062 pushes the prediction toward lower AUC/sensitivity. The absence of certain fingerprint features, such as fp_0443, fp_0204, and fp_0367, in the sample may contribute to its exceptional sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, train RMSE of 1.8342, and train correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for salermide is -0.0579, indicating limited predictability. The availability of cell subtype metadata, specifically squamous cell carcinoma, may provide additional context for understanding the sample's response.

---

## RPT-0432 - KX2-391 on HUNS1
_Split: test_

## Executive Summary
The sample RPT-0432, treated with KX2-391 on the HUNS1 cell line, exhibited an observed AUC of 3.0988, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The observed AUC of 3.0988 is lower than the predicted AUC of 11.9252, indicating that the sample is more sensitive than expected. The sample's sensitivity is also notable compared to the drug cohort (3.1 percentile) and cell cohort (4.5 percentile) baselines. The top TreeSHAP features contributing to this prediction error include TNFRSF12A (SHAP=-0.7402), fp_0443 (SHAP=+0.3707), fp_0706 (SHAP=-0.2173), fp_1009 (SHAP=-0.1924), and fp_0062 (SHAP=-0.1024).

## Feature and Neighborhood Analysis
The top TreeSHAP features suggest that the sample's sensitivity is influenced by the expression of TNFRSF12A, which is below the cross-cell-line mean. The presence or absence of specific fingerprint features, such as fp_0443, fp_0706, fp_1009, and fp_0062, also contributes to the prediction error. These features are associated with various compounds, including nilotinib, bleomycin A2, paclitaxel, and curcumin. The same-drug cohort examples (IMR32 and SNU16) and same-cell cohort examples (CR-1-31B and leptomycin B) also exhibit sensitivity profiles that are more sensitive than the predicted response.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The max-depth and n-estimator tuning results indicate optimal hyperparameters for the Random Forest model. The top global fingerprint features and most common genes across predictable per-drug models provide additional context for the model's performance. The per-drug cross-validated predictability for KX2-391 (R2=0.4019) and cell subtype metadata (plasma cell myeloma) are also available.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results are specific to the KX2-391 and HUNS1 cell line combination and may not generalize to other contexts.

---

## RPT-0436 - pluripotin on PFEIFFER
_Split: test_

## Executive Summary
The sample RPT-0436, involving the drug **pluripotin** on the **PFEIFFER** cell line, exhibits an observed AUC of **3.3353**, which is exceptionally sensitive compared to the RF-predicted AUC of **12.1584** and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on SHAP values, feature analysis, and model-level context.

## Evidence-Based Interpretation
The large negative prediction error (**-8.8231**) suggests that the model underestimated the sensitivity of **pluripotin** on the **PFEIFFER** cell line. The top TreeSHAP features, including **fp_0623**, **fp_0367**, **fp_0235**, and **fp_0372**, have negative SHAP values, indicating that they contribute to the observed sensitivity. In contrast, **fp_0204** has a positive SHAP value, suggesting that its absence contributes to the sensitivity.

## Feature and Neighborhood Analysis
The presence of **fp_0623**, **fp_0367**, **fp_0235**, and **fp_0372** in the **pluripotin** compound is associated with increased sensitivity. These features are present in a relatively small percentage of CTRPv2 compounds, ranging from 0.6% to 6.4%. The absence of **fp_0204** also contributes to the sensitivity, and its presence is observed in 2.9% of CTRPv2 compounds. Same-drug cohort examples, such as **EOL1** and **MV411**, and same-cell cohort examples, such as **CR-1-31B** and **SB-743921**, also exhibit sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The top global fingerprint features and most common genes across predictable per-drug models are also reported. However, it is essential to note that these metrics are based on training data and should not be considered as held-out performance. The per-drug cross-validated predictability for **pluripotin** is **R2=0.1556**, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge the limitations of the analysis, including the potential for overfitting and the lack of direct causal evidence. The TreeSHAP values explain the fitted Random Forest prediction for this sample but should not be considered as direct causal evidence. Additionally, the cell subtype metadata is available, but its impact on the results is not explicitly evaluated in this analysis.

---

## RPT-0440 - ABT-199 on RL
_Split: test_

## Executive Summary
The sample **RL** treated with **ABT-199** exhibits an observed AUC of **3.5868**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include **TNFRSF12A** (gene_expression; SHAP=-0.6288), **fp_0443** (fingerprint_bit; SHAP=+0.3594), **fp_1009** (fingerprint_bit; SHAP=-0.1672), **fp_0227** (fingerprint_bit; SHAP=+0.1002), and **fp_0806** (fingerprint_bit; SHAP=+0.0875). The negative SHAP value for **TNFRSF12A** indicates that its low expression level in this sample contributes to the observed sensitivity. In contrast, the presence or absence of certain fingerprint bits (**fp_0443**, **fp_1009**, **fp_0227**, and **fp_0806**) pushes the prediction towards higher AUC (resistance) or lower AUC (sensitivity).

## Feature and Neighborhood Analysis
The sample's gene expression profile and fingerprint bits are compared to the cohort baselines. The **TNFRSF12A** gene expression is below the cross-cell-line mean, which may contribute to the observed sensitivity. The presence or absence of specific fingerprint bits (**fp_0443**, **fp_1009**, **fp_0227**, and **fp_0806**) is also analyzed, providing insights into the structural features of the drug that may influence its efficacy. Same-drug cohort examples (e.g., **EOL1** and **NUDHL1**) and same-cell cohort examples (e.g., **LBH-589** and **SB-743921**) are provided to contextualize the sample's response.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. These metrics should not be interpreted as held-out performance. The model's predictability for **ABT-199** is moderate, with a per-drug cross-validated **R2=0.2474**. The top global fingerprint features and most common genes across predictable per-drug models are listed, but their relevance to this specific sample is not directly inferred.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should not be extrapolated to other samples or drugs without caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are limited to the local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics are treated as training diagnostics, and their generalizability is not assessed.

---

## RPT-0441 - PF-3758309 on D283MED
_Split: test_

## Executive Summary
The sample **D283MED** treated with **PF-3758309** exhibits an observed AUC of **3.0751**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the drug's mechanism as an inhibitor of serine/threonine p21-activating kinase 4 (PAK4).

## Evidence-Based Interpretation
The observed AUC of **3.0751** is significantly lower than the RF-predicted AUC of **11.8887**, indicating a large negative prediction error. This discrepancy suggests that the model underestimated the sensitivity of **D283MED** to **PF-3758309**. The sample's sensitivity is also evident when compared to the drug cohort (4.3 percentile) and cell cohort (2.5 percentile) baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include **fp_0367**, **fp_0091**, **TNFRSF12A (51330)**, **fp_1001**, and **fp_0062**. These features have negative SHAP values, indicating that they push the prediction toward lower AUC (greater sensitivity). The presence of certain fingerprint bits (**fp_0367**, **fp_0091**, **fp_1001**) and the low expression of **TNFRSF12A** contribute to the sample's sensitivity. The absence of **fp_0062** also plays a role in this sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of **0.4928**, RMSE of **1.8342**, and correlation of **0.7061**. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for **PF-3758309** has an R2 of **0.3602**, suggesting moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models provide additional context but do not directly influence the interpretation of this specific sample's sensitivity.

## Confidence and Caveats
The interpretation of this sample's sensitivity is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is essential to recognize the limitations of this analysis, including the potential for overfitting and the reliance on training diagnostics rather than held-out performance metrics. Additionally, the molecular descriptions and feature importance should be considered in the context of the local CTRPv2 metadata and cohort summaries only.

---

## RPT-0449 - BMS-754807 on KMS26
_Split: test_

## Executive Summary
The sample RPT-0449, treated with BMS-754807 on the KMS26 cell line, exhibited an exceptionally sensitive response with an observed AUC of 3.6784, which is significantly lower than the predicted AUC of 12.4736. This discrepancy suggests that the model underestimated the sensitivity of the KMS26 cell line to BMS-754807.

## Evidence-Based Interpretation
The observed AUC of 3.6784 indicates a high sensitivity of the KMS26 cell line to BMS-754807. In contrast, the predicted AUC of 12.4736 suggests a lower sensitivity. The large negative prediction error of -8.7952 highlights the discrepancy between the observed and predicted responses. The sample's sensitivity is also evident when compared to the drug cohort (0.1 percentile) and cell cohort (4.4 percentile) baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP = -0.4655), fp_0204 (SHAP = 0.1679), fp_0367 (SHAP = -0.1472), fp_0062 (SHAP = -0.0910), and fp_0443 (SHAP = 0.0668). The negative SHAP value for TNFRSF12A suggests that its low expression (below the cross-cell-line mean) contributes to the increased sensitivity of the KMS26 cell line to BMS-754807. The presence of fp_0367 and absence of fp_0204 and fp_0062 also contribute to the increased sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311,258 samples with 2,024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for BMS-754807 has an R2 of 0.2101, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The molecular descriptions are limited to the provided data and should not be extrapolated to other contexts. Additionally, the global model metrics should be treated with caution, as they represent training diagnostics rather than held-out performance.

---

## RPT-0460 - RITA on MV411
_Split: test_

## Executive Summary
The sample MV411 treated with RITA exhibits an exceptionally sensitive response, with an observed AUC of 3.8603, which is significantly lower than the predicted AUC of 12.6318. This discrepancy suggests that the model underestimated the sensitivity of MV411 to RITA.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top contributing features to the predicted AUC are TNFRSF12A (gene_expression) with a SHAP value of -0.6709, and several fingerprint bits (fp_0204, fp_0062, fp_0443, and fp_0760) with SHAP values ranging from -0.0831 to 0.1671. The negative SHAP value for TNFRSF12A indicates that its low expression in MV411 contributes to the increased sensitivity to RITA.

## Feature and Neighborhood Analysis
The presence or absence of specific fingerprint bits, such as fp_0204, fp_0062, fp_0443, and fp_0760, also influences the predicted AUC. For example, the absence of fp_0204 and fp_0062 contributes to the increased sensitivity, while the absence of fp_0443 and presence of fp_0760 have smaller but still notable effects. The neighborhood analysis shows that other cell lines, such as TE441T and BCP1, also exhibit sensitive responses to RITA, while other drugs, such as AZD7762 and foretinib, show similar sensitivity profiles in the MV411 cell line.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed, but these should be treated as training diagnostics rather than held-out performance metrics. The per-drug cross-validated predictability for RITA is 0.2078, indicating moderate predictability. The cell subtype metadata confirms that MV411 is an acute myeloid leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should not be used to provide clinical advice.

---

## RPT-0463 - KX2-391 on PECAPJ34CLONEC12
_Split: test_

## Executive Summary
The observed AUC of 4.3771 for KX2-391 on the PECAPJ34CLONEC12 cell line indicates that this cell line is more sensitive to the drug than the model predicted, with a prediction error of -8.7625. This sensitivity is notable given the cell line's tissue origin (upper aerodigestive tract) and histology (squamous cell carcinoma).

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction include fingerprint bits (fp_0443, fp_0706, fp_1009, fp_0806) and a gene expression feature (TNFRSF12A). Positive SHAP values for fp_0443 and TNFRSF12A suggest that these factors would increase the AUC (or resistance) if they were more prominent, while negative SHAP values for fp_0706 and fp_1009 indicate that their presence contributes to the observed sensitivity. The presence of these fingerprint bits and the expression level of TNFRSF12A in this cell line are key factors in understanding its sensitivity to KX2-391.

## Feature and Neighborhood Analysis
The local analysis around KX2-391 and PECAPJ34CLONEC12 reveals that similar cell lines (e.g., IMR32, SNU16) also exhibit sensitivity to KX2-391, with low AUC values. Similarly, other drugs (e.g., leptomycin B, SB-743921) show sensitivity on the PECAPJ34CLONEC12 cell line, suggesting a pattern of vulnerability in this cell line to certain drugs. The fingerprint bits highlighted by TreeSHAP are present in a small percentage of CTRPv2 compounds, indicating specific structural features that may contribute to the drug's efficacy in this context.

## Model-Level Context
The global model context provides training diagnostics (train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061) that should not be interpreted as held-out performance. The model's ability to predict AUC values for KX2-391 has a cross-validated R2 of 0.4019, indicating moderate predictability. The most common genes across predictable per-drug models, including TNFRSF12A, suggest that these genes may play significant roles in drug response across various cell lines. However, these findings are based on training data and should be considered in the context of the model's limitations and potential biases. The availability of cell subtype metadata (squamous cell carcinoma) for PECAPJ34CLONEC12 adds context to its sensitivity profile but does not directly inform the prediction model. 

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by TreeSHAP and the characteristics of the cell line and drug in question. However, it is essential to recognize the limitations of the model, including its training diagnostics and the potential for overfitting or biases in the data. The prediction error and the specific factors contributing to the sensitivity of PECAPJ34CLONEC12 to KX2-391 should be considered

---

## RPT-0468 - daporinad on DND41
_Split: test_

## Executive Summary
The sample DND41 treated with daporinad exhibits an exceptionally sensitive response, with an observed AUC of 3.1634, which is significantly lower than the predicted AUC of 11.8994. This discrepancy suggests that the model underestimated the sensitivity of DND41 to daporinad.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top contributing features to this prediction error are primarily negative SHAP values, indicating that these features push the prediction towards lower AUC (greater sensitivity). The most significant contributor is TNFRSF12A (gene_expression) with a SHAP value of -0.7209, followed by several fingerprint bits (fp_0706, fp_0062, fp_0830) with negative SHAP values. In contrast, fp_0443 has a positive SHAP value, suggesting it pushes the prediction towards higher AUC (lower sensitivity).

## Feature and Neighborhood Analysis
The neighborhood analysis shows that DND41 is more sensitive to daporinad compared to other cell lines in the same-drug cohort (e.g., GA10, 697) and other drugs in the same-cell cohort (e.g., leptomycin B, topotecan). The presence or absence of specific fingerprint bits (e.g., fp_0706, fp_0062, fp_0443, fp_0830) may contribute to this sensitivity. Notably, TNFRSF12A is a common gene across predictable per-drug models, including daporinad.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The model was trained on a large dataset (n_samples=311258, n_features=2024) and achieved a reasonable training fit (train_r2=0.4928). The top global fingerprint features and most common genes across predictable per-drug models are provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for daporinad is relatively low (R2=0.1876), indicating that the model may not capture the underlying mechanisms of daporinad's action on DND41.

## Confidence and Caveats
The interpretation of these results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata (acute lymphoblastic T cell leukaemia) is available but not explicitly used in this analysis.

---

## RPT-0482 - ZSTK474 on RI1
_Split: test_

## Executive Summary
The sample RI1 treated with ZSTK474 exhibits an observed AUC of 3.7580, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include TNFRSF12A (gene_expression) with a SHAP value of -0.7081, indicating that the low expression of TNFRSF12A in this sample pushes the prediction towards lower AUC (greater sensitivity). Other contributing features include fingerprint bits fp_0062, fp_0443, fp_0806, and fp_0920, which have smaller SHAP values. These features suggest that the molecular characteristics of ZSTK474 and the genetic profile of RI1 contribute to the observed sensitivity.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that other cell lines, such as SUDHL6 and JVM2, also exhibit sensitivity to ZSTK474. Additionally, RI1 is sensitive to other drugs, including vincristine and paclitaxel. The top global fingerprint features, including fp_0443 and fp_0806, are also present in the feature importance list, suggesting that these molecular characteristics are important for predicting sensitivity across multiple cell lines and drugs.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The model was trained on a large dataset with 311258 samples and 2024 features. The per-drug cross-validated predictability for ZSTK474 is relatively low, with an R2 of 0.0724. The most common genes across predictable per-drug models, including TNFRSF12A, may be important for predicting sensitivity to ZSTK474 and other drugs.

## Confidence and Caveats
The interpretation of these results is limited to the local context of the sample and the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, the results should be interpreted with caution, and further validation is necessary to confirm the findings.

---

## RPT-0486 - BRD-K97651142 on FADU
_Split: test_

## Executive Summary
The sample RPT-0486, which involves the drug BRD-K97651142 and the cell line FADU, exhibits an observed AUC of 4.8298, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the large negative prediction error, where the observed AUC is significantly lower than the predicted AUC of 13.5141.

## Evidence-Based Interpretation
The observed sensitivity of the FADU cell line to BRD-K97651142 is exceptionally high, with an AUC value of 4.8298. This is in contrast to the predicted AUC of 13.5141, resulting in a large negative prediction error of -8.6843. The drug cohort and cell cohort analyses further support this finding, with the sample percentile indicating that the observed AUC is in the 1.3% and 0.5% of the drug and cell cohorts, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A, fp_0443, fp_0367, fp_0806, and fp_0062. Positive SHAP values for TNFRSF12A, fp_0443, fp_0367, and fp_0806 suggest that these features push the prediction towards higher AUC/resistance, while the negative SHAP value for fp_0062 pushes the prediction towards lower AUC/sensitivity. The presence or absence of these features in the sample contributes to the predicted AUC, with the actual observed AUC being lower than predicted.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311258 samples with 2024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for BRD-K97651142 has an R2 of 0.1367, indicating some degree of predictability. Cell subtype metadata is available, confirming that the FADU cell line is a squamous cell carcinoma.

## Confidence and Caveats
The interpretation of the results should be treated with caution, as the model's performance is based on training diagnostics rather than held-out performance. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out generalization.

---

## RPT-0497 - BRD-K50799972 on AM38
_Split: test_

## Executive Summary
The sample RPT-0497, which involves the drug BRD-K50799972 and the cell line AM38, exhibits an observed AUC of 4.7224, indicating greater sensitivity than the model's prediction of 13.3690. This discrepancy suggests that the model underestimated the sensitivity of BRD-K50799972 in the AM38 cell line.

## Evidence-Based Interpretation
The observed AUC of 4.7224 is lower than the global mean AUC across all pairs, indicating greater sensitivity. The drug cohort and cell cohort summaries also support this interpretation, with the sample percentile being 0.1 for the drug cohort and 22.1 for the cell cohort. The large negative prediction error (-8.6466) further emphasizes the model's underestimation of sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include TNFRSF12A (gene_expression) with a positive SHAP value (+0.2068), indicating that this feature pushes the prediction towards higher AUC/resistance. In contrast, the fingerprint bit fp_0227 has a negative SHAP value (-0.1640), suggesting that its presence contributes to lower AUC/sensitivity. Other notable features include fp_0204, fp_0443, and fp_0393, which have positive SHAP values and are associated with specific molecular structures.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics are not indicative of held-out performance, they suggest that the model has captured some underlying patterns in the data. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, highlighting the importance of certain molecular structures and genes in predicting AUC values. However, the per-drug cross-validated predictability for BRD-K50799972 is low (R2=-0.0049), indicating that the model may not be well-suited for predicting the behavior of this specific drug.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and metadata, but it is essential to recognize the limitations of the model and the potential for overfitting. The large prediction error and low per-drug cross-validated predictability for BRD-K50799972 suggest that the model may not be reliable for predicting the behavior of this drug. Additionally, the molecular descriptions and feature analysis are based on local CTRPv2 metadata and feature tables, which may not capture the full complexity of the underlying biology. Therefore, these results should be treated with caution and considered in the context of additional experimental validation and clinical expertise.

---

## RPT-0500 - SGX-523 on SNU620
_Split: test_

## Executive Summary
The SNU620 cell line treated with SGX-523 (a MET inhibitor) shows an exceptionally sensitive response with an observed AUC of 4.9811, which is lower than the RF-predicted AUC of 13.6218. This discrepancy suggests that the model predicts a higher resistance than what is actually observed.

## Evidence-Based Interpretation
The observed sensitivity of the SNU620 cell line to SGX-523 is notable, given that the predicted AUC is significantly higher. The large negative prediction error (-8.6407) indicates that the model underestimates the sensitivity of this cell line to SGX-523. This suggests that there may be specific factors contributing to the increased sensitivity of SNU620 cells to SGX-523 that are not fully captured by the model.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a positive SHAP value (+0.2166), indicating that higher expression of this gene would push the prediction towards higher AUC (resistance). Other features, such as fp_0204, fp_0443, and fp_0227, also have positive SHAP values, suggesting that their presence or absence contributes to the predicted resistance. In contrast, fp_0062 has a negative SHAP value (-0.0596), indicating that its absence would push the prediction towards lower AUC (sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The model was trained on a large dataset (n_samples=311258, n_features=2024) and achieved a reasonable fit. However, the per-drug cross-validated predictability for SGX-523 is relatively low (R2=0.1795), indicating that the model may not capture the underlying mechanisms of SGX-523 response as well as it does for other drugs. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to the specific response of SNU620 cells to SGX-523 is unclear.

## Confidence and Caveats
The interpretation of the results is limited by the availability of data and the complexity of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the per-drug cross-validated predictability for SGX-523 is relatively low, which may indicate that the model is not well-suited to predict the response of SNU620 cells to SGX-523.

---
