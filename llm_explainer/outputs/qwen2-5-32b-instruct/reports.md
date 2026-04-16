# Generated Reports - Qwen2.5-32B-Instruct

## RPT-0001 - cytarabine hydrochloride on SKMEL2
_Source evidence: SHAP-0001_

## Executive Summary

The response of SKMEL2, a malignant melanoma cell line derived from skin tissue, to cytarabine hydrochloride is exceptionally resistant, with an observed AUC of 27.1820, significantly higher than the model-predicted AUC of 13.5949. This resistance is notable given the drug's mechanism as an inducer of DNA damage. The SHAP analysis reveals that specific molecular features of cytarabine hydrochloride and the cell line contribute to this resistance profile.

## Evidence-Based Interpretation

The observed AUC of 27.1820 for cytarabine hydrochloride on SKMEL2 is exceptionally high, indicating strong resistance. The model predicted an AUC of 13.5949, resulting in a positive prediction error of +13.5871. This suggests that the cell line exhibits a higher degree of resistance than anticipated by the model. The SHAP analysis identifies key molecular features that influence this resistance.

## Feature and Neighborhood Analysis

The top TreeSHAP features influencing the prediction are:

1. **fp_0443**: This fingerprint bit, represented by the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, is present in the compound and pushes the prediction toward lower AUC (relative sensitivity). However, its presence in only 0.4% of CTRPv2 compounds suggests it may not be a dominant factor in this context.
   
2. **fp_0504**: This feature, represented by the SMARTS `[#6]:[#6](=[#8]):[#7]`, is absent in the compound and pushes the prediction toward higher AUC (relative resistance). It is present in 4.4% of CTRPv2 compounds and is seen in drugs like topotecan and IC-87114.

3. **fp_0767**: This feature, represented by the SMARTS `[#6]-[#7](-[#6])-[#6]`, is also absent and pushes the prediction toward higher AUC (relative resistance). It is present in 11.0% of CTRPv2 compounds and is seen in drugs like Bax channel blocker and trifluoperazine.

4. **fp_0450**: This fingerprint bit, represented by the SMARTS `[#7]-[#6](:[#6]):[#6](:[#6]:[#6])-[#7]`, is present in the compound and pushes the prediction toward lower AUC (relative sensitivity). It is present in 0.8% of CTRPv2 compounds and is seen in compounds like Repligen 136.

5. **fp_0864**: This feature, represented by the SMARTS `[#7]=[#6]-[#6]`, is absent and pushes the prediction toward higher AUC (relative resistance). It is present in 2.5% of CTRPv2 compounds and is seen in drugs like mitomycin and

---

## RPT-0002 - birinapant on KYM1
_Source evidence: SHAP-0002_

## Executive Summary

The response of KYM1, a rhabdomyosarcoma cell line, to birinapant, an SMAC mimetic and inhibitor of IAPs, is exceptionally sensitive compared to both the SHAP-predicted response and cohort baselines. The observed AUC of 0.6877 is significantly lower than the predicted AUC of 13.8762, indicating a large negative prediction error of -13.1885. This sensitivity is further highlighted by the sample's percentile ranking within the drug cohort (0.1) and cell cohort (0.2).

## Evidence-Based Interpretation

The observed response of KYM1 to birinapant is characterized by a low AUC of 0.6877, indicating high sensitivity. The model predicted a much higher AUC of 13.8762, suggesting a significant deviation from the expected response. The SHAP analysis reveals that the fingerprint bit `fp_0443` has the strongest influence, pushing the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.5166. This feature is present in only 0.4% of CTRPv2 compounds and is associated with compounds like nilotinib and bleomycin A2. Conversely, other fingerprint bits such as `fp_0767`, `fp_0504`, `fp_0864`, `fp_1009`, and `fp_0925` push the prediction toward higher AUC (relative resistance), but their values are zero in this case, reducing their impact.

## Feature and Neighborhood Analysis

The top TreeSHAP features influencing the prediction include:
- `fp_0443`: This fingerprint bit, representing the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, is present in the compound and strongly influences the prediction toward lower AUC, indicating sensitivity. It is rare, found in only 0.4% of CTRPv2 compounds.
- `fp_0767`, `fp_0504`, `fp_0864`, `fp_1009`, and `fp_0925`: These fingerprint bits are absent in the compound and push the prediction toward higher AUC, indicating resistance. They are more prevalent in CTRPv2 compounds, ranging from 2.5% to 11.0%.

In the same-drug cohort, KYM1 is more sensitive compared to other cell lines like WSUDLCL2 and ESS1, which also show sensitivity, while BL70 and NAMALWA exhibit higher resistance. In the same-cell cohort, KYM1 shows sensitivity to leptomycin B and ouabain, but resistance to compound 1B and ML320.

## Model-Level Context

The model used for prediction is a Random Forest (RF) with a max depth of 20 and 100 estimators, achieving a cross

---

## RPT-0003 - nilotinib on BT549
_Source evidence: SHAP-0003_

## Executive Summary

The response of BT549 cells to nilotinib is exceptionally resistant, with an observed AUC of 23.7050, significantly higher than the model-predicted AUC of 13.4663. This case was selected due to its large positive prediction error, indicating a higher resistance than predicted. The BT549 cell line, derived from breast ductal carcinoma, exhibits a unique response profile compared to both the drug and cell cohort baselines.

## Evidence-Based Interpretation

The observed AUC of 23.7050 for nilotinib on BT549 indicates a high level of resistance, placing it at the 100th percentile within both the drug and cell cohorts. The model-predicted AUC of 13.4663 suggests a lower resistance, leading to a positive prediction error of +10.2387. This discrepancy highlights the exceptional resistance of BT549 cells to nilotinib.

## Feature and Neighborhood Analysis

### Top TreeSHAP Features
1. **TNFRSF12A (51330)**: This gene expression feature pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2006. The gene expression value is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
2. **fp_0367**: This fingerprint bit pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1002. It is present in 6.4% of CTRPv2 compounds, with representative SMARTS `[#6]:[#6](-[#6]):[#6]`.
3. **fp_0443**: This fingerprint bit pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0993. It is present in 0.4% of CTRPv2 compounds, with representative SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`.
4. **fp_0204**: This fingerprint bit pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0815. It is present in 2.9% of CTRPv2 compounds, with representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`.
5. **fp_0538**: This fingerprint bit pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0727. It is present in 0.6% of CTRPv2 compounds, with representative SMARTS `[#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6]`.
6. **fp_0811**: This fingerprint bit pushes the prediction toward higher AUC (relative resistance) with a SHAP

---

## RPT-0004 - N9-isopropylolomoucine on CADOES1
_Source evidence: SHAP-0004_

## Executive Summary

