# Model Comparison

This file collates the generated markdown reports for each model.

## Summary

The heuristic score below is a rough quality indicator based on section coverage, output length, and repetition. Higher is better.

| Model | Reports | Avg Words | Heading Coverage | Unique-Line Ratio | Heuristic Score | Note |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Meta-Llama-3.1-8B-Instruct | 25/25 | 373.8 | 0.83 | 1.00 | 83.2 | usable |
| Qwen2.5-32B-Instruct | 25/25 | 365.0 | 0.70 | 1.00 | 69.6 | usable |
| gpt-oss-20b | 25/25 | 194.8 | 0.18 | 1.00 | 9.7 | weak format following |
| BioMistral-7B | 25/25 | 6.6 | 0.10 | 1.00 | 0.1 | weak format following |
| Meditron-7b | 25/25 | 83.3 | 0.00 | 0.96 | 0.0 | weak format following |

## Models Present
- Meta-Llama-3.1-8B-Instruct
- Qwen2.5-32B-Instruct
- gpt-oss-20b
- BioMistral-7B
- Meditron-7b

## RPT-0001 - cytarabine hydrochloride on SKMEL2

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0001
- observed_auc: 27.1820
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: skin / malignant melanoma
- model_predicted_auc: 13.5949
- prediction_error: +13.5871
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=6, headings=0.00)
# Case Report: cytarabine hydrochloride on SKMEL2

### Meditron-7b (score=0.0, words=75, headings=0.00)
---
title: "Predictive Model Results"
date: "2021-09-01T00:00:01Z"
output: html_document
---

<h1>Predictive Model Summary</h1><br/>

<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th colspan="2"><strong>Model Metrics</strong></th>
    </tr>
  </thead>
  <tbody>
    <td>
      <img src="https://user-images.githubusercontent.com/1011101/131111411-cbeeeb0e-27ba-44bd-ad5b-11555550175e.png"/>
    </td>
    <tbody>
      <tr>
        <td>
          <em>n_samples</em>: number of samples used by the model during fitting or evaluation
        </td>

### Meta-Llama-3.1-8B-Instruct (score=60.0, words=320, headings=0.60)
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

### Qwen2.5-32B-Instruct (score=60.0, words=375, headings=0.60)
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

### gpt-oss-20b (score=9.6, words=120, headings=0.20)
## Executive Summary  
The cytarabine hydrochloride assay on the melanoma cell line **SKMEL2** yielded an observed AUC of **27.18**, markedly higher than the Random Forest (RF) model prediction of **13.59** and the cohort baselines (drug mean ≈ 11.63, cell mean ≈ 14.22). This indicates an exceptionally resistant phenotype relative to both the model and the broader drug‑cell population. The large positive prediction error (+13.59) is driven by a combination of fingerprint features that collectively bias the RF toward higher AUC predictions.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The observed AUC exceeds the model’s prediction by 13.59 units, placing SKMEL2 in the 100th percentile of the drug cohort and the 100th percentile of the cell cohort

---

## RPT-0002 - birinapant on KYM1

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0002
- observed_auc: 0.6877
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: soft tissue / rhabdomyosarcoma
- model_predicted_auc: 13.8762
- prediction_error: -13.1885
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=7, headings=0.00)
# Case Report: Birinapant on KYM1 (RPT-0002)

### Meditron-7b (score=0.0, words=79, headings=0.00)
---
title: "Grounded report"
output: html_document
---

<h1>Grounded report</h1><br/>

<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th colspan="2"><i>Model parameters</i></th>
    </tr>
    <tbody>
      <tr>
        <td>Parameter name</td>
        <cdf_colgroup class="justify-content-between justify-items-center">
          <cdf_column width="auto" align="left">Value</cdf_column>
          <c df_column width="10em" align="right">Units</cdf_ column>
        </cdf_col group>
      </tr>
      <row>
        <varlist itemized>
          <varlistitem label="Max depth">max_depth</varlistitem>
          <value>20</value>
        </varlist>
        <value>n_estimators</value

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=355, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=361, headings=0.80)
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

### gpt-oss-20b (score=5.5, words=69, headings=0.20)
## Executive Summary  
The soft‑tissue rhabdomyosarcoma cell line **KYM1** was treated with the SMAC mimetic **birinapant** (drug ID 660778). The observed area‑under‑curve (AUC) was **0.6877**, markedly lower than the random‑forest (RF) model prediction of **13.8762** and the global mean AUC of **12.8580**. This 13.2‑unit negative prediction error places KYM1 in the lowest 0.1 % of the drug cohort and 0.2

---

## RPT-0003 - nilotinib on BT549

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0003
- observed_auc: 23.7050
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: breast / carcinoma
- model_predicted_auc: 13.4663
- prediction_error: +10.2387
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=7, headings=0.00)
# Case Report: RPT-0003 - Nilotinib on BT549

### Meditron-7b (score=0.0, words=93, headings=0.00)
---
title: "Nilotinib"
description: "Prediction of nilotinib's activity against breast cancer cells."
author: <NAME>
date: 2021-09-01
output: html_document
tags:
- machine learning
- pharmacogenetics
- precision medicine
- chemotherapy
- breast neoplasms
- molecular profiling
- genomics
- biomedical informatics
- computational biology
- bioinformatics
- oncology
- drug repurposing
- drug repositioning
- drug discovery
- drug development
- drug screening
- drug safety
- drug efficacy
- drug combinations
- drug synergy
- drug combination therapy
- drug resistance
- drug resistance mechanisms
- drug metabolism
- drug metabolisminduced adverse effects
- drug metablism-induced side effects
- drug interactions
- drug-drug interactions
- drug toxicity
- drug tolerance
- drug dosage
- drug dose optimization
- drug formulation
- drug delivery

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=405, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=60.0, words=348, headings=0.60)
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

### gpt-oss-20b (score=5.3, words=66, headings=0.20)
## Executive Summary  
Nilotinib exhibited an observed AUC of **23.71** in the BT549 breast ductal carcinoma cell line, markedly higher than the RF‑predicted AUC of **13.47** and the cohort mean of **13.96**. This indicates an unusually resistant phenotype relative to both the drug’s overall CTRPv2 performance and the BT549 cell line baseline. The model’s positive prediction error (+10.24) reflects this

---

## RPT-0004 - N9-isopropylolomoucine on CADOES1

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0004
- observed_auc: 0.0835
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: bone / Ewings sarcoma peripheral primitive neuroectodermal tumor
- model_predicted_auc: 12.5703
- prediction_error: -12.4868
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=9, headings=0.00)
# Executive Summary: Case RPT-0004 - N9-isopropylolomoucine on CADOES1

### Meditron-7b (score=0.0, words=70, headings=0.00)
---
title: "N9-Isopropylolmoucine"
description: "Performance on the CTRPv1 dataset."
output: html_document
header-includes:
  - \usepackage{booktabs}
  - \begin{tabular}{@{}l@{}}
      <NAME>, <NAME>
    \end{tabular}
  - inset: {fontsize: large, fontfamily:"Times New Roman"}
  - \section*{References}
  - [<NAME>, <NAME>.](https://www.ncbi.nlm.nih.gov/pubmed/?term=%22Gonzalez-Angulo,%20Alvaro%20J%22%5BAuthor:%22Gonza%C3%Alez-Angulo%2C%20A.%22%20AND%22Gonzelez-Angulo,% 20A.J.%22%)
  - [GonzalezAJ, Alvaro J.]. (n.d.). PubMed. Retrieved April 1, 2

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=385, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=378, headings=0.80)
## Executive Summary

The response of CADOES1, a bone-derived Ewing's sarcoma peripheral primitive neuroectodermal tumor cell line, to N9-isopropylolomoucine was exceptionally sensitive, with an observed AUC of 0.0835. This sensitivity is significantly lower than the model-predicted AUC of 12.5703, indicating a large negative prediction error of -12.4868. The observed AUC places the sample in the 0.1 percentile among the drug cohort and the 1.9 percentile among the cell cohort, highlighting its unique sensitivity to the drug.

## Evidence-Based Interpretation

The observed response of CADOES1 to N9-isopropylolomoucine is characterized by a highly sensitive phenotype, as evidenced by the low observed AUC of 0.0835. This sensitivity is notably lower than the model-predicted AUC of 12.5703, indicating that the cell line is much more sensitive to the drug than the model anticipated. The large negative prediction error suggests that the model underestimates the sensitivity of CADOES1 to N9-isopropylolomoucine.

## Feature and Neighborhood Analysis

The top TreeSHAP features contributing to the prediction include gene expression and molecular fingerprint bits. The most significant feature is TNFRSF12A (gene expression), which pushes the prediction toward lower AUC (relative sensitivity) with a SHAP value of -0.6577. This gene is below the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, suggesting its importance in the model's prediction.

Fingerprint bits such as fp_0227 and fp_0204 push the prediction toward higher AUC (relative resistance), with SHAP values of +0.0985 and +0.0901, respectively. These bits are associated with specific SMARTS patterns and are present in a small percentage of CTRPv2 compounds. Conversely, fingerprint bits like fp_0062 and fp_0538 push the prediction toward lower AUC (relative sensitivity), with SHAP values of -0.0887 and -0.0829, respectively.

## Model-Level Context

The model's training diagnostics indicate a moderate fit with a training R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a max depth of 20 and 100 estimators, achieving an R² of 0.6648. The most common genes across predictable per-drug models include TNFRSF12A, MYOF, SDC4, PRSS23, LAMB2, GPRC5A, IKZF1, and ITGA3. For N9-isopropylolomoucine, the cross-validated predictability is relatively low with an R² of 0.

### gpt-oss-20b (score=0.0, words=355, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use the provided data. Must not invent pathways. Must not give clinical advice. Must separate local evidence from global diagnostics. Must treat train diagnostics as training fit only. Must not mention training diagnostics in local interpretation. Must not mention "clinical" or "treatment". Must not mention "cancer" or "tumor"? The prompt says not to give clinical advice. But we can mention the cell line and tissue. It's okay.

We need to incorporate the sample context: observed AUC 0.0835, predicted 12.5703, difference -12.4868, meaning observed is much lower (more sensitive). The cohort baselines: drug cohort mean 12.9659, cell cohort mean 11.3701. So the observed is far below both. So we interpret as exceptionally sensitive relative to predictions and baselines.

