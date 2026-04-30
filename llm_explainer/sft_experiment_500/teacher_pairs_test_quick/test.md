# Teacher Pairs - Llama-3.3-70B-Instruct - test

## RPT-0009 - linifanib on EOL1
_Split: test_

## Executive Summary
The sample EOL1 treated with linifanib shows an exceptionally sensitive response with an observed AUC of 0.2525, which is significantly lower than the predicted AUC of 12.5787. This discrepancy suggests that the model underestimated the sensitivity of EOL1 to linifanib.

## Evidence-Based Interpretation
The observed AUC of 0.2525 indicates a high sensitivity of EOL1 to linifanib, which is consistent with the cell line's subtype of acute myeloid leukaemia. The large negative prediction error (-12.3262) suggests that the model did not capture the specific characteristics of EOL1 that contribute to its sensitivity to linifanib.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a negative SHAP value of -0.7195, indicating that lower expression of TNFRSF12A is associated with higher sensitivity to linifanib. The absence of certain fingerprint features (fp_0204, fp_0443, fp_0062, and fp_0227) also contributes to the predicted AUC, with positive SHAP values indicating that their presence would increase the predicted AUC (i.e., decrease sensitivity). The same-drug cohort examples (MV411 and MOLM13) and same-cell cohort examples (foretinib and dinaciclib) provide additional context, showing that EOL1 is more sensitive to linifanib compared to other cell lines and drugs.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also listed, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for linifanib (R2=0.1316) suggests that the model has limited ability to predict the response of EOL1 to linifanib. The availability of cell subtype metadata (acute myeloid leukaemia) provides additional context for the analysis.

## Confidence and Caveats
The results should be interpreted with caution, considering the limitations of the model and the specific characteristics of EOL1. The large prediction error and limited predictability of the model for linifanib suggest that the results may not generalize to other cell lines or drugs. Additionally, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be taken as direct causal evidence. Further analysis and experimentation would be necessary to fully understand the mechanisms underlying the sensitivity of EOL1 to linifanib.

---

## RPT-0017 - dasatinib on EOL1
_Split: test_

## Executive Summary
The sample in question involves the drug dasatinib and the cell line EOL1, with an observed AUC of 0.1834, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of EOL1 to dasatinib.

## Evidence-Based Interpretation
The observed AUC of 0.1834 is significantly lower than the global mean AUC across all pairs (12.8580), indicating greater sensitivity. The drug cohort and cell cohort summaries also suggest that EOL1 is more sensitive to dasatinib compared to other cell lines and drugs. The top TreeSHAP features, including fp_0367 and fp_0760, have negative SHAP values, pushing the prediction towards lower AUC/sensitivity, while features like fp_0204 and fp_0443 have positive SHAP values, pushing the prediction towards higher AUC/resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the molecular properties contributing to the observed sensitivity. Fingerprint bits fp_0367 and fp_0760 are present in dasatinib and have negative SHAP values, suggesting that these features contribute to the sensitivity of EOL1 to dasatinib. In contrast, fingerprint bits fp_0204 and fp_0443 are absent in dasatinib and have positive SHAP values, indicating that their absence may also contribute to the sensitivity. The same-drug cohort examples, such as KYO1 and LAMA84, also exhibit sensitivity to dasatinib, while the same-cell cohort examples, such as foretinib and dinaciclib, exhibit sensitivity to other drugs.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but are not directly relevant to the interpretation of the EOL1-dasatinib sample. The per-drug cross-validated predictability for dasatinib (R2=0.2203) suggests moderate predictability, and the availability of cell subtype metadata (acute myeloid leukaemia) provides additional context for the sample.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should not be used to provide clinical advice. Additionally, the absence of certain features or pathways in the analysis does not imply their irrelevance to the underlying biology.

---

## RPT-0045 - tandutinib on EOL1
_Split: test_

## Executive Summary
The sample EOL1 treated with tandutinib exhibits an observed AUC of 0.7004, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of EOL1 to tandutinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction error are TNFRSF12A (gene_expression; SHAP=-0.6376), fp_0227 (fingerprint_bit; SHAP=-0.1614), fp_0062 (fingerprint_bit; SHAP=-0.0958), fp_0806 (fingerprint_bit; SHAP=+0.0836), and fp_0443 (fingerprint_bit; SHAP=+0.0555). The negative SHAP values for TNFRSF12A, fp_0227, and fp_0062 indicate that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP values for fp_0806 and fp_0443 push the prediction towards higher AUC (greater resistance).

## Feature and Neighborhood Analysis
The local analysis reveals that the EOL1 cell line has a low expression of TNFRSF12A, which is below the cross-cell-line mean. The presence of fp_0227 and absence of fp_0062 in the tandutinib fingerprint also contribute to the predicted sensitivity. In contrast, the presence of fp_0806 and absence of fp_0443 have a smaller positive effect on the predicted AUC. The same-drug cohort examples (MOLM13 and MV411) and same-cell cohort examples (foretinib and dinaciclib) also exhibit sensitive profiles, suggesting that EOL1 is exceptionally sensitive to tandutinib.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for tandutinib is relatively low (R2=0.0849), indicating that the model may not capture the underlying mechanisms of tandutinib's action on EOL1.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, but its relevance to the prediction is unclear.

---

## RPT-0062 - dasatinib on JK1
_Split: test_

## Executive Summary
The sample JK1 treated with dasatinib exhibits an observed AUC of 1.2201, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of JK1 to dasatinib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction error are fp_0367, fp_0760, fp_0204, fp_0062, and TNFRSF12A (51330). The presence of fp_0367 and fp_0760, and the absence of fp_0204 and fp_0062, push the prediction towards lower AUC (greater sensitivity). The gene expression of TNFRSF12A (51330) has a positive SHAP value, indicating that it contributes to higher AUC (lower sensitivity), but its effect is outweighed by the other features.

## Feature and Neighborhood Analysis
The local neighborhood analysis reveals that the cell lines KYO1 and EOL1, which are also of haematopoietic and lymphoid tissue origin, exhibit higher sensitivity to dasatinib (AUC values of 0.1676 and 0.1834, respectively). Similarly, the drugs leptomycin B and oligomycin A, which target different genes, exhibit higher sensitivity in the JK1 cell line (AUC values of 1.4886 and 1.5326, respectively).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for dasatinib is 0.2203, indicating moderate predictability. The cell subtype metadata is available, which may be useful for further analysis. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence.

---

## RPT-0066 - RITA on BCP1
_Split: test_

## Executive Summary
The sample RPT-0066, involving the drug RITA and cell line BCP1, exhibits an observed AUC of 1.5251, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.5251 is significantly lower than the predicted AUC of 12.6318, indicating that the cell line BCP1 is more sensitive to RITA than expected. The large negative prediction error of -11.1067 suggests that there are specific factors contributing to this increased sensitivity. The top TreeSHAP features, including TNFRSF12A, fp_0204, fp_0062, fp_0443, and fp_0760, provide insight into the molecular mechanisms underlying this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP feature, TNFRSF12A, has a SHAP value of -0.6659, indicating that its low expression level (below the cross-cell-line mean) contributes to the increased sensitivity of BCP1 to RITA. The absence of fingerprint bits fp_0204, fp_0062, and fp_0443 also contributes to the sensitivity, while the presence of fp_0760 has a smaller negative effect. These features are present in a small percentage of CTRPv2 compounds, suggesting that they may be specific to certain molecular mechanisms.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features, including fp_0443 and fp_0767, are different from the top features for this specific sample, highlighting the complexity of the model and the importance of local interpretations. The per-drug cross-validated predictability for RITA is moderate (R2=0.2078), indicating that the model is able to capture some of the variability in the response to RITA, but there may be additional factors at play.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the specific sample and cell line. The TreeSHAP values explain the fitted Random Forest prediction for this sample, but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata and feature tables, and may not generalize to other contexts. Additionally, the global model metrics should be treated as training diagnostics rather than held-out performance, and the results should not be used to provide clinical advice.

---

## RPT-0073 - compound 1B on JHUEM1
_Split: test_

## Executive Summary
The sample in question involves compound 1B and cell line JHUEM1, with an observed AUC of 2.5603, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this compound-cell pair.

