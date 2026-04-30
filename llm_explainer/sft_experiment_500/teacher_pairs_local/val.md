# Teacher Pairs - Llama-3.3-70B-Instruct - val

## RPT-0003 - cytarabine hydrochloride on BV173
_Split: val_

## Executive Summary
The sample in question involves the drug cytarabine hydrochloride and the cell line BV173, with an observed AUC of 0.3812, indicating exceptional sensitivity relative to the predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 0.3812 is significantly lower than the predicted AUC of 13.1844, indicating that the cell line BV173 is more sensitive to cytarabine hydrochloride than expected. This sensitivity is also evident when compared to the global mean AUC across all pairs (12.8580) and the drug cohort mean (11.6275). The cell line's sensitivity is further supported by its position in the lower percentile of both the drug and cell cohorts.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443 (SHAP=-0.7340), fp_0504 (SHAP=+0.5531), fp_0767 (SHAP=+0.4454), TNFRSF12A (SHAP=-0.3734), and fp_0864 (SHAP=+0.2678). The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 in cytarabine hydrochloride contribute to the underestimation of sensitivity. The low expression of TNFRSF12A (below the cross-cell-line mean) also pushes the prediction towards lower sensitivity. The same-drug and same-cell cohort examples (e.g., REH, 697, BI-2536, and paclitaxel) provide additional context, showing that BV173 is more sensitive than other cell lines to cytarabine hydrochloride and other drugs.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061), which should not be interpreted as held-out performance. The model's top global fingerprint features and most common genes across predictable per-drug models offer insight into the broader predictive landscape. The per-drug cross-validated predictability for cytarabine hydrochloride (R2=0.5313) indicates moderate predictability. The availability of cell subtype metadata (blast phase; chronic myeloid leukaemia) adds context to the cell line's characteristics.

## Confidence and Caveats
While the analysis provides evidence for the exceptional sensitivity of BV173 to cytarabine hydrochloride, it is essential to recognize the limitations of the model and the data. The TreeSHAP values explain the fitted Random Forest prediction but do not constitute direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, feature tables, and cohort summaries, and any global model metrics should be treated with caution. The results should not be used for clinical advice, and further investigation is necessary to fully understand the underlying mechanisms and pathways involved.

---

## RPT-0024 - AZD4547 on NCIH716
_Split: val_

## Executive Summary
The sample NCIH716 treated with AZD4547 shows an exceptionally sensitive response with an observed AUC of 1.1299, which is significantly lower than the predicted AUC of 13.2363. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of 1.1299 indicates a high sensitivity of the NCIH716 cell line to AZD4547. In contrast, the predicted AUC of 13.2363 suggests a much higher resistance. The large negative prediction error of -12.1064 highlights the model's underestimation of the drug's effectiveness in this case. The sample's percentile ranks within the drug and cell cohorts (0.1 and 0.2, respectively) further emphasize its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a positive SHAP value of 0.2038, indicating that higher expression of this gene would push the prediction towards higher AUC (resistance). In contrast, fingerprint features fp_0227 and fp_0468 have negative SHAP values (-0.1489 and -0.1446, respectively), suggesting that their presence would decrease the predicted AUC (increase sensitivity). The absence of fingerprint features fp_0443 and fp_0204 also contributes to the predicted AUC, with positive SHAP values of 0.0964 and 0.0720, respectively.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for AZD4547 has an R2 of 0.2060, indicating moderate predictability. The availability of cell subtype metadata (adenocarcinoma) may be relevant for understanding the drug's mechanism of action. However, it is essential to note that the model's predictions are based on the training data, and any interpretations should be grounded in the local evidence provided by the TreeSHAP values and feature analysis.

## Confidence and Caveats
The interpretation of the results is limited to the provided evidence and should not be extrapolated to other drug-cell line combinations or clinical settings. The model's underestimation of the drug's effectiveness in this case highlights the importance of considering the local evidence and not relying solely on global model metrics. Additionally, the absence of direct causal evidence and the reliance on TreeSHAP values as explanatory features should be acknowledged when interpreting the results.

---

## RPT-0039 - ABT-199 on EOL1
_Split: val_

## Executive Summary
The sample RPT-0039, involving the drug ABT-199 on the cell line EOL1, exhibits an observed AUC of 0.6042, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the drug's mechanism as an inhibitor of BCL2 and the cell line's origin from haematopoietic and lymphoid tissue, specifically classified as acute myeloid leukaemia.

## Evidence-Based Interpretation
The observed AUC of 0.6042 for ABT-199 on EOL1 is significantly lower than the predicted AUC, indicating a higher sensitivity than expected. This discrepancy suggests that specific factors, as identified by SHAP values, contribute to this enhanced sensitivity. The top TreeSHAP features, including gene expression and fingerprint bits, provide insights into the molecular underpinnings of this response.

## Feature and Neighborhood Analysis
Key features influencing the prediction include TNFRSF12A (gene_expression) with a SHAP value of -0.6636, indicating its contribution to the increased sensitivity. Fingerprint bits such as fp_0443, fp_1009, fp_0227, and fp_0806 also play roles, with positive SHAP values for fp_0443, fp_0227, and fp_0806 suggesting they push towards resistance, while the negative SHAP value for fp_1009 suggests it contributes to sensitivity. The presence or absence of these fingerprint bits and their representative SMARTS patterns may influence the drug's efficacy.

## Model-Level Context
The global model context provides training diagnostics with an R2 of 0.4928 and RMSE of 1.8342, indicating a moderate fit. The model's performance on the training data does not directly imply its generalizability but suggests that the features used are somewhat predictive of the response. The per-drug cross-validated predictability for ABT-199 shows an R2 of 0.2474, indicating some variability in the model's ability to predict responses for this drug across different cell lines. The most common genes across predictable per-drug models, including TNFRSF12A, highlight potential biomarkers for drug response.

## Confidence and Caveats
While the analysis provides insights into the factors contributing to the sensitivity of EOL1 to ABT-199, it is essential to consider the limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The molecular descriptions are grounded in local metadata and feature tables, and any global model metrics should be treated as training diagnostics rather than indicators of held-out performance. Therefore, the interpretation should be cautious, focusing on the relative contributions of features to the predicted response rather than absolute predictions of drug efficacy.

---

## RPT-0068 - nilotinib on KU812
_Split: val_

## Executive Summary
The sample RPT-0068, involving the drug nilotinib on the KU812 cell line, exhibits an observed AUC of 1.4730, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The prediction error is significantly negative, indicating that the observed sensitivity is higher than the model's prediction.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction include TNFRSF12A (gene_expression) with a negative SHAP value, indicating that its lower expression in this cell line pushes the prediction towards higher sensitivity. Fingerprint features such as fp_0204, fp_0443, fp_0538, and fp_0227 also contribute to the prediction, with some features being absent or present in the compound, influencing the predicted AUC.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that the KU812 cell line is more sensitive to nilotinib compared to other cell lines, such as EOL1 and KYO1, which also exhibit high sensitivity. Similarly, the same-cell cohort examples show that dasatinib and leptomycin B are more sensitive on the KU812 cell line. The top global fingerprint features, including fp_0443, which is present in nilotinib, contribute to the predictability of the model.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was tuned for max-depth and n-estimators, resulting in optimal values of 20 and 100, respectively. The per-drug cross-validated predictability for nilotinib is relatively low, with an R2 of 0.0227. The cell subtype metadata confirms that the KU812 cell line is associated with chronic myeloid leukaemia.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the per-drug cross-validated predictability for nilotinib is relatively low, which may impact the confidence in the predictions.

---

## RPT-0069 - cytarabine hydrochloride on JM1
_Split: val_

## Executive Summary
The sample in question involves the drug cytarabine hydrochloride and the cell line JM1, with an observed AUC of 2.1291, indicating exceptional sensitivity relative to the predicted response and cohort baselines. The prediction error is significantly negative, suggesting that the model overestimated the resistance of this cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 2.1291 is lower than the predicted AUC of 13.1844, indicating that the cell line JM1 is more sensitive to cytarabine hydrochloride than expected. This sensitivity is also evident when compared to the global mean AUC across all pairs (12.8580) and the drug cohort mean (11.6275). The large negative prediction error (-11.0553) further supports the notion that the model underestimated the sensitivity of JM1 to cytarabine hydrochloride.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include fp_0443 (SHAP=-0.7267), fp_0504 (SHAP=+0.5526), fp_0767 (SHAP=+0.4309), TNFRSF12A (SHAP=-0.3692), and fp_0864 (SHAP=+0.2592). The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 in cytarabine hydrochloride contribute to the predicted sensitivity. The low expression of TNFRSF12A (z=-2.01) also pushes the prediction towards sensitivity. The same-drug cohort examples (BV173 and REH) and same-cell cohort examples (dinaciclib and gemcitabine) further support the exceptional sensitivity of JM1 to cytarabine hydrochloride.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The top global fingerprint features and most common genes across predictable per-drug models are also listed. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata confirms that JM1 is a B cell lymphoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any pathways, biomarkers, or mechanisms not supported by the prompt should not be inferred.

---

## RPT-0071 - AT13387 on EOL1
_Split: val_

## Executive Summary
The sample RPT-0071, which involves the drug AT13387 and the cell line EOL1, exhibits an observed AUC of 1.4829, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.4829 is significantly lower than the predicted AUC of 12.5016, suggesting that the sample is more sensitive to the drug AT13387 than expected. The large negative prediction error of -11.0187 further supports this conclusion. The sample's sensitivity is also evident when compared to the drug cohort and cell cohort, with the sample percentile being 0.3 and 11.8, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression; SHAP=-0.6219), fp_0443 (fingerprint_bit; SHAP=+0.3944), fp_1009 (fingerprint_bit; SHAP=-0.1999), fp_0204 (fingerprint_bit; SHAP=+0.1443), and fp_0062 (fingerprint_bit; SHAP=-0.0736). The negative SHAP value for TNFRSF12A suggests that its low expression level contributes to the sample's sensitivity. The presence or absence of specific fingerprint bits, such as fp_0443 and fp_1009, also influences the predicted AUC.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model's performance is further characterized by the top global fingerprint features and the most common genes across predictable per-drug models. The per-drug cross-validated predictability for AT13387 is 0.2709, indicating moderate predictability. The availability of cell subtype metadata, specifically acute myeloid leukaemia, provides additional context for the sample's sensitivity.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any conclusions drawn from this analysis should be considered in the context of the available data and limitations of the model.

---

## RPT-0074 - dabrafenib on WM88
_Split: val_

## Executive Summary
The WM88 cell line exhibits exceptional sensitivity to dabrafenib, with an observed AUC of 2.5202, which is significantly lower than the RF-predicted AUC of 13.5149. This discrepancy suggests that the model underestimated the sensitivity of WM88 to dabrafenib.