SHAP evidence: list top features with direction. Provide explanation: TNFRSF12A pushes toward lower AUC (sensitivity) with shap -0.6577. fp_0227 pushes toward higher AUC (resistance) +0.0985. fp_0204 pushes toward higher AUC +0.0901. fp_0062 pushes toward lower AUC -0.0887. fp_0538 pushes toward lower AUC -0.0829. fp_0504 pushes toward higher AUC +0.0438. Summarize net effect: negative contributions outweigh positive? Let's sum: negative: -0.6577 -0.0887 -0.0829 = -0.8293. Positive: +0.0985 +0.0901 +0.0438 = +0.2324. Net -0.5969. So overall pushes toward lower AUC (sensitivity). That aligns with observed.

Metadata grounding: gene recurrence counts: TNFRSF12A appears in 166 drugs. Fingerprint SMARTS: fp_0227 SMARTS [#8]-[#6@H], present in 6.7% of compounds. fp_0204 SMARTS [#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6], present 2.9%. fp_0062 SMARTS [#6]-[#6](:[#6]):[#16], present 3.7%. fp_0538 SMARTS [#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6], present 0.6%. fp_0504 SMARTS [#6]:[#6](=[#8]):[#7], present 4.4%. Provide examples of drugs with same fingerprints. Provide same-drug cohort examples: CAL78, SNU1079, BEN, NCIH1184. Provide same-cell cohort examples: leptomy

---

## RPT-0005 - GSK461364 on MC116

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0005
- observed_auc: 17.4070
- interpretation: more resistant than the model predicted
- tissue / histology: haematopoietic and lymphoid tissue / lymphoid neoplasm
- model_predicted_auc: 7.3230
- prediction_error: +10.0840
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=122, headings=0.00)
---
title: "Report - GSK463164"
author: <NAME>
date: 2021-09-01T19:00:00+00:01
output: html_document
---

<h1 id="report">Report</h1><br/>

<div class="figure"><img src="/figures/report/GSK4613.png"></div><br/>
<div class = "caption">
    <b>Figure 1.</b>
    <i>The figure shows the distribution of the area under the curve (AUC) values from the random forest predictions on the test set for each drug in the dataset. The red line indicates the average AUC value over all drugs in the dataset. Drugs that are below this line have an overall higher probability to be active against cancer cells compared to those above it.</i>
</div><br/><br/>


<h2 id="model">Model</h2><br/>
<!--
<table border="1" style="width: 100%; margin-left

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=374, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=384, headings=0.80)
## Executive Summary
The observed response of GSK461364 on MC116 indicates a higher resistance than predicted by the model, with an observed AUC of 17.4070 compared to a predicted AUC of 7.3230. This case is selected due to its large positive prediction error, suggesting the cell line is more resistant than anticipated. The SHAP analysis reveals that fingerprint features and gene expressions contribute significantly to this prediction, with specific chemical structures and gene expression levels pushing the prediction towards higher or lower AUC values.

## Evidence-Based Interpretation
The observed AUC of 17.4070 for GSK461364 on MC116 is notably higher than the model's prediction of 7.3230, indicating a more resistant phenotype than expected. The SHAP analysis identifies several key features that influence this prediction. Fingerprint bits `fp_0504` and `fp_0443`, which are associated with chemical structures `[#6]:[#6](=[#8]):[#7]` and `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, respectively, both push the prediction towards lower AUC values, suggesting relative sensitivity. However, the observed AUC is still high, implying other factors may be at play. Gene expression levels of `TNFRSF12A` also push the prediction towards lower AUC, while `SYTL2` pushes it towards higher AUC, contributing to the overall resistance profile.

## Feature and Neighborhood Analysis
The top TreeSHAP features indicate that fingerprint bits `fp_0504` and `fp_0443` are significant contributors to the prediction, both pushing towards lower AUC values. These features are present in a small percentage of compounds, with `fp_0504` found in 4.4% and `fp_0443` in 0.4% of CTRPv2 compounds. The gene expression of `TNFRSF12A` is below the cross-cell-line mean and recurs in 166 predictable-drug RF signatures, further supporting sensitivity. Conversely, `SYTL2` expression is near the mean and recurs in 84 signatures, pushing towards higher AUC. The same-drug cohort examples show varying sensitivities, while the same-cell cohort examples indicate a range of responses, with some drugs showing high resistance similar to GSK461364.

## Model-Level Context
The model's training diagnostics include a train R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061, reflecting the model's fit to the training data. The best-performing model configuration has a max depth of 20 and 100 estimators, achieving an R2 of 0.6648. Globally, fingerprint features like `fp_0443` and `fp_0504` are significant, aligning with their importance

### gpt-oss-20b (score=0.0, words=424, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Use rules: lower AUC means greater sensitivity; higher AUC means greater resistance. SHAP positive pushes toward higher AUC/resistance; negative pushes toward lower AUC/sensitivity. Provide local evidence separate from global diagnostics. Use training diagnostics only as diagnostics. Provide local case evidence. Provide metadata grounding: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Provide caveats: non-causal, SHAP explains RF prediction not biology directly, separate local case evidence from global training diagnostics.

We have data: observed_auc 17.4070, predicted 7.3230, error +10.0840, global_mean_auc 12.8580. So observed is higher than predicted, meaning more resistant than model predicted. The drug is GSK461364, target PLK1 inhibitor. The cell line MC116 is B cell lymphoma. The drug cohort mean AUC 7.3729, cell cohort mean 13.0759. So the observed AUC is higher than both drug cohort mean and cell cohort mean. So it's more resistant relative to both cohorts.

Now SHAP features: top 5 features. All first four are fingerprint bits pushing toward lower AUC (sensitivity). The fifth gene TNFRSF12A pushes toward lower AUC (sensitivity). Sixth gene SYTL2 pushes toward higher AUC (resistance). So overall, the SHAP contributions: negative contributions from fingerprints and TNFRSF12A, positive from SYTL2. But the net predicted AUC is lower than observed, so the model predicted lower AUC due to negative contributions dominating. The positive contribution from SYTL2 is small (+0.1654). The negative contributions sum to about -5.79? Let's sum: -2.5354 -2.5230 -0.4914 -0.3354 -0.2506 = -6.1368. Add +0.1654 gives -5.9714. So net negative SHAP ~ -5.97, which reduces predicted AUC relative to baseline. Baseline is global mean 12.8580? Actually baseline is global mean AUC? The model predicted 7.3230, which is lower than baseline. So the SHAP contributions explain that.

Now we need to ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Provide that.

Also mention that the drug cohort context: n=770, mean_auc=7.3729, etc. The cell cohort context: n=395, mean_auc=13.0759. So the observed AUC is above both.

Also mention same-drug cohort examples: NB4, SKM1,

---

## RPT-0006 - niclosamide on IALM

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0006
- observed_auc: 0.9043
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: lung / carcinoma
- model_predicted_auc: 13.3307
- prediction_error: -12.4264
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=7, headings=0.00)
## Executive Summary: RPT-0006 - niclosamide on IALM

### Meditron-7b (score=0.0, words=65, headings=0.00)
---
title: "Niclosamide"
description: "Predictive biomarker discovery for niclosamidesensitive NSCLC patients."
author: <NAME>
date: 2021-09-01T12:00:00Z
output:
  html_document:
    fig_caption: true
    keep_tex: false
    latex_knit: false
    toc: true
    toc_depth: 2
    toc-numbers: true
    number_sections: true
    numbers_global: true
    bibliography: default
    bibliography_style: apalike
    bibliography-style: apalikee
    bibliography style: apalikee
    bibliography styles: apalikeee, apalikeeee, apalikee, apalikee, apalike, apalikeff, apalikemm, apalikeme, apalikemi, apalikemo, apalikems, apalikes, apaliket, apalikel, apalikelooo, apal

### Meta-Llama-3.1-8B-Instruct (score=60.0, words=357, headings=0.60)
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

### Qwen2.5-32B-Instruct (score=60.0, words=387, headings=0.60)
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

### gpt-oss-20b (score=10.4, words=130, headings=0.20)
## Executive Summary  
For the lung large‑cell carcinoma line **IALM**, niclosamide produced an observed AUC of **0.9043**, indicating strong sensitivity. The random‑forest (RF) model predicted a much higher AUC of **13.3307**, suggesting resistance. The prediction error of **–12.43** places this case in the lowest 0.1 % of the drug cohort and 0.3 % of the cell cohort, underscoring an unusually sensitive response relative to both cohort baselines and the model’s expectation.

## Evidence‑Based Interpretation  
The RF prediction is driven by a mix of gene‑expression and chemical‑fingerprint features.  
- **TNFRSF12A (51330)** – gene expression value 7.6074, SHAP = +0.2028 → pushes the model toward higher AUC (resistance).  
- **fp_0623** – fingerprint bit present, SHAP = –0.1794 → pushes toward lower AUC (sensitivity).  
- **fp_0771** – SHAP = –0.1178 → sensitivity.  
- **fp_0443** – SHAP

---

## RPT-0007 - pitstop2 on SNU886

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0007
- observed_auc: 23.1410
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: liver / carcinoma
- model_predicted_auc: 13.6419
- prediction_error: +9.4991
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=11, headings=0.00)
## Executive Summary: Case-level Evidence for Pitstop2 Resistance in SNU886 Cells --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Meditron-7b (score=0.0, words=80, headings=0.00)
---
title: "Grounded report"
output: html_document
header-includes:
  include_header:
    components:
      - header-include::cite-paper(citation="'Huang et al., 2020', 'https://doi.org/10.1038/s41598-020-60372-w')")
      - header_includes::cite-package("DEM", package = c("DEM"), version = "1.0.0"))
      - header includes::cite-package ("TreeExplainer", package = c('treeexplainer'), version = "0.14.1"))
      - # Header includes::cite-data("CTRPv1", url = "http://www.broadinstitute.org/~yuehua/datasets/CTRP/CTRP_v1.zip", path = "/home/yuehua/.local/share/data/CTRP")
      - #Header includes::cite-url("https://github.com/YuehuaCh

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=363, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=60.0, words=364, headings=0.60)
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