## Evidence-Based Interpretation
The observed AUC of 2.5603 is significantly lower than the predicted AUC of 13.5611, indicating that compound 1B is more sensitive than expected against the JHUEM1 cell line. This sensitivity is also evident when compared to the drug cohort and cell cohort baselines. The sample percentile of 0.3 in the drug cohort and 1.0 in the cell cohort further supports the exceptional sensitivity of this compound-cell pair.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A, fp_0443, fp_0204, fp_0367, and fp_0062. Positive SHAP values for TNFRSF12A, fp_0443, fp_0204, and fp_0367 suggest that these features push the prediction towards higher AUC/resistance, while the negative SHAP value for fp_0062 pushes the prediction towards lower AUC/sensitivity. However, the absence of these fingerprint features in compound 1B may contribute to its exceptional sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for compound 1B is relatively low, with an R2 of 0.0545, indicating that the model may not capture the underlying mechanisms of this compound-cell pair.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be taken as direct causal evidence. The global model metrics should be treated as training diagnostics, and the per-drug cross-validated predictability for compound 1B is relatively low. Therefore, the results should be interpreted with caution, and further investigation is necessary to fully understand the mechanisms underlying the exceptional sensitivity of compound 1B against the JHUEM1 cell line.

---

## RPT-0077 - barasertib on EOL1
_Split: test_

## Executive Summary
The sample EOL1 treated with barasertib shows an exceptionally sensitive response with an observed AUC of 1.0544, which is significantly lower than the predicted AUC of 12.0153. This discrepancy suggests that the model underestimated the sensitivity of EOL1 to barasertib.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are primarily negative, indicating that they push the prediction towards lower AUC (greater sensitivity). The most significant contributor is TNFRSF12A (gene_expression) with a SHAP value of -0.4578, followed by several fingerprint bits (fp_0227, fp_0367, fp_0131) with negative SHAP values. The presence of these features in the EOL1 cell line contributes to its increased sensitivity to barasertib.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that other cell lines (MOLT16, OCILY19) treated with barasertib also exhibit sensitive responses, although to a lesser extent than EOL1. Similarly, other drugs (foretinib, dinaciclib) tested on the EOL1 cell line show even more sensitive responses. This suggests that EOL1 is a sensitive cell line, and barasertib is a relatively effective drug against it.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928 and RMSE of 1.8342, indicating moderate predictive performance. The top global fingerprint features and most common genes across predictable per-drug models are listed, but their relevance to this specific sample is unclear. The per-drug cross-validated predictability for barasertib is relatively low (R2=0.3743), which may contribute to the prediction error observed in this sample.

## Confidence and Caveats
The interpretation of these results is limited by the availability of data and the constraints of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, and any global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, while the results suggest that EOL1 is exceptionally sensitive to barasertib, further validation and experimentation would be necessary to confirm these findings.

---

## RPT-0121 - daporinad on A673
_Split: test_

## Executive Summary
The sample RPT-0121, involving the drug daporinad on the A673 cell line, exhibits an observed AUC of 1.3954, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.3954 is significantly lower than the predicted AUC of 11.8994, indicating a large negative prediction error. This suggests that the model underestimated the sensitivity of the A673 cell line to daporinad. The sample's sensitivity is also notable when compared to the drug cohort (0.4 percentile) and cell cohort (1.5 percentile) baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP = -0.7232), fp_0706 (SHAP = -0.2173), fp_0062 (SHAP = -0.1073), fp_0443 (SHAP = 0.0811), and fp_0830 (SHAP = -0.0771). The negative SHAP values for TNFRSF12A, fp_0706, fp_0062, and fp_0830 indicate that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP value for fp_0443 pushes the prediction towards higher AUC (greater resistance).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311,258 samples with 2,024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for daporinad has an R2 of 0.1876, indicating moderate predictability. It is essential to note that these metrics are training diagnostics and should not be interpreted as held-out performance.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is crucial to consider the limitations of the model and the potential biases in the training data. The results should not be extrapolated to other cell lines or drugs without proper validation. Additionally, the molecular descriptions are based on local CTRPv2 metadata and feature tables, which may not capture the full complexity of the biological mechanisms involved. Therefore, the results should be treated with caution and considered in the context of the available evidence.

---

## RPT-0133 - birinapant on SKOV3
_Split: test_

## Executive Summary
The SKOV3 cell line treated with birinapant exhibits an exceptionally sensitive response, with an observed AUC of 3.6946, which is significantly lower than the RF-predicted AUC of 14.0506. This discrepancy suggests that the model underestimated the sensitivity of the SKOV3 cell line to birinapant.

## Evidence-Based Interpretation
The observed AUC of 3.6946 indicates a high sensitivity of the SKOV3 cell line to birinapant, which is consistent with the drug's mechanism of action as a SMAC mimetic and inhibitor of inhibitor of apoptosis proteins (IAPs). The large negative prediction error (-10.3560) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443 (SHAP=-0.3551), fp_0767 (SHAP=+0.2438), fp_0504 (SHAP=+0.1826), fp_1009 (SHAP=+0.1696), and fp_0864 (SHAP=+0.1533). The presence of fp_0443 and the absence of fp_0767, fp_0504, fp_1009, and fp_0864 in the birinapant fingerprint contribute to the predicted AUC. The same-drug cohort examples (KYM1 and WSUDLCL2) and same-cell cohort examples (GSK461364 and LBH-589) provide additional context for the sensitivity of the SKOV3 cell line to birinapant.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061), which should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to the specific prediction for birinapant and SKOV3 is limited. The per-drug cross-validated predictability for birinapant (R2=0.0192) suggests that the model may not have fully captured the underlying relationships between birinapant and cell line responses.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The large prediction error and low per-drug cross-validated predictability for birinapant suggest that the model may not have fully captured the underlying relationships between birinapant and cell line responses. Therefore, the results should be treated with caution, and additional experiments or analyses may be necessary to fully understand the sensitivity of the SKOV3 cell line to birinapant.

---

## RPT-0136 - AT13387 on SUPM2
_Split: test_

## Executive Summary
The sample RPT-0136, involving the drug AT13387 on the SUPM2 cell line, exhibits an exceptionally sensitive response with an observed AUC of 2.8574, which is significantly lower than the RF-predicted AUC of 13.1962. This discrepancy suggests that the model underestimated the sensitivity of AT13387 in this specific context.

## Evidence-Based Interpretation
The observed AUC of 2.8574 indicates a higher sensitivity of the SUPM2 cell line to AT13387 compared to the predicted value. According to the rules, a lower AUC value signifies greater sensitivity. The large negative prediction error (-10.3388) further emphasizes the model's underestimation of the drug's effectiveness in this case.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443, fp_1009, TNFRSF12A, fp_0367, and fp_0017. Positive SHAP values for fp_0443, TNFRSF12A, and fp_0367 suggest that these features would push the prediction towards higher AUC (resistance) if present or more expressed, while negative SHAP values for fp_1009 and fp_0017 indicate they contribute to lower AUC (sensitivity). The absence of fp_0443 and presence of fp_1009 in the compound's fingerprint, along with the near-average expression of TNFRSF12A, are key factors influencing the prediction.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061, based on 311,258 samples and 2,024 features. While these metrics are not indicative of held-out performance, they suggest a reasonable fit of the model to the training data. The per-drug cross-validated predictability for AT13387 (R2=0.2709) and the identification of TNFRSF12A as one of the most common genes across predictable per-drug models highlight the complexity of predicting drug responses and the potential for gene expression to influence these predictions.

## Confidence and Caveats
The interpretation of the results is grounded in the provided evidence and adheres to the rules regarding AUC values and SHAP interpretations. However, it is essential to recognize the limitations of the model and the potential for overfitting or underfitting, as indicated by the training diagnostics. The absence of clinical advice and the focus on explaining the model's prediction for this specific sample within the context of the provided data and rules are crucial for a nuanced understanding of the results.

---

## RPT-0143 - cytarabine hydrochloride on KE37
_Split: test_

## Executive Summary
The KE37 cell line exhibits exceptional sensitivity to cytarabine hydrochloride, with an observed AUC of 2.8796, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of KE37 to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 2.8796 indicates that the KE37 cell line is more sensitive to cytarabine hydrochloride than expected. The large negative prediction error of -10.3048 further supports this conclusion. The drug and cell cohorts also show that KE37 is exceptionally sensitive, with a sample percentile of 1.4 in the drug cohort and 2.5 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443, fp_0504, fp_0767, TNFRSF12A, and fp_0864. The presence of fp_0443 (SHAP=-0.7287) and the absence of fp_0504 (SHAP=+0.5512), fp_0767 (SHAP=+0.4276), and fp_0864 (SHAP=+0.2678) contribute to the lower predicted AUC. The low expression of TNFRSF12A (SHAP=-0.3748) also contributes to the predicted sensitivity. The same-drug cohort examples, such as BV173 and REH, and the same-cell cohort examples, such as SB-743921 and leptomycin B, also exhibit sensitivity to their respective drugs.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features include fp_0443, fp_0767, and fp_0504, which are also present in the local feature analysis. The most common genes across predictable per-drug models include TNFRSF12A, which is also featured in the local analysis. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata confirms that KE37 is an acute lymphoblastic T cell leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and supported by the global model context. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to the local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and further investigation is necessary to fully understand the mechanisms underlying the sensitivity of KE37 to cytarabine hydrochloride.