## Evidence-Based Interpretation
The observed AUC of 2.5202 indicates that WM88 is more sensitive to dabrafenib than expected. The large negative prediction error (-10.9947) and the sample's position at the 0.8 percentile in the drug cohort and 0.5 percentile in the cell cohort further support this interpretation. The top TreeSHAP features, including TNFRSF12A and various fingerprint bits (fp_0443, fp_0902, fp_0760, and fp_0204), contribute to the predicted AUC, but their effects are outweighed by other factors, resulting in the observed sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the predicted response. TNFRSF12A, a gene with a positive SHAP value (+0.2010), pushes the prediction toward higher AUC/resistance, while the absence of certain fingerprint bits (fp_0443, fp_0902, and fp_0204) also contributes to the predicted resistance. In contrast, the presence of fp_0760 has a negative SHAP value (-0.0917), which would push the prediction toward lower AUC/sensitivity. The neighborhood analysis, including same-drug and same-cell cohort examples, reveals that other cell lines (DU4475 and SIGM5) are also sensitive to dabrafenib, and other drugs (trametinib and leptomycin B) exhibit similar sensitivity profiles in the WM88 cell line.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). While these metrics are not directly applicable to this sample, they indicate the model's overall performance. The per-drug cross-validated predictability for dabrafenib (R2=0.3967) suggests that the model has some capacity to predict responses to this drug. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to this specific sample is limited.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance. Therefore, the confidence in the results is limited to the local evidence, and caution should be exercised when generalizing to other contexts.

---

## RPT-0092 - gefitinib on PC14
_Split: val_

## Executive Summary
The PC14 cell line exhibits exceptional sensitivity to gefitinib, with an observed AUC of 2.4605, which is significantly lower than the predicted AUC of 13.2809. This discrepancy suggests that the model underestimated the sensitivity of PC14 cells to gefitinib.

## Evidence-Based Interpretation
The observed AUC of 2.4605 indicates that the PC14 cell line is more sensitive to gefitinib than expected. The large negative prediction error (-10.8204) further supports this conclusion. The cell line's sensitivity is also evident when compared to the drug cohort (0.3 percentile) and cell cohort (1.3 percentile) baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP=+0.1821), fp_0367 (SHAP=-0.1291), fp_1019 (SHAP=+0.1271), fp_0443 (SHAP=+0.0974), and fp_0227 (SHAP=-0.0825). The presence of TNFRSF12A and absence of fp_1019 and fp_0443 push the prediction towards higher AUC (resistance), while the presence of fp_0367 and fp_0227 push the prediction towards lower AUC (sensitivity). The same-drug cohort examples (HCC827 and HCC4006) and same-cell cohort examples (afatinib and SB-743921) also exhibit sensitivity to their respective drugs.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for gefitinib is R2=0.1400, indicating moderate predictability. Cell subtype metadata is available, confirming that the PC14 cell line is a non-small cell carcinoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics should be treated with caution, as they are training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice.

---

## RPT-0093 - canertinib on HCC827
_Split: val_

## Executive Summary
The sample RPT-0093, involving the drug canertinib on the HCC827 cell line, exhibits an observed AUC of 1.8419, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 1.8419 is significantly lower than the predicted AUC of 12.6404, suggesting that the HCC827 cell line is more sensitive to canertinib than expected. The large negative prediction error of -10.7985 further supports this conclusion. The sample's sensitivity is also evident when compared to the drug cohort and cell cohort, with the sample percentile being 0.1 and 0.5, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fingerprint bits fp_0367 and fp_0017, which have negative SHAP values, indicating that their presence pushes the prediction towards lower AUC (greater sensitivity). In contrast, the gene expression feature TNFRSF12A (51330) has a positive SHAP value, suggesting that its high expression level contributes to higher AUC (lower sensitivity). The absence of fingerprint bit fp_1019 also has a positive SHAP value, indicating that its absence contributes to lower AUC (greater sensitivity).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311,258 samples with 2,024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for canertinib is 0.1843, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. Additionally, the global model metrics should be treated as training diagnostics rather than held-out performance. The cell subtype metadata is available, and the sample is classified as adenocarcinoma. Overall, the results suggest that the HCC827 cell line is exceptionally sensitive to canertinib, but further investigation is necessary to fully understand the underlying mechanisms.

---

## RPT-0101 - nilotinib on JK1
_Split: val_

## Executive Summary
The sample JK1 treated with nilotinib shows an exceptionally sensitive response with an observed AUC of 1.8342, which is significantly lower than the RF-predicted AUC of 12.5365. This discrepancy suggests that the model underestimated the sensitivity of JK1 to nilotinib.

## Evidence-Based Interpretation
The observed AUC of 1.8342 indicates a high sensitivity of JK1 to nilotinib, which is consistent with the drug's mechanism as an inhibitor of ABL1, BCR, and c-KIT. The large negative prediction error (-10.7023) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression; SHAP=-0.6495), which has a negative SHAP value indicating that its low expression in JK1 pushes the prediction towards lower AUC (higher sensitivity). The presence of certain fingerprint bits, such as fp_0443 and fp_0538, also contributes to the predicted AUC. The absence of other fingerprint bits, like fp_0204 and fp_0227, has a smaller positive SHAP value, indicating a lesser contribution to the predicted AUC.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for nilotinib is low (R2=0.0227), suggesting that the model may not have fully captured the underlying relationships between nilotinib and cell line responses.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be taken as direct causal evidence. The model's performance and feature importance should be considered in the context of its training data and limitations. Additionally, the availability of cell subtype metadata (blast phase; chronic myeloid leukaemia) may provide further insight into the underlying biology, but its relevance to the model's predictions is unclear.

---

## RPT-0105 - decitabine on EOL1
_Split: val_

## Executive Summary
The sample EOL1 treated with decitabine exhibits an observed AUC of 2.9783, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of EOL1 to decitabine.

## Evidence-Based Interpretation
The observed AUC of 2.9783 is lower than the predicted AUC of 13.6451, indicating that EOL1 is more sensitive to decitabine than expected. The top TreeSHAP features contributing to this prediction error include fingerprint bits fp_0504, fp_0767, and gene expression of TNFRSF12A. The absence of fp_0504 and fp_0767 and the low expression of TNFRSF12A push the prediction towards lower AUC (greater sensitivity).

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. The absence of fp_0504 and fp_0767, which are present in only 4.4% and 11.0% of CTRPv2 compounds, respectively, contributes to the increased sensitivity. The low expression of TNFRSF12A, which is below the cross-cell-line mean, also pushes the prediction towards lower AUC. The presence of fp_0204, which is present in 2.9% of CTRPv2 compounds, has a negative SHAP value, indicating that it contributes to the increased sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr. The per-drug cross-validated predictability for decitabine is R2=0.5143, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but are not directly relevant to the local interpretation of the EOL1 sample. The cell subtype metadata confirms that EOL1 is an acute myeloid leukaemia cell line.

## Confidence and Caveats
The interpretation is based on the local TreeSHAP values and should be treated with caution. The global model metrics are training diagnostics and should not be used to infer held-out performance. The molecular descriptions are grounded in local CTRPv2 metadata and feature tables, but may not generalize to other datasets or contexts. The results should not be used for clinical decision-making without further validation and consideration of additional factors.

---

## RPT-0117 - ML210 on OV7
_Split: val_

## Executive Summary
The sample RPT-0117, involving drug ML210 and cell line OV7, exhibits an observed AUC of 2.9334, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 2.9334 is significantly lower than the predicted AUC of 13.4979, indicating a large negative prediction error. The sample's sensitivity is also notable when compared to the drug cohort (1.2 percentile) and cell cohort (0.7 percentile) baselines. The top TreeSHAP features contributing to this prediction error include fingerprint bits fp_0443, TNFRSF12A gene expression, fp_0367, fp_1009, and fp_0204.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the factors driving the predicted response. Fingerprint bits fp_0443, fp_0367, and fp_0204 have positive SHAP values, indicating that their absence pushes the prediction towards higher AUC/resistance. In contrast, fp_1009 has a negative SHAP value, suggesting that its presence contributes to lower AUC/sensitivity. The TNFRSF12A gene expression also has a positive SHAP value, indicating that its near-average expression level in this sample contributes to the predicted resistance.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability.

## Confidence and Caveats
The interpretation of this sample's sensitivity is grounded in the local TreeSHAP values and cohort summaries. However, it is essential to recognize the limitations of this analysis, including the potential for overfitting and the lack of direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the molecular descriptions are constrained to local CTRPv2 metadata, feature tables, and cohort summaries, and should not be extrapolated to other contexts without further validation.

---

## RPT-0122 - cytarabine hydrochloride on SKNMC
_Split: val_

## Executive Summary
The SKNMC cell line exhibits exceptional sensitivity to cytarabine hydrochloride, with an observed AUC of 3.1012, which is significantly lower than the predicted AUC of 13.5949. This discrepancy suggests that the model underestimated the sensitivity of the SKNMC cell line to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 3.1012 indicates that the SKNMC cell line is more sensitive to cytarabine hydrochloride than expected. The large negative prediction error of -10.4937 further supports this conclusion. The drug cohort and cell cohort summaries also show that the SKNMC cell line is exceptionally sensitive to cytarabine hydrochloride, with a sample percentile of 1.5 in the drug cohort and 3.0 in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0504, fp_0443, fp_0767, TNFRSF12A, and fp_0864. The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 contribute to the lower predicted AUC, while the low expression of TNFRSF12A also contributes to the sensitivity of the SKNMC cell line to cytarabine hydrochloride. The same-drug cohort examples, such as BV173 and REH, and the same-cell cohort examples, such as SB-743921 and docetaxel, also exhibit similar sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, training RMSE of 1.8342, and training correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated with caution, as they are based on training diagnostics rather than held-out performance. Additionally, the molecular descriptions are limited to the local data and may not generalize to other contexts.

---

## RPT-0131 - ML210 on SUPM2
_Split: val_

## Executive Summary
The sample RPT-0131, involving the drug ML210 and cell line SUPM2, exhibits an exceptionally sensitive response with an observed AUC of 3.1088, which is significantly lower than the RF-predicted AUC of 13.4714. This discrepancy suggests that the actual sensitivity of ML210 to SUPM2 cells is higher than what the model predicts.

