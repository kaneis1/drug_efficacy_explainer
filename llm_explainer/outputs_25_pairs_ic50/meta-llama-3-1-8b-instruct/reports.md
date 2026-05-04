# Generated Reports - Meta-Llama-3.1-8B-Instruct

## RPT-0001 - AZD7762 on A204
_Source evidence: SHAP-0001_

## Executive Summary
The observed response of AZD7762 on A204 is characterized by an observed log10(IC50) of -1.1810, which is lower than the model-predicted log10(IC50) of -0.3207. This indicates that AZD7762 is more sensitive to A204 than predicted by the model. The prediction error is -0.8602, suggesting that the model underestimates the sensitivity of AZD7762 to A204.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The top features are:

* fp_0141, a fingerprint bit that is present in 1.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.7413.
* fp_0157, a fingerprint bit that is present in 8.9% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.3092.
* fp_0032, a fingerprint bit that is present in 3.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.1493.
* fp_0994, a fingerprint bit that is present in 2.3% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0677.
* fp_0876, a fingerprint bit that is present in 1.5% of CTRPv2 compounds, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0629.
* fp_0071, a fingerprint bit that is present in 5.2% of CTRPv2 compounds, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0462.

## Feature and Neighborhood Analysis
The fingerprint bits contributing to the prediction are all present in less than 10% of CTRPv2 compounds, indicating that they are relatively rare features. The SMARTS patterns associated with these features are:

* fp_0141: `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`
* fp_0157: `[#6]-[#6](-[#6])-[#7]`
* fp_0032: `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`
* fp_0994: `[#7]-[#6](:[#6]):[#6]`
* fp_0876: `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`
* fp_0071: `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`

These SMARTS patterns are representative of specific molecular substructures that may contribute to the sensitivity or resistance of AZD7762 to A204.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, GPX8.

Note that these diagnostics are only relevant to the training process and do not reflect the performance of the model on unseen data.

## Confidence and Caveats
The SHAP values provide a local explanation of the prediction for AZD7762 on A204, but it is essential to note that SHAP explains the RF prediction rather than the underlying biology directly. The model's performance on this specific case should be interpreted in the context of the global model diagnostics and the local feature explanations. Additionally, the rarity of the contributing fingerprint bits suggests that the prediction may be sensitive to changes in the feature space.

---

## RPT-0002 - SCH-79797 on DAUDI
_Source evidence: SHAP-0002_

## Executive Summary
SCH-79797, an antagonist of proteinase-activated receptor 1 (PAR1), was tested on the DAUDI cell line. The observed log10(IC50) was -0.0633, which is close to the model prediction of 0.2079 and the cohort baselines. The prediction error is -0.2712, indicating that the model underestimates the compound's activity.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0017, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3733.
* fp_0263, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2619.
* CCN1 (3491), a gene expression feature, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0969.
* fp_0673, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0572.
* fp_0141, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0571.
* fp_0688, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0230.

## Feature and Neighborhood Analysis
The top fingerprint bit features, fp_0017 and fp_0263, are present in 2.3% of CTRPv2 compounds and are associated with lower log10(IC50) (relative sensitivity). These features are representative of SMARTS patterns `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]` and `[#8]-[#6](=[#8])-[#6]-[#6]`, respectively. The gene expression feature, CCN1 (3491), is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, GPX8.

## Confidence and Caveats
The SHAP values explain the RF prediction, but do not directly explain the underlying biology. The local evidence for this sample should be considered in the context of the global model context. The model's performance on this sample is close to the prediction and cohort baselines, but the prediction error indicates that the model underestimates the compound's activity.

---

## RPT-0003 - obatoclax on DAUDI
_Source evidence: SHAP-0003_

## Executive Summary
Obatoclax, an inhibitor of MCL1, BCL2, and BCL-xL, was tested on the DAUDI cell line. The observed log10(IC50) was -1.3840, indicating a more sensitive response than the model predicted (-0.3547). The prediction error was 1.0294, with the global mean log10(IC50) being 0.6392.

## Evidence-Based Interpretation
The TreeSHAP analysis identified the top features contributing to the prediction. The top features pushing the prediction toward lower log10(IC50) (relative sensitivity) were:

* fp_0141, a fingerprint bit, with a SHAP value of -0.4976
* fp_0329, a fingerprint bit, with a SHAP value of -0.1799
* CCN1 (3491), a gene expression feature, with a SHAP value of -0.1335
* fp_0994, a fingerprint bit, with a SHAP value of -0.1043
* fp_0423, a fingerprint bit, with a SHAP value of -0.0924
* fp_0110, a fingerprint bit, with a SHAP value of -0.0805

These features are representative of compounds with specific structural patterns, such as aromatic rings and heterocycles, and are present in a small percentage of compounds in the CTRPv2 dataset.

## Feature and Neighborhood Analysis
The local metadata provides additional context for the top features:

* fp_0141 is a fingerprint bit present in 1.5% of CTRPv2 compounds, with example drugs including dexamethasone, austocystin D, and daporinad.
* fp_0329 is a fingerprint bit present in 5.0% of CTRPv2 compounds, with example drugs including NSC23766, PD 153035, and gefitinib.
* CCN1 (3491) is a gene expression feature that recurs in 71 predictable-drug RF signatures and is below the cross-cell-line mean.
* fp_0994 is a fingerprint bit present in 2.3% of CTRPv2 compounds, with example drugs including NSC23766, compound 1B, and BRD-K92856060.
* fp_0423 is a fingerprint bit present in 3.1% of CTRPv2 compounds, with example drugs including chlorambucil, CIL70, and axitinib.
* fp_0110 is a fingerprint bit present in 1.7% of CTRPv2 compounds, with example drugs including SNX-2112, TPCA-1, and BRD-K66453893.

## Model-Level Context
The global model context provides information on the training fit and tuning:

* DEM training fit: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385 (treat these as training diagnostics, not held-out generalization).
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141 (0.11630), fp_0513 (0.04974), fp_0535 (0.03781), fp_0017 (0.03749), fp_0723 (0.03716), fp_0071 (0.03714), fp_0777 (0.03127), fp_0518 (0.02657).
* Most common genes across predictable per-drug models: MYOF (26509) (92 drugs), TNFRSF12A (51330) (82 drugs), SDC4 (6385) (74 drugs), CCN1 (3491) (71 drugs), PRSS23 (11098) (69 drugs), WWTR1 (25937) (61 drugs), LAMB2 (3913) (60 drugs), GPX8 (493869) (59 drugs).