---

## RPT-0153 - daporinad on IMR32
_Split: test_

## Executive Summary
The observed AUC of daporinad on the IMR32 cell line is 1.7024, which is exceptionally sensitive compared to the predicted AUC of 11.8994. This sample was selected due to its large negative prediction error, indicating that the actual sensitivity is higher than the model's prediction.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are TNFRSF12A, fp_0706, fp_0062, fp_0443, and fp_0830. The negative SHAP values for TNFRSF12A, fp_0706, fp_0062, and fp_0830 suggest that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP value for fp_0443 pushes the prediction towards higher AUC (lower sensitivity).

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that TNFRSF12A has a low expression value (1.9073) compared to the cross-cell-line mean, which may contribute to the increased sensitivity of daporinad on the IMR32 cell line. The presence or absence of specific fingerprint bits (fp_0706, fp_0062, fp_0443, and fp_0830) also influences the prediction, with some features being more common in certain compounds. The same-drug cohort examples (GA10 and 697 cell lines) and same-cell cohort examples (SB-743921 and paclitaxel) provide additional context, showing that daporinad tends to be more sensitive on certain cell lines and that the IMR32 cell line is more sensitive to various drugs.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed, with TNFRSF12A being a prominent gene. The per-drug cross-validated predictability for daporinad has an R2 of 0.1876, indicating moderate predictability. It is essential to note that these metrics are based on training data and should not be considered as held-out performance.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the specific sample and cell line. The TreeSHAP values explain the fitted Random Forest prediction but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and any conclusions drawn from this analysis should be carefully considered in the context of these limitations.

---

## RPT-0163 - methotrexate on SUPM2
_Split: test_

## Executive Summary
The SUPM2 cell line exhibits exceptional sensitivity to methotrexate, with an observed AUC of 1.9983, which is significantly lower than the predicted AUC of 12.1192. This discrepancy suggests that the model underestimated the sensitivity of SUPM2 to methotrexate.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the presence of certain fingerprint features, such as fp_0538 and fp_0694, contributes to the observed sensitivity. These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). In contrast, the presence of TNFRSF12A gene expression and the absence of fp_0204 have positive SHAP values, suggesting that they contribute to resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include fp_0538, fp_0694, TNFRSF12A, fp_0204, and fp_0195. The presence of fp_0538 and fp_0694 is associated with increased sensitivity, while the presence of TNFRSF12A is associated with decreased sensitivity. The absence of fp_0204 also contributes to increased sensitivity. The neighborhood analysis shows that other cell lines, such as EOL1 and TF1, also exhibit sensitivity to methotrexate.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr. The model was trained on a large dataset with 311258 samples and 2024 features. The top global fingerprint features are different from those identified in the local analysis, suggesting that the model is capturing different patterns at the global level. The per-drug cross-validated predictability for methotrexate is relatively low (R2=0.1418), indicating that the model may not be well-suited for predicting the response of SUPM2 to methotrexate.

## Confidence and Caveats
The interpretation of the results is limited by the availability of data and the quality of the model. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the per-drug cross-validated predictability for methotrexate is relatively low, which may affect the accuracy of the predictions.

---

## RPT-0181 - AT13387 on GA10
_Split: test_

## Executive Summary
The sample GA10 treated with AT13387 exhibits an observed AUC of 2.4924, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of GA10 to AT13387.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a SHAP value of -0.5999, indicating that the low expression of TNFRSF12A in GA10 pushes the prediction towards lower AUC (greater sensitivity). The presence of fingerprint bits fp_1009 and the absence of fp_0443, fp_0204, and fp_0062 also contribute to the predicted AUC.

## Feature and Neighborhood Analysis
The local analysis reveals that GA10 has a low expression of TNFRSF12A, which is markedly below the cross-cell-line mean. The presence and absence of specific fingerprint bits, such as fp_1009, fp_0443, fp_0204, and fp_0062, also influence the predicted AUC. The same-drug cohort examples, including EOL1 and SIGM5, exhibit more sensitive profiles, while the same-cell cohort examples, including vincristine and SB-743921, also show more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for AT13387 is R2=0.2709, indicating moderate predictability. Cell subtype metadata is available, confirming that GA10 is a Burkitt lymphoma cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should not be used for clinical advice.

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
The observed sensitivity of the SUDHL8 cell line to decitabine can be attributed to various molecular features. According to the TreeSHAP analysis, the absence of certain fingerprint bits (fp_0504, fp_0767, and fp_0864) and the presence of fp_0204 contribute to the sensitivity. Additionally, the low expression of the TNFRSF12A gene (below the cross-cell-line mean) also plays a role in the observed sensitivity. These features push the prediction towards a lower AUC, indicating greater sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include fp_0504, fp_0767, fp_0204, TNFRSF12A, and fp_0864. The absence of fp_0504 and fp_0767, which are present in only 4.4% and 11.0% of CTRPv2 compounds, respectively, contributes to the sensitivity. The presence of fp_0204, found in 2.9% of CTRPv2 compounds, also pushes the prediction towards sensitivity. The low expression of TNFRSF12A, a gene that recurs in 166 predictable-drug RF signatures, further supports the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311258 samples with 2024 features. The top global fingerprint features include fp_0443, fp_0767, and fp_0925, among others. The most common genes across predictable per-drug models are TNFRSF12A, MYOF, and SDC4, among others. The per-drug cross-validated predictability for decitabine is 0.5143, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, which may provide further context for the observed sensitivity.

---

## RPT-0223 - RITA on SH10TC
_Split: test_

## Executive Summary
The sample RPT-0223, involving the drug RITA and cell line SH10TC, exhibits an observed AUC of 3.8331, which is lower than the RF-predicted AUC of 13.5650. This discrepancy indicates that the sample is exceptionally sensitive relative to the predicted response and cohort baselines. The purpose of this report is to provide an evidence-based interpretation of this sensitivity using SHAP values and feature analysis.

## Evidence-Based Interpretation
The observed AUC of 3.8331 is significantly lower than the predicted AUC, suggesting that the sample is more sensitive to the drug RITA than expected. The large negative prediction error of -9.7319 further supports this conclusion. The sample's sensitivity is also evident when compared to the global mean AUC across all pairs (12.8580) and the drug cohort mean AUC (12.6550).

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP=+0.2017), fp_0902 (SHAP=+0.1067), fp_0760 (SHAP=-0.1011), fp_0204 (SHAP=+0.0755), and fp_0367 (SHAP=+0.0753). The presence of fp_0760 and the absence of fp_0902, fp_0204, and fp_0367 contribute to the sample's sensitivity. The neighborhood analysis reveals that similar cell lines, such as TE441T and BCP1, also exhibit sensitivity to RITA, with AUC values of 1.3692 and 1.5251, respectively.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features include fp_0443, fp_0767, and fp_0925. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4. The per-drug cross-validated predictability for RITA has an R2 of 0.2078, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any conclusions drawn from this analysis should be considered in the context of the available data and limitations of the model.

---

## RPT-0224 - PRIMA-1-Met on NCIH2291
_Split: test_

## Executive Summary
The NCIH2291 cell line exhibits exceptional sensitivity to PRIMA-1-Met, with an observed AUC of 3.9753, which is significantly lower than the RF-predicted AUC of 13.6951. This discrepancy suggests that the model underestimated the sensitivity of NCIH2291 to PRIMA-1-Met.

## Evidence-Based Interpretation
The observed AUC of 3.9753 indicates that NCIH2291 is more sensitive to PRIMA-1-Met than expected. The large negative prediction error of -9.7198 further supports this conclusion. The cell line's sensitivity is also evident when compared to the drug cohort, where NCIH2291 falls at the 0.5 percentile, and the cell cohort, where it falls at the 0.3 percentile.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A, fp_0443, fp_0062, fp_0367, and fp_0204. The presence of TNFRSF12A, a gene involved in apoptosis, may contribute to the cell line's sensitivity to PRIMA-1-Met, which re-activates the pro-apoptotic activity of mutant p53. The absence of certain fingerprint features, such as fp_0443 and fp_0062, may also play a role in the cell line's sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061. While these metrics indicate a reasonable fit to the training data, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for PRIMA-1-Met is low, with an R2 of 0.0141, suggesting that the model may not capture the underlying mechanisms of action for this specific drug. The availability of cell subtype metadata, including adenocarcinoma, may provide additional context for understanding the cell line's sensitivity to PRIMA-1-Met.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, the global model context and training diagnostics should be treated with caution, as they may not generalize to held-out data. Additionally, the molecular descriptions and feature importance should be considered in the context of the local CTRPv2 metadata and cohort summaries, rather than being extrapolated to broader biological mechanisms or clinical applications.