## Evidence-Based Interpretation
The observed AUC of 3.1088 indicates a greater sensitivity of SUPM2 cells to ML210 compared to the predicted response. The large negative prediction error of -10.3626 further supports this interpretation, suggesting that the model underestimated the sensitivity of SUPM2 cells to ML210. The sample percentile of 1.6 in the drug cohort and 4.8 in the cell cohort also indicate that this response is unusually sensitive.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include fp_0443, TNFRSF12A, fp_1009, fp_0367, and fp_0204. The positive SHAP values for fp_0443, TNFRSF12A, fp_0367, and fp_0204 suggest that these features would increase the predicted AUC (i.e., decrease sensitivity) if present or increased. In contrast, the negative SHAP value for fp_1009 indicates that its presence would decrease the predicted AUC (i.e., increase sensitivity). The absence of fp_0443, fp_0367, and fp_0204 in the sample may contribute to the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for ML210 is 0.3111, suggesting moderate predictability. The cell subtype metadata confirms that SUPM2 is an anaplastic large cell lymphoma. The most common genes across predictable per-drug models, including TNFRSF12A, may be relevant for understanding the mechanisms underlying the response, but their role in this specific sample is not directly supported by the evidence.

---

## RPT-0145 - BRD-K99006945 on IGR37
_Split: val_

## Executive Summary
The sample RPT-0145, involving the drug BRD-K99006945 and cell line IGR37, exhibits an observed AUC of 3.2701, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this drug-cell line pair.

## Evidence-Based Interpretation
The observed AUC of 3.2701 is significantly lower than the RF-predicted AUC of 13.5590, indicating that the drug BRD-K99006945 is more sensitive than expected in the IGR37 cell line. This sensitivity is also evident when compared to the global mean AUC across all pairs (12.8580) and the drug cohort mean (14.0290). The sample percentile of 1.0 in the drug cohort and 0.7 in the cell cohort further supports the exceptional sensitivity of this drug-cell line pair.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression) with a SHAP value of +0.1907, and several fingerprint bits (fp_0367, fp_0204, fp_0623, and fp_0443) with positive SHAP values. These features push the prediction toward higher AUC/resistance, but the observed AUC is lower than predicted, suggesting that other factors may be contributing to the sensitivity of this drug-cell line pair. The absence of these fingerprint bits in the drug BRD-K99006945 may be contributing to its sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for BRD-K99006945 has an R2 of -0.0120, indicating limited predictability for this drug. The model's performance should be interpreted with caution, considering the limitations of the training data and the specific drug-cell line pair being analyzed.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The molecular descriptions are limited to the local data and should not be extrapolated to other contexts. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should be interpreted with caution considering the limitations of the model and the data.

---

## RPT-0191 - AZD8055 on KMS34
_Split: val_

## Executive Summary
The sample RPT-0191, involving the drug AZD8055 on the KMS34 cell line, exhibits an observed AUC of 1.2128, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are primarily fingerprint bits (fp_0623, fp_0141, fp_0227, fp_0202) and a gene expression feature (TNFRSF12A). These features have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). The presence of these fingerprint bits and the low expression of TNFRSF12A contribute to the observed sensitivity of the KMS34 cell line to AZD8055.

## Feature and Neighborhood Analysis
The fingerprint bits identified as top features are present in a small percentage of CTRPv2 compounds, suggesting that they may be unique to certain chemical structures. The gene expression feature, TNFRSF12A, is below the cross-cell-line mean, which may indicate a specific cellular context that contributes to the sensitivity of the KMS34 cell line. The same-drug and same-cell cohort examples provide additional context, showing that other cell lines (EOL1, BCP1) are also sensitive to AZD8055, and that other drugs (SB-743921, paclitaxel) can also exhibit high sensitivity on the KMS34 cell line.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928 and an RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also listed, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for AZD8055 is relatively low (R2=0.1274), indicating that the model may not capture all the relevant factors contributing to the response of this drug.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. Additionally, the global model metrics should be treated with caution, as they are based on training diagnostics rather than held-out performance. The results should not be used to provide clinical advice, and further investigation is necessary to fully understand the mechanisms underlying the observed sensitivity of the KMS34 cell line to AZD8055.

---

## RPT-0194 - ML210 on DAUDI
_Split: val_