## Confidence and Caveats
The SHAP analysis explains the RF prediction, but does not directly explain the underlying biology. The local case evidence should be interpreted with caution, as it may not generalize to other contexts. The global model context provides information on the training fit and tuning, but should not be used to make predictions or draw conclusions about the model's performance on unseen data.

---

## RPT-0004 - obatoclax on A2780
_Source evidence: SHAP-0004_

## Executive Summary
Obatoclax, an inhibitor of MCL1, BCL2, and BCL-xL, was tested on the A2780 cell line. The observed log10(IC50) was -0.7250, which is close to the model prediction (-0.1646) and cohort baselines. The prediction error was -0.5604, indicating that the model underpredicted the observed log10(IC50).

## Evidence-Based Interpretation
The TreeSHAP analysis identified six top features that contributed to the prediction. All six features are fingerprint bits that push the prediction toward lower log10(IC50), indicating relative sensitivity. The top feature, fp_0141, has a SHAP value of -0.6725, meaning that its presence increases the predicted log10(IC50) by 0.6725 units. This feature is present in 1.5% of CTRPv2 compounds and is representative of SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])`. Other notable features include fp_0329, fp_0994, fp_0423, fp_0110, and CCN1 (3491), which pushes the prediction toward higher log10(IC50) (relative resistance).

## Feature and Neighborhood Analysis
The top fingerprint bit features are all present in less than 5% of CTRPv2 compounds, suggesting that they are relatively rare. The SMARTS patterns associated with these features are diverse, but they all involve aromatic rings and heteroatoms. The gene expression feature, CCN1 (3491), is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The same-drug cohort examples show that obatoclax is more sensitive in some cell lines (e.g., ML1, DND41) and more resistant in others (e.g., NCIH226, MJ). The same-cell cohort examples show that other drugs are more sensitive or resistant in A2780 cells.

## Model-Level Context
The global model context includes training diagnostics (n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385) and tuning results (max_depth=20, n_estimators=100, r2=0.5459). The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for obatoclax is R2=0.1628.

## Confidence and Caveats
This report is based on a single case (obatoclax on A2780) and should be interpreted with caution. The SHAP analysis explains the RF prediction, not the underlying biology. The local evidence presented here should be considered in the context of the global model and its limitations. The model's performance on this case is close to the prediction and cohort baselines, but the prediction error is significant (-0.5604). Further investigation is needed to understand the underlying mechanisms and to validate the model's predictions.

---

## RPT-0005 - obatoclax on NCIH520
_Source evidence: SHAP-0005_

## Executive Summary
The observed response of obatoclax on NCIH520 shows a log10(IC50) of -0.4511, which is close to the model prediction (-0.1952) and cohort baselines. The prediction error is 0.2560, indicating a moderate deviation from the model's expectation.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are fingerprint bits and gene expression. Specifically, the presence of fp_0141, fp_0329, CCN1, fp_0994, fp_0423, and fp_0110 push the prediction toward lower log10(IC50), indicating relative sensitivity. These features are representative SMARTS patterns and are present in a small percentage of CTRPv2 compounds. The gene CCN1 is also below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Feature and Neighborhood Analysis
The top TreeSHAP features are:

* fp_0141: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 1.5% of CTRPv2 compounds, and represented by SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`. Example compounds include dexamethasone, austocystin D, and daporinad.
* fp_0329: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 5.0% of CTRPv2 compounds, and represented by SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`. Example compounds include NSC23766, PD 153035, and gefitinib.
* CCN1: a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity), below the cross-cell-line mean, and recurs in 71 predictable-drug RF signatures.
* fp_0994: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 2.3% of CTRPv2 compounds, and represented by SMARTS `[#7]-[#6](:[#6]):[#6]`. Example compounds include NSC23766, compound 1B, and BRD-K92856060.
* fp_0423: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 3.1% of CTRPv2 compounds, and represented by SMARTS `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`. Example compounds include chlorambucil, CIL70, and axitinib.
* fp_0110: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity), present in 1.7% of CTRPv2 compounds, and represented by SMARTS `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`. Example compounds include SNX-2112, TPCA-1, and BRD-K66453893.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, GPX8.
* Per-drug cross-validated predictability for obatoclax: R2=0.1628.

## Confidence and Caveats
This report is based on the TreeSHAP analysis of the RF model's prediction for obatoclax on NCIH520. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution and in conjunction with the global model context. The model's performance on this specific case is moderate, with a prediction error of 0.2560. The top features contributing to the prediction are fingerprint bits and gene expression, which push the prediction toward lower log10(IC50), indicating relative sensitivity.

---

## RPT-0006 - obatoclax on A204
_Source evidence: SHAP-0006_

## Executive Summary
Obatoclax, an inhibitor of MCL1, BCL2, and BCL-xL, was tested on A204 cells. The observed log10(IC50) was -0.5184, which is close to the model prediction (-0.1471) and cohort baselines. The prediction error was 0.3713, indicating a moderate discrepancy between the observed and predicted values.

## Evidence-Based Interpretation
The TreeSHAP analysis identified six top features that contributed to the prediction. All six features are fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). These features are:

* fp_0141: a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, present in 1.5% of CTRPv2 compounds, with example drugs dexamethasone, austocystin D, and daporinad.
* fp_0329: a representative SMARTS pattern `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`, present in 5.0% of CTRPv2 compounds, with example drugs NSC23766, PD 153035, and gefitinib.
* fp_0994: a representative SMARTS pattern `[#7]-[#6](:[#6]):[#6]`, present in 2.3% of CTRPv2 compounds, with example drugs NSC23766, compound 1B, and BRD-K92856060.
* fp_0423: a representative SMARTS pattern `[#6]-[#6](:[#6]:[#6]:[#6]):[#6]`, present in 3.1% of CTRPv2 compounds, with example drugs chlorambucil, CIL70, and axitinib.
* fp_0110: a representative SMARTS pattern `[#6]:[#6](:[#6])-[#6](-[#7])=[#8]`, present in 1.7% of CTRPv2 compounds, with example drugs SNX-2112, TPCA-1, and BRD-K66453893.
* CCN1 (3491): a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance), with a value of 5.2402 and a z-score of -0.01.