### gpt-oss-20b (score=15.2, words=190, headings=0.20)
## Executive Summary  
The hepatocellular carcinoma cell line **SNU886** shows an **observed AUC of 23.14** for **pitstop2**, markedly higher than both the drug‑specific cohort (mean ≈ 14.84) and the cell‑specific cohort (mean ≈ 12.74). The random‑forest model predicts an AUC of 13.64, underestimating resistance by **+9.50**. The prediction error is driven largely by features that push the model toward higher AUC, indicating that the model attributes resistance to specific gene expression and chemical substructures present in this sample.

## Evidence‑Based Interpretation  
- **TNFRSF12A (51330)** expression is elevated (value 7.86, z +0.64) and contributes **+0.21** to the predicted AUC, aligning with its recurrence in 166 drug signatures.  
- Three fingerprint bits (**fp_0204**, **fp_0443**, **fp_0367**) are present (value 0) and each adds **+0.08, +0.07, +0.06** respectively, reflecting structural motifs associated with resistance.  
- **fp_0062** is also present but contributes **–0.06**, slightly mitigating the resistance signal.  
- The net SHAP contribution (+0.36) explains the model’s higher predicted AUC relative to the global mean (12.86).

These local signals collectively explain why the model predicts a resistant phenotype for this sample, despite the overall

---

## RPT-0008 - trametinib on DU4475

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0008
- observed_auc: 0.1282
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: breast / carcinoma
- model_predicted_auc: 12.4028
- prediction_error: -12.2746
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=94, headings=0.00)
---
title: "Trametinib"
description: "The top 10 most important features are shown."
output: html_document
header-includes:
  - \usepackage{booktabs}
  - \begin{tabular}{@{}l@{}}
      <NAME>, <NAME>
    \end{tabular}
  - inset: true
  - \section{Background}
    <h2 id="background">Background</h2>
    <div class="highlight"><pre><span></span><code class="sourceText">&lt;!DOCTYPE HTML PUBLIC &quot;&quot;
                       &quot;http://www.w3.org/TR/html4/strict.dtd&gt;</code>&nbsp;<br />
                   &lt;html xmlns=&quot;http://W3C.org/NS/xhtml&quot;&gt;
                     &lt;head&gt;
                         &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot;&gt;&lt;/meta&

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=342, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=361, headings=0.80)
## Executive Summary
The response of trametinib on the DU4475 cell line, characterized by an observed AUC of 0.1282, indicates exceptional sensitivity compared to both the model-predicted AUC of 12.4028 and the cohort baselines. The SHAP analysis reveals that specific molecular features, including fingerprint bits and gene expression levels, contribute significantly to this sensitivity. The model's prediction error of -12.2746 underscores the discrepancy between the observed and predicted responses, highlighting the need for further investigation into the underlying mechanisms.

## Evidence-Based Interpretation
The observed AUC of 0.1282 for trametinib on DU4475 is exceptionally low, indicating high sensitivity to the drug. This is in stark contrast to the model-predicted AUC of 12.4028, which suggests a much higher resistance. The SHAP analysis identifies several key features that contribute to this sensitivity. The top contributing feature is fingerprint bit `fp_0367`, which has a SHAP value of -0.2979, indicating a strong push toward lower AUC (relative sensitivity). Other significant contributors include gene expression of `TNFRSF12A` and fingerprint bits `fp_0409`, `fp_0062`, and `fp_1008`, all of which also push the prediction toward lower AUC.

## Feature and Neighborhood Analysis
The fingerprint bit `fp_0367` with SMARTS `[#6]:[#6](-[#6]):[#6]` is present in 6.4% of CTRPv2 compounds and is associated with drugs like betulinic acid, gossypol, and simvastatin. This feature significantly contributes to the model's prediction of lower AUC, suggesting a structural characteristic that enhances trametinib's sensitivity in DU4475. Gene expression of `TNFRSF12A` at a value of 4.5098 (near the cross-cell-line mean) is another key factor, supporting sensitivity in 166 predictable-drug RF signatures. Fingerprint bits `fp_0409`, `fp_0062`, and `fp_1008` also contribute to lower AUC predictions, with SMARTS patterns `[#7]-[#6](:[#7]):[#7]`, `[#6]-[#6](:[#6]):[#16]`, and `[#7]-[#6](:[#7]:[#6]):[#7]:[#6]`, respectively.

## Model-Level Context
The model's training diagnostics indicate a moderate fit with a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a max depth of 20 and 100 estimators, achieving an R2 of 0.6648. The global fingerprint features and gene signatures suggest that while `

### gpt-oss-20b (score=33.6, words=210, headings=0.40)
## Executive Summary  
Trametinib shows an exceptionally low AUC (0.1282) in the breast carcinoma cell line DU4475, indicating high sensitivity. The random‑forest model predicted a much higher AUC (12.40), yielding a large negative prediction error of –12.27. Compared with drug and cell cohort baselines (mean AUC ≈ 10.5 and 11.2 respectively, 0.3 th percentile), DU4475 is markedly more responsive to trametinib than most breast carcinoma lines.

## Evidence‑Based Interpretation  
The model’s prediction is driven by a combination of fingerprint and gene‑expression signals.  
- **fp_0367** (SMARTS `[#6]:[#6](-[#6]):[#6]`) contributes a negative SHAP value (–0.298), pushing the prediction toward lower AUC (greater sensitivity).  
- **TNFRSF12A (51330)** expression (value 4.51) adds a negative SHAP value (–0.156), also favoring sensitivity.  
- **fp_0204** (SMARTS `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`) provides a positive SHAP value (+0.121), nudging the prediction toward higher AUC (resistance).  
- Additional fingerprints (**fp_0409**, **fp_0062**, **fp_1008**) each supply small negative SHAP contributions (≈ –0.087), reinforcing sensitivity.  

The net effect of these features is a strong bias toward sensitivity, yet the overall RF output remains high, suggesting other unobserved factors in the model contribute to the resistance prediction.

## Feature and Neighborhood Analysis  
- **Fingerprint prevalence**: fp_0367 appears in 6.4 % of CTRPv2 compounds; fp_0204

---

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

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=79, headings=0.00)
---
title: "Docetaxel"
author: <NAME>
date: 2021-09-01
output: html_document
---

<h1 id="docetaxel">Docetaxel</h1>

<div class="figure"><img src="./figures/docetaxel.png"></div><br/>

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th colspan="2">Per-drug CV R2</th>
      <!-- <th colspan=2>Predictive power</th> -->
      <th>Observed AUC</th>
    </tr>
  </thead>
  <tbody>
    <td>n</td>
    <th>CV R2</th><td>0.29</td>
<!--     <td>--><td>--</td>
<td>--</ td>
<td><b>Observed</b> AUC</td>
  </

### Meta-Llama-3.1-8B-Instruct (score=60.0, words=359, headings=0.60)
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

### Qwen2.5-32B-Instruct (score=60.0, words=385, headings=0.60)
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

### gpt-oss-20b (score=1.5, words=19, headings=0.20)
## Executive Summary  
The Random Forest model predicts a docetaxel AUC of **7.94** for the neuroblastoma cell line **KPN

---

## RPT-0010 - RITA on TE441T

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0010
- observed_auc: 1.3692
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: soft tissue / rhabdomyosarcoma
- model_predicted_auc: 13.5331
- prediction_error: -12.1639
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=4, headings=0.00)
# Case: RITA on TE441T

### Meditron-7b (score=0.0, words=86, headings=0.00)
---
title: "Predictive Model Results"
date: "2021-09-01"
output: html_document
header-includes:
  include_header:
    elements:
      # Add your own header content here!
      - text::value("DEM Training Fit Only")
      - text(text = "Max-Depth Tuning Best Row", style="italic")
      - code::value("max_depth=21")
      - table::value(caption = "N-Estimator Tuning Best Row")
        caption_format = "table_caption"
        colwidths = c(10, 10, 20, 25, 25)
        align = "l"
        strip.table = TRUE
        alignment = "c"
        border = "solid"
        bordercolor = "#ccc"
        borderstyle = "double"
        borderthickness = 1
        borderradius = 0.1
        fontsize = 12
        footnote = "Note: The number of trees is set by default

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=366, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=40.0, words=345, headings=0.40)
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

### gpt-oss-20b (score=9.5, words=119, headings=0.20)
## Executive Summary  
RITA shows an **exceptionally sensitive** response in the TE441T rhabdomyosarcoma cell line (observed AUC = 1.37) compared with the RF model’s prediction (predicted AUC = 13.53) and cohort baselines (drug mean ≈ 12.66, cell mean ≈ 12.46). The large negative prediction error (−12.16) highlights a mismatch between the model’s expectation of resistance and the actual sensitivity observed.

## Evidence‑Based Interpretation  
The RF prediction is driven by several features that collectively push the AUC upward (toward resistance). The top TreeSHAP contributors are:

| Feature | SHAP effect | Direction |
|---------|-------------|-----------|
| **TNFRSF12A** (gene expression) | +0.202 | ↑ AUC (resistance) |
| **fp_0443** | +0.089 | ↑ AUC |
| **fp_0902** | +0.080 | ↑ AUC |
| **fp_0204** | +0.078 | ↑ AUC |
| **fp_0367** | +0.076 | ↑ AUC |
| **fp_0760** | –0.090 | ↓ AUC (sensitivity) |

Only

---

## RPT-0011 - GSK2636771 on SUDHL10

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0011
- observed_auc: 21.9540
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: haematopoietic and lymphoid tissue / lymphoid neoplasm
- model_predicted_auc: 12.5439
- prediction_error: +9.4101
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=100, headings=0.00)
---
title: "Grounded SHAP explanation"
author: <NAME>
date: 2021-09-01T15:00:00Z
output: html_document
---

<h1 id="top">Top</h1>