---

## RPT-0227 - trametinib on WM88
_Split: test_

## Executive Summary
The sample RPT-0227, which involves the drug trametinib on the cell line WM88, exhibits an observed AUC of 1.4912, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of this observation, focusing on the local SHAP values and global model context.

## Evidence-Based Interpretation
The observed AUC of 1.4912 is significantly lower than the predicted AUC of 11.1998, suggesting that the WM88 cell line is more sensitive to trametinib than expected. The large negative prediction error of -9.7086 further supports this conclusion. The sample percentile of 0.8 in the drug cohort and 0.2 in the cell cohort also indicate that the observed AUC is lower than the average AUC in both cohorts.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC are fp_0367, fp_1008, fp_0409, fp_1001, and fp_0728, with SHAP values of -0.7518, -0.2370, -0.1622, -0.1214, and -0.1061, respectively. These features are present in the trametinib compound and have representative SMARTS patterns. The presence of these features pushes the prediction towards a lower AUC, indicating that they contribute to the sensitivity of the WM88 cell line to trametinib.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The max-depth tuning and N-estimator tuning results suggest that the model is optimized for a max depth of 20 and 100 estimators. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to the specific sample RPT-0227 is limited. The per-drug cross-validated predictability for trametinib has an R2 of 0.3821, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local SHAP values and global model context. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should not be used for clinical advice.

---

## RPT-0234 - cytarabine hydrochloride on P12ICHIKAWA
_Split: test_

## Executive Summary
The sample in question involves the drug cytarabine hydrochloride and the cell line P12ICHIKAWA, with an observed AUC of 3.5152, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 3.5152 is significantly lower than the predicted AUC of 13.1844, indicating that the cell line P12ICHIKAWA is more sensitive to cytarabine hydrochloride than expected. This sensitivity is also evident when compared to the drug cohort and cell cohort baselines, where the sample percentile is 2.3 and 2.7, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443, fp_0504, fp_0767, TNFRSF12A, and fp_0864. The presence of fp_0443 (SHAP=-0.7283) and the absence of fp_0504 (SHAP=+0.5429), fp_0767 (SHAP=+0.4244), and fp_0864 (SHAP=+0.2674) contribute to the lower AUC, indicating increased sensitivity. The low expression of TNFRSF12A (SHAP=-0.3712) also contributes to the increased sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata is available, confirming that the cell line P12ICHIKAWA is an acute lymphoblastic T cell leukaemia. 

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and any clinical implications or decisions should not be based on this analysis alone.

---

## RPT-0253 - cytarabine hydrochloride on MINO
_Split: test_

## Executive Summary
The sample **MINO** treated with **cytarabine hydrochloride** exhibits an observed AUC of **3.6165**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include **fp_0443** (SHAP=-0.7346), **fp_0504** (SHAP=+0.5652), **fp_0767** (SHAP=+0.4308), **TNFRSF12A (51330)** (SHAP=-0.3708), and **fp_0864** (SHAP=+0.2659). The presence of **fp_0443** and the absence of **fp_0504**, **fp_0767**, and **fp_0864** contribute to the observed sensitivity. The low expression of **TNFRSF12A (51330)** also contributes to the sensitivity.

## Feature and Neighborhood Analysis
The same-drug cohort examples, such as **BV173** and **REH**, exhibit more sensitive profiles with AUC values of **0.3812** and **0.3967**, respectively. The same-cell cohort examples, such as **SB-743921** and **docetaxel**, also exhibit more sensitive profiles with AUC values of **0.175** and **0.4282**, respectively. These examples suggest that the observed sensitivity of **MINO** treated with **cytarabine hydrochloride** is consistent with the behavior of similar samples.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The per-drug cross-validated predictability for **cytarabine hydrochloride** is **R2=0.5313**, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The cell subtype metadata confirms that **MINO** is a **mantle cell lymphoma**.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should not be extrapolated to other samples or contexts without caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are limited to the local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance.

---

## RPT-0284 - docetaxel on KPNYN
_Split: test_

## Executive Summary
The KPNYN cell line showed a higher resistance to docetaxel than predicted by the model, with an observed AUC of 17.3740 compared to a predicted AUC of 7.9419. This discrepancy suggests that the model underestimated the resistance of KPNYN cells to docetaxel.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction error are primarily fingerprint bits (fp_1009, fp_0443, fp_0204, and fp_0741) and a gene expression feature (TNFRSF12A). These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). However, the observed AUC is higher than predicted, suggesting that other factors not captured by the model contribute to the resistance of KPNYN cells to docetaxel.

## Feature and Neighborhood Analysis
The fingerprint bits identified as top features are present in a small percentage of CTRPv2 compounds, with example compounds including betulinic acid, isoliquiritigenin, and curcumin. The gene expression feature, TNFRSF12A, has a value markedly below the cross-cell-line mean, which may contribute to the resistance of KPNYN cells to docetaxel. The same-drug cohort examples show that other cell lines (697 and OCIAML3) are more sensitive to docetaxel, while the same-cell cohort examples show that KPNYN cells are more resistant to docetaxel compared to other drugs (leptomycin B and 1S,3R-RSL-3).

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
The top TreeSHAP features contributing to the predicted AUC value include fingerprint bits fp_0367, fp_0091, fp_1001, and fp_0760, as well as the gene expression of TNFRSF12A. These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). The presence of these features in the sample suggests that they may contribute to the observed sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features are associated with specific molecular structures and gene expressions. For example, fp_0367 is present in 6.4% of CTRPv2 compounds and is associated with compounds such as betulinic acid and gossypol. The gene expression of TNFRSF12A is below the cross-cell-line mean, which may also contribute to the observed sensitivity. The same-drug cohort examples, such as EOL1 and SIGM5, also exhibit high sensitivity, suggesting that PF-3758309 may be effective against certain cell lines.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and a training RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for PF-3758309 is 0.3602, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge the limitations of the model and the potential for overfitting. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. Therefore, the results should be treated with caution, and further validation is necessary to confirm the findings. Additionally, the cell subtype metadata is available, which may provide further insight into the observed sensitivity.

---

## RPT-0296 - cytarabine hydrochloride on SUDHL8
_Split: test_

## Executive Summary
The sample RPT-0296, involving cytarabine hydrochloride on the SUDHL8 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.8360, which is significantly lower than the RF-predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of cytarabine hydrochloride in this specific context.

## Evidence-Based Interpretation
The observed AUC of 3.8360 indicates a higher sensitivity of the SUDHL8 cell line to cytarabine hydrochloride compared to the predicted response. The large negative prediction error of -9.3484 further emphasizes the model's underestimation of the drug's effectiveness in this case. The sample's percentile ranks within the drug and cell cohorts (3.1 and 4.1, respectively) also highlight its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include fingerprint bits (fp_0443, fp_0504, fp_0767, and fp_0864) and a gene expression feature (TNFRSF12A). The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 have the most significant impact on the prediction, with SHAP values of -0.7386, 0.5580, 0.4455, and 0.2661, respectively. The gene expression feature TNFRSF12A has a negative SHAP value of -0.3682, indicating its contribution to the underestimation of the drug's sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics are not indicative of held-out performance, they suggest a reasonable fit of the model to the training data. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for cytarabine hydrochloride (R2=0.5313) and the availability of cell subtype metadata (diffuse large B cell lymphoma) are also noted.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is essential to recognize the limitations of the model and the potential for overfitting or underfitting. The large prediction error and the exceptional sensitivity of the sample suggest that there may be factors not captured by the model that contribute to the observed response. Therefore, these findings should be treated with caution and considered in the context of additional evidence and expert knowledge.

---

## RPT-0313 - ML210 on NCIH446
_Split: test_