## Feature and Neighborhood Analysis
The same-drug cohort examples show that obatoclax is more sensitive in some cell lines (e.g., ML1, DND41) and more resistant in others (e.g., NCIH226, MJ). The same-cell cohort examples show that obatoclax is more sensitive than some other drugs (e.g., paclitaxel, leptomycin B) and more resistant than others (e.g., BRD-K42260513, BCL-LZH-4).

## Model-Level Context
The global model context shows that the DEM training fit has a moderate R2 of 0.4042 and a moderate RMSE of 1.0264. The top global fingerprint features are fp_0141, fp_0513, and fp_0535. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4. The per-drug cross-validated predictability for obatoclax is R2=0.1628.

## Confidence and Caveats
This report is based on a single case and should be interpreted with caution. The SHAP analysis explains the RF prediction rather than the underlying biology directly. The local evidence presented here should be considered in the context of the global model diagnostics and the broader literature on obatoclax and its targets.

---

## RPT-0007 - doxorubicin on HGC27
_Source evidence: SHAP-0007_

## Executive Summary
Doxorubicin was tested on the HGC27 cell line, resulting in an observed log10(IC50) of -1.1839. The random forest model predicted a log10(IC50) of 0.4325, indicating that the cell line is more sensitive than the model predicted. The prediction error is 1.6164, with the observed value being lower than the predicted value.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0329, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4858.
* CCN1 (3491), a gene expression feature, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.2028.
* fp_0141, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1518.
* fp_0017, a fingerprint bit, pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0744.
* fp_0535, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0663.
* fp_0998, a fingerprint bit, pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0505.

## Feature and Neighborhood Analysis
The feature fp_0329 is a fingerprint bit that is present in 5.0% of CTRPv2 compounds and is representative of SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`. It is associated with example compounds such as NSC23766, PD 153035, and gefitinib. The gene CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bits fp_0141, fp_0017, and fp_0535 are present in 1.5%, 2.3%, and 1.7% of CTRPv2 compounds, respectively, and are associated with example compounds such as dexamethasone, austocystin D, daporinad, bexarotene, SR-II-138A, CR-1-31B, and BRD4132, BRD6340, parbendazole.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, GPX8.
* Per-drug cross-validated predictability for doxorubicin: R2=0.2707.

## Confidence and Caveats
This report is based on the analysis of a single case and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local evidence presented here should be considered in the context of the global model diagnostics and the feature descriptions provided.

---

## RPT-0008 - doxorubicin on DAUDI
_Source evidence: SHAP-0008_

## Executive Summary
The observed response of doxorubicin on DAUDI cells shows a lower IC50 (-2.3904) compared to the model's prediction (-0.8297), indicating that the cells are more sensitive to the drug than expected. This discrepancy is reflected in the prediction error of -1.5607 and an absolute error of 1.5607.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to this prediction are:

*   fp_0329: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7667.
*   CCN1 (3491): a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4748.
*   fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1001.
*   fp_0322: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0907.
*   fp_0535: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0679.
*   fp_0522: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0535.

These features indicate that the presence of certain molecular patterns in doxorubicin contributes to its increased sensitivity in DAUDI cells.

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

*   fp_0329 is a representative SMARTS pattern `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]` present in 5.0% of CTRPv2 compounds, with example drugs NSC23766, PD 153035, and gefitinib.
*   CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and has a below-average expression level across cell lines.
*   fp_0141 is a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]` present in 1.5% of CTRPv2 compounds, with example drugs dexamethasone, austocystin D, and daporinad.
*   fp_0322 is a representative SMARTS pattern `[#8]-[#6](:[#6]):[#6]` present in 15.0% of CTRPv2 compounds, with example drugs BRD9876, tamoxifen, and BRD9647.
*   fp_0535 is a representative SMARTS pattern `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]` present in 1.7% of CTRPv2 compounds, with example drugs BRD4132, BRD6340, and parbendazole.
*   fp_0522 is a representative SMARTS pattern `[#6]-[#6@@H](-[#6])/[#6]=[#6](\[#6])-[#6]` present in 1.0% of CTRPv2 compounds, with example drugs manumycin A, 16-beta-bromoandrosterone, and cyanoquinoline 11.

## Model-Level Context
The global model context provides information on the training fit and tuning:

*   The DEM training fit has n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, and train_corr=0.6385, which are training diagnostics and not held-out generalization metrics.
*   The max-depth tuning best row has max_depth=20, n_estimators=100, and r2=0.5459.
*   The N-estimator tuning best row has max_depth=10, n_estimators=235, mean_r2=0.3803, and std_r2=0.0031.
*   The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518.
*   The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction for doxorubicin on DAUDI cells. The SHAP values indicate the contribution of each feature to the prediction, but do not directly explain the underlying biology. The local case evidence should be considered in conjunction with the global model context to understand the broader implications of these findings.

---

## RPT-0009 - doxorubicin on A2780
_Source evidence: SHAP-0009_

## Executive Summary
The observed response of doxorubicin on A2780 cells is more sensitive than the model predicted, with an observed log10(IC50) of -2.0412 compared to the model-predicted log10(IC50) of 0.4531. The prediction error is -2.4944, indicating that the model underpredicted the sensitivity of doxorubicin on A2780 cells.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0329, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4796.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.2027.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1528.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0750.
* fp_0535, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0665.
* fp_0998, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0505.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0329 is present in 5.0% of CTRPv2 compounds and is representative of SMARTS `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]`. It is present in example compounds such as NSC23766, PD 153035, and gefitinib. The gene expression feature CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, GPX8.
* Per-drug cross-validated predictability for doxorubicin: R2=0.2707.

## Confidence and Caveats
This report is based on the local evidence for this sample and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The model's performance on this specific case may not generalize to other cases.

---

## RPT-0010 - doxorubicin on NCIH520
_Source evidence: SHAP-0010_

## Executive Summary
The observed response of doxorubicin on NCIH520 is characterized by a relatively low log10(IC50) of -0.1530, indicating high sensitivity. The model-predicted log10(IC50) is -0.8557, which is lower than the observed value, resulting in a prediction error of +0.7027. This suggests that the model underestimates the sensitivity of NCIH520 to doxorubicin.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_0329: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7743.
*   CCN1 (3491): a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.4798.
*   fp_0322: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0903.
*   fp_0535: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0664.
*   fp_0522: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0555.
*   fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0851.