## Executive Summary
The DAUDI cell line shows exceptional sensitivity to the ML210 drug, with an observed AUC of 2.5808, which is significantly lower than the predicted AUC of 12.5487. This discrepancy suggests that the model underestimated the sensitivity of DAUDI to ML210.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include TNFRSF12A gene expression, which has a negative SHAP value of -0.6639, indicating that its low expression in DAUDI cells contributes to the increased sensitivity. Additionally, the presence or absence of specific molecular fingerprints, such as fp_0443, fp_1009, fp_0204, and fp_0062, also influence the prediction. These features suggest that the model is capturing complex interactions between the drug and cell line characteristics.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that TNFRSF12A is markedly below the cross-cell-line mean, which may contribute to the increased sensitivity of DAUDI to ML210. The molecular fingerprints, such as fp_0443 and fp_0204, are absent in ML210, while fp_1009 is present. These features are representative of specific chemical structures, such as SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` for fp_0443, which may interact with the cell line in a way that increases sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The top global fingerprint features, such as fp_0443 and fp_0767, are also identified. However, it is essential to note that these metrics are based on the training data and should not be considered as held-out performance. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability. The cell subtype metadata, which includes Burkitt lymphoma, is also available and may provide additional context for understanding the sensitivity of DAUDI to ML210.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and further investigation is necessary to fully understand the mechanisms underlying the sensitivity of DAUDI to ML210.

---

## RPT-0203 - ML210 on PFEIFFER
_Split: val_

## Executive Summary
The sample **PFEIFFER** (master_ccl_id=943) treated with **ML210** (master_cpd_id=609110) shows an observed AUC of **2.6488**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. This sensitivity is notable given the drug's mechanism of selectively killing engineered cells expressing mutant HRAS.

## Evidence-Based Interpretation
The observed AUC of **2.6488** is significantly lower than the RF-predicted AUC of **12.5487**, indicating a large negative prediction error. This discrepancy suggests that the model underestimated the sensitivity of **PFEIFFER** cells to **ML210**. The sample's sensitivity is also highlighted by its position in the 0.9 percentile of the drug cohort and the 4.5 percentile of the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include **TNFRSF12A (51330)** with a SHAP value of **-0.6669**, indicating that lower expression of this gene pushes the prediction towards higher sensitivity. Fingerprint features such as **fp_0443**, **fp_1009**, **fp_0204**, and **fp_0062** also contribute to the prediction, with **fp_0443** having a positive SHAP value, suggesting its absence contributes to higher sensitivity. The presence or absence of these fingerprint features in **ML210** and their representation in other compounds provide insights into potential structural elements influencing the drug's activity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of **0.4928** and RMSE of **1.8342**, which should not be interpreted as held-out performance. The model's top global fingerprint features and most common genes across predictable per-drug models offer a broader view of the factors influencing drug sensitivity across different cell lines and drugs. The per-drug cross-validated predictability for **ML210** is **R2=0.3111**, indicating moderate predictability of its sensitivity across cell lines. The availability of cell subtype metadata, such as **diffuse large B cell lymphoma** for **PFEIFFER**, adds context to the interpretation of drug sensitivity.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the SHAP values and the characteristics of the **PFEIFFER** cell line and **ML210** drug. However, it is essential to consider the limitations of the model, including the potential for overfitting or underfitting, as indicated by the training diagnostics. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not constitute direct causal evidence. Therefore, any conclusions drawn from this analysis should be treated with caution and considered in the context of additional experimental validation.

---

## RPT-0206 - trametinib on HUT78
_Split: val_

## Executive Summary
The sample in question involves the drug trametinib and the cell line HUT78, with an observed AUC of 2.7358, indicating exceptional sensitivity relative to the predicted response and cohort baselines. The prediction error is significantly negative, suggesting that the actual sensitivity is higher than the model's prediction.

## Evidence-Based Interpretation
The observed AUC of 2.7358 is lower than the predicted AUC of 12.6106, indicating that the cell line HUT78 is more sensitive to trametinib than expected. This sensitivity is also evident when compared to the drug cohort and cell cohort baselines, where the sample percentile is 2.3 and 1.1, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction include fp_0367, TNFRSF12A, fp_0204, fp_0062, and fp_0227. The presence of fp_0367 and the low expression of TNFRSF12A (below the cross-cell-line mean) contribute to the increased sensitivity, as indicated by their negative SHAP values. In contrast, the absence of fp_0204, fp_0062, and fp_0227 has a smaller positive effect on the prediction, pushing it towards higher AUC/resistance. The same-drug cohort examples, such as DU4475 and OCIAML3, also exhibit higher sensitivity, while the same-cell cohort examples, such as leptomycin B and LBH-589, show similar sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for trametinib is 0.3821, indicating moderate predictability. The cell subtype metadata is available, providing additional context for the sample. However, it is essential to note that the TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence.

---

## RPT-0221 - selumetinib on HUT78
_Split: val_

## Executive Summary
The sample RPT-0221, involving the drug selumetinib on the HUT78 cell line, exhibits an exceptionally sensitive response with an observed AUC of 2.8796, which is significantly lower than the RF-predicted AUC of 12.6289. This discrepancy suggests that the model underestimated the sensitivity of selumetinib in this context.

## Evidence-Based Interpretation
The observed AUC of 2.8796 indicates a higher sensitivity of the HUT78 cell line to selumetinib compared to the model's prediction. The large negative prediction error of -9.7493 further emphasizes this point. The sample's percentile ranks within the drug and cell cohorts also support its exceptional sensitivity, with a 0.3 percentile rank in the drug cohort and a 1.8 percentile rank in the cell cohort.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP = -0.3823), fp_0367 (SHAP = -0.1420), fp_0053 (SHAP = -0.1008), fp_0443 (SHAP = 0.0892), and fp_0806 (SHAP = 0.0830). The negative SHAP values for TNFRSF12A, fp_0367, and fp_0053 suggest that these features contribute to the increased sensitivity of the HUT78 cell line to selumetinib. In contrast, the positive SHAP values for fp_0443 and fp_0806 indicate that these features would increase the resistance if they were present or more prominent.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics are not directly applicable to this sample, they indicate the model's overall performance during training. The per-drug cross-validated predictability for selumetinib (R2 = 0.2298) suggests moderate predictability. The presence of TNFRSF12A as one of the most common genes across predictable per-drug models (166 drugs) highlights its potential importance in predicting drug responses. However, it is essential to consider these findings within the constraints of the model and the specific context of this sample.

---

## RPT-0229 - cytarabine hydrochloride on PL21
_Split: val_

## Executive Summary
The sample PL21 treated with cytarabine hydrochloride exhibits an exceptionally sensitive response, with an observed AUC of 3.4879, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of PL21 to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 3.4879 indicates a high sensitivity of PL21 to cytarabine hydrochloride, which is consistent with the drug's mechanism as an inducer of DNA damage. The large negative prediction error (-9.6965) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443 (SHAP=-0.7250), fp_0504 (SHAP=+0.5523), fp_0767 (SHAP=+0.4111), TNFRSF12A (SHAP=-0.3717), and fp_0864 (SHAP=+0.2686). The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 in cytarabine hydrochloride may contribute to its high sensitivity in PL21. The low expression of TNFRSF12A (z=-1.16) may also play a role in this sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata confirms that PL21 is an acute myeloid leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should be interpreted with caution. Additionally, the absence of certain features or genes in the analysis may limit the understanding of the underlying mechanisms.

---

## RPT-0231 - AZD7762 on KASUMI1
_Split: val_

## Executive Summary
The sample RPT-0231, treated with AZD7762 on the KASUMI1 cell line, exhibits an exceptionally sensitive response with an observed AUC of 2.2485, which is significantly lower than the RF-predicted AUC of 11.9324. This discrepancy suggests that the model underestimated the sensitivity of the KASUMI1 cell line to AZD7762.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC value include fingerprint bits fp_0623, fp_0141, and gene expression feature TNFRSF12A (51330), which have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). In contrast, fingerprint bit fp_0204 has a positive SHAP value, suggesting that its absence contributes to the predicted resistance.

## Feature and Neighborhood Analysis
The presence of fingerprint bits fp_0623 and fp_0141 in the AZD7762 compound, as well as the low expression of TNFRSF12A (51330) in the KASUMI1 cell line, are associated with increased sensitivity. The absence of fp_0204 in AZD7762 also contributes to the predicted sensitivity. The same-drug cohort examples, such as EOL1 and MV411, exhibit more sensitive responses, while the same-cell cohort examples, such as LBH-589 and leptomycin B, also show more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for AZD7762 has an R2 of 0.2710, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics, such as training R2 and RMSE, should be treated with caution and not used to infer held-out performance. Additionally, the cell subtype metadata is available, but its impact on the prediction is not explicitly evaluated in this analysis.

---

## RPT-0233 - NVP-BEZ235 on AM38
_Split: val_

## Executive Summary
The sample RPT-0233, involving the drug NVP-BEZ235 on the cell line AM38, exhibits an exceptionally sensitive response with an observed AUC of 2.8377, which is significantly lower than the RF-predicted AUC of 12.5101. This discrepancy suggests that the model underestimated the sensitivity of NVP-BEZ235 in this specific context.

## Evidence-Based Interpretation
The observed AUC of 2.8377 indicates a higher sensitivity of the AM38 cell line to NVP-BEZ235 compared to the model's prediction. The large negative prediction error of -9.6724 further emphasizes this discrepancy. The sample's sensitivity is also notable when compared to the drug cohort and cell cohort baselines, with the sample percentile being 0.3 and 5.7, respectively.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fingerprint bits fp_0235, fp_0538, fp_0486, and fp_0722, which have negative SHAP values, indicating that their presence pushes the prediction towards lower AUC (higher sensitivity). In contrast, the gene expression feature TNFRSF12A (51330) has a positive SHAP value, suggesting that its expression level contributes to higher AUC (lower sensitivity). The presence of these features in the sample and their corresponding SHAP values provide insight into the local factors influencing the predicted response.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics indicate a reasonable fit to the training data, they should not be interpreted as held-out performance. The model's predictability for NVP-BEZ235 specifically is relatively low, with an R2 of 0.1277. The availability of cell subtype metadata, such as astrocytoma Grade IV, may be relevant for understanding the sample's behavior but does not directly influence the model's prediction. The top global fingerprint features and most common genes across predictable per-drug models provide additional context but do not directly relate to the specific sample's response. 

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is essential to recognize the limitations of the model and the potential for overfitting or underfitting. The large prediction error and the sample's exceptional sensitivity highlight the complexity of the underlying biology and the need for further investigation. The results should not be used for clinical advice, and any conclusions drawn from this analysis should be treated with caution, considering the constraints and limitations of the model and the data.

---

## RPT-0239 - cediranib on NCIH716
_Split: val_

## Executive Summary
The sample NCIH716 treated with cediranib shows an observed AUC of 3.5276, which is exceptionally sensitive compared to the predicted AUC of 13.1739 and cohort baselines. This report aims to provide an evidence-based interpretation of this observation using SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (-9.6463) indicates that the model underestimated the sensitivity of NCIH716 to cediranib. The top TreeSHAP features contributing to this prediction error include TNFRSF12A (SHAP=+0.1814), fp_0227 (SHAP=-0.1640), fp_0062 (SHAP=-0.0675), fp_0443 (SHAP=+0.0645), and fp_0728 (SHAP=-0.0627). These features suggest that the gene expression of TNFRSF12A and the presence or absence of specific molecular substructures (represented by fingerprint bits) may be influencing the sensitivity of NCIH716 to cediranib.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. For example, the positive SHAP value for TNFRSF12A suggests that its gene expression is pushing the prediction towards higher AUC (resistance), while the negative SHAP values for fp_0227, fp_0062, and fp_0728 indicate that their presence or absence is pushing the prediction towards lower AUC (sensitivity). The same-drug and same-cell cohort examples also provide context, showing that other cell lines (e.g., EOL1 and SW579) are more sensitive to cediranib, and other drugs (e.g., AZD4547 and pluripotin) are more effective against NCIH716.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061). While these metrics are not indicative of held-out performance, they suggest that the model is reasonably well-fit to the training data. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, highlighting the importance of specific molecular substructures and genes in predicting drug responses. The per-drug cross-validated predictability for cediranib (R2=0.0754) is relatively low, indicating that the model may not be highly effective in predicting responses to this drug.

## Confidence and Caveats
This report is grounded in structured evidence from the SHAP values and feature analysis. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. Additionally, molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance, and the per-drug cross-validated predictability for cediranib is relatively low. Therefore, the interpretation of these results should be approached with caution,

---

## RPT-0241 - cytarabine hydrochloride on DND41
_Split: val_

## Executive Summary
The sample DND41 treated with cytarabine hydrochloride exhibits an exceptionally sensitive response, with an observed AUC of 3.5494, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of DND41 to cytarabine hydrochloride.

## Evidence-Based Interpretation
The observed AUC of 3.5494 indicates a high sensitivity of DND41 to cytarabine hydrochloride, which is consistent with the drug's mechanism as an inducer of DNA damage. The large negative prediction error (-9.6350) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443 (SHAP=-0.6876), fp_0504 (SHAP=+0.5052), fp_0767 (SHAP=+0.3951), TNFRSF12A (SHAP=-0.3674), and fp_0864 (SHAP=+0.2608). The presence of fp_0443 and the absence of fp_0504, fp_0767, and fp_0864 in cytarabine hydrochloride may contribute to its high sensitivity in DND41. The low expression of TNFRSF12A (z=-1.37) may also play a role in the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata confirms that DND41 is an acute lymphoblastic T cell leukaemia cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the results should be interpreted with caution. Additionally, the absence of certain features or genes in the analysis may limit the understanding of the underlying mechanisms.

---

## RPT-0255 - daporinad on SKNDZ
_Split: val_

## Executive Summary
The SKNDZ cell line exhibits exceptional sensitivity to daporinad, with an observed AUC of 2.3535, which is significantly lower than the predicted AUC of 11.8994. This discrepancy suggests that the model underestimated the sensitivity of SKNDZ to daporinad.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top contributing features to the predicted AUC are primarily negative, indicating that they push the prediction towards lower AUC (greater sensitivity). The most significant contributor is TNFRSF12A (SHAP = -0.7200), a gene expression feature that is markedly below the cross-cell-line mean. Other notable contributors include fingerprint bits fp_0706, fp_0062, and fp_0830, which are absent in daporinad, and fp_0227, which is also absent but has a positive SHAP value.

## Feature and Neighborhood Analysis
The local analysis of the SKNDZ cell line and daporinad reveals that the combination is exceptionally sensitive compared to other cell lines and drugs. The same-drug cohort examples show that other cell lines, such as GA10 and 697, also exhibit high sensitivity to daporinad. Similarly, the same-cell cohort examples demonstrate that SKNDZ is sensitive to other drugs, including GSK461364 and LBH-589. These findings suggest that the sensitivity of SKNDZ to daporinad is not unique and may be related to the cell line's characteristics or the drug's mechanism of action.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928 and an RMSE of 1.8342. The top global fingerprint features and most common genes across predictable per-drug models are also listed. However, it is essential to note that these metrics are based on training data and should not be considered as held-out performance. The per-drug cross-validated predictability for daporinad is relatively low (R2 = 0.1876), indicating that the model may not capture the underlying relationships between daporinad and cell line sensitivity accurately.

## Confidence and Caveats
The interpretation of the results is grounded in the local analysis and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries only. Therefore, any conclusions drawn from this analysis should be treated with caution and considered in the context of the available data and model constraints.

---

## RPT-0258 - myriocin on HEC265
_Split: val_

## Executive Summary
The observed AUC of myriocin on the HEC265 cell line is 4.5123, which is exceptionally sensitive compared to the predicted AUC of 14.0469 and cohort baselines. This sample was selected due to its large negative prediction error, indicating that the actual sensitivity is higher than the model's prediction.

## Evidence-Based Interpretation
The TreeSHAP values provide insight into the features driving the predicted response. The top feature, fp_0443, has a negative SHAP value of -0.4767, indicating that its presence pushes the prediction towards lower AUC (greater sensitivity). In contrast, features like fp_0504, fp_0767, fp_0864, and fp_1009 have positive SHAP values, suggesting that their absence contributes to the predicted sensitivity.

## Feature and Neighborhood Analysis
The presence of fp_0443, characterized by the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, is a key factor in the observed sensitivity. This feature is present in only 0.4% of CTRPv2 compounds, with examples including nilotinib and bleomycin A2. The absence of features like fp_0504, fp_0767, fp_0864, and fp_1009 also contributes to the predicted sensitivity. These features are present in varying percentages of CTRPv2 compounds, with examples including topotecan, IC-87114, and erastin.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features include fp_0443, fp_0767, and fp_0925. The per-drug cross-validated predictability for myriocin has an R2 of -0.0805, indicating limited predictability. The cell subtype metadata confirms that the HEC265 cell line is an adenocarcinoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the per-drug cross-validated predictability for myriocin is limited, which may impact the accuracy of the predictions.

---

## RPT-0272 - ML210 on SUDHL1
_Split: val_

## Executive Summary
The sample RPT-0272, involving the drug ML210 and the cell line SUDHL1, exhibits an exceptionally sensitive response with an observed AUC of 3.9778, which is significantly lower than the RF-predicted AUC of 13.4714. This discrepancy suggests that the actual sensitivity of ML210 to SUDHL1 is higher than what the model predicts.

## Evidence-Based Interpretation
The observed AUC of 3.9778 indicates a higher sensitivity of the SUDHL1 cell line to ML210 compared to the predicted value. According to the rules, a lower AUC value signifies greater sensitivity. The large negative prediction error of -9.4936 further supports this interpretation, suggesting that the model underestimated the sensitivity of SUDHL1 to ML210.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0443, TNFRSF12A, fp_1009, fp_0367, and fp_0204. Positive SHAP values for fp_0443, TNFRSF12A, fp_0367, and fp_0204 push the prediction toward higher AUC/resistance, while the negative SHAP value for fp_1009 pushes the prediction toward lower AUC/sensitivity. The presence or absence of these fingerprint bits and the expression level of TNFRSF12A influence the predicted response. The same-drug cohort examples, such as DOHH2 and SKNDZ, and the same-cell cohort examples, such as leptomycin B and CR-1-31B, provide additional context for the sensitivity of ML210 to SUDHL1.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance metrics. The top global fingerprint features and the most common genes across predictable per-drug models offer insight into the broader patterns in the data. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability. The availability of cell subtype metadata, specifically anaplastic large cell lymphoma, adds to the understanding of the SUDHL1 cell line.

## Confidence and Caveats
The interpretation of the results is grounded in the provided evidence and adheres to the rules for AUC values and SHAP inputs. However, it is essential to recognize the limitations of the model and the potential for errors in prediction. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not constitute direct causal evidence. The molecular descriptions are based solely on local CTRPv2 metadata, feature tables, and cohort summaries. Therefore, any conclusions drawn from this analysis should be considered within the context of these constraints and limitations.

---

## RPT-0279 - PF-3758309 on A4FUK
_Split: val_

## Executive Summary
The sample **A4FUK** treated with **PF-3758309** exhibits an observed AUC of **2.4295**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are **fp_0367**, **fp_0091**, **TNFRSF12A (51330)**, **fp_1001**, and **fp_0062**, with negative SHAP values indicating that they push the prediction towards lower AUC (greater sensitivity). These features are associated with specific molecular structures and gene expressions that are present or absent in the sample.

## Feature and Neighborhood Analysis
The presence of **fp_0367** and **fp_0091** in the sample, as well as the low expression of **TNFRSF12A (51330)**, contribute to the increased sensitivity. The absence of **fp_0062** also plays a role in this phenomenon. The same-drug cohort examples, such as **EOL1** and **SIGM5**, and same-cell cohort examples, such as **leptomycin B** and **dinaciclib**, demonstrate similar sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The top global fingerprint features and most common genes across predictable per-drug models are also listed. The per-drug cross-validated predictability for **PF-3758309** is **R2=0.3602**. However, these metrics should be treated as training diagnostics rather than held-out performance.

## Confidence and Caveats
The interpretation of the results is grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The cell subtype metadata is available, and the sample is classified as **diffuse large B cell lymphoma**. The results should be considered in the context of these limitations and constraints.

---

## RPT-0291 - cytarabine hydrochloride on CMLT1
_Split: val_

## Executive Summary
The sample CMLT1 treated with cytarabine hydrochloride exhibits an exceptionally sensitive response, with an observed AUC of 3.7892, which is significantly lower than the predicted AUC of 13.1844. This discrepancy suggests that the model underestimated the sensitivity of CMLT1 to cytarabine hydrochloride.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the presence of fingerprint feature **fp_0443** and the low expression of gene **TNFRSF12A (51330)** contribute to the increased sensitivity of CMLT1 to cytarabine hydrochloride. In contrast, the absence of fingerprint features **fp_0504**, **fp_0767**, and **fp_0864** also pushes the prediction towards higher sensitivity. These findings are based on the local CTRPv2 metadata and cohort summaries.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include **fp_0443** (SHAP=-0.7144), **fp_0504** (SHAP=+0.5330), **fp_0767** (SHAP=+0.4152), **TNFRSF12A (51330)** (SHAP=-0.3717), and **fp_0864** (SHAP=+0.2655). The presence or absence of these features, along with their corresponding SHAP values, influences the predicted AUC. The same-drug cohort examples, such as BV173 and REH, also exhibit sensitive responses to cytarabine hydrochloride. Similarly, the same-cell cohort examples, such as dasatinib and leptomycin B, show sensitive responses to their respective drugs.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features, such as **fp_0443**, **fp_0767**, and **fp_0504**, are also identified. The per-drug cross-validated predictability for cytarabine hydrochloride is 0.5313, indicating moderate predictability. The cell subtype metadata, including blast phase and chronic myeloid leukaemia, is available but not directly used in this analysis.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The global model metrics, such as training R2 and RMSE, should be treated as training diagnostics rather than held-out performance. Additionally, the molecular descriptions are limited to the local CTRPv2 metadata, feature tables, and cohort summaries.

---

## RPT-0297 - decitabine on KE37
_Split: val_

## Executive Summary
The KE37 cell line exhibits exceptional sensitivity to decitabine, with an observed AUC of 4.2974, which is significantly lower than the predicted AUC of 13.6451. This discrepancy suggests that the model underestimated the sensitivity of KE37 to decitabine.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the presence of certain molecular features contributes to the observed sensitivity. The absence of features fp_0504 and fp_0767, represented by specific SMARTS patterns, pushes the prediction towards higher AUC (resistance), while their absence in the actual compound contributes to the observed sensitivity. In contrast, the presence of feature fp_0204 and the low expression of gene TNFRSF12A (51330) contribute to the observed sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include fingerprint bits fp_0504, fp_0767, fp_0204, and gene expression feature TNFRSF12A (51330). The absence of fp_0504 and fp_0767, which are present in only a small percentage of CTRPv2 compounds, contributes to the observed sensitivity. The presence of fp_0204, which is present in 2.9% of CTRPv2 compounds, also contributes to the sensitivity. The low expression of TNFRSF12A (51330), which is markedly below the cross-cell-line mean, is another contributing factor.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311258 samples with 2024 features. The top global fingerprint features include fp_0443, fp_0767, and fp_0925, among others. The most common genes across predictable per-drug models include TNFRSF12A (51330), MYOF (26509), and SDC4 (6385). The per-drug cross-validated predictability for decitabine is 0.5143.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results are specific to the KE37 cell line and decitabine, and caution should be exercised when generalizing to other cell lines or compounds.

---

## RPT-0304 - decitabine on REH
_Split: val_

## Executive Summary
The REH cell line exhibits exceptional sensitivity to decitabine, with an observed AUC of 4.3492, which is significantly lower than the predicted AUC of 13.6451. This discrepancy suggests that the model underestimated the sensitivity of REH cells to decitabine.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the presence of certain molecular features contributes to the observed sensitivity. The absence of features represented by `fp_0504` and `fp_0767` pushes the prediction towards higher AUC (resistance), while the presence of `fp_0204` and low expression of `TNFRSF12A (51330)` push the prediction towards lower AUC (sensitivity). The observed AUC is also lower than the cohort baselines, indicating that REH cells are exceptionally sensitive to decitabine.

## Feature and Neighborhood Analysis
The top TreeSHAP features for this sample include `fp_0504`, `fp_0767`, `fp_0204`, `TNFRSF12A (51330)`, and `fp_0864`. The presence or absence of these features influences the predicted AUC, with `fp_0204` and low `TNFRSF12A (51330)` expression contributing to the observed sensitivity. The neighborhood analysis shows that other cell lines, such as BV173 and JURLMK1, also exhibit sensitivity to decitabine, while other drugs, such as SB-743921 and cytarabine hydrochloride, show similar sensitivity profiles on the REH cell line.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The model was trained on 311258 samples with 2024 features. The top global fingerprint features include `fp_0443`, `fp_0767`, and `fp_0925`. The most common genes across predictable per-drug models include `TNFRSF12A (51330)` and `MYOF (26509)`. The per-drug cross-validated predictability for decitabine is 0.5143, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, the TreeSHAP values explain the fitted Random Forest prediction for this sample and should not be considered direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the cell subtype metadata is available, but its impact on the results is not explicitly evaluated.

---

## RPT-0320 - WZ8040 on HCC827
_Split: val_

## Executive Summary
The sample RPT-0320, involving the drug WZ8040 on the HCC827 cell line, exhibits an observed AUC of 2.7443, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are fp_0367, fp_1019, fp_0385, fp_0204, and fp_0811. The presence of fp_0367, fp_1019, and fp_0385, and the absence of fp_0204 and fp_0811, push the prediction towards lower AUC (greater sensitivity). These features are associated with specific molecular structures, such as the presence of certain fingerprint bits, which are present in a subset of CTRPv2 compounds.

## Feature and Neighborhood Analysis
The same-drug cohort examples, such as NCIH1975 and PC14, also exhibit sensitivity to WZ8040, with AUC values of 3.643 and 4.6346, respectively. The same-cell cohort examples, such as afatinib and canertinib, also show sensitivity to EGFR inhibitors, with AUC values of 1.7283 and 1.8419, respectively. These examples suggest that the HCC827 cell line is particularly sensitive to EGFR inhibitors, and that WZ8040 is a potent inhibitor of this target.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features, such as fp_0443 and fp_0767, are associated with predictability across multiple drugs. The per-drug cross-validated predictability for WZ8040 is relatively low, with an R2 of 0.0516. The availability of cell subtype metadata, such as adenocarcinoma, may provide additional context for understanding the sensitivity of the HCC827 cell line to WZ8040.

## Confidence and Caveats
The interpretation of these results is limited to the local context of the sample and the training data. The TreeSHAP values explain the fitted Random Forest prediction for this sample, but are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. Additionally, the per-drug cross-validated predictability for WZ8040 is relatively low, which may indicate that the model is not well-suited for predicting the response of this drug.

---

## RPT-0322 - ABT-199 on NUDUL1
_Split: val_

## Executive Summary
The sample NUDUL1 treated with ABT-199 (a BCL2 inhibitor) shows an exceptionally sensitive response with an observed AUC of 3.1846, which is significantly lower than the RF-predicted AUC of 12.4005. This large negative prediction error indicates that the model underestimated the sensitivity of NUDUL1 to ABT-199.

## Evidence-Based Interpretation
The observed AUC of 3.1846 suggests that NUDUL1 is more sensitive to ABT-199 than predicted by the model. The top TreeSHAP features contributing to this prediction error include TNFRSF12A (gene_expression) with a negative SHAP value of -0.6295, indicating that lower expression of TNFRSF12A is associated with increased sensitivity. Additionally, fingerprint features such as fp_0443, fp_1009, fp_0227, and fp_0806 also contribute to the prediction, with positive SHAP values indicating that their presence or absence pushes the prediction towards higher AUC (resistance) or lower AUC (sensitivity).

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the local neighborhood of the sample. TNFRSF12A, a gene involved in apoptosis, has a negative SHAP value, suggesting that its lower expression contributes to the increased sensitivity of NUDUL1 to ABT-199. The fingerprint features, such as fp_0443 and fp_0806, have positive SHAP values, indicating that their presence or absence may contribute to the model's prediction of resistance. However, the actual effect of these features on the response is complex and depends on the interplay with other factors.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The model was trained on a large dataset with 311258 samples and 2024 features, and the best-performing model had a max depth of 20 and 100 estimators. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The per-drug cross-validated predictability for ABT-199 is relatively low (R2=0.2474), indicating that the model's performance for this drug may not be optimal.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, it is essential to consider the limitations of the model and the data. The model's performance may not generalize to other samples or drugs, and the features identified as important may not be causal. Additionally, the cell subtype metadata (B cell lymphoma) may provide context, but its relevance to the specific response of NUDUL1 to ABT-199 is unclear. Therefore, these results should be treated with caution and considered in the context of additional evidence and expert knowledge.

---

## RPT-0332 - decitabine on NALM6
_Split: val_

## Executive Summary
The sample RPT-0332, involving the drug decitabine on the NALM6 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.4831, which is significantly lower than the RF-predicted AUC of 13.6451. This discrepancy suggests that the model underestimated the sensitivity of decitabine in this specific context.

## Evidence-Based Interpretation
The observed AUC of 4.4831 indicates a higher sensitivity of the NALM6 cell line to decitabine compared to the predicted response. The large negative prediction error of -9.1620 further emphasizes this discrepancy. The sample's sensitivity is also notable when compared to the drug cohort (1.9 percentile) and cell cohort (4.7 percentile) baselines.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include fingerprint bits fp_0504, fp_0767, fp_0204, and gene expression feature TNFRSF12A. The presence of fp_0204 and the absence of fp_0504, fp_0767, and fp_0864 have negative SHAP values, pushing the prediction towards lower AUC (higher sensitivity). In contrast, the absence of fp_0504 and fp_0767 has positive SHAP values, which would typically increase AUC (decrease sensitivity). The gene expression feature TNFRSF12A has a negative SHAP value, indicating its contribution to the higher sensitivity of the sample.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The top global fingerprint features and most common genes across predictable per-drug models are also provided, offering insight into the broader patterns within the data. The per-drug cross-validated predictability for decitabine (R2=0.5143) suggests moderate predictability of the model for this specific drug. The availability of cell subtype metadata (acute lymphoblastic B cell leukaemia) provides additional context for understanding the sample's behavior. 

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the model's limitations. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics, such as training R2, RMSE, and correlation, should be treated as training diagnostics rather than indicators of held-out performance.

---

## RPT-0343 - pluripotin on SUDHL6
_Split: val_

## Executive Summary
The sample RPT-0343, involving the drug **pluripotin** on the **SUDHL6** cell line, exhibits an observed AUC of **3.0431**, which is exceptionally sensitive compared to the predicted AUC of **12.1385** and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on the SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (**-9.0954**) suggests that the model underestimated the sensitivity of **pluripotin** on **SUDHL6**. The top TreeSHAP features, including **fp_0623**, **fp_0367**, **fp_0235**, and **fp_0372**, have negative SHAP values, indicating that they contribute to the observed sensitivity. In contrast, **fp_0204** has a positive SHAP value, suggesting that its absence contributes to the sensitivity.

## Feature and Neighborhood Analysis
The presence of **fp_0623**, **fp_0367**, **fp_0235**, and **fp_0372** in the **pluripotin** compound is associated with increased sensitivity. These features are present in a relatively small percentage of CTRPv2 compounds, ranging from 0.6% to 6.4%. The absence of **fp_0204** also contributes to the sensitivity, and its presence is observed in 2.9% of CTRPv2 compounds. The same-drug cohort examples, such as **EOL1** and **MV411**, exhibit more sensitive profiles, while the same-cell cohort examples, such as **GSK461364** and **SB-743921**, also show more sensitive profiles.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for **pluripotin** is **R2=0.1556**, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge the limitations of the analysis, including the potential for overfitting and the lack of direct causal evidence. The TreeSHAP values explain the fitted Random Forest prediction for this sample but should not be considered direct causal evidence. Additionally, the cell subtype metadata is available, but its impact on the results is not explicitly evaluated in this analysis.

---

## RPT-0356 - KX2-391 on NB4
_Split: val_

## Executive Summary
The sample RPT-0356, treated with KX2-391 on the NB4 cell line, exhibits an observed AUC of 2.8633, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The observed AUC of 2.8633 is significantly lower than the predicted AUC of 11.9252, indicating that the sample is more sensitive than expected. The sample percentile of 2.1 in the drug cohort and 2.9 in the cell cohort further supports this interpretation. The top TreeSHAP features, including TNFRSF12A, fp_0443, fp_0706, fp_1009, and fp_0062, contribute to the predicted AUC, with TNFRSF12A having the largest negative SHAP value, pushing the prediction towards lower AUC/sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features provide insight into the factors contributing to the predicted AUC. TNFRSF12A, a gene expression feature, has a negative SHAP value of -0.7424, indicating that its low expression in this sample contributes to the predicted sensitivity. The fingerprint features, such as fp_0443, fp_0706, fp_1009, and fp_0062, also have significant SHAP values, suggesting that the presence or absence of specific molecular substructures in the drug affects the predicted AUC. The same-drug and same-cell cohort examples, such as IMR32 and SNU16 for KX2-391, and BI-2536 and GSK461364 for NB4, provide additional context for the sensitivity of this sample.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be interpreted as held-out performance. The max-depth and n-estimator tuning results, as well as the top global fingerprint features, offer insight into the model's behavior. The per-drug cross-validated predictability for KX2-391 and the cell subtype metadata for acute myeloid leukaemia provide additional context for the model's performance and the sample's characteristics. However, it is essential to note that these metrics are based on training data and should be treated with caution.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, the global model context and training diagnostics should be treated with caution, as they may not generalize to held-out data. The results should not be used to inform clinical decisions, and any conclusions drawn from this analysis should be carefully considered in the context of the available evidence. Additionally, the absence of certain information, such as pathways, biomarkers, or mechanisms, should not be inferred as evidence for or against their relevance to the sample's sensitivity.

---

## RPT-0363 - PF-3758309 on OCILY19
_Split: val_

## Executive Summary
The sample OCILY19 treated with PF-3758309 exhibits an exceptionally sensitive response, with an observed AUC of 2.8461, which is significantly lower than the predicted AUC of 11.8887. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that several fingerprint features contribute to the predicted AUC value. The top features, including fp_0367, fp_0091, fp_1001, fp_0760, and fp_0062, have negative SHAP values, indicating that they push the prediction towards lower AUC (greater sensitivity). These features are present in a subset of CTRPv2 compounds, including betulinic acid, gossypol, and simvastatin.

## Feature and Neighborhood Analysis
The presence of specific fingerprint features, such as fp_0367 and fp_0091, in the PF-3758309 compound contributes to its predicted sensitivity. The absence of fp_0062 also plays a role in this prediction. The neighborhood analysis shows that other cell lines, such as EOL1 and SIGM5, exhibit similar sensitivity profiles when treated with PF-3758309. Additionally, other drugs, like SB-743921 and vincristine, demonstrate similar sensitivity profiles when tested on the OCILY19 cell line.

## Model-Level Context
The global model context provides training diagnostics, including an R2 value of 0.4928 and an RMSE of 1.8342. The model was trained on a dataset with 311258 samples and 2024 features. The top global fingerprint features, such as fp_0443 and fp_0767, are not directly relevant to this specific sample's prediction. The per-drug cross-validated predictability for PF-3758309 is 0.3602, indicating moderate predictability. The cell subtype metadata confirms that OCILY19 is a diffuse large B cell lymphoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. The results should not be used for clinical advice, and any conclusions drawn from this analysis are limited to the specific context of this sample and model.

---

## RPT-0367 - AZD7762 on KELLY
_Split: val_

## Executive Summary
The KELLY cell line treated with AZD7762 shows an exceptionally sensitive response with an observed AUC of 2.8965, which is significantly lower than the RF-predicted AUC of 11.9118. This discrepancy suggests that the model underestimated the sensitivity of this particular drug-cell line combination.

## Evidence-Based Interpretation
The observed AUC of 2.8965 indicates a higher sensitivity of the KELLY cell line to AZD7762 compared to the predicted value. According to the rules, a lower AUC value means greater sensitivity. The large negative prediction error (-9.0153) further supports this interpretation, suggesting that the model's prediction was overly resistant.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the prediction error include fp_0623, fp_0141, TNFRSF12A (51330), fp_0204, and fp_0760. The negative SHAP values for fp_0623, fp_0141, TNFRSF12A (51330), and fp_0760 indicate that these features push the prediction towards lower AUC (higher sensitivity), while the positive SHAP value for fp_0204 pushes the prediction towards higher AUC (lower sensitivity). The presence of these features in the KELLY cell line and AZD7762 contributes to the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be considered as held-out performance metrics. The per-drug cross-validated predictability for AZD7762 has an R2 of 0.2710, indicating moderate predictability. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but their relevance to this specific sample is limited. The same-drug and same-cell cohort examples show that other cell lines (EOL1 and MV411) and drugs (BI-2536 and SB-743921) exhibit similar sensitivity profiles, supporting the notion that the KELLY cell line is exceptionally sensitive to AZD7762.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be considered in the context of the training data. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not provide direct causal evidence. The molecular descriptions are based on local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics, such as train_r2, train_rmse, and train_corr, should be treated as training diagnostics rather than held-out performance metrics.

---

## RPT-0369 - ZSTK474 on SUDHL6
_Split: val_

## Executive Summary
The sample RPT-0369, treated with ZSTK474 on the SUDHL6 cell line, exhibits an exceptionally sensitive response with an observed AUC of 3.4418, which is significantly lower than the RF-predicted AUC of 12.4541. This discrepancy suggests that the model underestimated the sensitivity of the SUDHL6 cell line to ZSTK474.

## Evidence-Based Interpretation
The observed AUC of 3.4418 indicates a high sensitivity of the SUDHL6 cell line to ZSTK474, which is consistent with the drug's mechanism as an inhibitor of PI3K catalytic subunits beta, delta, and gamma. The large negative prediction error (-9.0123) suggests that the model did not fully capture the factors contributing to this sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (SHAP=-0.7070), which has a low expression value (1.9561) and is below the cross-cell-line mean. The presence or absence of specific fingerprint bits (fp_0062, fp_0443, fp_0806, and fp_0920) also contributes to the prediction, with some features pushing the prediction towards higher AUC (resistance) and others towards lower AUC (sensitivity). The neighborhood analysis reveals that other cell lines (RI1 and JVM2) treated with ZSTK474 exhibit similar sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on a large dataset (n_samples=311258, n_features=2024) and exhibits a moderate level of predictability for ZSTK474 (R2=0.0724). The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but do not directly inform the interpretation of the RPT-0369 sample.

## Confidence and Caveats
The interpretation of the RPT-0369 sample is grounded in the local evidence and should be considered in the context of the model's limitations. The large prediction error and exceptional sensitivity of the SUDHL6 cell line to ZSTK474 suggest that there may be additional factors at play that are not fully captured by the model. Therefore, the results should be treated with caution and considered in the context of additional experimental or clinical evidence.

---

## RPT-0379 - PF-3758309 on A3KAW
_Split: val_

## Executive Summary
The sample **A3KAW** treated with **PF-3758309** exhibits an observed AUC of **2.9152**, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error are **fp_0367**, **fp_0091**, **fp_1001**, **TNFRSF12A (51330)**, and **fp_0760**, all with negative SHAP values. These features push the prediction towards lower AUC (greater sensitivity). The presence of these features in the compound and the low expression of **TNFRSF12A** contribute to the observed sensitivity.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that **fp_0367** and **fp_0091** are present in a small percentage of CTRPv2 compounds, suggesting that these features may be unique to certain compounds. The low expression of **TNFRSF12A** is also notable, as it recurs in 166 predictable-drug RF signatures. The same-drug cohort examples (**EOL1** and **SIGM5**) and same-cell cohort examples (**leptomycin B** and **CR-1-31B**) also exhibit sensitivity, suggesting that these features may be relevant to the observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including **train_r2=0.4928**, **train_rmse=1.8342**, and **train_corr=0.7061**. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for **PF-3758309** is **R2=0.3602**, indicating moderate predictability. The cell subtype metadata is available, confirming that **A3KAW** is a diffuse large B cell lymphoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence and should be treated with caution. The TreeSHAP values explain the fitted Random Forest prediction for this sample but are not direct causal evidence. The molecular descriptions are limited to local CTRPv2 metadata, feature tables, and cohort summaries. The global model metrics should be treated as training diagnostics rather than held-out performance.

---

## RPT-0384 - birinapant on NB4
_Split: val_

## Executive Summary
The sample RPT-0384, involving the drug birinapant on the cell line NB4, exhibits an exceptionally sensitive response with an observed AUC of 4.6003, which is significantly lower than the RF-predicted AUC of 13.5547. This discrepancy suggests that the model underestimated the sensitivity of birinapant in this specific context.

## Evidence-Based Interpretation
The observed AUC of 4.6003 indicates a higher sensitivity of the NB4 cell line to birinapant compared to the model's prediction. The large negative prediction error of -8.9544 further emphasizes this discrepancy. The sample's percentile rank of 1.0 within the drug cohort and 5.6 within the cell cohort underscores its unusual sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0767, TNFRSF12A, fp_0443, fp_0864, and fp_1009. The positive SHAP values for fp_0767, fp_0864, and fp_1009 suggest that their absence pushes the prediction towards higher AUC (resistance), while the negative SHAP value for TNFRSF12A and fp_0443 indicates that their presence or higher expression pushes the prediction towards lower AUC (sensitivity). The presence of fp_0443 and the lower expression of TNFRSF12A in this sample may contribute to its observed sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. These metrics should not be interpreted as held-out performance but rather as indicators of the model's fit to the training data. The per-drug cross-validated predictability for birinapant is relatively low (R2=0.0192), suggesting that the model may not capture the underlying mechanisms of birinapant's action accurately. The availability of cell subtype metadata (acute myeloid leukaemia) may provide additional context for understanding the sample's response.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the sample's characteristics. However, the model's limitations, such as its relatively low predictability for birinapant, should be acknowledged. Additionally, the results should not be extrapolated to clinical advice or used to infer causal relationships between the features and the response. The analysis is limited to the provided data and should be considered in the context of the model's constraints and the available metadata.

---

## RPT-0390 - KU-0063794 on SKMEL2
_Split: val_

## Executive Summary
The SKMEL2 cell line exhibited an exceptionally resistant response to the drug KU-0063794, with an observed AUC of 21.2320, which is higher than the RF-predicted AUC of 12.2996. This sample was selected for its large positive prediction error, indicating a higher resistance than predicted.

## Evidence-Based Interpretation
The observed AUC of 21.2320 indicates a higher resistance to KU-0063794 in the SKMEL2 cell line compared to the predicted value. The top TreeSHAP features contributing to this prediction include fingerprint bits (fp_0202, fp_0623, fp_0227, and fp_0771) and gene expression (TNFRSF12A). The presence of these fingerprint bits and the expression level of TNFRSF12A push the prediction towards a higher AUC, indicating resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features include fingerprint bits fp_0202, fp_0623, fp_0227, and fp_0771, which have negative SHAP values, indicating that their presence contributes to a lower predicted AUC (higher sensitivity). However, the actual observed AUC is higher, suggesting that other factors may be contributing to the resistance. The gene expression feature TNFRSF12A has a positive SHAP value, indicating that its expression level contributes to a higher predicted AUC (resistance).

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The model was trained on 311258 samples with 2024 features. The top global fingerprint features and most common genes across predictable per-drug models are also provided, but these should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for KU-0063794 has an R2 of 0.1121, indicating some variability in the model's performance for this specific drug. 

## Confidence and Caveats
The interpretation of the results is based on the TreeSHAP values, which explain the fitted Random Forest prediction for this sample. However, these values are not direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only. Any global model metrics referenced should be treated as training diagnostics rather than held-out performance. The results should not be used for clinical advice, and the analysis is limited to the provided data and models.

---

## RPT-0395 - daporinad on JMSU1
_Split: val_

## Executive Summary
The sample RPT-0395, involving the drug daporinad on the JMSU1 cell line, exhibits an exceptionally sensitive response with an observed AUC of 4.1656, which is significantly lower than the RF-predicted AUC of 13.0815. This discrepancy suggests that the model underestimated the sensitivity of daporinad on JMSU1 cells.

## Evidence-Based Interpretation
The observed AUC of 4.1656 indicates a higher sensitivity of JMSU1 cells to daporinad compared to the predicted response. The large negative prediction error of -8.9159 further emphasizes this discrepancy. The sample's percentile ranks within the drug and cell cohorts (4.7% and 1.5%, respectively) also highlight its exceptional sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted response include TNFRSF12A (gene_expression) with a positive SHAP value (+0.2208), indicating that higher expression of this gene would push the prediction towards higher AUC (resistance). In contrast, the absence of certain fingerprint features (e.g., fp_0706, fp_0062) contributes to the predicted sensitivity. The presence of fp_0706, for example, would increase the predicted AUC (resistance) if it were present.

## Model-Level Context
The global model context provides training diagnostics, including an R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics indicate a reasonable fit, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for daporinad (R2=0.1876) suggests that the model's performance may vary for this specific drug. The top global fingerprint features and most common genes across predictable per-drug models provide additional context, but their relevance to this specific sample is limited.

## Confidence and Caveats
The interpretation of this sample's response is grounded in the local TreeSHAP values and cohort summaries. However, the model's performance and feature importance should be treated with caution, as they are based on training diagnostics rather than held-out evaluations. Additionally, the molecular descriptions are limited to local CTRPv2 metadata and feature tables, and any global model metrics should be considered as training diagnostics rather than indicators of generalizability.

---

## RPT-0422 - methotrexate on OCILY3
_Split: val_

## Executive Summary
The OCILY3 cell line exhibits exceptional sensitivity to methotrexate, with an observed AUC of 3.5013, which is significantly lower than the predicted AUC of 12.3491. This discrepancy suggests that the model underestimated the sensitivity of OCILY3 to methotrexate.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the predicted AUC include TNFRSF12A (gene_expression; SHAP=-0.3850), fp_0538 (fingerprint_bit; SHAP=-0.2146), fp_0694 (fingerprint_bit; SHAP=-0.1262), fp_0204 (fingerprint_bit; SHAP=+0.1092), and fp_0062 (fingerprint_bit; SHAP=-0.0934). The negative SHAP values for TNFRSF12A, fp_0538, fp_0694, and fp_0062 indicate that these features push the prediction towards lower AUC (greater sensitivity), while the positive SHAP value for fp_0204 pushes the prediction towards higher AUC (lower sensitivity).

## Feature and Neighborhood Analysis
The presence of certain fingerprint bits (fp_0538, fp_0694) and the low expression of TNFRSF12A contribute to the exceptional sensitivity of OCILY3 to methotrexate. The absence of fp_0204 and fp_0062 also contributes to this sensitivity. The same-drug cohort examples (EOL1 and SUPM2) and same-cell cohort examples (vincristine and docetaxel) further support the notion that OCILY3 is exceptionally sensitive to methotrexate.

## Model-Level Context
The global model context provides training diagnostics, including train_r2=0.4928, train_rmse=1.8342, and train_corr=0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. However, it is essential to note that these metrics should be treated as training diagnostics rather than held-out performance. The per-drug cross-validated predictability for methotrexate is R2=0.1418, indicating moderate predictability.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is crucial to acknowledge that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. Additionally, the model's performance may not generalize to other datasets or scenarios, and the results should be treated with caution. The availability of cell subtype metadata (diffuse large B cell lymphoma) provides context for the analysis, but further investigation is necessary to fully understand the underlying mechanisms.

---

## RPT-0452 - methotrexate on KMS12BM
_Split: val_

## Executive Summary
The KMS12BM cell line exhibits exceptional sensitivity to methotrexate, with an observed AUC of 3.5602, which is significantly lower than the predicted AUC of 12.3491. This discrepancy suggests that the model underestimated the sensitivity of KMS12BM to methotrexate.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that several features contribute to the predicted AUC value. The top features include TNFRSF12A gene expression, fingerprint bits fp_0538, fp_0694, fp_0204, and fp_0062. Notably, TNFRSF12A has a negative SHAP value of -0.4250, indicating that its low expression in KMS12BM pushes the predicted AUC towards lower values, consistent with increased sensitivity. The presence of fingerprint bits fp_0538 and fp_0694 also contributes to the predicted sensitivity, while the absence of fp_0204 and fp_0062 has a smaller positive effect on the predicted AUC.

## Feature and Neighborhood Analysis
The neighborhood analysis shows that other cell lines, such as EOL1 and SUPM2, also exhibit sensitivity to methotrexate, with AUC values of 1.8733 and 1.9983, respectively. Additionally, the same-cell cohort examples reveal that KMS12BM is sensitive to other drugs, including paclitaxel and leptomycin B, with AUC values of 0.4397 and 0.459, respectively. These findings suggest that KMS12BM may have a unique molecular profile that contributes to its sensitivity to various drugs.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. While these metrics indicate a reasonable fit to the training data, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for methotrexate is relatively low, with an R2 of 0.1418, suggesting that the model may not capture all the relevant factors influencing methotrexate response. The availability of cell subtype metadata, including plasma cell myeloma, may provide additional context for understanding the sensitivity of KMS12BM to methotrexate.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to recognize that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance, and the per-drug cross-validated predictability for methotrexate is relatively low. Therefore, the results should be interpreted with caution, and further investigation is necessary to fully understand the mechanisms underlying the sensitivity of KMS12BM to methotrexate.

---

## RPT-0462 - I-BET151 on SEM
_Split: val_

## Executive Summary
The sample SEM treated with I-BET151 exhibits an observed AUC of 3.4332, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The large negative prediction error suggests that the model underestimated the sensitivity of this sample.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction error include TNFRSF12A (gene_expression) with a SHAP value of -0.6618, indicating that the low expression of this gene pushes the prediction towards lower AUC (greater sensitivity). Other contributing features include fingerprint bits fp_0443, fp_0623, fp_0227, and fp_0062, which have positive or negative SHAP values that influence the prediction.

## Feature and Neighborhood Analysis
The neighborhood analysis reveals that the sample SEM is more sensitive than other cell lines treated with I-BET151, such as OPM2 and OCIAML3. Additionally, the same-cell cohort examples show that other drugs like LBH-589 and SB-743921 also exhibit high sensitivity in the SEM cell line. The top global fingerprint features and most common genes across predictable per-drug models provide context for the importance of these features in the model.

## Model-Level Context
The global model context provides training diagnostics, including train_r2, train_rmse, and train_corr, which should not be treated as held-out performance. The per-drug cross-validated predictability for I-BET151 is 0.3448, indicating moderate predictability. The cell subtype metadata is available and confirms that the sample SEM is an acute lymphoblastic B cell leukaemia.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated with caution, and any conclusions drawn from this analysis should be limited to the specific sample and drug combination studied.

---

## RPT-0467 - ML210 on SNU8
_Split: val_

## Executive Summary
The sample RPT-0467, which involves the drug ML210 and the cell line SNU8, exhibits an observed AUC of 4.7615, indicating exceptional sensitivity relative to the SHAP-predicted response and cohort baselines. This report provides an evidence-based interpretation of the factors contributing to this sensitivity.

## Evidence-Based Interpretation
The observed AUC of 4.7615 is significantly lower than the predicted AUC of 13.4979, suggesting that the model underestimated the sensitivity of the SNU8 cell line to ML210. The large negative prediction error of -8.7364 indicates that the actual response is more sensitive than expected. The sample percentile of 4.8 in the drug cohort and 1.0 in the cell cohort further supports the exceptional sensitivity of this sample.

## Feature and Neighborhood Analysis
The top TreeSHAP features contributing to the predicted AUC include fp_0443, TNFRSF12A, fp_0367, fp_1009, and fp_0204. The presence of fp_1009 and the absence of fp_0443, fp_0367, and fp_0204 push the prediction towards lower AUC (greater sensitivity), while the expression of TNFRSF12A pushes the prediction towards higher AUC (lower sensitivity). The neighborhood analysis reveals that similar cell lines, such as DOHH2 and SKNDZ, also exhibit high sensitivity to ML210, while similar drugs, such as leptomycin B and 1S,3R-RSL-3, exhibit high sensitivity in the SNU8 cell line.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The top global fingerprint features and most common genes across predictable per-drug models are also provided. The per-drug cross-validated predictability for ML210 is 0.3111, indicating moderate predictability. The cell subtype metadata confirms that the SNU8 cell line is an adenocarcinoma.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to note that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The global model metrics should be treated as training diagnostics rather than held-out performance. Additionally, the results should not be used to provide clinical advice, and any conclusions drawn from this analysis should be carefully considered in the context of the available data and limitations of the model.

---

## RPT-0469 - ouabain on TUHR10TKB
_Split: val_

## Executive Summary
The sample TUHR10TKB treated with ouabain exhibits an exceptionally resistant response, with an observed AUC of 29.3500, which is higher than the RF-predicted AUC of 20.6181. This resistance is notable compared to both the drug cohort and cell line cohort baselines.

## Evidence-Based Interpretation
The observed resistance in the TUHR10TKB cell line treated with ouabain can be attributed to several key features. The top TreeSHAP features contributing to this resistance include CSF1 gene expression, fingerprint bits fp_0009 and fp_0443, and gene expressions of SDC4 and COL18A1. These features have positive SHAP values, indicating they push the prediction towards higher AUC or resistance.

## Feature and Neighborhood Analysis
The local analysis of the top TreeSHAP features reveals that CSF1 gene expression is markedly above the cross-cell-line mean, and its high value contributes to the resistance. The presence and absence of specific fingerprint bits (fp_0009 and fp_0443) also play a role, with these bits being present in a small percentage of CTRPv2 compounds. Additionally, the gene expressions of SDC4 and COL18A1 are above their respective cross-cell-line means, further contributing to the observed resistance.

## Model-Level Context
The global model context provides training diagnostics, including a training R2 of 0.4928 and RMSE of 1.8342. The model's performance on the training data suggests a moderate fit, but these metrics should not be taken as indicative of held-out performance. The per-drug cross-validated predictability for ouabain has an R2 of 0.1544, suggesting some variability in the model's ability to predict responses for this drug. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, and SDC4, but their relevance to the specific response of TUHR10TKB to ouabain is not directly inferred from this information.

## Confidence and Caveats
The interpretation of the results is grounded in the local evidence provided by the TreeSHAP values and the characteristics of the TUHR10TKB cell line and ouabain. However, it is essential to recognize the limitations of the analysis, including the use of training diagnostics as opposed to held-out performance metrics and the potential for variability in the model's predictions across different drugs and cell lines. The molecular descriptions and interpretations are constrained to the local CTRPv2 metadata and feature tables, and any broader implications or mechanisms should be considered speculative without additional evidence.

---

## RPT-0473 - methotrexate on COLO684
_Split: val_

## Executive Summary
The COLO684 cell line exhibits exceptional sensitivity to methotrexate, with an observed AUC of 3.7512, which is significantly lower than the predicted AUC of 12.4743. This discrepancy suggests that the model underestimated the sensitivity of COLO684 to methotrexate.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that several features contribute to the predicted AUC value. The top feature, TNFRSF12A (gene_expression), has a negative SHAP value of -0.4531, indicating that its low expression in COLO684 pushes the predicted AUC towards lower values (i.e., increased sensitivity). Other features, such as fp_0538, fp_0062, and fp_0694, also have negative SHAP values, suggesting that their presence or absence contributes to the predicted sensitivity.

## Feature and Neighborhood Analysis
The presence of certain fingerprint features, such as fp_0538 and fp_0694, and the absence of others, like fp_0204 and fp_0062, contribute to the predicted sensitivity of COLO684 to methotrexate. The representative SMARTS patterns for these features provide insight into the chemical structures that may be associated with sensitivity to methotrexate. Additionally, the low expression of TNFRSF12A in COLO684 is a key factor in the predicted sensitivity.

## Model-Level Context
The global model context provides training diagnostics, including an R2 value of 0.4928 and an RMSE of 1.8342. While these metrics indicate a reasonable fit to the training data, they should not be interpreted as held-out performance. The per-drug cross-validated predictability for methotrexate is relatively low (R2=0.1418), suggesting that the model may not capture all the relevant factors influencing the response to this drug. The availability of cell subtype metadata (adenocarcinoma) may provide additional context for understanding the response of COLO684 to methotrexate.

## Confidence and Caveats
The interpretation of the results is grounded in the local CTRPv2 metadata, feature tables, and cohort summaries. However, it is essential to recognize that TreeSHAP values explain the fitted Random Forest prediction for this sample and are not direct causal evidence. The model's performance and feature importance should be considered in the context of the training data and the specific cell line and drug being studied. Additionally, the results should not be used to provide clinical advice, and any conclusions drawn from this analysis should be carefully evaluated in the context of the available evidence.

---

## RPT-0499 - KX2-391 on OPM2
_Split: val_

## Executive Summary
The sample RPT-0499, involving the drug KX2-391 on the OPM2 cell line, exhibits an observed AUC of 3.3164, which is exceptionally sensitive compared to the predicted AUC of 11.9603 and cohort baselines. This report aims to provide an evidence-based interpretation of this observation, focusing on the SHAP values and feature analysis.

## Evidence-Based Interpretation
The large negative prediction error (-8.6439) suggests that the model underestimated the sensitivity of KX2-391 on OPM2. The top TreeSHAP features contributing to this prediction error include TNFRSF12A (gene_expression) with a SHAP value of -0.7439, indicating that lower expression of TNFRSF12A is associated with increased sensitivity. Other notable features include fingerprint bits fp_0443, fp_0706, fp_1009, and fp_0062, which have positive or negative SHAP values influencing the prediction.

## Feature and Neighborhood Analysis
The feature analysis reveals that TNFRSF12A is a key contributor to the predicted response, with its low expression level (z=-1.17) pushing the prediction towards higher sensitivity. The fingerprint bits, such as fp_0443 and fp_0706, also play a role in shaping the predicted response, with their presence or absence influencing the SHAP values. The neighborhood analysis, including same-drug and same-cell cohort examples, provides additional context, highlighting that other cell lines (e.g., IMR32 and SNU16) and drugs (e.g., vincristine and leptomycin B) exhibit similar sensitivity profiles.

## Model-Level Context
The global model context provides training diagnostics, including train_r2 (0.4928), train_rmse (1.8342), and train_corr (0.7061), which should not be interpreted as held-out performance. The max-depth and n-estimator tuning results, as well as the top global fingerprint features, offer insights into the model's behavior. The per-drug cross-validated predictability for KX2-391 (R2=0.4019) and the availability of cell subtype metadata (plasma cell myeloma) further contextualize the model's performance.

## Confidence and Caveats
While the SHAP values and feature analysis provide valuable insights into the predicted response, it is essential to acknowledge the limitations of the model and the data. The TreeSHAP values explain the fitted Random Forest prediction for this sample but do not constitute direct causal evidence. The molecular descriptions are grounded in local CTRPv2 metadata, feature tables, and cohort summaries only. Therefore, any conclusions drawn from this analysis should be treated with caution, and further investigation is necessary to fully understand the underlying mechanisms.

---