<div class="highlight"><pre><code class="language-python"><span></span><span class="k">import</span> <span class="nn">os</span><span class='p'>.</span><span class ="kw">pathlib</span><span>.</span><span ></span><span>get_project_root()</span><span>)</span><span>, </span><span class = "nb">'DEM':</span><span>[</span><span>"</span><span>/</span><span>\</span><span><span>data</span><span>",</span><span>'train':</span>< span>['</span><span/></span><span>&quot;&lt;</span><span>./</span><span>;</span><span>=</span><span>:</span><span>>&quot;&gt

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=370, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=60.0, words=331, headings=0.60)
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

### gpt-oss-20b (score=5.4, words=67, headings=0.20)
## Executive Summary  
GSK2636771 shows an observed AUC of **21.95** in the SUDHL10 cell line, markedly higher than the RF‑predicted AUC (**12.54**) and both drug (mean 14.24) and cell (mean 12.76) cohort baselines. The large positive prediction error (+9.41) indicates exceptional resistance in this specific sample.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The 9.41‑point excess places the sample at the

---

## RPT-0012 - dabrafenib on DU4475

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0012
- observed_auc: 0.6377
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: breast / carcinoma
- model_predicted_auc: 12.7509
- prediction_error: -12.1132
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=104, headings=0.00)
---
title: "Grounded Case Study"
author: <NAME>
date: 2021-09-01T12:00:00-04:00
output: html_document
---

<h1 id="top">Top</h1><br/>

<div class="highlight"><pre class="language-python"><code class="sourceCode monospac">import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import KFold
from sklearn._utils import check_random_state
from sklearn_pandas import DataFrame
from sklearn _extras import plot_partial_dependence
from sklearn .ensemble import GradientBoostingRegressor
from sklearn __version__
from sklearn.__version__
from scipy import stats
from sklearn_.metrics import mean_squared_error
from sklearn__.metrics import mean squared error
from sklearn__metrics import mean square error
from sklearn__metrics import root mean squared error # noqa F401
from sklearn___metrics

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=429, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=100.0, words=408, headings=1.00)
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

### gpt-oss-20b (score=33.1, words=207, headings=0.40)
## Executive Summary  
The breast ductal carcinoma cell line **DU4475** shows an **observed AUC of 0.64** for **dabrafenib**, markedly lower than the **RF‑predicted AUC of 12.75** and the **global mean AUC of 12.86**. This places the sample in the 0.3 th percentile of the drug cohort and the 80 th percentile of the cell cohort, indicating exceptional sensitivity relative to both drug‑ and cell‑specific baselines. The large negative prediction error (≈ −12.1) prompted the selection of this case for detailed SHAP analysis.

## Evidence‑Based Interpretation  
The Random Forest model attributes the low predicted AUC primarily to the expression of **TNFRSF12A (51330)**, whose SHAP contribution of **−0.51** drives the prediction toward sensitivity. Two fingerprint bits (**fp_0760** and **fp_0062**) also push the prediction downward (−0.07 and −0.05, respectively). Conversely, three fingerprint bits (**fp_0204**, **fp_0443**, **fp_0227**) contribute positively (+0.12, +0.08, +0.06), nudging the prediction toward resistance. The net effect of these local features is a strong bias toward a high‑AUC (resistant) prediction, which contrasts with the observed low AUC.

## Feature and Neighborhood Analysis  
- **TNFRSF12A (51330)**: Gene expression near the cross‑cell‑line mean; appears in 166 drug RF signatures, indicating a recurrent predictive signal across compounds.  
- **fp_0204**: SMARTS `

---

## RPT-0013 - MLN2238 on KARPAS620

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0013
- observed_auc: 18.6540
- interpretation: more resistant than the model predicted
- tissue / histology: haematopoietic and lymphoid tissue / lymphoid neoplasm
- model_predicted_auc: 9.2450
- prediction_error: +9.4090
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=25, headings=0.00)
## Executive Summary: Case Report for MLN2238 on KARPAS620 Using TreeSHAP Feature Importance and Local SHAP Explanations for MLR Models in the CTRP v2 Data Set

### Meditron-7b (score=0.0, words=55, headings=0.00)
---
title: "MLN2235"
description: ""
keywords: []
image: "/static/images/logo.png"
date: 2021-09-01
tags: [plasma cell myelomas, MLN22235, MLN235, iberdomide, IBER, ibrutomide, ibrutamide, ibrudomide, ibruadomide, ibuprofen, ibuprost, ibuten, ibuterone, ibutex, ibutixanol, ibutizane, ibutizan, ibutizanole, ibutizanon, ibutizanos, ibutizans, ibutizanyl, ibutizaxon, ibutizazone, ibutizazon, ibutizaton, ibutizato, ibutizate, ibutizati, ibutizatu, ibutizau, ibutizav, ibutizaw, ibutizab, ibutizac, ibutizad, ibutizae, ibutiza, i

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=358, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=60.0, words=345, headings=0.60)
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

### gpt-oss-20b (score=10.7, words=134, headings=0.20)
## Executive Summary  
The KARPAS620 cell line treated with MLN2238 exhibited an observed AUC of **18.65**, markedly higher than the RF‑predicted AUC of **9.25** (error + 9.41). Compared with the drug cohort (mean 9.14) and the cell cohort (mean 14.45), the sample is unusually resistant. The model’s prediction was driven by several fingerprint and gene‑expression features that collectively push the AUC downward, yet the actual response suggests additional, unmodeled factors.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The sample’s AUC exceeds both the global mean (12.86) and the cohort means, indicating a resistant phenotype.  
- **Local Cohort Context**: Within the MLN2238 drug cohort, the sample sits at the 100th percentile; within the KARPAS620 cell cohort, it also occupies the upper tail.  
- **Model Prediction**: The RF model, trained on

---

## RPT-0014 - AZD4547 on NCIH716

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0014
- observed_auc: 1.1299
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: large intestine / carcinoma
- model_predicted_auc: 13.2363
- prediction_error: -12.1064
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=96, headings=0.00)
---
title: "Grounded SHAP explanation"
author: <NAME>
date: 2021-09-01T19:00:00-04:00
output: html_document
---

<h1 id="top">Top</h1>

<div class="highlight"><pre><code class="language-python"><span></span><span class="k">import</span> <span class="n">ast</span>
<span class="k"></span><span class='na'>from</span> <a href="https://github.com/scikit-learn-contrib/sklearn-deeplearning-ensemble/blob/master/src/deep_learning/tree_shap_explainer.py">sklearn.deeplearning.ensemble</a>.<span class="nf">TreeShapExplainer</span>(<span class="nb">max_depth</span>=<span class="mi">None</span>, <span class="nb"></span><span>feature_interaction_strength</span>=<i>False</i>)

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=352, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=60.0, words=349, headings=0.60)
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

### gpt-oss-20b (score=33.9, words=212, headings=0.40)
## Executive Summary  
The NCIH716 cell line shows an **observed AUC of 1.13** for AZD4547, far below the **RF‑predicted AUC of 13.24** and the cohort medians (drug ≈ 12.89, cell ≈ 13.72). This indicates exceptional sensitivity relative to both the drug and cell baselines. The large negative prediction error (−12.11) prompted selection of this case for detailed SHAP analysis.

## Evidence‑Based Interpretation  
The RF model attributes the high predicted resistance mainly to the expression of **TNFRSF12A** (shap +0.204) and the presence of fingerprint bits **fp_0443** (+0.096) and **fp_0204** (+0.072). These features push the prediction toward higher AUC (resistance). Conversely, three fingerprint bits (**fp_0227**, **fp_0468**, **fp_0062**) contribute negative SHAP values (−0.149, −0.145, −0.071), nudging the prediction toward lower AUC (sensitivity). The net effect of these local features is a predicted AUC far above the observed value, explaining the discrepancy.

## Feature and Neighborhood Analysis  
- **TNFRSF12A (51330)**: Gene expression near the cross‑cell‑line mean; appears in 166 drug signatures, indicating a broad predictive role.  
- **fp_0227**: SMARTS `[#8]-[#6@H]`, present in 6.7 % of CTRPv2 compounds; exemplified by paclitaxel and teniposide.  
- **fp_0468**: SMARTS `[#6]:[#6](:[#6](-[#6]-[#7]):[#6](-[#6]):[#6]):[#6]`, rare (0.6 %) but seen in potent kinase inhibitors like staurosporine.  
- **fp_0062**: SMARTS `

---

## RPT-0015 - LBH-589 on KARPAS620

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0015
- observed_auc: 14.7440
- interpretation: more resistant than the model predicted
- tissue / histology: haematopoietic and lymphoid tissue / lymphoid neoplasm
- model_predicted_auc: 5.4171
- prediction_error: +9.3269
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=101, headings=0.00)
---
title: "Predictions for LBH589"
author: <NAME>
date: 2021-09-01
output: html_document
---

<h1 id="top">Top</h1>

<table class="dataframe">
  <thead><tr style="text-align: right"><th></th><th colspan="2">Per Drug</th><th col span="2">Per Cell Line</th><th>All</th></tr></thead>
  <tbody><tr><td>n</td><td>auc</td><td style="text-decoration: underline;">q10</td><td >median</td><td colspan="2" style="text-decora tion: underline;">sample percentile</td></tr>
  <tr><td>1</td><td>.</td><td .</td><td ..</td><td..</td><td.</td></tr> 
  <tr>
    <td>2</td><td></td><td </td><td ></

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=394, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=60.0, words=347, headings=0.60)
## Executive Summary
The response of LBH-589 on the KARPAS620 cell line, characterized by an observed AUC of 14.7440, indicates a higher resistance than the model's predicted AUC of 5.4171. This case was selected due to its large positive prediction error, suggesting that the cell line exhibits a more resistant profile than the model anticipated. The SHAP analysis highlights several molecular features that contribute to this resistance, including specific fingerprint bits and gene expression levels.

## Evidence-Based Interpretation
The observed AUC of 14.7440 for LBH-589 on KARPAS620 is significantly higher than the model's prediction of 5.4171, indicating a more resistant phenotype. The SHAP analysis reveals that several fingerprint bits and gene expression levels are driving the prediction towards lower AUC, which is contrary to the observed higher resistance. Specifically, fingerprint bit `fp_0223` with a SHAP value of -2.4886, `fp_0623` (-0.7250), `TNFRSF12A` (-0.6997), `fp_0362` (-0.5959), `fp_0053` (-0.5671), and `fp_0799` (-0.3937) all push the prediction towards lower AUC, suggesting relative sensitivity. However, the observed resistance suggests that other factors not captured by the model may be contributing to the higher AUC.

## Feature and Neighborhood Analysis
The top TreeSHAP features indicate that fingerprint bits `fp_0223`, `fp_0623`, `fp_0362`, `fp_0053`, and `fp_0799` are associated with relative sensitivity, pushing the prediction towards lower AUC. These fingerprint bits are present in a small percentage of compounds and are associated with specific SMARTS patterns. For instance, `fp_0223` is linked to the SMARTS pattern `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]`, found in compounds like gossypol, cytochalasin B, and erastin. Gene expression of `TNFRSF12A` also contributes to the prediction of lower AUC, with a SHAP value of -0.6997, indicating below-average expression levels.

In the drug cohort context, LBH-589 has a mean AUC of 5.3007, placing the KARPAS620 response at the 99.5th percentile, indicating extreme resistance. In the cell cohort context, KARPAS620 has a mean AUC of 14.4543, placing the LBH-589 response at the 55.4th percentile, suggesting moderate resistance within the cell line.

### gpt-oss-20b (score=11.0, words=137, headings=0.20)
## Executive Summary  
For KARPAS620 treated with LB 589, the observed AUC (14.74) is markedly higher than the RF model’s prediction (5.42), indicating greater resistance than expected. The drug is an outlier within its cohort (99.5th percentile) while the cell line sits near the median of its cohort. The model’s under‑prediction is driven by several fingerprint and gene‑expression features that collectively push the prediction toward lower AUC (greater sensitivity).

## Evidence‑Based Interpretation  
The RF prediction was largely shaped by six top TreeSHAP features, all of which exert negative SHAP values, thereby lowering the predicted AUC:

| Feature | SHAP | Direction |
|---------|------|-----------|
| fp_0223 | –2.49 | pushes toward lower AUC |
| fp_0623 | –0.73 | pushes toward lower AUC |
| TNFRSF12A | –0.70 | pushes toward lower AUC |
| fp_0362 | –0.60 | pushes toward lower AUC |
| fp_0053 | –0.57 | pushes toward

---

## RPT-0016 - ceranib-2 on SNU398

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0016
- observed_auc: 0.9898
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: liver / carcinoma
- model_predicted_auc: 13.0950
- prediction_error: -12.1052
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=67, headings=0.00)
---
title: "Predictive Model Results"
date: "2021-09-01T00:00:01Z"
output: html_document
---

<h1>Predictive Model Summary</h1><br/>

<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th colspan="2"><b>Model Metrics</b></th>
    </tr>
  </thead>
  <tbody>
    <td>
      <img src="https://user-images.githubusercontent.com/1011401/131911111-cbeeeba8-27ba-41bd-ad5b-4541915459bb.png"/>
    </td>
    <tbody>
      <tr>
        <td>
          <div id="plotly_embedded_figure_1"></div>
        </td>
        <th align

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=316, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=368, headings=0.80)
## Executive Summary
The response of SNU398, a hepatocellular carcinoma cell line, to ceranib-2 was exceptionally sensitive, with an observed AUC of 0.9898, significantly lower than the model-predicted AUC of 13.0950. This large negative prediction error indicates that the cell line is more sensitive to ceranib-2 than predicted by the model. The SHAP analysis reveals that fingerprint features and gene expression levels contribute to the model's prediction, with some features pushing toward higher AUC (resistance) and others toward lower AUC (sensitivity).

## Evidence-Based Interpretation
The observed AUC of 0.9898 for ceranib-2 on SNU398 is exceptionally low, indicating high sensitivity. The model predicted an AUC of 13.0950, which is much higher, suggesting a significant discrepancy between the observed and predicted responses. The SHAP analysis identifies several key features influencing the model's prediction. Fingerprint bit `fp_0443` and gene expression of `TNFRSF12A` push the prediction toward higher AUC (resistance), while fingerprint bits `fp_0227`, `fp_0362`, and `fp_1009` push the prediction toward lower AUC (sensitivity). These features collectively contribute to the model's prediction, but the observed response is much more sensitive than predicted.

## Feature and Neighborhood Analysis
The top SHAP features influencing the model's prediction include fingerprint bits and gene expression levels. Fingerprint bit `fp_0443` with a SHAP value of +0.3525 and `TNFRSF12A` with a SHAP value of +0.2492 both push the prediction toward higher AUC (resistance). Conversely, fingerprint bits `fp_0227` (-0.1804), `fp_0362` (-0.1707), and `fp_1009` (-0.1700) push the prediction toward lower AUC (sensitivity). The presence of these fingerprint bits in a small percentage of compounds suggests they are specific to certain chemical structures. For instance, `fp_0443` is present in 0.4% of compounds, while `fp_0227` is present in 6.7%. The gene expression of `TNFRSF12A` is near the cross-cell-line mean and recurs in 166 predictable-drug RF signatures.

## Model-Level Context
The model's training diagnostics indicate a moderate fit with a training R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration during tuning had a maximum depth of 20 and 100 estimators, achieving an R² of 0.6648. The global fingerprint features `fp_0443`, `fp_0