These features are all fingerprint bits, indicating that the molecular structure of doxorubicin plays a significant role in its interaction with NCIH520.

## Feature and Neighborhood Analysis
The local metadata provides additional context for these features:

*   fp_0329 is a representative SMARTS pattern `[#6]-[#7]-[#6](:[#6]:[#6]):[#6]:[#6]` present in 5.0% of CTRPv2 compounds, with example drugs NSC23766, PD 153035, and gefitinib.
*   CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and has a below-average expression level across cell lines.
*   fp_0322 is a representative SMARTS pattern `[#8]-[#6](:[#6]):[#6]` present in 15.0% of CTRPv2 compounds, with example drugs BRD9876, tamoxifen, and BRD9647.
*   fp_0535 is a representative SMARTS pattern `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]` present in 1.7% of CTRPv2 compounds, with example drugs BRD4132, BRD6340, and parbendazole.
*   fp_0522 is a representative SMARTS pattern `[#6]-[#6@@H](-[#6])/[#6]=[#6](\[#6])-[#6]` present in 1.0% of CTRPv2 compounds, with example drugs manumycin A, 16-beta-bromoandrosterone, and cyanoquinoline 11.
*   fp_0141 is a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]` present in 1.5% of CTRPv2 compounds, with example drugs dexamethasone, austocystin D, and daporinad.

## Model-Level Context
The global model context provides additional information about the training data and model performance:

*   The DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385, indicating a moderate level of fit.
*   The per-drug cross-validated predictability for doxorubicin is R2=0.2707, indicating a relatively low level of predictability.
*   The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8.

## Confidence and Caveats
This analysis is based on the SHAP values of the top features contributing to the prediction, which explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other cell lines or compounds. The global model context provides additional information about the training data and model performance, but should be treated as training diagnostics rather than held-out generalization.

---

## RPT-0011 - N9-isopropylolomoucine on SNU761
_Source evidence: SHAP-0011_

## Executive Summary
The observed response of N9-isopropylolomoucine on SNU761 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.7423 and a model-predicted log10(IC50) of 1.0604. The prediction error is -4.8028, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_0017: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1363.
*   CCN1 (3491): a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0997.
*   fp_0141: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0870.
*   fp_0673: a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0726.
*   fp_0513: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0191.
*   fp_0535: a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0161.

## Feature and Neighborhood Analysis
The feature descriptions are grounded in local metadata:

*   fp_0017 is a fingerprint bit present in 2.3% of CTRPv2 compounds, with representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`, and example compounds bexarotene, SR-II-138A, CR-1-31B.
*   CCN1 (3491) is a gene with above the cross-cell-line mean expression, recurs in 71 predictable-drug RF signatures, and has 71 supporting drugs.
*   fp_0141 is a fingerprint bit present in 1.5% of CTRPv2 compounds, with representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`, and example compounds dexamethasone, austocystin D, daporinad.
*   fp_0673 is a fingerprint bit present in 17.5% of CTRPv2 compounds, with representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`, and example compounds tamoxifen, procarbazine, methotrexate.
*   fp_0513 is a fingerprint bit present in 0.8% of CTRPv2 compounds, with representative SMARTS `[#8]-[#6](:[#6]):[#6]:[#6](:[#6])-[#8]`, and example compounds epigallocatechin-3-monogallate, CAY10594, avrainvillamide.
*   fp_0535 is a fingerprint bit present in 1.7% of CTRPv2 compounds, with representative SMARTS `[#6]:[#7]:[#6](:[#6](:[#7]):[#6]):[#6]:[#6]`, and example compounds BRD4132, BRD6340, parbendazole.

## Model-Level Context
The global model context includes:

*   DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
*   Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
*   N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
*   Top global fingerprint features: fp_0141 (0.11630), fp_0513 (0.04974), fp_0535 (0.03781), fp_0017 (0.03749), fp_0723 (0.03716), fp_0071 (0.03714), fp_0777 (0.03127), fp_0518 (0.02657).
*   Most common genes across predictable per-drug models: MYOF (26509) (92 drugs), TNFRSF12A (51330) (82 drugs), SDC4 (6385) (74 drugs), CCN1 (3491) (71 drugs), PRSS23 (11098) (69 drugs), WWTR1 (25937) (61 drugs), LAMB2 (3913) (60 drugs), GPX8 (493869) (59 drugs).

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction, which may not directly reflect the underlying biological mechanisms. The local case evidence should be considered separately from the global training diagnostics. The SHAP values indicate the relative contribution of each feature to the prediction, but do not imply causality.

---

## RPT-0012 - chlorambucil on MDAMB453
_Source evidence: SHAP-0012_

## Executive Summary
The observed response of chlorambucil on MDAMB453 is exceptionally sensitive, with an observed log10(IC50) of -3.6833. This is in contrast to the model-predicted log10(IC50) of 1.0653, indicating a significant prediction error of -4.7486. The local drug/cell cohort baselines show that chlorambucil is generally less effective against this cell line, with a mean log10(IC50) of 1.8527 across the drug cohort and 0.6302 across the cell cohort.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0723, and fp_0059. These features all push the prediction toward higher log10(IC50) values, indicating relative resistance. CCN1 is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bits fp_0141, fp_0017, fp_0513, fp_0723, and fp_0059 are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds and are associated with resistance to various drugs.

## Feature and Neighborhood Analysis
The feature CCN1 is a gene expression feature that is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. This suggests that CCN1 may be a general biomarker for resistance to many drugs. The fingerprint bits fp_0141, fp_0017, fp_0513, fp_0723, and fp_0059 are representative SMARTS patterns that are present in a small percentage of CTRPv2 compounds and are associated with resistance to various drugs. These features are likely indicative of specific molecular mechanisms of resistance.

## Model-Level Context
The global model context shows that the DEM training fit has a moderate R2 of 0.4042 and a moderate correlation of 0.6385. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for chlorambucil is R2=0.2533, indicating a moderate level of predictability.

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction for chlorambucil on MDAMB453. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution and in the context of the global model diagnostics. The model's performance on held-out data is not evaluated here, and the results should not be used for clinical decision-making.

---

## RPT-0013 - NSC23766 on NCIH322
_Source evidence: SHAP-0013_