## Executive Summary
The sample RPT-0313, involving the drug ML210 and the cell line NCIH446, exhibits an observed AUC of 4.2146, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 4.2146 is significantly lower than the RF-predicted AUC of 13.4714, indicating a large negative prediction error. This suggests that the model underestimated the sensitivity of the NCIH446 cell line to ML210. The sample percentile of 3.0 in the drug cohort and 2.0 in the cell cohort further emphasizes the exceptional sensitivity of this sample.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443, TNFRSF12A, fp_1009, fp_0367, and fp_0204. The presence of fp_1009 and the absence of fp_0443, fp_0367, and fp_0204 push the prediction towards lower AUC (greater sensitivity), while the expression of TNFRSF12A pushes the prediction towards higher AUC (lower sensitivity). The same-drug cohort examples, such as DOHH2 and SKNDZ, and same-cell cohort examples, such as leptomycin B and SB-743921, also exhibit higher sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability. The cell subtype metadata, small cell carcinoma, is also available.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge the limitations of the analysis, including the potential for overfitting and the lack of direct causal evidence. The TreeSHAP values explain the fitted Random Forest prediction for this sample but should not be considered as direct causal evidence. Additionally, the global model metrics should be treated with caution, as they are based on training diagnostics rather than held-out performance.

---

## RPT-0321 - mitomycin on IMR32
_Split: test_

## Executive Summary
The IMR32 cell line exhibits exceptional sensitivity to mitomycin, with an observed AUC of 3.2914, which is significantly lower than the predicted AUC of 12.5119. This discrepancy suggests that the model underestimated the sensitivity of IMR32 to mitomycin.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top contributing features to the predicted AUC are TNFRSF12A gene expression, and several fingerprint bits (fp_0204, fp_0443, fp_0062, and fp_0741). The negative SHAP value for TNFRSF12A (-0.6876) indicates that its low expression in IMR32 pushes the prediction towards lower AUC (greater sensitivity). In contrast, the positive SHAP values for fp_0204 and fp_0443 suggest that their absence in mitomycin contributes to the predicted higher AUC (lower sensitivity).

## Feature and Neighborhood Analysis
The presence of fp_0741 in mitomycin has a negative SHAP value (-0.0773), indicating that it contributes to the predicted lower AUC (greater sensitivity). The absence of fp_0062 also has a negative SHAP value (-0.0962), suggesting that its presence would increase the predicted AUC (lower sensitivity). The same-drug cohort examples (KASUMI2 and MV411) and same-cell cohort examples (SB-743921 and paclitaxel) demonstrate that IMR32 is more sensitive to mitomycin compared to other cell lines and drugs.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, it is essential to note that these metrics are based on training data and should not be considered as held-out performance. The per-drug cross-validated predictability for mitomycin (R2=0.3579) suggests moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The model's performance and feature importance should be considered in the context of the training data and may not generalize to unseen data. Additionally, the absence of certain information, such as the gene target for mitomycin, may limit the interpretation of the results.

---

## RPT-0334 - ML210 on NCO2
_Split: test_