### gpt-oss-20b (score=0.0, words=457, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Must not give clinical advice. Must mention that SHAP explains RF prediction, not biology. Must separate local case evidence from global training diagnostics. Must treat train_r2 etc as diagnostics only. Must not mention training diagnostics in local interpretation. Must mention that observed AUC 0.9898 vs predicted 13.0950, huge negative error. Must note that sample percentile 0.1 in drug cohort, 0.3 in cell cohort. Must mention that the drug is an inhibitor of ceramidase activity. Must mention gene targets. Must mention top SHAP features and their direction. Must ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Must note that SHAP pushes toward higher AUC for fp_0443 and TNFRSF12A, pushes toward lower AUC for fp_0227, fp_0362, fp_1009, fp_0204. Must mention that fp_0204 pushes toward higher AUC but small effect. Must mention that the local case shows sensitivity relative to cohort baselines. Must mention that the same-drug cohort examples show variable responses. Must mention that same-cell cohort examples show variable responses. Must mention that the model predicted high AUC due to features like fp_0443 and TNFRSF12A. Must mention that the observed low AUC indicates sensitivity. Must mention that the model's prediction error is large. Must mention that the per-drug CV R2 is 0.3366, moderate. Must mention that global mean AUC is 12.8580. Must mention that the drug cohort mean AUC is 11.1811. Must mention that the cell cohort mean AUC is 12.6859. Must mention that the sample percentile is 0.1 drug, 0.3 cell. Must mention that the model predicted 13.0950, close to global mean. Must mention that the observed is 0.9898, far lower. Must mention that the model predicted high resistance but actual is sensitive. Must mention that the SHAP features indicate that the drug has fingerprint bits that push toward sensitivity (fp_0227, fp_0362, fp_1009) but also bits that push toward resistance (fp_0443, TNFRSF12A). The net effect is high predicted AUC. Must mention that the local case is exceptional sensitivity relative to cohort baselines. Must mention that the evidence is non-causal. Must mention that SHAP explains RF prediction. Must mention that training diagnostics are separate. Must mention that the model's per-drug R2 is moderate. Must mention that the training diagnostics show R2 0.4928, etc. Must mention that the model uses 202

---

## RPT-0017 - LBH-589 on 253JBV

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0017
- observed_auc: 20.4490
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: urinary tract / carcinoma
- model_predicted_auc: 11.2021
- prediction_error: +9.2469
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=69, headings=0.00)
---
title: "LBH-598"
description: ""
date: "2021-09-01"
output: html_document
header-includes:
 - \usepackage{booktabs}
 - \usepackage[margin=1cm]{caption}
 - \begin{document}$$\begin{tabular}{l@{}}$$\end{tabular}$${\color{red}\textsf{*}}\textsf{*} $$\end{tabular}$$
 - \begin {document}$$\begin {tabular}{lll} $$${\color{blue}\textsf{**}}$\\ {\color{green}\textsf{***}} \\ ${\color{yellow}\textsf{****}}$ $\end{tabular}${\color{black}\textsf{}}$${\color{cyan}\textsf{+++}}$${\color{#ff0000}\textsf{####}}$${\color#cbbb33}{\textsf{#####}}$${\color:#aaccdd}{\textsf{########}}$${\color##e69f06}{\textsf{################}}$${\color#{ffffff}\textsf{aaaaaa

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=390, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=80.0, words=380, headings=0.80)
## Executive Summary

The response of the 253JBV cell line to LBH-589, an inhibitor of HDAC1, HDAC2, HDAC3, HDAC6, and HDAC8, is exceptionally resistant relative to both the model prediction and cohort baselines. The observed AUC of 20.4490 is significantly higher than the model-predicted AUC of 11.2021, indicating a large positive prediction error of +9.2469. This places the sample at the 100th percentile in the drug cohort and the 99.4th percentile in the cell cohort, highlighting its unique resistance profile.

## Evidence-Based Interpretation

The observed resistance of 253JBV to LBH-589 is driven by several key features identified through TreeSHAP analysis. The most influential feature, fingerprint bit `fp_0223`, is associated with a representative SMARTS pattern `[#6]-[#6](-[#6])-[#6](:[#6](-[#8]):[#6]):[#6](:[#6]):[#6]` and pushes the prediction toward lower AUC (relative sensitivity). However, the presence of this feature in the compound does not align with the observed resistance, suggesting other factors are at play. Gene expression features, particularly PLK2 and TNFRSF12A, contribute significantly to the prediction of higher AUC (relative resistance). PLK2, with a z-score of +1.69, and TNFRSF12A, with a z-score of +0.62, both push the prediction toward higher AUC, indicating their role in the observed resistance.

## Feature and Neighborhood Analysis

The top TreeSHAP features include fingerprint bits and gene expressions. Fingerprint bit `fp_0223` is present in only 1.2% of CTRPv2 compounds and is associated with compounds like gossypol, cytochalasin B, and erastin. Despite its association with relative sensitivity, the presence of this feature does not mitigate the observed resistance. Gene expression features PLK2 and TNFRSF12A, which are above and near the cross-cell-line mean respectively, contribute to the prediction of higher AUC. These genes recur in multiple predictable-drug RF signatures, with PLK2 appearing in 102 signatures and TNFRSF12A in 166 signatures. Other fingerprint bits, such as `fp_0362`, `fp_0623`, and `fp_0902`, also push the prediction toward lower AUC but do not counterbalance the influence of the gene expression features.

## Model-Level Context

The Random Forest model used for prediction has been trained on a dataset with 311,258 samples and 2024 features, achieving a training R2 of 0.4928, RMSE of 1.8342, and correlation of 0.7061. The best-performing model configuration has a

### gpt-oss-20b (score=0.0, words=435, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, caveats. Use short paragraphs, under 550 words. Use only evidence from prompt. No invented pathways. Must mention that SHAP explains RF prediction not biology. Must separate local case evidence from global training diagnostics. Must not give clinical advice. Must not mention hidden reasoning. Must use the exact headings. Must include sample context: observed AUC, predicted AUC, local cohort baselines. Must mention that observed AUC 20.4490, predicted 11.2021, error +9.2469, global mean 12.8580. Must mention that it's exceptionally resistant relative to SHAP-predicted response and cohort baselines. Must mention that drug cohort mean 5.3007, cell cohort mean 13.6723. Must mention that sample percentile 100% for drug cohort, 99.4% for cell cohort. Must mention top SHAP features and their direction. Must ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Must note that SHAP pushes toward higher or lower AUC. Must mention that PLK2 and TNFRSF12A push toward higher AUC (resistance). fp_0223, fp_0362, fp_0623, fp_0902 push toward lower AUC (sensitivity). Must mention that PLK2 expression 10.5297, z=+1.69, recurs in 102 drugs. TNFRSF12A expression 7.8195, z=+0.62, recurs in 166 drugs. Must mention fingerprint bits prevalence percentages. Must mention SMARTS. Must mention same-drug cohort examples: KMS26, SEM, TE441T, HUCCT1. Must mention same-cell cohort examples: ouabain, leptomycin B, triazolothiadiazine, ML203. Must mention that the drug is HDAC inhibitor. Must mention that the cell line is transitional cell carcinoma of urinary tract. Must mention that the model's per-drug CV R2 is 0.2277. Must mention training diagnostics but treat them as diagnostics only. Must mention that the model's global mean AUC is 12.8580. Must mention that the observed AUC is above global mean. Must mention that the prediction error is large. Must mention that the SHAP explanation indicates that the high PLK2 and TNFRSF12A expression contributed to higher predicted AUC, but the fingerprint bits contributed to lower predicted AUC. Must mention that the net predicted AUC is lower than observed, indicating resistance. Must mention that the local case evidence is separate from global training diagnostics. Must mention that the SHAP explanation is for the RF prediction, not biology. Must mention that the model's per-drug R2 is low, so predictions may be uncertain. Must mention that the

---

## RPT-0018 - foretinib on EBC1

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0018
- observed_auc: 0.8572
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: lung / carcinoma
- model_predicted_auc: 12.9169
- prediction_error: -12.0597
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=7, headings=0.00)
# Executive Summary: RPT-0018 - Foretinib on EBC1