## Executive Summary
The observed response of NSC23766 on NCIH322 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.2596 and a model-predicted log10(IC50) of 1.0653. The prediction error is -4.3249, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are:

* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0870.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0865.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0378.
* fp_0059, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0362.
* fp_0263, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0304.
* fp_0513, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0168.

## Feature and Neighborhood Analysis
The top TreeSHAP features are primarily fingerprint bits, which are binary features that represent the presence or absence of specific substructures in the molecular structure of the compound. These features are often used to capture the chemical properties of the compound that are relevant to its activity. The gene expression feature CCN1 (3491) is also a significant contributor to the prediction.

The fingerprint bits are present in a small percentage of compounds in the CTRPv2 dataset, indicating that they are relatively rare features. However, they are representative of specific substructures that are associated with resistance to the compound. The example compounds listed for each fingerprint bit are compounds that have been identified as having similar substructures.

## Model-Level Context
The global model context provides information about the overall performance of the model. The DEM training fit diagnostics indicate that the model has a moderate level of fit, with an R-squared value of 0.4042 and a root mean squared error of 1.0264. The model's performance is likely influenced by the presence of outliers and the complexity of the data.

The top global fingerprint features are primarily fingerprint bits, which are similar to the top TreeSHAP features. The most common genes across predictable per-drug models are primarily involved in cellular processes such as cell adhesion and signaling.

## Confidence and Caveats
The SHAP values provide a local explanation of the prediction, but it is essential to note that they do not provide a causal explanation of the underlying biology. The SHAP values are based on the model's prediction and may not reflect the actual biological mechanisms involved.

The local evidence for this sample is based on the TreeSHAP features and their SHAP values, which provide a snapshot of the model's prediction for this specific sample. The global model context provides information about the overall performance of the model and the features that are most relevant to the prediction. However, it is essential to consider the limitations of the model and the potential biases in the data when interpreting the results.

---

## RPT-0014 - ML050 on FADU
_Source evidence: SHAP-0014_

## Executive Summary
The observed log10(IC50) for ML050 on FADU cells is -3.4516, which is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines. The model-predicted log10(IC50) is 1.0653, resulting in a prediction error of -4.5168.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0924.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0794.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0498.
* fp_0513, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0185.
* fp_0723, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0171.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0129.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bits fp_0017, fp_0513, fp_0723, and fp_0535 are all present in a small percentage of CTRPv2 compounds and are associated with various compounds.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, fp_0518.
* Most common genes across predictable per-drug models: MYOF (26509), TNFRSF12A (51330), SDC4 (6385), CCN1 (3491), PRSS23 (11098), WWTR1 (25937), LAMB2 (3913), GPX8 (493869).

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction for ML050 on FADU cells. The SHAP values indicate that the top features contributing to the prediction are fingerprint bits and a gene expression feature that push the prediction toward higher log10(IC50) (relative resistance). However, it is essential to note that SHAP explains the RF prediction rather than the underlying biology directly. Additionally, the local case evidence should be separated from global training diagnostics.

---

## RPT-0015 - BRD1835 on MONOMAC6
_Source evidence: SHAP-0015_

## Executive Summary
The observed response of BRD1835 on MONOMAC6 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.3440 and a model-predicted log10(IC50) of 0.8039. The prediction error is -4.1480, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1844.
* fp_0141, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1234.
* fp_0518, a fingerprint bit feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0659.
* fp_0062, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0458.
* fp_0017, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0393.
* fp_0513, a fingerprint bit feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0190.

## Feature and Neighborhood Analysis
The feature CCN1 (3491) is a gene expression feature that is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. This suggests that CCN1 may play a role in modulating the sensitivity of BRD1835 on MONOMAC6.

The fingerprint bit features fp_0141, fp_0518, fp_0062, fp_0017, and fp_0513 are all present in a small percentage of CTRPv2 compounds, indicating that they may be specific to certain chemical subspaces. The SMARTS patterns associated with these features are representative of specific molecular structures, such as aromatic rings and heterocycles.

## Model-Level Context
The global model context indicates that the DEM training fit has a train_r2 of 0.4042, train_rmse of 1.0264, and train_corr of 0.6385. These metrics suggest that the model is moderately well-fitted to the training data. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are all related to aromatic rings and heterocycles.

The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8, which may be involved in modulating the sensitivity of various drugs across different cell lines.

## Confidence and Caveats
The SHAP values provide a local explanation of the prediction, but do not necessarily reflect the underlying biological mechanisms. The prediction error of -4.1480 indicates that the model is not accurately capturing the observed response of BRD1835 on MONOMAC6. The same-drug and same-cell cohort examples provide additional context, but may not be directly applicable to this specific case. The model's performance on this case should be interpreted with caution, and further investigation is needed to understand the underlying biology.

---

## RPT-0017 - ML203 on JIMT1
_Source evidence: SHAP-0017_

## Executive Summary
The observed response of ML203 on JIMT1 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.6063 and a model-predicted log10(IC50) of 1.0653. The prediction error is -4.6716, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

*   fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1632.
*   CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0805.
*   fp_0518, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0748.
*   fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0514.
*   fp_0513, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0186.
*   fp_0723, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0178.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. CCN1 (3491) is a gene that recurs in 71 predictable-drug RF signatures and is near the cross-cell-line mean. The fingerprint bit fp_0518 is present in 4.0% of CTRPv2 compounds and is associated with compounds such as valdecoxib, neuronal differentiation inducer III, and BMS-754807.

## Model-Level Context
The global model context includes:

*   DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
*   Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
*   N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
*   Top global fingerprint features: fp_0141 (0.11630), fp_0513 (0.04974), fp_0535 (0.03781), fp_0017 (0.03749), fp_0723 (0.03716), fp_0071 (0.03714), fp_0777 (0.03127), fp_0518 (0.02657).
*   Most common genes across predictable per-drug models: MYOF (26509) (92 drugs), TNFRSF12A (51330) (82 drugs), SDC4 (6385) (74 drugs), CCN1 (3491) (71 drugs), PRSS23 (11098) (69 drugs), WWTR1 (25937) (61 drugs), LAMB2 (3913) (60 drugs), GPX8 (493869) (59 drugs).

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction for ML203 on JIMT1. The SHAP values indicate the contribution of each feature to the prediction, but do not explain the underlying biology. The local case evidence should be interpreted in the context of the global model diagnostics and metadata. The model's performance on held-out data is not evaluated here, and the results should be treated with caution.