The response of CADOES1, a bone-derived Ewing's sarcoma peripheral primitive neuroectodermal tumor cell line, to N9-isopropylolomoucine was exceptionally sensitive, with an observed AUC of 0.0835. This sensitivity is significantly lower than the model-predicted AUC of 12.5703, indicating a large negative prediction error of -12.4868. The observed AUC places the sample in the 0.1 percentile among the drug cohort and the 1.9 percentile among the cell cohort, highlighting its unique sensitivity to the drug.

## Evidence-Based Interpretation

The observed response of CADOES1 to N9-isopropylolomoucine is characterized by a highly sensitive phenotype, as evidenced by the low observed AUC of 0.0835. This sensitivity is notably lower than the model-predicted AUC of 12.5703, indicating that the cell line is much more sensitive to the drug than the model anticipated. The large negative prediction error suggests that the model underestimates the sensitivity of CADOES1 to N9-isopropylolomoucine.

## Feature and Neighborhood Analysis

The top TreeSHAP features contributing to the prediction include gene expression and molecular fingerprint bits. The most significant feature is TNFRSF12A (gene expression), which pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.6577. This gene is below the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, suggesting its importance in the model's prediction.

Fingerprint bits such as fp_0227 and fp_0204 push the prediction toward higher AUC (relative resistance), with SHAP values of +0.0985 and +0.0901, respectively. These bits are associated with specific SMARTS patterns and are present in a small percentage of CTRPv2 compounds. Conversely, fingerprint bits like fp_0062 and fp_0538 push the prediction toward lower AUC (relative sensitivity), with SHAP values of -0.0887 and -0.0829, respectively.

## Model-Level Context

The model's training diagnostics indicate a moderate fit with a training R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a max depth of 20 and 100 estimators, achieving an R² of 0.6648. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, SDC4, PRSS23, LAMB2, GPRC5A, IKZF1, and ITGA3. For N9-isopropylolomoucine, the cross-validated predictability is relatively low with an R² of 0.

---

## RPT-0005 - GSK461364 on MC116
_Source evidence: SHAP-0005_

## Executive Summary
The observed response of GSK461364 on MC116 indicates a higher resistance than predicted by the model, with an observed AUC of 17.4070 compared to a predicted AUC of 7.3230. This case is selected due to its large positive prediction error, suggesting the cell line is more resistant than anticipated. The SHAP analysis reveals that fingerprint features and gene expressions contribute significantly to this prediction, with specific chemical structures and gene expression levels pushing the prediction towards higher or lower AUC values.

## Evidence-Based Interpretation
The observed AUC of 17.4070 for GSK461364 on MC116 is notably higher than the model's prediction of 7.3230, indicating a more resistant phenotype than expected. The SHAP analysis identifies several key features that influence this prediction. Fingerprint bits `fp_0504` and `fp_0443`, which are associated with chemical structures `[#6]:[#6](=[#8]):[#7]` and `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, respectively, both push the prediction towards lower AUC values, suggesting relative sensitivity. However, the observed AUC is still high, implying other factors may be at play. Gene expression levels of `TNFRSF12A` also push the prediction towards lower AUC, while `SYTL2` pushes it towards higher AUC, contributing to the overall resistance profile.

## Feature and Neighborhood Analysis
The top TreeSHAP features indicate that fingerprint bits `fp_0504` and `fp_0443` are significant contributors to the prediction, both pushing towards lower AUC values. These features are present in a small percentage of compounds, with `fp_0504` found in 4.4% and `fp_0443` in 0.4% of CTRPv2 compounds. The gene expression of `TNFRSF12A` is below the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, further supporting sensitivity. Conversely, `SYTL2` expression is near the mean and recurs in 84 signatures, pushing towards higher AUC. The same-drug cohort examples show varying sensitivities, while the same-cell cohort examples indicate a range of responses, with some drugs showing high resistance similar to GSK461364.

## Model-Level Context
The model's training diagnostics include a train R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061, reflecting the model's fit to the training data. The best-performing model configuration has a max depth of 20 and 100 estimators, achieving an R2 of 0.6648. Globally, fingerprint features like `fp_0443` and `fp_0504` are significant, aligning with their importance

---

## RPT-0006 - niclosamide on IALM
_Source evidence: SHAP-0006_

## Executive Summary
The case RPT-0006 examines the response of niclosamide on the IALM cell line, which is derived from large cell carcinoma of the lung. The observed AUC of 0.9043 indicates an exceptionally sensitive response to niclosamide, which is significantly lower than the RF-predicted AUC of 13.3307. This large negative prediction error suggests that the model underestimates the sensitivity of IALM to niclosamide. The SHAP analysis identifies key features influencing this prediction, including gene expression and molecular fingerprints.

## Evidence-Based Interpretation
The observed AUC of 0.9043 for niclosamide on IALM is markedly lower than the predicted AUC of 13.3307, indicating that the cell line is more sensitive to the drug than the model predicts. This sensitivity is further contextualized by the drug cohort's mean AUC of 11.8062 and the cell cohort's mean AUC of 13.8401, placing the observed response at the lower end of both distributions.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction include:
1. **TNFRSF12A**: This gene expression feature pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.2028. The gene expression level is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
2. **fp_0623**: This fingerprint bit pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1794. It is present in 5.8% of CTRPv2 compounds and is associated with compounds like trifluoperazine and prochlorperazine.
3. **fp_0771**: Another fingerprint bit that pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1178. It is present in 6.4% of CTRPv2 compounds and is associated with compounds like tacedinaline and AM-580.
4. **fp_0443**: This fingerprint bit pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1124. It is present in 0.4% of CTRPv2 compounds and is associated with compounds like nilotinib and bleomycin A2.
5. **fp_0204**: This fingerprint bit pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0885. It is present in 2.9% of CTRPv2 compounds and is associated with compounds like BRD-K26531177 and NVP-BEZ235.
6. **fp_0062**: This fingerprint bit pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0551. It is

---

## RPT-0007 - pitstop2 on SNU886
_Source evidence: SHAP-0007_

## Executive Summary

The response of SNU886, a hepatocellular carcinoma cell line, to the drug pitstop2 is exceptionally resistant, with an observed AUC of 23.1410, significantly higher than the model-predicted AUC of 13.6419. This large positive prediction error indicates that the cell line is more resistant than predicted by the model and the cohort baselines. The analysis highlights key features influencing this resistance, including gene expression and molecular fingerprints.

## Evidence-Based Interpretation

The observed AUC of 23.1410 for pitstop2 on SNU886 is notably higher than the model-predicted AUC of 13.6419, indicating a significant deviation towards higher resistance. This deviation is further supported by the cell line's position at the 100th percentile in both the drug and cell cohort contexts, suggesting an exceptionally resistant profile compared to other cell lines and drugs.

## Feature and Neighborhood Analysis

The top TreeSHAP features contributing to the higher AUC prediction include:

1. **TNFRSF12A (51330)**: This gene expression feature pushes the prediction towards higher AUC (relative resistance) with a SHAP value of +0.2107. The gene expression value is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, indicating its relevance across multiple drug responses.