### Meditron-7b (score=0.0, words=72, headings=0.00)
---
title: "Foretinib"
description: "Prediction of anti-cancer activity against EBC1 cells using the DeepExplore DREAM challenge pipeline."
author: "<NAME>"
date: "2021-09-01"
output:
  html_document:
    fig_caption: true
    keep_source: true
    toc: false
    toc_depth: 2
    toc-numbers: true
    number_sections: true
    css: report.css
    latex_options:
      captionpos: figure
      tex_preamble: \usepackage{amsmath}
      tex_postamble: \end{document}
    theme: report
    plot_link_color: blue
    plot_bg_color: white
    plot_font_size: 12pt
    plot_margin: 0mm
    plot_width: auto
    plot_height: auto
    font_family: 'Roboto'
    font_style: normal
    font_weight: bold
    font_variant: normal

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=451, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=40.0, words=365, headings=0.40)
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

### gpt-oss-20b (score=9.6, words=120, headings=0.20)
## Executive Summary  
Foretinib shows an **exceptionally low AUC (0.8572)** in the EBC1 squamous‑cell carcinoma line, far below the **RF‑predicted AUC of 12.92** and the **cell‑line cohort mean (12.74)**. The observed sensitivity places EBC1 at the 0.5th percentile of all cell lines tested with foretinib, underscoring a pronounced deviation from the model’s expectation.

## Evidence‑Based Interpretation  
The large negative prediction error (-12.06) indicates that the model overestimates resistance for this sample. The SHAP analysis attributes this discrepancy to a combination of gene expression and chemical fingerprint signals that collectively lower the predicted AUC. The overall interpretation is that EBC1 is **highly sensitive** to foretinib relative to both the drug’s global performance

---

## RPT-0019 - 1S,3R-RSL-3 on CAL62

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0019
- observed_auc: 18.6380
- interpretation: more resistant than the model predicted
- tissue / histology: thyroid / carcinoma
- model_predicted_auc: 9.6448
- prediction_error: +8.9932
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=68, headings=0.00)
---
title: "Predictive Model Results"
date: "2021-09-01T00:00:01.001Z"
description: "Summary statistics for the final model."
output:
  html_document:
    fig_caption: true
    toc: false
    toc_depth: 2
    toc-numbers: true
    keep_source: true
    preserve_html_formatting: true
    latex_engine: xslate
    theme: bootswatch/luminosity
    highlight: pygments
    plotly: true
    knit: true
    cleanup: true
    bookdown_version: '0.11'
    bookdown::bookdown_base_url: https://github.com/jbloomlab/DEM_publications/tree/master/manuscripts/2021_dem_paper_results
    bookdown:
      cite_format: harvard
      bibliography: default
      bibliogroup_order: alphabetical
      bibliogrpah

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=400, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=80.0, words=376, headings=0.80)
## Executive Summary

The response of CAL62, an anaplastic carcinoma cell line derived from thyroid tissue, to the drug 1S,3R-RSL-3 was observed to be more resistant than the model predicted. The observed AUC of 18.6380 is significantly higher than the model's predicted AUC of 9.6448, indicating a substantial positive prediction error of +8.9932. This case is notable for its large positive prediction error, placing it at the 100th percentile within the drug cohort and the 98.3rd percentile within the cell cohort.

## Evidence-Based Interpretation

The TreeSHAP analysis reveals that the observed resistance of CAL62 to 1S,3R-RSL-3 is influenced by several molecular features. The most significant contributors are fingerprint bits that generally push the prediction toward lower AUC (relative sensitivity). Specifically, fingerprint bit `fp_0204` with a SHAP value of -1.7674, `fp_0271` with a SHAP value of -0.8043, and `fp_1017` with a SHAP value of -0.3293, all contribute to a more sensitive prediction. Conversely, the expression level of the gene TNFRSF12A (51330) pushes the prediction toward higher AUC (relative resistance) with a SHAP value of +0.3501.

## Feature and Neighborhood Analysis

The fingerprint bit `fp_0204` is characterized by the SMARTS pattern `[#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6]`, which is present in only 2.9% of CTRPv2 compounds. This feature is associated with compounds like BRD-K26531177, NVP-BEZ235, and CD-437, suggesting a rare structural motif that may confer sensitivity. Similarly, `fp_0271` with SMARTS `[#7]-[#6](:[#6]):[#6]` is present in 5.0% of compounds and is linked to drugs such as trifluoperazine and prochlorperazine. The presence of these fingerprint bits in 1S,3R-RSL-3 likely contributes to its sensitivity profile in CAL62.

In contrast, the gene TNFRSF12A, which is expressed at a level near the cross-cell-line mean, is associated with resistance. This gene recurs in 166 predictable-drug RF signatures, indicating its importance in the model's resistance predictions.

## Model-Level Context

The Random Forest model used for prediction has a training fit characterized by an R² of 0.4928, RMSE of 1.8342, and correlation of 0.7061, based on 311,258 samples and 2,024 features. The model's performance is optimized with a maximum depth of 20

### gpt-oss-20b (score=11.8, words=148, headings=0.20)
## Executive Summary  
The anaplastic thyroid carcinoma line **CAL62** shows a markedly **resistant** response to the GPX4 inhibitor **1S,3R‑RSL‑3** (observed AUC = 18.64). The random‑forest model predicted a much lower AUC of 9.64, yielding a positive prediction error of +8.99. Compared with the drug cohort (mean = 8.04, 100th percentile) and the cell cohort (mean = 13.69, 98.3rd percentile), CAL62’s response is unusually high, indicating that the model underestimates resistance for this combination.

## Evidence‑Based Interpretation  
The RF prediction is driven by several TreeSHAP features that collectively push the AUC upward (resistance) or downward (sensitivity).  
- **TNFRSF12A (51330)**: +0.3501 → higher AUC (resistance).  
- **fp_0204**: –1.7674 → lower AUC (sensitivity).  
- **fp_0271**: –0.8043 → lower AUC (sensitivity).  
- **fp_1017**: –0.3293 → lower AUC (sensitivity).  
- **fp_0806**: –0.2953 → lower AUC (sensitivity).  
- **fp_0062**: –0.1521 → lower AUC (sensitivity).  

The net effect is a modest resistance signal from

---

## RPT-0020 - PHA-793887 on SNU398

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0020
- observed_auc: 1.5525
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: liver / carcinoma
- model_predicted_auc: 13.5394
- prediction_error: -11.9869
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.0, words=8, headings=0.00)
# Case Report: RPT-0020 - PHA-793887 on SNU398

### Meditron-7b (score=0.0, words=72, headings=0.00)
---
title: "Predictive Drug Response Model for Hepatocellular Carcinoma"
author: <NAME>
date: 2021-09-01T12:00:00Z
output:
  html_document:
    keep_source: true
    preserve_yaml: false
    toc: true
    toc_depth: 2
    toc-numbers: true
    number_sections: true
    theme: bootswatch
    css:
      url: https://raw.githubusercontent.com/jrcgg/DEM-report/master/css/bootswatch.min.css
    highlight:
      theme: bootsdash
    plotly:
      enable_interactive: false
    latex:
      enabled: true
    knitrin:
      enabled_themes: [default]
    figcaption:
      format: paragraph
    footnote:
      enabled:::
        style: default
    bibliography:
      citation_style: apa
      style: apalike
    code_highlight:

### Meta-Llama-3.1-8B-Instruct (score=60.0, words=364, headings=0.60)
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

### Qwen2.5-32B-Instruct (score=60.0, words=358, headings=0.60)
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

### gpt-oss-20b (score=0.0, words=399, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Must not give clinical advice. Must not mention training diagnostics as generalization. Must separate local case evidence from global training diagnostics. Must treat train_r2 etc as diagnostics only. Must not mention any other info. Must use the given data.