---

## RPT-0018 - BRD-K51490254 on L540
_Source evidence: SHAP-0018_

## Executive Summary
The observed response of BRD-K51490254 on L540 is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.5904 and a model-predicted log10(IC50) of 0.7137. This discrepancy indicates that the model underestimates the compound's effectiveness on this cell line.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* CCN1 (3491), a gene expression feature that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.2094.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0659.
* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0301.
* fp_0513, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0202.
* fp_0723, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0160.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0138.

These features suggest that the model is overestimating the compound's resistance to L540 cells, which may be due to the presence of these fingerprint bits in other compounds that are more resistant to this cell line.

## Feature and Neighborhood Analysis
The CCN1 gene expression feature is below the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. This suggests that CCN1 may play a role in modulating the sensitivity of L540 cells to BRD-K51490254. The fingerprint bits fp_0141, fp_0017, fp_0513, fp_0723, and fp_0535 are present in a small percentage of CTRPv2 compounds and are associated with resistance to L540 cells. These features may indicate that BRD-K51490254 has a unique molecular structure that contributes to its exceptional sensitivity on this cell line.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with a train R-squared of 0.4042 and a train RMSE of 1.0264. The model's performance on this specific compound is reflected in its per-drug cross-validated R2 of 0.0405. The most common genes across predictable per-drug models include CCN1, which is also a top feature in this case. The cell subtype metadata is available, indicating that the model has been trained on data from Hodgkin lymphoma cells.

## Confidence and Caveats
This analysis is based on the SHAP values of the top features contributing to the prediction, which explain the RF prediction rather than the underlying biology directly. The conclusions drawn from this analysis should be interpreted with caution, as they are based on a single case and may not generalize to other compounds or cell lines. The model's performance on this compound is exceptional, but this may be due to the specific features present in BRD-K51490254 rather than a general property of the compound.

---

## RPT-0019 - N9-isopropylolomoucine on AN3CA
_Source evidence: SHAP-0019_

## Executive Summary
The observed response of N9-isopropylolomoucine on AN3CA is exceptionally sensitive relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.2225 and a model-predicted log10(IC50) of 1.0565. The prediction error is -4.2790, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are:

* fp_0017, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.1421.
* CCN1 (3491), a gene expression feature that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0995.
* fp_0141, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0922.
* fp_0673, a fingerprint bit that pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0750.
* fp_0513, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0195.
* fp_0535, a fingerprint bit that pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0172.

## Feature and Neighborhood Analysis
The fingerprint bit fp_0017 is present in 2.3% of CTRPv2 compounds and is associated with representative SMARTS `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`. This feature is also present in example compounds such as bexarotene, SR-II-138A, and CR-1-31B. The gene CCN1 (3491) is near the cross-cell-line mean and recurs in 71 predictable-drug RF signatures. The fingerprint bit fp_0673 is present in 17.5% of CTRPv2 compounds and is associated with representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#6])-[#6]`. This feature is also present in example compounds such as tamoxifen, procarbazine, and methotrexate.

## Model-Level Context
The global model context includes:

* DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385.
* Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459.
* N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031.
* Top global fingerprint features: fp_0141 (0.11630), fp_0513 (0.04974), fp_0535 (0.03781), fp_0017 (0.03749), fp_0723 (0.03716), fp_0071 (0.03714), fp_0777 (0.03127), fp_0518 (0.02657).
* Most common genes across predictable per-drug models: MYOF (26509) (92 drugs), TNFRSF12A (51330) (82 drugs), SDC4 (6385) (74 drugs), CCN1 (3491) (71 drugs), PRSS23 (11098) (69 drugs), WWTR1 (25937) (61 drugs), LAMB2 (3913) (60 drugs), GPX8 (493869) (59 drugs).

## Confidence and Caveats
This report is based on the SHAP explanation of the RF prediction for N9-isopropylolomoucine on AN3CA. The SHAP values indicate the contribution of each feature to the prediction, but do not directly explain the underlying biology. The local case evidence should be interpreted in the context of the global model diagnostics and metadata. The model's performance on held-out data is not evaluated here, and the results should be treated with caution.

---

## RPT-0020 - Ko-143 on JHUEM3
_Source evidence: SHAP-0020_

## Executive Summary
Ko-143 on JHUEM3 shows an exceptionally sensitive response relative to the SHAP-predicted response and cohort baselines, with an observed log10(IC50) of -3.4507 and a model-predicted log10(IC50) of 1.0653. The prediction error is -4.5160, indicating a significant discrepancy between the observed and predicted responses.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to this prediction are CCN1, fp_0141, fp_0017, fp_0513, fp_0535, fp_0723, which all push the prediction toward higher log10(IC50) (relative resistance). These features are associated with a near-cross-cell-line mean expression of CCN1, and representative SMARTS patterns in the fingerprint bits, such as `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]` and `[#8]-[#6@](-[#6@@H])(-[#6])-[#6@@](-[#8]-[#6])(-[#6@@H](-[#6@@H])-[#6])-[#6](:[#6]):[#6]`. These features are present in a small percentage of CTRPv2 compounds, indicating that they may be indicative of a specific subset of compounds with similar properties.

## Feature and Neighborhood Analysis
The same-drug cohort examples show a mix of sensitive and resistant profiles, with some cells showing more sensitive responses (MJ, AM38) and others showing more resistant responses (RPMI8226, SNU387). The same-cell cohort examples also show a mix of sensitive and resistant profiles, with some drugs showing more sensitive responses (docetaxel, BMS-754807) and others showing more resistant responses (BRD8958, necrostatin-1). The local metadata grounding for these features is limited, but the presence of these features in a small percentage of CTRPv2 compounds suggests that they may be indicative of a specific subset of compounds with similar properties.

## Model-Level Context
The global model context shows that the model has a moderate level of training fit, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, and fp_0723, which are also among the top features contributing to the prediction for Ko-143 on JHUEM3. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8, but CCN1 is the only one that is relevant to this specific prediction.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly, and the local case evidence should be interpreted with caution. The global model diagnostics are available, but they should not be used to make inferences about the performance of the model on unseen data. The model's performance on this specific case is exceptional, but it is unclear whether this is due to the specific features of Ko-143 or the JHUEM3 cell line. Further investigation is needed to understand the underlying mechanisms driving this prediction.