## Executive Summary
The sample **NCO2** treated with **ML210** exhibits an exceptionally sensitive response with an observed AUC of **3.3964**, which is significantly lower than the predicted AUC of **12.5487**. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of **3.3964** indicates a higher sensitivity of the **NCO2** cell line to **ML210** compared to the predicted response. The large negative prediction error of **-9.1523** further supports this interpretation. The sample's percentile ranks within the drug and cell cohorts (1.7% and 4.7%, respectively) also indicate that this response is unusually sensitive.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include **TNFRSF12A** (SHAP=-0.6706), **fp_0443** (SHAP=+0.4031), **fp_1009** (SHAP=-0.1715), **fp_0204** (SHAP=+0.1396), and **fp_0367** (SHAP=+0.0440). The negative SHAP value for **TNFRSF12A** suggests that its expression level pushes the prediction towards lower AUC (higher sensitivity), while the positive SHAP values for the fingerprint features **fp_0443**, **fp_0204**, and **fp_0367** indicate that their presence or absence contributes to higher AUC (lower sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of **0.4928** and a training RMSE of **1.8342**. The top global fingerprint features and most common genes across predictable per-drug models are also listed, but these should be treated as training diagnostics rather than held-out performance metrics. The per-drug cross-validated predictability for **ML210** is **0.3111**, indicating moderate predictability. The cell subtype metadata confirms that **NCO2** is a chronic myeloid leukaemia cell line. 

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance.

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
The sample RPT-0345, involving the drug ML210 and cell line PEER, exhibits an observed AUC of 3.4663, which is exceptionally sensitive compared to the predicted AUC of 12.5487 and cohort baselines. This report aims to provide an evidence-based interpretation of this observation using SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (-9.0824) suggests that the model underestimated the sensitivity of ML210 in the PEER cell line. The observed AUC is lower than the global mean AUC across all pairs (12.8580), indicating greater sensitivity. The sample percentile of 2.0 in the drug cohort and 2.3 in the cell cohort further supports this interpretation.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP=-0.6682), fp_0443 (SHAP=+0.4206), fp_1009 (SHAP=-0.1750), fp_0204 (SHAP=+0.1396), and fp_0062 (SHAP=-0.0499). The negative SHAP value for TNFRSF12A and fp_1009 suggests that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP value for fp_0443 and fp_0204 pushes the prediction towards higher AUC (lower sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The per-drug cross-validated predictability for ML210 is R2=0.3111, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The cell subtype metadata confirms that the PEER cell line is classified as acute lymphoblastic T cell leukaemia.

## Confidence and Caveats
The interpretation of this report is grounded in the provided SHAP values and feature analysis. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and any clinical implications or advice should not be inferred from this report.

---

## RPT-0353 - cytarabine hydrochloride on RPMI8402
_Split: test_

## Executive Summary
The sample RPMI8402 treated with cytarabine hydrochloride exhibits an exceptionally sensitive response, with an observed AUC of 4.1214, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of this particular cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 4.1214 indicates a high sensitivity of RPMI8402 cells to cytarabine hydrochloride. In contrast, the predicted AUC of 13.1844 suggests a lower sensitivity. The large negative prediction error of -9.0630 highlights the discrepancy between the observed and predicted responses. The sample's sensitivity is also notable when compared to the drug and cell cohorts, with a sample percentile of 3.3 and 3.8, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443, fp_0504, fp_0767, TNFRSF12A, and fp_0864. The presence of fp_0443 (SHAP = -0.7202) and the absence of fp_0504 (SHAP = 0.5370), fp_0767 (SHAP = 0.4164), and fp_0864 (SHAP = 0.2683) contribute to the predicted AUC. The low expression of TNFRSF12A (SHAP = -0.3708) also plays a role in the predicted response. These features are present or absent in specific compounds, such as nilotinib, bleomycin A2, topotecan, and mitomycin.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311,258 samples with 2,024 features. The top global fingerprint features include fp_0443, fp_0767, and fp_0504, which are also present in the local feature analysis. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, which may provide further context for the observed response.

---

## RPT-0360 - birinapant on HEC265
_Split: test_

## Executive Summary
The sample HEC265 treated with birinapant exhibits an exceptionally sensitive response, with an observed AUC of 5.0118, which is significantly lower than the RF-predicted AUC of 14.0621. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The Top TreeSHAP features provide insight into the factors contributing to this sensitive response. The presence of **fp_0443** (SHAP=-0.3698) and the absence of **fp_0767** (SHAP=+0.2403), **fp_0864** (SHAP=+0.1776), **fp_0504** (SHAP=+0.1704), and **fp_1009** (SHAP=+0.1598) are the most influential factors. These fingerprint bits are associated with specific molecular structures, but their presence or absence does not imply a direct causal relationship with the observed sensitivity.

## Feature and Neighborhood Analysis
The same-drug cohort examples (KYM1 and WSUDLCL2) and same-cell cohort examples (leptomycin B and oligomycin A) demonstrate that the observed sensitivity is not unique to this specific drug-cell line combination. The presence of **fp_0443** in birinapant and its association with a negative SHAP value suggests that this feature may contribute to the increased sensitivity of HEC265 to birinapant.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance metrics. The per-drug cross-validated predictability for birinapant (R2=0.0192) indicates that the model's performance for this specific drug is limited. The availability of cell subtype metadata (adenocarcinoma) may be relevant for understanding the biology underlying the observed sensitivity, but it is not directly related to the model's prediction. The top global fingerprint features and most common genes across predictable per-drug models are provided for context, but their relevance to this specific sample is unclear.

---

## RPT-0393 - BRD-K61166597 on GSS
_Split: test_

## Executive Summary
The sample RPT-0393, involving the drug BRD-K61166597 on the GSS cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.6444, which is significantly lower than the RF-predicted AUC of 13.5650. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of 4.6444 indicates a higher sensitivity than expected, given the predicted AUC and cohort baselines. The large negative prediction error of -8.9206 further emphasizes this point. The sample's sensitivity is notable, ranking in the 0.1 percentile of the drug cohort and 3.8 percentile of the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a positive SHAP value of +0.2158, and several fingerprint bits (fp_0443, fp_0204, fp_0367) with positive SHAP values, indicating that their presence or absence pushes the prediction towards higher AUC (resistance). In contrast, fp_0062 has a negative SHAP value of -0.0575, suggesting its absence contributes to lower AUC (sensitivity). The local neighborhood analysis shows that similar cell lines (EOL1, SEM) and drugs (paclitaxel, SB-743921) exhibit more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model's performance on the training data is notable, but these metrics should not be taken as indicative of held-out performance. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but do not directly influence the interpretation of this specific sample. The per-drug cross-validated predictability for BRD-K61166597 (R2=0.3454) and available cell subtype metadata (adenocarcinoma) further inform the analysis.

## Confidence and Caveats
The interpretation of this sample's sensitivity is grounded in the local evidence and TreeSHAP analysis. However, it is essential to recognize the limitations of the model and the potential for overfitting, as indicated by the training diagnostics. The absence of direct causal evidence and the reliance on training data metrics mean that these findings should be treated with caution. Further investigation and validation would be necessary to confirm the observed sensitivity and underlying mechanisms.

---

## RPT-0398 - cytarabine hydrochloride on CHP212
_Split: test_

## Executive Summary
The sample RPT-0398, involving cytarabine hydrochloride on the CHP212 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.6951, which is significantly lower than the RF-predicted AUC of 13.5949. This discrepancy suggests that the model underestimated the sensitivity of cytarabine hydrochloride on CHP212 cells.

## Evidence-Based Interpretation
The observed AUC of 4.6951 indicates a high sensitivity of the CHP212 cell line to cytarabine hydrochloride. In contrast, the RF-predicted AUC of 13.5949 suggests a lower sensitivity. The large negative prediction error of -8.8998 highlights the model's underestimation of the actual sensitivity. The sample's percentile ranks within the drug and cell cohorts (4.6 and 4.1, respectively) further emphasize its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443 (SHAP=-0.7612), fp_0504 (SHAP=+0.4053), fp_0767 (SHAP=+0.3200), fp_0864 (SHAP=+0.1892), and fp_0450 (SHAP=-0.1741). The presence of fp_0443 and fp_0450, and the absence of fp_0504, fp_0767, and fp_0864, contribute to the observed sensitivity. The representative SMARTS patterns and example compounds associated with these features provide insight into the molecular characteristics influencing the response.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models offer a broader understanding of the model's performance. The per-drug cross-validated predictability for cytarabine hydrochloride (R2=0.5313) indicates moderate predictability. However, it is essential to treat these metrics as training diagnostics rather than held-out performance.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The model's underestimation of the actual sensitivity may be due to various factors, including the complexity of the biological system, limitations of the training data, or the specific characteristics of the CHP212 cell line. Therefore, these findings should be considered in the context of the available data and model constraints.

---

## RPT-0418 - selumetinib on OCUM1
_Split: test_

## Executive Summary
The OCUM1 cell line exhibits exceptional sensitivity to selumetinib, with an observed AUC of 3.8209, which is lower than the predicted AUC of 12.6775. This discrepancy suggests that the model underestimated the sensitivity of OCUM1 to selumetinib. The top TreeSHAP features contributing to this prediction error include fingerprint bits fp_0367, fp_1001, and gene expression of TNFRSF12A.

## Evidence-Based Interpretation
The observed AUC of 3.8209 indicates that OCUM1 is more sensitive to selumetinib than predicted. The negative SHAP values for fp_0367, fp_1001, and fp_0053 suggest that the presence of these fingerprint bits contributes to the increased sensitivity. In contrast, the positive SHAP value for TNFRSF12A gene expression indicates that higher expression levels of this gene may be associated with decreased sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the molecular characteristics contributing to the exceptional sensitivity of OCUM1 to selumetinib. Fingerprint bits fp_0367, fp_1001, and fp_0053 are present in a small percentage of CTRPv2 compounds, suggesting that these features may be unique to a subset of compounds with high potency against OCUM1. The presence of these fingerprint bits may be associated with increased binding affinity or specificity for the target protein.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The per-drug cross-validated predictability for selumetinib is relatively low (R2=0.2298), indicating that the model may not capture all the relevant factors contributing to the response. The most common genes across predictable per-drug models, including TNFRSF12A, may be important for understanding the mechanisms of action for selumetinib and other compounds.

## Confidence and Caveats
The interpretation of the results is limited to the local context of the OCUM1 cell line and selumetinib. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated with caution, as they are based on training diagnostics rather than held-out performance.

---

## RPT-0421 - ML210 on RH18
_Split: test_

## Executive Summary
The sample RPT-0421, involving drug ML210 and cell line RH18, exhibits an exceptionally sensitive response with an observed AUC of 4.6495, which is significantly lower than the RF-predicted AUC of 13.4979. This discrepancy suggests that the model underestimated the sensitivity of ML210 in RH18 cells.

## Evidence-Based Interpretation
The Top TreeSHAP features for this sample indicate that the presence or absence of specific molecular fingerprints (fp_0443, fp_0367, fp_1009, and fp_0204) and the expression level of the gene TNFRSF12A contribute to the predicted AUC. The positive SHAP values for fp_0443, fp_0367, and fp_0204 suggest that their absence pushes the prediction towards higher AUC (resistance), while the negative SHAP value for fp_1009 indicates that its presence pushes the prediction towards lower AUC (sensitivity). The positive SHAP value for TNFRSF12A suggests that its expression level also contributes to the predicted AUC.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the absence of fp_0443, fp_0367, and fp_0204, and the presence of fp_1009, are associated with the observed sensitivity of ML210 in RH18 cells. The expression level of TNFRSF12A is near the cross-cell-line mean, which may not be a significant contributor to the observed sensitivity. The same-drug cohort examples (DOHH2 and SKNDZ) and same-cell cohort examples (1S,3R-RSL-3 and LBH-589) also exhibit more sensitive responses, suggesting that ML210 may be generally effective against certain cell lines.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance metrics. The top global fingerprint features and most common genes across predictable per-drug models provide additional context for the model's predictions. The per-drug cross-validated predictability for ML210 (R2=0.3111) suggests that the model has some ability to predict the response of ML210 in different cell lines. However, the large prediction error for RPT-0421 highlights the limitations of the model and the need for further investigation.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance. Further investigation is needed to fully understand the mechanisms underlying the observed sensitivity of ML210 in RH18 cells.

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
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any pathways, biomarkers, or mechanisms inferred from the data are not supported by the prompt.

---

## RPT-0427 - salermide on SCC25
_Split: test_

## Executive Summary
The sample RPT-0427, involving the drug salermide on the SCC25 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.7206, which is significantly lower than the RF-predicted AUC of 13.5650. This discrepancy suggests that the model underestimated the sensitivity of salermide on SCC25 cells.

## Evidence-Based Interpretation
The observed AUC of 4.7206 indicates a higher sensitivity of the SCC25 cell line to salermide compared to the predicted response. The large negative prediction error of -8.8444 further supports this interpretation. The sample's sensitivity is also notable when compared to the drug cohort and cell cohort baselines, with the sample percentile being 0.2 for the drug cohort and 2.4 for the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include TNFRSF12A, fp_0443, fp_0204, fp_0062, and fp_0367. Positive SHAP values for TNFRSF12A, fp_0443, fp_0204, and fp_0367 suggest that these features push the prediction towards higher AUC/resistance, while the negative SHAP value for fp_0062 pushes the prediction towards lower AUC/sensitivity. The absence of certain fingerprint features, such as fp_0443, fp_0204, and fp_0367, in the sample may contribute to its exceptional sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, train RMSE of 1.8342, and train correlation of 0.7061. The model's performance on the training data is moderate, but these metrics should not be taken as indicative of held-out performance. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to the specific sample RPT-0427 is limited. The per-drug cross-validated predictability for salermide is negative (R2=-0.0579), suggesting that the model may not be well-suited for predicting the response of salermide on various cell lines.

---

## RPT-0432 - KX2-391 on HUNS1
_Split: test_

## Executive Summary
The sample RPT-0432, treated with KX2-391 on the HUNS1 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.0988, which is significantly lower than the RF-predicted AUC of 11.9252. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of 3.0988 indicates a higher sensitivity to KX2-391 compared to the predicted value. According to the rules, a lower AUC value corresponds to greater sensitivity. The large negative prediction error of -8.8264 further emphasizes the unexpected sensitivity of the HUNS1 cell line to KX2-391.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC value include TNFRSF12A (gene_expression) with a SHAP value of -0.7402, indicating that its low expression pushes the prediction towards lower AUC (higher sensitivity). Fingerprint features such as fp_0443, fp_0706, fp_1009, and fp_0062 also contribute to the prediction, with positive SHAP values indicating their presence or absence pushes the prediction towards higher AUC (lower sensitivity). The presence of these features in the compound and their frequency in the CTRPv2 dataset provide additional context for the prediction.

## Model-Level Context
The global model context provides training diagnostics, including an R2 value of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The top global fingerprint features and most common genes across predictable per-drug models offer insight into the broader patterns in the data. The per-drug cross-validated predictability for KX2-391 (R2=0.4019) suggests moderate predictability for this specific drug. The availability of cell subtype metadata (plasma cell myeloma) provides additional context for the HUNS1 cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the provided evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not constitute direct causal evidence. The molecular descriptions are based solely on local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated with caution, as they represent training diagnostics rather than held-out performance.

---

## RPT-0436 - pluripotin on PFEIFFER
_Split: test_

## Executive Summary
The sample RPT-0436, involving the drug **pluripotin** on the **PFEIFFER** cell line, exhibits an exceptionally sensitive response with an observed AUC of **3.3353**, which is significantly lower than the RF-predicted AUC of **12.1584**. This discrepancy suggests that the model underestimated the sensitivity of **pluripotin** in this specific context.

## Evidence-Based Interpretation
The observed AUC of **3.3353** indicates a higher sensitivity of the **PFEIFFER** cell line to **pluripotin** compared to the model's prediction. The large negative prediction error of **-8.8231** further emphasizes this point. The sample's percentile rank of 1.6 in the drug cohort and 5.8 in the cell cohort also supports the interpretation that this response is exceptionally sensitive.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include **fp_0623**, **fp_0367**, **fp_0235**, **fp_0204**, and **fp_0372**. The presence of **fp_0623**, **fp_0367**, **fp_0235**, and **fp_0372** pushes the prediction towards lower AUC (higher sensitivity), while the absence of **fp_0204** has a smaller effect in the opposite direction. These features are associated with specific molecular structures and are present in various compounds, including trifluoperazine, prochlorperazine, and pifithrin-alpha.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model's performance on the **pluripotin** drug is modest, with a per-drug cross-validated predictability R2 of 0.1556. The most common genes across predictable per-drug models do not directly relate to the **pluripotin** mechanism but provide a broader context for the model's capabilities. The cell subtype metadata confirms that the **PFEIFFER** cell line is classified as diffuse large B cell lymphoma.

## Confidence and Caveats
While the analysis provides insights into the exceptional sensitivity of **pluripotin** on the **PFEIFFER** cell line, it is essential to recognize the limitations of the model and the data. The TreeSHAP values explain the fitted Random Forest prediction but do not constitute direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata and feature tables, and any global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, the interpretation should be considered in the context of these constraints and not used for clinical advice.

---

## RPT-0440 - ABT-199 on RL
_Split: test_

## Executive Summary
The sample **RL** treated with **ABT-199** shows an observed AUC of **3.5868**, which is exceptionally sensitive compared to the predicted AUC of **12.4005** and cohort baselines. This large negative prediction error indicates that the model underestimated the sensitivity of **RL** to **ABT-199**.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include **TNFRSF12A** (gene_expression) with a SHAP value of **-0.6288**, indicating that lower expression of **TNFRSF12A** in **RL** contributes to its sensitivity to **ABT-199**. Other contributing features include fingerprint bits **fp_0443**, **fp_1009**, **fp_0227**, and **fp_0806**, which represent specific molecular structures present or absent in **ABT-199**.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that **RL** is more sensitive to **ABT-199** compared to other cell lines, such as **EOL1** and **NUDHL1**, which have lower AUC values. Similarly, **RL** is more sensitive to other drugs, such as **LBH-589** and **SB-743921**, which target different genes. The presence or absence of specific fingerprint bits in **ABT-199** also influences its predicted AUC value.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of **0.4928** and RMSE of **1.8342**. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for **ABT-199** is **0.2474**, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are limited to the provided data and should not be extrapolated to other contexts. Additionally, the global model metrics should be treated with caution, as they are based on training data and may not generalize to held-out data.

---

## RPT-0441 - PF-3758309 on D283MED
_Split: test_

## Executive Summary
The sample **D283MED** treated with **PF-3758309** shows an observed AUC of **3.0751**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The prediction error is **-8.8136**, indicating that the actual response is more sensitive than predicted.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this sensitivity include **fp_0367**, **fp_0091**, **TNFRSF12A (51330)**, **fp_1001**, and **fp_0062**, with negative SHAP values pushing the prediction towards lower AUC/sensitivity. However, since the observed AUC is already low, these features are actually contributing to the observed sensitivity. The presence of certain fingerprint bits (**fp_0367**, **fp_0091**, **fp_1001**) and the low expression of **TNFRSF12A (51330)** are associated with increased sensitivity.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that the presence of specific molecular substructures (**fp_0367**, **fp_0091**, **fp_1001**) and the low expression of **TNFRSF12A (51330)** are contributing to the observed sensitivity. The absence of **fp_0062** also plays a role. The same-drug cohort examples (**EOL1**, **SIGM5**) and same-cell cohort examples (**LBH-589**, **ouabain**) further support the notion that **D283MED** is exceptionally sensitive to **PF-3758309**.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for **PF-3758309** is **R2=0.3602**, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Clinical advice should not be given based on this report.

---

## RPT-0449 - BMS-754807 on KMS26
_Split: test_

## Executive Summary
The sample RPT-0449, treated with BMS-754807 on the KMS26 cell line, exhibited an observed AUC of 3.6784, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The observed AUC of 3.6784 is lower than the predicted AUC of 12.4736, indicating that the sample is more sensitive than expected. The sample percentile of 0.1 in the drug cohort and 4.4 in the cell cohort further supports this interpretation. The top TreeSHAP features, including TNFRSF12A, fp_0204, fp_0367, fp_0062, and fp_0443, contribute to the predicted AUC, with TNFRSF12A having the largest negative SHAP value, pushing the prediction towards lower AUC/sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. TNFRSF12A, a gene expression feature, has a negative SHAP value, indicating that its low expression in this sample contributes to the observed sensitivity. The fingerprint features, such as fp_0204, fp_0367, fp_0062, and fp_0443, also play a role in the predicted AUC, with some features being present or absent in the sample. The same-drug cohort examples, such as RH41 and NCIH929, and same-cell cohort examples, such as SB-743921 and paclitaxel, provide additional context for the sample's sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models offer insight into the broader model landscape. The per-drug cross-validated predictability for BMS-754807 is relatively low, with an R2 of 0.2101. The availability of cell subtype metadata, such as plasma cell myeloma, may be relevant for future analyses.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. The global model metrics should be treated as training diagnostics rather than held-out performance, and any conclusions drawn from this analysis should be carefully considered in the context of these limitations.

---

## RPT-0460 - RITA on MV411
_Split: test_

## Executive Summary
The sample RPT-0460, involving the drug RITA and cell line MV411, exhibits an exceptionally sensitive response with an observed AUC of 3.8603, which is significantly lower than the RF-predicted AUC of 12.6318. This discrepancy suggests that the model underestimated the sensitivity of RITA in MV411 cells.

## Evidence-Based Interpretation
The observed AUC of 3.8603 indicates a higher sensitivity of MV411 cells to RITA compared to the predicted response. The large negative prediction error of -8.7715 further supports this interpretation, suggesting that the model's prediction was overly resistant. The sample's percentile rank of 1.0 in the drug cohort and 6.9 in the cell cohort also indicates that MV411 cells are more sensitive to RITA than expected.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include TNFRSF12A (gene_expression) with a SHAP value of -0.6709, indicating that lower expression of TNFRSF12A pushes the prediction towards higher sensitivity. The absence of fingerprint bits fp_0204, fp_0062, and fp_0443 also contributes to the predicted response, with SHAP values of +0.1671, -0.0831, and +0.0754, respectively. The presence of fp_0760 has a SHAP value of -0.0594, indicating a push towards higher sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model's performance on the training data is moderate, but these metrics should not be taken as indicative of held-out performance. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for RITA is 0.2078, indicating moderate predictability. The availability of cell subtype metadata, specifically acute myeloid leukaemia, may be relevant for understanding the sample's response.

---

## RPT-0463 - KX2-391 on PECAPJ34CLONEC12
_Split: test_

## Executive Summary
The observed AUC of 4.3771 for KX2-391 on the PECAPJ34CLONEC12 cell line indicates that this cell line is more sensitive to the drug than the model predicted, with a prediction error of -8.7625. This sensitivity is notable given the cell line's tissue origin (upper aerodigestive tract) and histology (squamous cell carcinoma).

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction include fingerprint bits (fp_0443, fp_0706, fp_1009, fp_0806) and a gene expression feature (TNFRSF12A). Positive SHAP values for fp_0443 and TNFRSF12A suggest that these factors would increase the AUC (or resistance) if they were more prominent, while negative SHAP values for fp_0706 and fp_1009 indicate that their presence contributes to the observed sensitivity. The presence of these fingerprint bits and the expression level of TNFRSF12A in this cell line are key factors in understanding its sensitivity to KX2-391.

## Feature and Neighborhood Analysis
The neighborhood analysis, including same-drug and same-cell cohort examples, provides context for the sensitivity of PECAPJ34CLONEC12 to KX2-391. Other cell lines, such as IMR32 and SNU16, also show sensitivity to KX2-391, suggesting a pattern of response across different tissues and cell types. Similarly, other drugs like leptomycin B and SB-743921 show sensitivity in the PECAPJ34CLONEC12 cell line, indicating that this cell line may have a broader susceptibility profile. The fingerprint bits and gene expression features identified by TreeSHAP offer insights into the molecular characteristics that contribute to this sensitivity.

## Model-Level Context
The global model context provides training diagnostics (train_r2=0.4928, train_rmse=1.8342, train_corr=0.7061) that indicate the model's fit to the training data but should not be interpreted as held-out performance. The per-drug cross-validated predictability for KX2-391 (R2=0.4019) suggests moderate predictability of its effects across different cell lines. The most common genes across predictable per-drug models, including TNFRSF12A, may play significant roles in determining drug sensitivity across various cell lines. However, these findings are based on training data and should be considered in the context of the model's limitations and the specific query regarding KX2-391 and PECAPJ34CLONEC12.

## Confidence and Caveats
The interpretation of the results is grounded in the evidence provided by the TreeSHAP analysis and the characteristics of the cell line and drug in question. However, it is essential to consider the limitations of the model, including its training diagnostics and the potential for overfitting or biases in the data. The absence of direct causal evidence and the reliance on training data for model evaluation are significant caveats. Clinical applications or interpretations of these findings should be approached with caution and ideally validated through additional experiments or analyses

---

## RPT-0468 - daporinad on DND41
_Split: test_

## Executive Summary
The sample RPT-0468, involving the drug daporinad on the DND41 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.1634, which is significantly lower than the RF-predicted AUC of 11.8994. This discrepancy suggests that the model underestimated the sensitivity of daporinad in this specific context.

## Evidence-Based Interpretation
The observed AUC of 3.1634 indicates a higher sensitivity of the DND41 cell line to daporinad compared to the predicted value. The large negative prediction error of -8.7360 further emphasizes this discrepancy. The sample's percentile ranks within the drug and cell cohorts (2.2 and 1.2, respectively) also indicate that this response is unusually sensitive.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to this prediction include TNFRSF12A (gene_expression) with a SHAP value of -0.7209, indicating that lower expression of this gene pushes the prediction towards higher sensitivity. Fingerprint features such as fp_0706, fp_0062, fp_0443, and fp_0830 also contribute to the prediction, with some being present or absent in the compound structure. These features suggest that the molecular characteristics of daporinad and the genetic profile of the DND41 cell line interact to produce this sensitive response.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928 and RMSE of 1.8342, which should not be interpreted as held-out performance. The model's ability to predict the response of daporinad is modest, with a per-drug cross-validated R2 of 0.1876. The most common genes across predictable per-drug models, including TNFRSF12A, may play important roles in determining drug responses. However, these findings should be treated with caution and considered in the context of the specific sample and cell line.

## Confidence and Caveats
The interpretation of these results is grounded in the local evidence and should not be extrapolated to other contexts without caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata and feature tables, and any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the absence of certain information, such as clinical advice, is intentional, as this report aims to provide a neutral, evidence-based explanation of the observed phenomenon.

---

## RPT-0482 - ZSTK474 on RI1
_Split: test_

## Executive Summary
The sample RI1 treated with ZSTK474 exhibits an observed AUC of 3.7580, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of RI1 to ZSTK474.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression; SHAP=-0.7081), which has a value below the cross-cell-line mean, and several fingerprint bits (fp_0062, fp_0443, fp_0806, fp_0920) with varying SHAP values. These features suggest that the model is using a combination of gene expression and chemical structure information to predict the response of RI1 to ZSTK474.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that other cell lines (SUDHL6, JVM2) treated with ZSTK474 exhibit similar sensitivity profiles, with AUC values ranging from 3.4418 to 3.979. Additionally, other drugs (vincristine, paclitaxel) tested on RI1 exhibit even greater sensitivity, with AUC values ranging from 1.8879 to 1.9355. The top TreeSHAP features for this sample, particularly TNFRSF12A, recur in multiple predictable-drug RF signatures, suggesting that these features may be important for predicting response to other drugs as well.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics suggest that the model is reasonably well-fit to the training data, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for ZSTK474 is relatively low (R2=0.0724), indicating that the model may not be highly confident in its predictions for this specific drug. The availability of cell subtype metadata (B cell lymphoma) may provide additional context for interpreting the results, but it is not directly used in the model.