We need to explain observed response of PHA-793887 on SNU398 using observed AUC, RF predicted AUC, local drug/cell cohort baselines. Observed AUC 1.5525, predicted 13.5394, error -11.9869. Cohort baselines: drug cohort mean 11.4834, cell cohort mean 12.6859. So observed is far lower, indicating high sensitivity relative to predictions and baselines. Provide interpretation: exceptionally sensitive relative to SHAP-predicted response and cohort baselines.

SHAP evidence: list top features with direction. Provide each feature and whether pushes toward higher AUC/resistance or lower AUC/sensitivity. Provide shap values.

Metadata grounding: ground feature descriptions in local metadata only: gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, same-drug/same-cell cohort examples. Use the provided data: e.g., fp_0443 SMARTS, prevalence 0.4%, example drugs nilotinib, bleomycin A2. TNFRSF12A gene expression value 6.1374, z -0.05, supporting drugs 166. fp_1009 SMARTS, prevalence 9.1%, example drugs betulinic acid etc. fp_0367 SMARTS, prevalence 6.4%. fp_0623 SMARTS, prevalence 5.8%. fp_0062 SMARTS, prevalence 3.7%. Provide same-drug cohort examples: EOL1, OCIAML3, DMS454, KPL1 with AUCs. Same-cell cohort examples: ceranib-2, tosedostat, erlotinib, abiraterone with AUCs.

Model-level context: global mean AUC 12.8580, training diagnostics: train_r2 0.4928, train_rmse 1.8342, train_corr 0.7061. Also per-drug cross-validated R2 0.3621. Provide that these are diagnostics only. Provide global fingerprint features list. Provide most common genes across predictable per-drug models. Provide that the model predicted high AUC due to features like fp_0443 etc.

Confidence and Caveats: note non-causal, SHAP explains RF prediction not biology directly, separate local case evidence from global training diagnostics. Note that prediction error large, but local evidence shows features pushing toward sensitivity. Note that training diagnostics not generalization. Provide caveats about limited sample size, etc.

Word count: keep under

---

## RPT-0021 - KU-0063794 on SKMEL2

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0021
- observed_auc: 21.2320
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: skin / malignant melanoma
- model_predicted_auc: 12.2996
- prediction_error: +8.9324
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=8, headings=0.00)
# Case Study: RPT-0021 - KU-0063794 on SKMEL2

### Meditron-7b (score=0.0, words=107, headings=0.00)
---
title: "SHAP Explanations"
author: <NAME>
date: 2021-09-01
output: html_document
---

<h1 id="top">Top</h1>

<div class="highlight"><pre><code class="language-python"><span></span><span class="k">import</span> <span class="n">pandas</span> <br/>
<span class="k"></span><span class='na'>from</span> <a href="https://github.com/scikit-learn-contrib/sklearn-shap/blob/master/docs/source/notebooks/examples/example_tree_explainer.py">here</a><br/>
<br/>
<i>Note:</i> This is an example notebook using the sklearn-shap package.<br/>
<b>This code was generated automatically by the Notebook Viewer.</b><br/>
</code></pre></div>

<h2 id="summary">Summary</h2>

<table border="1" style="width:

### Meta-Llama-3.1-8B-Instruct (score=100.0, words=407, headings=1.00)
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

### Qwen2.5-32B-Instruct (score=80.0, words=343, headings=0.80)
## Executive Summary

The response of SKMEL2, a malignant melanoma cell line, to KU-0063794, an mTOR inhibitor, is exceptionally resistant compared to both the model prediction and cohort baselines. The observed AUC of 21.2320 is significantly higher than the predicted AUC of 12.2996, indicating a large positive prediction error of +8.9324. This resistance is further highlighted by the sample's position at the 100th percentile in the drug cohort and 99.5th percentile in the cell cohort.

## Evidence-Based Interpretation

The observed response of SKMEL2 to KU-0063794 is characterized by a high AUC, indicating resistance. The model predicts a lower AUC, suggesting a misprediction of sensitivity. The SHAP analysis reveals that several molecular features contribute to this resistance. The top SHAP features include fingerprint bits and gene expression levels. Specifically, the fingerprint bit `fp_0202` with a SHAP value of -0.4209 and `TNFRSF12A` gene expression with a SHAP value of +0.1665 are key contributors. The fingerprint bit `fp_0202` is associated with a chemical structure `[#6]:[#6](-[#8]):[#6]`, which is present in 7.3% of compounds and is linked to compounds like gossypol, teniposide, and epigallocatechin-3-monogallate. The `TNFRSF12A` gene expression, near the cross-cell-line mean, is associated with 166 predictable-drug RF signatures and pushes the prediction toward higher AUC (resistance).

## Feature and Neighborhood Analysis

The SHAP analysis identifies several fingerprint bits that push the prediction toward lower AUC (sensitivity), including `fp_0202`, `fp_0623`, `fp_0227`, `fp_0771`, and `fp_0722`. These bits represent specific chemical structures such as `[#6]:[#6](-[#8]):[#6]`, `[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]):[#6]`, `[#8]-[#6@H]`, `[#6]-[#7]-[#6](=[#8])-[#6](:[#6]):[#6]`, and `[#6]:[#6](:[#16])-[#6](=[#8])-[#7]-[#6]`. Each of these structures is present in a small percentage of compounds and is associated with various drugs. The `TNFRSF12A` gene expression, with a SHAP value of +0.1665, is the only feature pushing the prediction toward higher AUC (resistance).

## Model-Level Context

The model's performance is characterized by a training fit with an R2 of 0.4928, RM

### gpt-oss-20b (score=9.3, words=116, headings=0.20)
## Executive Summary  
KU‑0063794 shows an observed AUC of **21.23** in the SKMEL2 melanoma line, markedly higher than the RF‑predicted AUC of **12.30** and the cohort baselines (drug mean ≈ 11.85, cell mean ≈ 14.22). The prediction error (+8.93) places this case at the 100th percentile of drug‑specific errors, indicating exceptional resistance relative to both the model and the broader drug/cell populations.

## Evidence‑Based Interpretation  
The RF model attributes the low predicted AUC largely to several fingerprint bits that favor sensitivity:  
- **fp_0202** (SMARTS `[#6]:[#6](-[#8]):[#6]`) contributes **–0.42** toward lower AUC; present in 7.3 % of CTRPv2 compounds.  
- **fp_0623**, **fp_0227**, **fp_0771**, and **fp_0722** each add between **–0.09

---

## RPT-0022 - BRD-K99006945 on JHUEM1

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0022
- observed_auc: 1.5813
- interpretation: exceptionally sensitive relative to the SHAP-predicted response and cohort baselines
- tissue / histology: endometrium / carcinoma
- model_predicted_auc: 13.5611
- prediction_error: -11.9798
- selection_reason: selected for a large negative prediction error (observed sensitivity below the model prediction)

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=81, headings=0.00)
---
title: "BRD-K980069"
description: ""
date: "2021-09-01T00:00:01.000Z"
tags: ["brd"]
authors: []
categories: ["brd", "cancer"]
keywords: ["brd","cancer"]
image: "/static/images/logo.png"
featured: false
show_author: true
show_category: true
showTags: true
showKeywords: true
showAuthors: true
showCategory: true
showDate: true
showDescription: true
showImage: true
showAuthor: true
showTag: true
showSubcategory: true
isFeatured: false
isPublished: true
isArchived: false
isExternal: false
isSticky: false
isGallery: false
isPopular: false
isRandom: false
isSlider: false
hasTranslate: false
hasVote: false
hasComment: false
hasLike: false
hasBookmark: false
hasDownload: false

### Meta-Llama-3.1-8B-Instruct (score=60.0, words=332, headings=0.60)
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

### Qwen2.5-32B-Instruct (score=60.0, words=346, headings=0.60)
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

### gpt-oss-20b (score=9.8, words=122, headings=0.20)
## Executive Summary  
BRD‑K99006945 shows an observed AUC of **1.58** in the JHUEM1 endometrial carcinoma line, far below the RF‑predicted AUC of **13.56** and the cohort means (drug = 14.03, cell = 12.24). This indicates exceptional sensitivity relative to both the model expectation and the local drug/cell baselines. The large negative prediction error (≈ –12) was the primary reason for selecting this case for review.

## Evidence‑Based Interpretation  
The RF model attributes the high predicted resistance to several features that, in this instance, are not expressed or present. The top TreeSHAP contributors are:

| Feature | Type | SHAP | Direction |
|---------|------|------|-----------|
| TNFRSF12A (51330) | gene_expression | +0.19 | pushes toward higher AUC (resistance) |
| fp_0367 | fingerprint_bit | +0.13 | pushes toward higher AUC (resistance) |
| fp_0204 | fingerprint_bit | +0

---

## RPT-0023 - SCH-529074 on MESSA

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0023
- observed_auc: 22.3390
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: soft tissue / sarcoma
- model_predicted_auc: 13.4876
- prediction_error: +8.8514
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=35, headings=0.00)
# Case Study: SCH-529074 on MESSA: Resistance to SCH-529074 in MESSA Cells Is Predicted by a TreeSHAP Feature Related to Mutant p53 Activity and Two Other Features Related to Gene Expression and Fingerprint Bits

### Meditron-7b (score=0.0, words=98, headings=0.00)
---
title: "SHAP Explanations"
date: "2021-09-01T15:00:00Z"
output: html_document
---

<h1>SHAP Explanation</h1><br/>

<div class="highlight"><pre class="language-python">from sklearn import ensemble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import shap
import pickle
import os
import json
import time
import random
import copy
import warnings
warnings.filterwarnings("ignore")

def get_data(filepath):
    df = pd.read_pickle(filepath)
    return df['feature'].tolist(), df['value']

df_train = get_data('../results/training_data.pkl')
df_test = get_data('/home/matthew/Documents/DEM/results/testing_data.pdl')

x_train, y_train = df_train[:

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=344, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=353, headings=0.80)
## Executive Summary

The response of MESSA (a soft tissue sarcoma cell line) to SCH-529074, an activator of mutant p53, is exceptionally resistant relative to both the model prediction and cohort baselines. The observed AUC of 22.3390 is significantly higher than the predicted AUC of 13.4876, indicating a large positive prediction error of +8.8514. This places the sample at the 100th percentile in both the drug and cell line cohorts, highlighting its unique resistance profile.

## Evidence-Based Interpretation