---

## RPT-0021 - AZD7762 on GCT
_Source evidence: SHAP-0021_

## Executive Summary
The observed response of AZD7762 on GCT (malignant fibrous histiocytoma pleomorphic sarcoma) shows a relatively low sensitivity, with an observed log10(IC50) of 0.0929. The model-predicted log10(IC50) is -0.3147, indicating a predicted resistance. However, the prediction error is high at +0.4076, suggesting that the model's prediction may not accurately capture the true behavior of AZD7762 on GCT.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are all fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The most influential feature is fp_0141, which has a SHAP value of -0.7311 and is present in 1.5% of CTRPv2 compounds. Other significant features include fp_0157, fp_0032, fp_0994, and fp_0876, which all have SHAP values between -0.3087 and -0.0741. These features are representative SMARTS patterns that are associated with sensitive compounds.

## Feature and Neighborhood Analysis
The fingerprint bits contributing to the prediction are all associated with sensitive compounds. Fp_0141 is a representative SMARTS pattern `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]` that is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. Similarly, fp_0157 is a representative SMARTS pattern `[#6]-[#6](-[#6])-[#7]` that is present in 8.9% of CTRPv2 compounds and is associated with compounds such as CIL55, BRD4132, and phloretin. The same-drug cohort examples also show that AZD7762 is more sensitive on certain cell lines, such as MOLM13 and MFE319.

## Model-Level Context
The global model context shows that the model has a moderate training fit, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The per-drug cross-validated predictability for AZD7762 is R2=0.2053, indicating that the model has some ability to predict the behavior of AZD7762 on GCT. The top global fingerprint features are fp_0141, fp_0513, and fp_0535, which are all associated with sensitive compounds. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4, which are all associated with sensitive compounds.

## Confidence and Caveats
The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be interpreted with caution, as it may not generalize to other cell lines or compounds. The global model context provides some insight into the model's performance, but the training diagnostics should not be used as a direct measure of the model's generalizability.

---

## RPT-0022 - AZD7762 on NCIH2452
_Source evidence: SHAP-0022_

## Executive Summary
The observed response of AZD7762 on NCIH2452 is characterized by an observed log10(IC50) of -0.6016, which is close to the model-predicted log10(IC50) of -0.3125 and the local drug and cell cohort baselines.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The top features are:

* fp_0141, a fingerprint bit that is present in 1.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.7210.
* fp_0157, a fingerprint bit that is present in 8.9% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.3084.
* fp_0032, a fingerprint bit that is present in 3.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.1471.
* fp_0994, a fingerprint bit that is present in 2.3% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0709.
* fp_0611, a fingerprint bit that is present in 1.2% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0437.

## Feature and Neighborhood Analysis
The fingerprint bits that contribute to the prediction are all present in less than 10% of CTRPv2 compounds, indicating that they are relatively rare features. The example compounds associated with these features are dexamethasone, austocystin D, daporinad, CIL55, BRD4132, phloretin, SB-431542, apicidin, MK-2206, NSC23766, compound 1B, BRD-K92856060, triptolide, cucurbitacin I, and NPC-26. These compounds are all inhibitors of various kinases, which is consistent with the mechanism of action of AZD7762 as an inhibitor of checkpoint kinases 1 and 2.

## Model-Level Context
The global model context indicates that the model has a moderate level of training fit, with a train_r2 of 0.4042 and a train_rmse of 1.0264. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, SDC4, CCN1, PRSS23, WWTR1, LAMB2, and GPX8. The per-drug cross-validated predictability for AZD7762 is R2=0.2053.

## Confidence and Caveats
The SHAP analysis provides a local explanation of the prediction, but it is essential to note that it does not explain the underlying biology directly. The features that contribute to the prediction are based on the model's learned relationships between the input data and the target variable, and may not necessarily reflect the actual biological mechanisms involved. Additionally, the model's performance on this specific case should be interpreted in the context of the global model diagnostics, which indicate a moderate level of training fit.

---

## RPT-0023 - AZD7762 on T24
_Source evidence: SHAP-0023_

## Executive Summary
The observed response of AZD7762 on T24 cells shows a moderate level of sensitivity, with an observed log10(IC50) of 0.3256. The model-predicted log10(IC50) is -0.2994, indicating a close match to the observed value. The prediction error is +0.6250, which is within the range of the global mean log10(IC50) of 0.6392.

## Evidence-Based Interpretation
The top TreeSHAP features contributing to the prediction are all fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The top feature, fp_0141, has a SHAP value of -0.7204, indicating that its presence increases the predicted sensitivity of AZD7762 on T24 cells. The other top features, fp_0157, fp_0032, and fp_0994, also contribute to increased sensitivity. In contrast, the two features that push the prediction toward higher log10(IC50) (relative resistance) have smaller SHAP values, indicating a weaker effect.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits with SMARTS patterns that are representative of specific chemical substructures. The feature fp_0141 is present in 1.5% of CTRPv2 compounds and is associated with compounds such as dexamethasone, austocystin D, and daporinad. The other top features have similar characteristics, with varying frequencies of occurrence in the CTRPv2 dataset. The same-drug cohort examples show that AZD7762 is more sensitive in some cell lines (e.g., MOLM13, MFE319) and more resistant in others (e.g., MALME3M, MKN45). The same-cell cohort examples show that other drugs are more sensitive or resistant in T24 cells, depending on their target and chemical structure.

## Model-Level Context
The global model context provides information on the training fit, tuning, and feature importance. The DEM training fit has a train_r2 of 0.4042 and train_rmse of 1.0264, indicating a moderate level of fit. The top global fingerprint features are fp_0141, fp_0513, and fp_0535, which are also among the top features for AZD7762. The most common genes across predictable per-drug models are MYOF, TNFRSF12A, and SDC4, which are not directly related to the target CHEK1;CHEK2. The per-drug cross-validated predictability for AZD7762 is R2=0.2053, indicating a moderate level of predictability.

## Confidence and Caveats
This report is based on the TreeSHAP feature importance and does not provide a direct explanation of the biological mechanisms underlying the prediction. The SHAP values should be interpreted as explaining the RF prediction rather than the underlying biology. The local evidence for this sample is based on the top TreeSHAP features and same-drug/same-cell cohort examples, while the global model context provides information on the training fit, tuning, and feature importance. The conclusions should be treated as non-causal and subject to the limitations of the model and data.