## Confidence and Caveats
The results should be interpreted with caution, as the model is not perfect and may be subject to various sources of error. The large negative prediction error for this sample suggests that the model may be underestimating the sensitivity of RI1 to ZSTK474, but this could be due to various factors, including noise in the data or limitations of the model. Additionally, the results are based on a single sample and may not generalize to other cell lines or drugs. Further experimentation and validation would be necessary to confirm the findings and establish their broader applicability.

---

## RPT-0486 - BRD-K97651142 on FADU
_Split: test_

## Executive Summary
The sample RPT-0486, involving the drug BRD-K97651142 on the FADU cell line, exhibits an observed AUC of 4.8298, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The prediction error is -8.6843, indicating that the actual sensitivity is higher than predicted.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction include TNFRSF12A (gene_expression) with a SHAP value of +0.1928, and several fingerprint bits (fp_0443, fp_0367, fp_0806, and fp_0062) with varying SHAP values. These features suggest that the presence or absence of specific molecular structures and gene expressions influence the predicted AUC. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that the sample is more sensitive than other samples in the same-drug cohort (e.g., NCIH1975 and EOL1 cell lines) and same-cell cohort (e.g., leptomycin B and topotecan drugs). The presence of specific fingerprint bits, such as fp_0806, and the absence of others, like fp_0443 and fp_0367, may contribute to this increased sensitivity. The gene expression of TNFRSF12A, which is near the cross-cell-line mean, also plays a role in the predicted response.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, it is crucial to treat these metrics as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for BRD-K97651142 has an R2 of 0.1367, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results should be grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. The TreeSHAP values and feature analysis provide insights into the predicted response, but it is essential to recognize that these are not direct causal evidence. The global model context and training diagnostics should be treated with caution, and any conclusions drawn from this analysis should be considered in the context of the available data and limitations of the model.

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
The SNU620 cell line treated with SGX-523 (a MET inhibitor) showed an observed AUC of 4.9811, which is exceptionally sensitive compared to the predicted AUC of 13.6218 and cohort baselines. This sample was selected due to its large negative prediction error, indicating higher sensitivity than expected.