The observed resistance of MESSA to SCH-529074 is driven by several key features identified through TreeSHAP analysis. The top contributing features include fingerprint bits and gene expression levels that push the prediction toward higher AUC (relative resistance). Specifically, fingerprint bit `fp_0443` with a SHAP value of +0.3470, and gene expression of `TNFRSF12A` with a SHAP value of +0.2027, are significant contributors to the predicted resistance. Additionally, fingerprint bits `fp_0367` and `fp_0204` also contribute positively to the resistance prediction, with SHAP values of +0.1125 and +0.0686, respectively. Conversely, fingerprint bit `fp_1009` with a SHAP value of -0.1453 and `fp_0062` with a SHAP value of -0.0489 push the prediction toward lower AUC (relative sensitivity).

## Feature and Neighborhood Analysis

The fingerprint bit `fp_0443` is associated with the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, which is present in only 0.4% of CTRPv2 compounds, including nilotinib and bleomycin A2. This feature is highly specific and contributes significantly to the resistance prediction. Gene expression of `TNFRSF12A` is near the cross-cell-line mean but recurs in 166 predictable-drug RF signatures, suggesting its importance in the model. Fingerprint bit `fp_1009` with the SMARTS pattern `[#6]-[#6](:[#6]):[#6]` is present in 9.1% of compounds, including betulinic acid, isoliquiritigenin, and curcumin, and pushes the prediction toward sensitivity. Other fingerprint bits like `fp_0367` and `fp_0204` also contribute to resistance, while `fp_0062` with the SMARTS pattern `[#6]-[#6](:[#6]):[#16]` pushes toward sensitivity.

## Model-Level Context

The Random Forest model used for prediction has a training fit with R2 of 0.4928, RMSE of 1.8342, and correlation of 0

### gpt-oss-20b (score=11.0, words=138, headings=0.20)
## Executive Summary  
SCH‑529074 shows an observed AUC of **22.34** in the MESSA sarcoma cell line, markedly higher than the RF‑predicted AUC (**13.49**) and both drug (mean 12.76) and cell (mean 13.50) cohort baselines. The prediction error (+8.85) places this case at the 100th percentile of the drug cohort, indicating exceptional resistance relative to the model’s expectation and cohort norms.

## Evidence‑Based Interpretation  
The Random Forest (RF) model attributes the elevated AUC to a combination of molecular fingerprints and gene expression signals. The top TreeSHAP contributors are:

| Feature | SHAP | Direction |
|---------|------|-----------|
| **fp_0443** | +0.3470 | pushes toward higher AUC (resistance) |
| **TNFRSF12A (51330)** | +0.2027 | pushes toward higher AUC (resistance) |
| **fp_1009** | –0.1453 | pushes toward lower AUC (sensitivity) |
| **fp_0367** | +0.1125 | pushes toward higher AUC (resistance) |
| **fp_0204** | +0.0686 | pushes toward higher AUC (resistance

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

### BioMistral-7B (score=0.2, words=2, headings=0.20)
## Executive Summary

### Meditron-7b (score=0.0, words=65, headings=0.00)
---
title: "SHAP Explanations"
author: <NAME>
date: 2021-09-01T12:00:00Z
output:
  html_document:
    keep_source: true
    preserve_yaml: false
    toc: true
    toc_depth: 2
    tocfiles: ["README.md"]
    theme: bootswatch
    highlight: pygments
    plotly:
      enable_interactive: false
      height: auto
      width: auto
    bibliography: default
    bibliography_style: apalike
    figcaption_fontsize: 12
    figcaption:
      fontsize: 14
      textalign: center
    footnote_fontsize: small
    footnotes: true
    latex_preamble: \usepackage{amsmath}
    latex: [pdftex, xetex]
    number_sections: true
    number_pages: true
    pagereferences: true
    pdf_height: 100%
    pdf

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=383, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=100.0, words=403, headings=1.00)
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

### gpt-oss-20b (score=0.0, words=409, headings=0.00)
analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, caveats. Use short paragraphs, under 550 words. Use the given data. Must not invent pathways. Must not give clinical advice. Must treat train diagnostics as training fit only. Must not mention hidden reasoning. Must not give clinical advice. Must not mention "clinical" or "treatment". Must keep under 550 words.

We need to incorporate sample context: observed AUC 1.4980, predicted 13.1396, difference -11.6416, observed is much lower (more sensitive). Cohort baselines: drug cohort mean 8.9221, cell cohort mean 11.2748. So sample is more sensitive than both.

SHAP evidence: list top features with direction. Provide explanation: fp_0443 pushes toward higher AUC (resistance), etc. Provide metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell examples.

We need to ground feature descriptions in local metadata only: gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, same-drug/same-cell cohort examples. So we can mention that TNFRSF12A appears in 166 drugs, etc. Provide SMARTS for fingerprints. Provide prevalence percentages.

Also mention same-drug cohort examples: IMR32, DB, SKMEL2, TUHR14TKB. Same-cell cohort examples: vincristine, dinaciclib, IC-87114, BRD-K48477130.

We need to note that SHAP explains RF prediction, not biology. Also separate local case evidence from global training diagnostics.

We need to mention that per-drug CV R2 is 0.4019.

We need to mention that global mean AUC is 12.8580.

We need to mention that the model predicted high AUC but observed low, so sample is exceptionally sensitive relative to prediction and cohort baselines.

We need to mention that the top SHAP features: fp_0443 (+0.2984), TNFRSF12A (+0.2193), fp_0706 (-0.2036), fp_1009 (-0.1539), fp_0806 (+0.0667), fp_0062 (-0.0608). Provide direction.

We need to mention that fp_0706 and fp_1009 push toward sensitivity, while fp_0443, TNFRSF12A, fp_0806 push toward resistance. The net effect is predicted high AUC.

We need to mention that the sample's observed AUC is far below predicted, indicating high sensitivity.

We need to mention that the drug is a peptide mimetic inhibitor of SRC activity.

We need to mention that the cell line is SNU16, stomach carcinoma, undifferentiated adenocarcinoma.

We need to mention that the per-drug CV R2 is 0.4019, moderate

---

## RPT-0025 - ouabain on TUHR10TKB

### Source Snapshot
- source_type: tree_shap_rf
- evidence_id: SHAP-0025
- observed_auc: 29.3500
- interpretation: exceptionally resistant relative to the SHAP-predicted response and cohort baselines
- tissue / histology: kidney / carcinoma
- model_predicted_auc: 20.6181
- prediction_error: +8.7319
- selection_reason: selected for a large positive prediction error (observed resistance above the model prediction)

### BioMistral-7B (score=0.0, words=7, headings=0.00)
# Case Report: RPT-0025 - ouabain on TUHR10TKB

### Meditron-7b (score=0.0, words=84, headings=0.00)
{r}
report(source="local", id="RPT-0001")
```

### Section headings

```{html}
<h1>Report</h1><br/>
<hr />
<div class="section">
    <h2>Summary</h2><br/>
    <ul>
        <li>n = 31126</li>
        <br/>
        <li style="font-size: small;">The number of unique chemical structures in the dataset.</li>
        </ul>
    <hr />
    <h3>Model performance</h3><br/>
    
    <table border="1" width="100%" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <td colspan="2"><b>Performance metrics</b></td>
        </tr>
      </thead>
      <tbody>
        <tbody>
            <tr>
                <td>Training set</td>
                <th colspan="2">Test set</th>

### Meta-Llama-3.1-8B-Instruct (score=80.0, words=430, headings=0.80)
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

### Qwen2.5-32B-Instruct (score=80.0, words=366, headings=0.80)
## Executive Summary
The case of ouabain on the TUHR10TKB cell line (kidney carcinoma) shows an exceptionally resistant response with an observed AUC of 29.35, significantly higher than the model-predicted AUC of 20.62. This resistance is notable given the cell line's position at the 100th percentile in both the drug and cell cohort contexts, indicating a highly resistant profile compared to other samples. The primary drivers of this resistance include high gene expression levels of CSF1, SDC4, COL18A1, and TNFRSF12A, as well as specific molecular fingerprints associated with the drug structure.

## Evidence-Based Interpretation
The observed AUC of 29.35 for ouabain on TUHR10TKB is markedly higher than the model-predicted AUC of 20.62, indicating a significant deviation towards higher resistance. The SHAP analysis reveals that several features contribute to this resistance. CSF1, with a SHAP value of +1.0870, is the most influential feature, pushing the prediction towards higher AUC. Other significant contributors include fingerprint bits fp_0009 (+0.9989) and fp_0443 (+0.5723), which also indicate resistance. Gene expressions of SDC4 (+0.4625), COL18A1 (+0.3655), and TNFRSF12A (+0.1918) further reinforce the resistance profile.

## Feature and Neighborhood Analysis
The SHAP analysis highlights that CSF1, a gene involved in macrophage activation and tumor progression, is markedly above the cross-cell-line mean and recurs in 13 predictable-drug RF signatures, contributing significantly to the resistance. Fingerprint bit fp_0009, representing the SMARTS pattern `[#6]-[#6](=[#8])-[#6]`, is present in 3.3% of CTRPv2 compounds and is associated with drugs like IC-87114, sorafenib, and SNX-2112. Similarly, fp_0443, with the SMARTS pattern `[#6]:[#7]:[#6]:[#7](:[#6])-[#6]`, is present in 0.4% of compounds and linked to nilotinib and bleomycin A2. Gene expressions of SDC4, COL18A1, and TNFRSF12A, all above the cross-cell-line mean, further support the resistance profile.

## Model-Level Context
The model used for prediction is a Random Forest (RF) with a max depth of 20 and 100 estimators, achieving a cross-validated R2 of 0.6648 on the training set. However, the per-drug cross-validated predictability for ouabain is relatively low (R2=0.1544), indicating limited generalizability for this specific drug. The global model context

### gpt-oss-20b (score=5.3, words=66, headings=0.20)
## Executive Summary  
The kidney carcinoma cell line **TUHR10TKB** shows an **observed AUC of 29.35** for the cardiac glycoside **ouabain**, markedly higher than the **RF‑predicted AUC of 20.62** and the cohort baselines (drug mean ≈ 5.85, cell mean ≈ 13.75). The prediction error (+8.73) places this sample at the 100th percentile of both drug and cell cohorts, indicating exceptional resistance relative to the

---