---

## RPT-0024 - AZD7762 on NCIH1341
_Source evidence: SHAP-0024_

## Executive Summary
The observed response of AZD7762 on NCIH1341 is characterized by an observed log10(IC50) of -0.5202, which is close to the model-predicted log10(IC50) of -0.3395 and the local drug/cell cohort baselines.

## Evidence-Based Interpretation
The TreeSHAP analysis reveals that the top features contributing to the prediction are fingerprint bits that push the prediction toward lower log10(IC50) (relative sensitivity). The top features are:

* fp_0141, a fingerprint bit that is present in 1.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.7563.
* fp_0157, a fingerprint bit that is present in 8.9% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.3149.
* fp_0032, a fingerprint bit that is present in 3.5% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.1481.
* fp_0611, a fingerprint bit that is present in 1.2% of CTRPv2 compounds, pushes the prediction toward lower log10(IC50) with a SHAP value of -0.0435.

In contrast, two fingerprint bits push the prediction toward higher log10(IC50) (relative resistance): fp_0876 and fp_0071, with SHAP values of +0.0626 and +0.0472, respectively.

## Feature and Neighborhood Analysis
The top features are fingerprint bits that are present in a small percentage of CTRPv2 compounds, suggesting that they may be indicative of a specific chemical structure or functional group that contributes to the sensitivity of AZD7762 on NCIH1341. The example compounds listed for each feature provide further context for the types of molecules that exhibit these characteristics.

## Model-Level Context
The global model context provides information on the training fit of the model, including the number of samples (181811), features (2024), and diagnostics (train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385). The model was tuned using a random forest approach with a maximum depth of 20 and 100 estimators, resulting in a best R2 of 0.5459. The top global fingerprint features are fp_0141, fp_0513, fp_0535, fp_0017, fp_0723, fp_0071, fp_0777, and fp_0518.

## Confidence and Caveats
The SHAP analysis provides a local explanation of the prediction for AZD7762 on NCIH1341, but it is essential to note that SHAP explains the RF prediction rather than the underlying biology directly. The local evidence should be considered in conjunction with the global model context and the caveats that the model is trained on a specific dataset and may not generalize to all scenarios. Additionally, the model's performance on this specific case is close to the model prediction and cohort baselines, indicating a reasonable fit.

---

## RPT-0025 - AZD7762 on SNU308
_Source evidence: SHAP-0025_

## Executive Summary
The observed response of AZD7762 on SNU308 is characterized by an observed log10(IC50) of 0.1881, which is close to the model prediction of -0.3135 and the local drug/cell cohort baselines. The prediction error is +0.5016, indicating a discrepancy between the observed and predicted values.

## Evidence-Based Interpretation
The top TreeSHAP features driving the prediction for AZD7762 on SNU308 are:

*   fp_0141: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.7233
*   fp_0157: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.3083
*   fp_0032: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.1477
*   fp_0994: pushes the prediction toward lower log10(IC50) (relative sensitivity) with a SHAP value of -0.0644
*   fp_0876: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0462
*   fp_0071: pushes the prediction toward higher log10(IC50) (relative resistance) with a SHAP value of +0.0450

These features are all fingerprint bits, indicating that the presence or absence of specific molecular substructures in AZD7762 contributes to its predicted sensitivity or resistance on SNU308.

## Feature and Neighborhood Analysis
The top TreeSHAP features are all fingerprint bits, which are binary features indicating the presence or absence of specific molecular substructures. The feature descriptions are grounded in local metadata:

*   fp_0141: representative SMARTS `[#7]-[#6](=[#8])-[#6]1(-[#6]-[#6]-1)-[#6](=[#8])-[#7]`; present in 1.5% of CTRPv2 compounds; example compounds: dexamethasone, austocystin D, daporinad
*   fp_0157: representative SMARTS `[#6]-[#6](-[#6])-[#7]`; present in 8.9% of CTRPv2 compounds; example compounds: CIL55, BRD4132, phloretin
*   fp_0032: representative SMARTS `[#6]:[#6](:[#7])-[#6](:[#6]:[#6]):[#6]:[#6]`; present in 3.5% of CTRPv2 compounds; example compounds: SB-431542, apicidin, MK-2206
*   fp_0994: representative SMARTS `[#7]-[#6](:[#6]):[#6]`; present in 2.3% of CTRPv2 compounds; example compounds: NSC23766, compound 1B, BRD-K92856060
*   fp_0876: representative SMARTS `[#6]:[#6]:[#6]:[#6](:[#16])-[#7+]`; present in 1.5% of CTRPv2 compounds; example compounds: triptolide, cucurbitacin I, NPC-26
*   fp_0071: representative SMARTS `[#7]:[#6]:[#7]:[#6](:[#6]):[#6]`; present in 5.2% of CTRPv2 compounds; example compounds: N9-isopropylolomoucine, purmorphamine, IC-87114

## Model-Level Context
The global model context includes:

*   DEM training fit diagnostics: n_samples=181811, n_features=2024, train_r2=0.4042, train_rmse=1.0264, train_corr=0.6385
*   Max-depth tuning best row: max_depth=20, n_estimators=100, r2=0.5459
*   N-estimator tuning best row: max_depth=10, n_estimators=235, mean_r2=0.3803, std_r2=0.0031
*   Top global fingerprint features: fp_0141 (0.11630), fp_0513 (0.04974), fp_0535 (0.03781), fp_0017 (0.03749), fp_0723 (0.03716), fp_0071 (0.03714), fp_0777 (0.03127), fp_0518 (0.02657)
*   Most common genes across predictable per-drug models: MYOF (26509) (92 drugs), TNFRSF12A (51330) (82 drugs), SDC4 (6385) (74 drugs), CCN1 (3491) (71 drugs), PRSS23 (11098) (69 drugs), WWTR1 (25937) (61 drugs), LAMB2 (3913) (60 drugs), GPX8 (493869) (59 drugs)
*   Per-drug cross-validated predictability for AZD7762: R2=0.2053

## Confidence and Caveats
This report is based on the provided data and should be interpreted with caution. The SHAP values explain the RF prediction rather than the underlying biology directly. The local case evidence should be separated from the global training diagnostics. The conclusions drawn from this report are non-causal and should not be used to make clinical decisions.

---