2. **fp_0204**: This fingerprint bit, representing the SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, also contributes to higher AUC with a SHAP value of +0.0847. It is present in 2.9% of CTRPv2 compounds and is associated with drugs like BRD-K26531177, NVP-BEZ235, and CD-437.

3. **fp_0443**: Another fingerprint bit, representing the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, contributes positively to higher AUC with a SHAP value of +0.0738. It is present in 0.4% of CTRPv2 compounds and is linked to drugs such as nilotinib and bleomycin A2.

4. **fp_0367**: This fingerprint bit, representing the SMARTS `[#6]:[#6](-[#6]):[#6]`, also pushes the prediction towards higher AUC with a SHAP value of +0.0646. It is present in 6.4% of CTRPv2 compounds and is associated with drugs like betulinic acid, gossypol, and simvastatin.

5. **fp_0062**: This fingerprint bit, representing the SMARTS `[#6]-[#6](:[#6]):[#16]`, is the only feature pushing the prediction towards lower AUC (relative

---

## RPT-0008 - trametinib on DU4475
_Source evidence: SHAP-0008_

## Executive Summary
The response of trametinib on the DU4475 cell line, characterized by an observed AUC of 0.1282, indicates exceptional sensitivity compared to both the model-predicted AUC of 12.4028 and the cohort baselines. The SHAP analysis reveals that specific molecular features, including fingerprint bits and gene expression levels, contribute significantly to this sensitivity. The model's prediction error of -12.2746 underscores the discrepancy between the observed and predicted responses, highlighting the need for further investigation into the underlying mechanisms.

## Evidence-Based Interpretation
The observed AUC of 0.1282 for trametinib on DU4475 is exceptionally low, indicating high sensitivity to the drug. This is in stark contrast to the model-predicted AUC of 12.4028, which suggests a much higher resistance. The SHAP analysis identifies several key features that contribute to this sensitivity. The top contributing feature is fingerprint bit `fp_0367`, which has a SHAP value of -0.2979, indicating a strong push toward lower AUC (relative sensitivity). Other significant contributors include gene expression of `TNFRSF12A` and fingerprint bits `fp_0409`, `fp_0062`, and `fp_1008`, all of which also push the prediction toward lower AUC.

## Feature and Neighborhood Analysis
The fingerprint bit `fp_0367` with SMARTS `[#6]:[#6](-[#6]):[#6]` is present in 6.4% of CTRPv2 compounds and is associated with drugs like betulinic acid, gossypol, and simvastatin. This feature significantly contributes to the model's prediction of lower AUC, suggesting a structural characteristic that enhances trametinib's sensitivity in DU4475. Gene expression of `TNFRSF12A` at a value of 4.5098 (near the cross-cell-line mean) is another key factor, supporting sensitivity in 166 predictable-drug RF signatures. Fingerprint bits `fp_0409`, `fp_0062`, and `fp_1008` also contribute to lower AUC predictions, with SMARTS patterns `[#7]-[#6](:[#7]):[#7]`, `[#6]-[#6](:[#6]):[#16]`, and `[#7]-[#6](:[#7]:[#6]):[#7]:[#6]`, respectively.

## Model-Level Context
The model's training diagnostics indicate a moderate fit with a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a max depth of 20 and 100 estimators, achieving an R2 of 0.6648. The global fingerprint features and gene signatures suggest that while `

---

## RPT-0009 - docetaxel on KPNYN
_Source evidence: SHAP-0009_

## Executive Summary
The observed response of docetaxel on the KPNYN cell line, derived from autonomic ganglia neuroblastoma, indicates a higher resistance (AUC = 17.3740) than the model's prediction (AUC = 7.9419). This case was selected due to its large positive prediction error, suggesting the cell line is more resistant than the model anticipated. The SHAP analysis reveals that several molecular fingerprints and gene expression levels contribute to this observed resistance.

## Evidence-Based Interpretation
The observed AUC of 17.3740 for docetaxel on KPNYN is significantly higher than the model's prediction of 7.9419, indicating a more resistant phenotype than expected. The SHAP analysis highlights several key features that contribute to this resistance:

1. **Fingerprint Bit fp_1009**: This feature, represented by the SMARTS `[#6]-[#6](:[#6]):[#6]`, is present in 9.1% of compounds and is associated with relative sensitivity, pushing the prediction toward a lower AUC. However, its presence in this case does not fully account for the observed resistance.
2. **Fingerprint Bit fp_0443**: Represented by the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, this feature is rare (0.4% of compounds) and also pushes the prediction toward lower AUC, indicating relative sensitivity.
3. **Fingerprint Bit fp_0204**: With SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, this feature is present in 2.9% of compounds and similarly pushes the prediction toward lower AUC.
4. **Gene Expression TNFRSF12A**: This gene, with a z-score of -2.18, is markedly below the cross-cell-line mean and is associated with relative sensitivity, pushing the prediction toward lower AUC.

These features collectively suggest that the model underestimates the resistance of KPNYN to docetaxel.

## Feature and Neighborhood Analysis
The SHAP analysis identifies several molecular fingerprints and gene expression levels that contribute to the observed resistance of KPNYN to docetaxel. The fingerprints fp_1009, fp_0443, fp_0204, and fp_0741, along with the gene expression of TNFRSF12A, all push the prediction toward lower AUC, indicating relative sensitivity. However, the observed AUC is much higher, suggesting additional factors not captured by these features.

In the same-drug cohort, cells like 697 and OCIAML3 show more sensitivity, while cells like TUHR14TKB and MALME3M exhibit more resistance, similar to KPNYN. In the same-cell cohort, drugs like leptomycin B and 1S,3R-RSL-3 show more sensitivity, whereas erlotinib and pevonedistat exhibit more resistance,

---

## RPT-0010 - RITA on TE441T
_Source evidence: SHAP-0010_

## Executive Summary

The case of RITA on TE441T (rhabdomyosarcoma) demonstrates an exceptionally sensitive response with an observed AUC of 1.3692, which is significantly lower than the model-predicted AUC of 13.5331. This large negative prediction error indicates that the cell line is more sensitive to RITA than the model anticipated. The SHAP analysis reveals that the primary drivers of this sensitivity include the gene expression of TNFRSF12A and specific molecular fingerprints of the drug.

## Evidence-Based Interpretation

The observed AUC of 1.3692 for RITA on TE441T is markedly lower than the global mean AUC of 12.8580 and the model-predicted AUC of 13.5331. This suggests that TE441T is exceptionally sensitive to RITA compared to the cohort baselines. The SHAP analysis identifies TNFRSF12A gene expression and specific molecular fingerprints as key factors influencing this sensitivity.

### SHAP/Feature Evidence

1. **TNFRSF12A (Gene Expression)**: This feature has a SHAP value of +0.2021, indicating it pushes the prediction toward higher AUC (relative resistance). However, the gene expression value is near the cross-cell-line mean, suggesting that its influence on resistance might be less pronounced in this context.
   
2. **fp_0760 (Fingerprint Bit)**: This feature has a SHAP value of -0.0898, pushing the prediction toward lower AUC (relative sensitivity). The SMARTS pattern `[#6]-[#6]-[#7](-[#6]-[#6])-[#6](=[#8])-[#6]` is present in 4.4% of CTRPv2 compounds and is associated with drugs like betulinic acid, paclitaxel, and ouabain.

3. **fp_0443 (Fingerprint Bit)**: This feature has a SHAP value of +0.0888, pushing the prediction toward higher AUC (relative resistance). The SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]` is present in 0.4% of CTRPv2 compounds and is associated with drugs like nilotinib and bleomycin A2.

4. **fp_0902 (Fingerprint Bit)**: This feature has a SHAP value of +0.0803, pushing the prediction toward higher AUC (relative resistance). The SMARTS pattern `[#8]-[#6@H](-[#8]-[#6@H](-[#6])-[#6])-[#6@@H]` is present in 1.0% of CTRPv2 compounds and is associated with drugs like teniposide, NSC23766, and etoposide.

5. **fp_0204 (Fingerprint Bit)**

---

## RPT-0011 - GSK2636771 on SUDHL10
_Source evidence: SHAP-0011_

## Executive Summary

The response of SUDHL10, a diffuse large B cell lymphoma cell line, to GSK2636771, an inhibitor of PI3K catalytic subunit beta (PIK3CB), is exceptionally resistant relative to both the model prediction and cohort baselines. The observed AUC of 21.9540 is significantly higher than the predicted AUC of 12.5439, indicating a substantial deviation towards resistance. This case was selected due to its large positive prediction error, highlighting an unexpected level of resistance.

## Evidence-Based Interpretation

The observed AUC of 21.9540 for GSK2636771 on SUDHL10 is notably higher than the global mean AUC of 12.8580 and the cell cohort mean AUC of 12.7645. The model predicted an AUC of 12.5439, resulting in a positive prediction error of +9.4101, indicating that the cell line is more resistant than expected. The SHAP analysis reveals that the primary drivers pushing the prediction towards lower AUC (relative sensitivity) are the gene expression of TNFRSF12A and specific fingerprint bits (fp_0623, fp_0062, fp_0760). Conversely, fingerprint bits fp_0806 and fp_0443 push the prediction towards higher AUC (relative resistance).

## Feature and Neighborhood Analysis

The top TreeSHAP features influencing the prediction are:
1. **TNFRSF12A (gene_expression)**: With a SHAP value of -0.6573, TNFRSF12A expression below the cross-cell-line mean pushes the prediction towards lower AUC, indicating relative sensitivity. This gene recurs in 166 predictable-drug RF signatures.
2. **fp_0623 (fingerprint_bit)**: Representing the SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, this bit is present in 5.8% of CTRPv2 compounds and pushes the prediction towards lower AUC.
3. **fp_0062 (fingerprint_bit)**: Representing the SMARTS `[#6]-[#6](:[#6]):[#16]`, this bit is present in 3.7% of CTRPv2 compounds and also pushes the prediction towards lower AUC.
4. **fp_0806 (fingerprint_bit)**: Representing the SMARTS `[#6]:[#7]:[#6]`, this bit is present in 6.0% of CTRPv2 compounds and pushes the prediction towards higher AUC.
5. **fp_0443 (fingerprint_bit)**: Representing the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, this bit is present in 0.4% of

---

## RPT-0012 - dabrafenib on DU4475
_Source evidence: SHAP-0012_

## Executive Summary
The response of dabrafenib on the DU4475 cell line, characterized by an observed AUC of 0.6377, indicates exceptional sensitivity compared to both the SHAP-predicted AUC of 12.7509 and the cohort baselines. This large negative prediction error highlights a significant discrepancy between the model's prediction and the actual observed response. The analysis identifies key features influencing the prediction, including gene expression and molecular fingerprints, which provide insights into the model's reasoning.

## Evidence-Based Interpretation
The observed AUC of 0.6377 for dabrafenib on DU4475 is exceptionally low, indicating high sensitivity to the drug. In contrast, the model predicted an AUC of 12.7509, suggesting a much higher resistance. This large negative prediction error of -12.1132 underscores the model's underestimation of the drug's efficacy. The DU4475 cell line falls in the 80th percentile of the cell cohort, while the dabrafenib response is in the 30th percentile of the drug cohort, further emphasizing the unusual sensitivity.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction include gene expression and molecular fingerprints. TNFRSF12A gene expression, with a SHAP value of -0.5127, significantly pushes the prediction toward lower AUC, indicating relative sensitivity. This gene recurs in 166 predictable-drug RF signatures and is near the cross-cell-line mean. Molecular fingerprints such as fp_0204 and fp_0443, with SHAP values of +0.1150 and +0.0805 respectively, push the prediction toward higher AUC, indicating relative resistance. These fingerprints are associated with specific SMARTS patterns and are present in a small percentage of CTRPv2 compounds. Other fingerprints like fp_0760 and fp_0062 also contribute to the prediction, with fp_0760 pushing toward lower AUC and fp_0062 toward higher AUC.

## Model-Level Context
The model's training diagnostics indicate a moderate fit with a train_r2 of 0.4928, train_rmse of 1.8342, and train_corr of 0.7061. The best-performing model configuration has a max_depth of 20 and n_estimators of 100, achieving an R2 of 0.6648. The global fingerprint features and gene signatures provide additional context, with TNFRSF12A being a common gene across many predictable-drug models. The per-drug cross-validated predictability for dabrafenib is R2=0.3967, indicating moderate predictability within the model.

## Confidence and Caveats
The SHAP values explain the model's prediction rather than the underlying biological mechanisms directly. The large negative prediction error suggests that the model may not fully capture the factors influencing dabrafenib's efficacy on DU44

---

## RPT-0013 - MLN2238 on KARPAS620
_Source evidence: SHAP-0013_

## Executive Summary
The response of MLN2238 on the KARPAS620 cell line, characterized by an observed AUC of 18.6540, indicates a higher resistance than the model's prediction of 9.2450. This case was selected due to its large positive prediction error, highlighting a significant deviation from the expected response. The cell line KARPAS620, derived from haematopoietic and lymphoid tissue with a plasma cell myeloma subtype, exhibits a more resistant profile compared to both the drug cohort and cell cohort baselines.

## Evidence-Based Interpretation
The observed AUC of 18.6540 for MLN2238 on KARPAS620 is notably higher than the model's prediction of 9.2450, indicating a more resistant phenotype than anticipated. The top TreeSHAP features contributing to this prediction include several fingerprint bits and a gene expression feature. Specifically, fingerprint bits fp_0204, fp_0271, fp_0806, fp_0062, and fp_0623, along with the gene expression of TNFRSF12A, all push the prediction toward lower AUC, suggesting relative sensitivity. However, the observed AUC is higher, indicating that other factors not captured by these features may be contributing to the resistance.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are:
1. **fp_0204**: This fingerprint bit, representing the SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, is present in 2.9% of CTRPv2 compounds and is associated with relative sensitivity. Example drugs include BRD-K26531177, NVP-BEZ235, and CD-437.
2. **fp_0271**: Representing the SMARTS `[#7]-[#6](:[#6]):[#6]`, this bit is present in 5.0% of compounds and is linked to relative sensitivity. Example drugs include trifluoperazine, prochlorperazine, and BRD-K94991378.
3. **TNFRSF12A**: Below the cross-cell-line mean, this gene expression feature is associated with relative sensitivity and recurs in 166 predictable-drug RF signatures.
4. **fp_0806**: Representing the SMARTS `[#6]:[#7]:[#6]`, this bit is present in 6.0% of compounds and is linked to relative sensitivity. Example drugs include fluorouracil, cimetidine, and dacarbazine.
5. **fp_0062**: Representing the SMARTS `[#6]-[#6](:[#6]):[#16]`, this bit is present in 3.7% of compounds and is linked to relative sensitivity. Example drugs include Merck60, cytarabine hydrochloride, and

---

## RPT-0014 - AZD4547 on NCIH716
_Source evidence: SHAP-0014_

## Executive Summary
The response of NCIH716 cells to AZD4547, an inhibitor of fibroblast growth factor receptors (FGFR1, FGFR2, FGFR3), is exceptionally sensitive, with an observed AUC of 1.1299, significantly lower than the model-predicted AUC of 13.2363. This sensitivity is further highlighted by the sample's percentile ranking within both the drug cohort (0.1) and the cell cohort (0.2). The SHAP analysis identifies key features influencing the prediction, including gene expression and molecular fingerprints, which provide insights into the model's reasoning.

## Evidence-Based Interpretation
The observed AUC of 1.1299 indicates that NCIH716 cells are highly sensitive to AZD4547, contrasting sharply with the model's prediction of 13.2363. This large negative prediction error suggests that the model underestimates the sensitivity of NCIH716 cells to AZD4547. The SHAP analysis reveals that TNFRSF12A gene expression and specific molecular fingerprints contribute to the prediction, with TNFRSF12A pushing the prediction toward higher AUC (resistance) and certain fingerprints pushing toward lower AUC (sensitivity).

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction include:
1. **TNFRSF12A**: This gene expression feature pushes the prediction toward higher AUC (resistance) with a SHAP value of +0.2038. TNFRSF12A is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
2. **fp_0227**: This fingerprint bit, representing the SMARTS `[#8]-[#6@H]`, pushes the prediction toward lower AUC (sensitivity) with a SHAP value of -0.1489. It is present in 6.7% of CTRPv2 compounds and is associated with drugs like Bax channel blocker, paclitaxel, and teniposide.
3. **fp_0468**: Another fingerprint bit, representing the SMARTS `[#6]:[#6](:[#6](-[#6]-[#7]):[#6](-[#6]):[#6]):[#6]`, also pushes the prediction toward lower AUC (sensitivity) with a SHAP value of -0.1446. It is present in 0.6% of CTRPv2 compounds and is associated with drugs like staurosporine, StemRegenin 1, and leptomycin B.
4. **fp_0443**: This fingerprint bit, representing the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, pushes the prediction toward higher AUC (resistance) with a SHAP value of +0.0964. It is present in 0.4% of CTRPv2 compounds and

---

## RPT-0015 - LBH-589 on KARPAS620
_Source evidence: SHAP-0015_

## Executive Summary
The response of LBH-589 on the KARPAS620 cell line, characterized by an observed AUC of 14.7440, indicates a higher resistance than the model's predicted AUC of 5.4171. This case was selected due to its large positive prediction error, suggesting that the cell line exhibits a more resistant profile than the model anticipated. The SHAP analysis highlights several molecular features that contribute to this resistance, including specific fingerprint bits and gene expression levels.

## Evidence-Based Interpretation
The observed AUC of 14.7440 for LBH-589 on KARPAS620 is significantly higher than the model's prediction of 5.4171, indicating a more resistant phenotype. The SHAP analysis reveals that several fingerprint bits and gene expression levels are driving the prediction towards lower AUC, which is contrary to the observed higher resistance. Specifically, fingerprint bit `fp_0223` with a SHAP value of -2.4886, `fp_0623` (-0.7250), `TNFRSF12A` (-0.6997), `fp_0362` (-0.5959), `fp_0053` (-0.5671), and `fp_0799` (-0.3937) all push the prediction towards lower AUC, suggesting relative sensitivity. However, the observed resistance suggests that other factors not captured by the model may be contributing to the higher AUC.

## Feature and Neighborhood Analysis
The top TreeSHAP features indicate that fingerprint bits `fp_0223`, `fp_0623`, `fp_0362`, `fp_0053`, and `fp_0799` are associated with relative sensitivity, pushing the prediction towards lower AUC. These fingerprint bits are present in a small percentage of compounds and are associated with specific SMARTS patterns. For instance, `fp_0223` is linked to the SMARTS pattern `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`, found in compounds like gossypol, cytochalasin B, and erastin. Gene expression of `TNFRSF12A` also contributes to the prediction of lower AUC, with a SHAP value of -0.6997, indicating below-average expression levels.

In the drug cohort context, LBH-589 has a mean AUC of 5.3007, placing the KARPAS620 response at the 99.5th percentile, indicating extreme resistance. In the cell cohort context, KARPAS620 has a mean AUC of 14.4543, placing the LBH-589 response at the 55.4th percentile, suggesting moderate resistance within the cell line.

---

## RPT-0016 - ceranib-2 on SNU398
_Source evidence: SHAP-0016_

## Executive Summary
The response of SNU398, a hepatocellular carcinoma cell line, to ceranib-2 was exceptionally sensitive, with an observed AUC of 0.9898, significantly lower than the model-predicted AUC of 13.0950. This large negative prediction error indicates that the cell line is more sensitive to ceranib-2 than predicted by the model. The SHAP analysis reveals that fingerprint features and gene expression levels contribute to the model's prediction, with some features pushing toward higher AUC (resistance) and others toward lower AUC (sensitivity).

## Evidence-Based Interpretation
The observed AUC of 0.9898 for ceranib-2 on SNU398 is exceptionally low, indicating high sensitivity. The model predicted an AUC of 13.0950, which is much higher, suggesting a significant discrepancy between the observed and predicted responses. The SHAP analysis identifies several key features influencing the model's prediction. Fingerprint bit `fp_0443` and gene expression of `TNFRSF12A` push the prediction toward higher AUC (resistance), while fingerprint bits `fp_0227`, `fp_0362`, and `fp_1009` push the prediction toward lower AUC (sensitivity). These features collectively contribute to the model's prediction, but the observed response is much more sensitive than predicted.

## Feature and Neighborhood Analysis
The top SHAP features influencing the model's prediction include fingerprint bits and gene expression levels. Fingerprint bit `fp_0443` with a SHAP value of +0.3525 and `TNFRSF12A` with a SHAP value of +0.2492 both push the prediction toward higher AUC (resistance). Conversely, fingerprint bits `fp_0227` (-0.1804), `fp_0362` (-0.1707), and `fp_1009` (-0.1700) push the prediction toward lower AUC (sensitivity). The presence of these fingerprint bits in a small percentage of compounds suggests they are specific to certain chemical structures. For instance, `fp_0443` is present in 0.4% of compounds, while `fp_0227` is present in 6.7%. The gene expression of `TNFRSF12A` is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

## Model-Level Context
The model's training diagnostics indicate a moderate fit with a training R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a maximum depth of 20 and 100 estimators, achieving an R² of 0.6648. The global fingerprint features `fp_0443`, `fp_0

---

## RPT-0017 - LBH-589 on 253JBV
_Source evidence: SHAP-0017_

## Executive Summary

The response of the 253JBV cell line to LBH-589, an inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8, is exceptionally resistant relative to both the model prediction and cohort baselines. The observed AUC of 20.4490 is significantly higher than the model-predicted AUC of 11.2021, indicating a large positive prediction error of +9.2469. This places the sample at the 100th percentile in the drug cohort and the 99.4th percentile in the cell cohort, highlighting its unique resistance profile.

## Evidence-Based Interpretation

The observed resistance of 253JBV to LBH-589 is driven by several key features identified through TreeSHAP analysis. The most influential feature, fingerprint bit `fp_0223`, is associated with a representative SMARTS pattern `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]` and pushes the prediction toward lower AUC (relative sensitivity). However, the presence of this feature in the compound does not align with the observed resistance, suggesting other factors are at play. Gene expression features, particularly PLK2 and TNFRSF12A, contribute significantly to the prediction of higher AUC (relative resistance). PLK2, with a z-score of +1.69, and TNFRSF12A, with a z-score of +0.62, both push the prediction toward higher AUC, indicating their role in the observed resistance.

## Feature and Neighborhood Analysis

The top TreeSHAP features include fingerprint bits and gene expressions. Fingerprint bit `fp_0223` is present in only 1.2% of CTRPv2 compounds and is associated with compounds like gossypol, cytochalasin B, and erastin. Despite its association with relative sensitivity, the presence of this feature does not mitigate the observed resistance. Gene expression features PLK2 and TNFRSF12A, which are above and near the cross-cell-line mean respectively, contribute to the prediction of higher AUC. These genes recur in multiple predictable-drug RF signatures, with PLK2 appearing in 102 signatures and TNFRSF12A in 166 signatures. Other fingerprint bits, such as `fp_0362`, `fp_0623`, and `fp_0902`, also push the prediction toward lower AUC but do not counterbalance the influence of the gene expression features.

## Model-Level Context

The Random Forest model used for prediction has been trained on a dataset with 311,258 samples and 2024 features, achieving a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration has a

---

## RPT-0018 - foretinib on EBC1
_Source evidence: SHAP-0018_

## Executive Summary
The response of the EBC1 cell line to foretinib, an inhibitor of MET and VEGFR2, is exceptionally sensitive, with an observed AUC of 0.8572, which is significantly lower than the model-predicted AUC of 12.9169. This sensitivity is notable given the global mean AUC of 12.8580 and the local drug cohort context where the median AUC is 10.5290. The SHAP analysis highlights key features that contribute to this sensitivity, including specific fingerprint bits and gene expression levels.

## Evidence-Based Interpretation
The EBC1 cell line, derived from squamous cell carcinoma of the lung, exhibits an exceptionally sensitive response to foretinib, as indicated by the observed AUC of 0.8572. This sensitivity is much lower than the model's prediction of 12.9169, suggesting that the cell line is more responsive to the drug than anticipated. The SHAP analysis reveals that several features contribute to this sensitivity, including fingerprint bits and gene expression levels.

### SHAP Evidence
The top TreeSHAP features influencing the prediction include:
1. **TNFRSF12A**: This gene expression level pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.1686. However, the overall prediction is still skewed towards sensitivity due to other contributing factors.
2. **fp_0227**: This fingerprint bit, representing the SMARTS `[#8]-[#6@H]`, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.1640.
3. **fp_0728**: Another fingerprint bit, representing the SMARTS `Br`, also pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0929.
4. **fp_0521**: This fingerprint bit, representing the SMARTS `[#6]-[#6](=[#8])-[#8]-[#6@H]`, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0710.
5. **fp_0806**: This fingerprint bit, representing the SMARTS `[#6]:[#7]:[#6]`, pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.0704.
6. **fp_0062**: This fingerprint bit, representing the SMARTS `[#6]-[#6](:[#6]):[#16]`, pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.0651.

### Metadata Grounding
The gene TNFRSF12A is recurrent in 166 predictable-drug RF signatures, indicating its importance in drug response prediction. The fingerprint bits fp_0227, fp_0728, fp_0521, fp_0806, and fp_

---

## RPT-0019 - 1S,3R-RSL-3 on CAL62
_Source evidence: SHAP-0019_

## Executive Summary

The response of CAL62, an anaplastic carcinoma cell line derived from thyroid tissue, to the drug 1S,3R-RSL-3 was observed to be more resistant than the model predicted. The observed AUC of 18.6380 is significantly higher than the model's predicted AUC of 9.6448, indicating a substantial positive prediction error of +8.9932. This case is notable for its large positive prediction error, placing it at the 100th percentile within the drug cohort and the 98.3rd percentile within the cell cohort.

## Evidence-Based Interpretation

The TreeSHAP analysis reveals that the observed resistance of CAL62 to 1S,3R-RSL-3 is influenced by several molecular features. The most significant contributors are fingerprint bits that generally push the prediction toward lower AUC (relative sensitivity). Specifically, fingerprint bit `fp_0204` with a SHAP value of -1.7674, `fp_0271` with a SHAP value of -0.8043, and `fp_1017` with a SHAP value of -0.3293, all contribute to a more sensitive prediction. Conversely, the expression level of the gene TNFRSF12A (51330) pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3501.

## Feature and Neighborhood Analysis

The fingerprint bit `fp_0204` is characterized by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, which is present in only 2.9% of CTRPv2 compounds. This feature is associated with compounds like BRD-K26531177, NVP-BEZ235, and CD-437, suggesting a rare structural motif that may confer sensitivity. Similarly, `fp_0271` with SMARTS `[#7]-[#6](:[#6]):[#6]` is present in 5.0% of compounds and is linked to drugs such as trifluoperazine and prochlorperazine. The presence of these fingerprint bits in 1S,3R-RSL-3 likely contributes to its sensitivity profile in CAL62.

In contrast, the gene TNFRSF12A, which is expressed at a level near the cross-cell-line mean, is associated with resistance. This gene recurs in 166 predictable-drug RF signatures, indicating its importance in the model's resistance predictions.

## Model-Level Context

The Random Forest model used for prediction has a training fit characterized by an R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061, based on 311,258 samples and 2,024 features. The model's performance is optimized with a maximum depth of 20

---

## RPT-0020 - PHA-793887 on SNU398
_Source evidence: SHAP-0020_

## Executive Summary
The response of SNU398, a hepatocellular carcinoma cell line, to PHA-793887, an inhibitor of cyclin-dependent kinases, is exceptionally sensitive compared to the model prediction and cohort baselines. The observed AUC of 1.5525 is significantly lower than the predicted AUC of 13.5394, indicating a large negative prediction error of -11.9869. This sensitivity is further supported by the cell line's position at the 1.1th percentile in its cohort and the drug's position at the 0.1th percentile in its cohort.

## Evidence-Based Interpretation
The observed response of SNU398 to PHA-793887 is characterized by an exceptionally low AUC of 1.5525, indicating high sensitivity. The RF model predicted a much higher AUC of 13.5394, resulting in a significant negative prediction error. This suggests that the model underestimates the sensitivity of SNU398 to PHA-793887.

## Feature and Neighborhood Analysis
The top TreeSHAP features influencing the prediction are:
1. **fp_0443**: A fingerprint bit representing the SMARTS `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, which pushes the prediction toward higher AUC (relative resistance). This feature is present in 0.4% of CTRPv2 compounds and is associated with drugs like nilotinib and bleomycin A2.
2. **TNFRSF12A (51330)**: Gene expression of TNFRSF12A, which also pushes the prediction toward higher AUC (relative resistance). The gene expression value is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
3. **fp_1009**: A fingerprint bit representing the SMARTS `[#6]-[#6](:[#6]):[#6]`, which pushes the prediction toward lower AUC (relative sensitivity). This feature is present in 9.1% of CTRPv2 compounds and is associated with drugs like betulinic acid, isoliquiritigenin, and curcumin.
4. **fp_0367**: A fingerprint bit representing the SMARTS `[#6]:[#6](-[#6]):[#6]`, which pushes the prediction toward higher AUC (relative resistance). This feature is present in 6.4% of CTRPv2 compounds and is associated with drugs like betulinic acid, gossypol, and simvastatin.
5. **fp_0623**: A fingerprint bit representing the SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, which pushes the prediction toward lower AUC (relative sensitivity). This feature is present in 5.8% of CTRPv2 compounds and is associated with drugs

---

## RPT-0021 - KU-0063794 on SKMEL2
_Source evidence: SHAP-0021_

## Executive Summary

The response of SKMEL2, a malignant melanoma cell line, to KU-0063794, an mTOR inhibitor, is exceptionally resistant compared to both the model prediction and cohort baselines. The observed AUC of 21.2320 is significantly higher than the predicted AUC of 12.2996, indicating a large positive prediction error of +8.9324. This resistance is further highlighted by the sample's position at the 100th percentile in the drug cohort and 99.5th percentile in the cell cohort.

## Evidence-Based Interpretation

The observed response of SKMEL2 to KU-0063794 is characterized by a high AUC, indicating resistance. The model predicts a lower AUC, suggesting a misprediction of sensitivity. The SHAP analysis reveals that several molecular features contribute to this resistance. The top SHAP features include fingerprint bits and gene expression levels. Specifically, the fingerprint bit `fp_0202` with a SHAP value of -0.4209 and `TNFRSF12A` gene expression with a SHAP value of +0.1665 are key contributors. The fingerprint bit `fp_0202` is associated with a chemical structure `[#6]:[#6](-[#8]):[#6]`, which is present in 7.3% of compounds and is linked to compounds like gossypol, teniposide, and epigallocatechin-3-monogallate. The `TNFRSF12A` gene expression, near the cross-cell-line mean, is associated with 166 predictable-drug RF signatures and pushes the prediction toward higher AUC (resistance).

## Feature and Neighborhood Analysis

The SHAP analysis identifies several fingerprint bits that push the prediction toward lower AUC (sensitivity), including `fp_0202`, `fp_0623`, `fp_0227`, `fp_0771`, and `fp_0722`. These bits represent specific chemical structures such as `[#6]:[#6](-[#8]):[#6]`, `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, `[#8]-[#6@H]`, `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`, and `[#6]:[#6](:[#16])-[#6](=[#8])-[#7]-[#6]`. Each of these structures is present in a small percentage of compounds and is associated with various drugs. The `TNFRSF12A` gene expression, with a SHAP value of +0.1665, is the only feature pushing the prediction toward higher AUC (resistance).

## Model-Level Context

The model's performance is characterized by a training fit with an R2 of 0.4928, RM

---

## RPT-0022 - BRD-K99006945 on JHUEM1
_Source evidence: SHAP-0022_

## Executive Summary

The response of BRD-K99006945 on the JHUEM1 cell line, derived from an endometrial adenocarcinoma, is characterized by an exceptionally sensitive phenotype with an observed AUC of 1.5813, significantly lower than the model-predicted AUC of 13.5611. This large negative prediction error indicates that the cell line is more sensitive to the drug than predicted by the model. The drug's response is also notably lower than the global mean AUC of 12.8580 and the local cell cohort mean AUC of 12.2365.

## Evidence-Based Interpretation

The observed AUC of 1.5813 for BRD-K99006945 on JHUEM1 is exceptionally low, indicating a highly sensitive response. The model-predicted AUC of 13.5611 suggests a much higher resistance, leading to a significant negative prediction error of -11.9798. This discrepancy highlights the cell line's unexpected sensitivity to the drug.

## Feature and Neighborhood Analysis

The top TreeSHAP features contributing to the model's prediction are primarily pushing toward higher AUC (relative resistance). However, the observed response is much lower, indicating sensitivity.

1. **TNFRSF12A (51330)**: This gene expression feature has a SHAP value of +0.1896, pushing the prediction toward higher AUC (resistance). The gene expression value is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.
2. **fp_0367**: This fingerprint bit, representing the SMARTS `[#6]:[#6](-[#6]):[#6]`, has a SHAP value of +0.1308, also pushing toward higher AUC (resistance). It is present in 6.4% of CTRPv2 compounds, with example drugs including betulinic acid, gossypol, and simvastatin.
3. **fp_0204**: Another fingerprint bit, with SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, has a SHAP value of +0.1090, contributing to higher AUC (resistance). It is present in 2.9% of CTRPv2 compounds, with example drugs such as BRD-K26531177, NVP-BEZ235, and CD-437.
4. **fp_0623**: With SMARTS `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, this fingerprint bit has a SHAP value of +0.0909, pushing toward higher AUC (resistance). It is present in 5.8% of CTRPv2 compounds, with example drugs like trif

---

## RPT-0023 - SCH-529074 on MESSA
_Source evidence: SHAP-0023_

## Executive Summary

The response of MESSA (a soft tissue sarcoma cell line) to SCH-529074, an activator of mutant p53, is exceptionally resistant relative to both the model prediction and cohort baselines. The observed AUC of 22.3390 is significantly higher than the predicted AUC of 13.4876, indicating a large positive prediction error of +8.8514. This places the sample at the 100th percentile in both the drug and cell line cohorts, highlighting its unique resistance profile.

## Evidence-Based Interpretation

The observed resistance of MESSA to SCH-529074 is driven by several key features identified through TreeSHAP analysis. The top contributing features include fingerprint bits and gene expression levels that push the prediction toward higher AUC (relative resistance). Specifically, fingerprint bit `fp_0443` with a SHAP value of +0.3470, and gene expression of `TNFRSF12A` with a SHAP value of +0.2027, are significant contributors to the predicted resistance. Additionally, fingerprint bits `fp_0367` and `fp_0204` also contribute positively to the resistance prediction, with SHAP values of +0.1125 and +0.0686, respectively. Conversely, fingerprint bit `fp_1009` with a SHAP value of -0.1453 and `fp_0062` with a SHAP value of -0.0489 push the prediction toward lower AUC (relative sensitivity).

## Feature and Neighborhood Analysis

The fingerprint bit `fp_0443` is associated with the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, which is present in only 0.4% of CTRPv2 compounds, including nilotinib and bleomycin A2. This feature is highly specific and contributes significantly to the resistance prediction. Gene expression of `TNFRSF12A` is near the cross-cell-line mean but recurs in 166 predictable-drug RF signatures, suggesting its importance in the model. Fingerprint bit `fp_1009` with the SMARTS pattern `[#6]-[#6](:[#6]):[#6]` is present in 9.1% of compounds, including betulinic acid, isoliquiritigenin, and curcumin, and pushes the prediction toward sensitivity. Other fingerprint bits like `fp_0367` and `fp_0204` also contribute to resistance, while `fp_0062` with the SMARTS pattern `[#6]-[#6](:[#6]):[#16]` pushes toward sensitivity.

## Model-Level Context

The Random Forest model used for prediction has a training fit with R2 of 0.4928, RMSE of 1.8342, and correlation of 0

---

## RPT-0024 - KX2-391 on SNU16
_Source evidence: SHAP-0024_

## Executive Summary

The response of KX2-391 on the SNU16 cell line, characterized by an observed AUC of 1.4980, indicates exceptional sensitivity compared to the model-predicted AUC of 13.1396. This large negative prediction error suggests that the model underestimates the sensitivity of SNU16 to KX2-391. The SHAP analysis reveals key features influencing the prediction, including fingerprint bits and gene expression levels, which push the prediction towards higher AUC (resistance) or lower AUC (sensitivity).

## Evidence-Based Interpretation

The observed AUC of 1.4980 for KX2-391 on SNU16 is significantly lower than the model-predicted AUC of 13.1396, indicating that SNU16 is exceptionally sensitive to KX2-391. This sensitivity is further supported by the drug cohort context, where the sample percentile is 0.3, and the cell cohort context, where the sample percentile is 2.5, both suggesting a lower-than-average AUC.

## Feature and Neighborhood Analysis

The top TreeSHAP features influencing the prediction include fingerprint bits and gene expression levels. Fingerprint bit `fp_0443` with a SHAP value of +0.2984 and `TNFRSF12A` gene expression with a SHAP value of +0.2193 push the prediction toward higher AUC (relative resistance). Conversely, fingerprint bits `fp_0706` (-0.2036) and `fp_1009` (-0.1539) push the prediction toward lower AUC (relative sensitivity). These features are grounded in the local metadata, such as SMARTS annotations and gene recurrence counts, which provide context for their presence and influence.

## Model-Level Context

The model's training diagnostics indicate a moderate fit with a train R2 of 0.4928, train RMSE of 1.8342, and train correlation of 0.7061. The best-performing model configuration has a max depth of 20 and 100 estimators, achieving an R2 of 0.6648. The global model context shows that fingerprint bits like `fp_0443` and `fp_0806` are among the top features, and genes like `TNFRSF12A` recur in multiple predictable drug models. However, these diagnostics are specific to the training set and do not reflect held-out generalization performance.

## Confidence and Caveats

The SHAP analysis provides insights into the model's prediction but does not directly explain biological mechanisms. The large negative prediction error suggests that the model underestimates the sensitivity of SNU16 to KX2-391. The SHAP values indicate that fingerprint bits and gene expression levels play significant roles in the prediction, but the biological implications of these features are not directly inferred. The model's performance metrics are based on

---

## RPT-0025 - ouabain on TUHR10TKB
_Source evidence: SHAP-0025_

## Executive Summary
The case of ouabain on the TUHR10TKB cell line (kidney carcinoma) shows an exceptionally resistant response with an observed AUC of 29.35, significantly higher than the model-predicted AUC of 20.62. This resistance is notable given the cell line's position at the 100th percentile in both the drug and cell cohort contexts, indicating a highly resistant profile compared to other samples. The primary drivers of this resistance include high gene expression levels of CSF1, SDC4, COL18A1, and TNFRSF12A, as well as specific molecular fingerprints associated with the drug structure.

## Evidence-Based Interpretation
The observed AUC of 29.35 for ouabain on TUHR10TKB is markedly higher than the model-predicted AUC of 20.62, indicating a significant deviation towards higher resistance. The SHAP analysis reveals that several features contribute to this resistance. CSF1, with a SHAP value of +1.0870, is the most influential feature, pushing the prediction towards higher AUC. Other significant contributors include fingerprint bits fp_0009 (+0.9989) and fp_0443 (+0.5723), which also indicate resistance. Gene expressions of SDC4 (+0.4625), COL18A1 (+0.3655), and TNFRSF12A (+0.1918) further reinforce the resistance profile.

## Feature and Neighborhood Analysis
The SHAP analysis highlights that CSF1, a gene involved in macrophage activation and tumor progression, is markedly above the cross-cell-line mean and recurs in 13 predictable-drug RF signatures, contributing significantly to the resistance. Fingerprint bit fp_0009, representing the SMARTS pattern `[#6]-[#6](=[#8])-[#6]`, is present in 3.3% of CTRPv2 compounds and is associated with drugs like IC-87114, sorafenib, and SNX-2112. Similarly, fp_0443, with the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, is present in 0.4% of compounds and linked to nilotinib and bleomycin A2. Gene expressions of SDC4, COL18A1, and TNFRSF12A, all above the cross-cell-line mean, further support the resistance profile.

## Model-Level Context
The model used for prediction is a Random Forest (RF) with a max depth of 20 and 100 estimators, achieving a cross-validated R2 of 0.6648 on the training set. However, the per-drug cross-validated predictability for ouabain is relatively low (R2=0.1544), indicating limited generalizability for this specific drug. The global model context

---