## Evidence-Based Interpretation
The observed AUC of 4.9811 suggests that the SNU620 cell line is more sensitive to SGX-523 than predicted. The top TreeSHAP features contributing to this prediction include TNFRSF12A gene expression and several fingerprint bits (fp_0204, fp_0443, fp_0062, and fp_0227). Positive SHAP values for TNFRSF12A, fp_0204, fp_0443, and fp_0227 indicate that these features push the prediction towards higher AUC (resistance), while the negative SHAP value for fp_0062 pushes the prediction towards lower AUC (sensitivity).

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of this sample. TNFRSF12A gene expression has a positive SHAP value, suggesting that its expression level contributes to the predicted resistance. The fingerprint bits (fp_0204, fp_0443, fp_0062, and fp_0227) also have significant SHAP values, indicating their importance in the prediction. The presence or absence of these fingerprint bits in the compound structure may influence the sensitivity of the cell line to SGX-523.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for SGX-523 (R2=0.1795) suggests moderate predictability. The most common genes across predictable per-drug models, including TNFRSF12A, may be important for understanding the mechanism of action of SGX-523. However, it is essential to note that these findings are based on training diagnostics and should be interpreted with caution.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is crucial to consider the limitations of the model and the data. The global model metrics are training diagnostics and should not be used to make predictions about held-out data. Additionally, the molecular descriptions are based on local CTRPv2 metadata and feature tables, which may not capture the full complexity of the biological system. Therefore, the results should be interpreted with caution, and further investigation is necessary to fully understand the mechanisms underlying the sensitivity of the SNU620 cell line to SGX-523.

---
