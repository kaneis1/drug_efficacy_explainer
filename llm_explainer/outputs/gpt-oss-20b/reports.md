# Generated Reports - gpt-oss-20b

## RPT-0001 - cytarabine hydrochloride on SKMEL2
_Source evidence: SHAP-0001_

## Executive Summary  
The cytarabine hydrochloride assay on the melanoma cell line **SKMEL2** yielded an observed AUC of **27.18**, markedly higher than the Random Forest (RF) model prediction of **13.59** and the cohort baselines (drug mean ≈ 11.63, cell mean ≈ 14.22). This indicates an exceptionally resistant phenotype relative to both the model and the broader drug‑cell population. The large positive prediction error (+13.59) is driven by a combination of fingerprint features that collectively bias the RF toward higher AUC predictions.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The observed AUC exceeds the model’s prediction by 13.59 units, placing SKMEL2 in the 100th percentile of the drug cohort and the 100th percentile of the cell cohort

---

## RPT-0002 - birinapant on KYM1
_Source evidence: SHAP-0002_

## Executive Summary  
The soft‑tissue rhabdomyosarcoma cell line **KYM1** was treated with the SMAC mimetic **birinapant** (drug ID 660778). The observed area‑under‑curve (AUC) was **0.6877**, markedly lower than the random‑forest (RF) model prediction of **13.8762** and the global mean AUC of **12.8580**. This 13.2‑unit negative prediction error places KYM1 in the lowest 0.1 % of the drug cohort and 0.2

---

## RPT-0003 - nilotinib on BT549
_Source evidence: SHAP-0003_

## Executive Summary  
Nilotinib exhibited an observed AUC of **23.71** in the BT549 breast ductal carcinoma cell line, markedly higher than the RF‑predicted AUC of **13.47** and the cohort mean of **13.96**. This indicates an unusually resistant phenotype relative to both the drug’s overall CTRPv2 performance and the BT549 cell line baseline. The model’s positive prediction error (+10.24) reflects this

---

## RPT-0004 - N9-isopropylolomoucine on CADOES1
_Source evidence: SHAP-0004_

analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use the provided data. Must not invent pathways. Must not give clinical advice. Must separate local evidence from global diagnostics. Must treat train diagnostics as training fit only. Must not mention training diagnostics in local interpretation. Must not mention "clinical" or "treatment". Must not mention "cancer" or "tumor"? The prompt says not to give clinical advice. But we can mention the cell line and tissue. It's okay.

We need to incorporate the sample context: observed AUC 0.0835, predicted 12.5703, difference -12.4868, meaning observed is much lower (more sensitive). The cohort baselines: drug cohort mean 12.9659, cell cohort mean 11.3701. So the observed is far below both. So we interpret as exceptionally sensitive relative to predictions and baselines.

SHAP evidence: list top features with direction. Provide explanation: TNFRSF12A pushes toward lower AUC (sensitivity) with shap -0.6577. fp_0227 pushes toward higher AUC (resistance) +0.0985. fp_0204 pushes toward higher AUC +0.0901. fp_0062 pushes toward lower AUC -0.0887. fp_0538 pushes toward lower AUC -0.0829. fp_0504 pushes toward higher AUC +0.0438. Summarize net effect: negative contributions outweigh positive? Let's sum: negative: -0.6577 -0.0887 -0.0829 = -0.8293. Positive: +0.0985 +0.0901 +0.0438 = +0.2324. Net -0.5969. So overall pushes toward lower AUC (sensitivity). That aligns with observed.

Metadata grounding: gene recurrence counts: TNFRSF12A appears in 166 drugs. Fingerprint SMARTS: fp_0227 SMARTS [#8]-[#6@H], present in 6.7% of compounds. fp_0204 SMARTS [#6]-[#6](:[#6]):[#6]:[#6](:[#6]):[#6], present 2.9%. fp_0062 SMARTS [#6]-[#6](:[#6]):[#16], present 3.7%. fp_0538 SMARTS [#6]-[#6](:[#6]):[#6]:[#7](:[#7])-[#6], present 0.6%. fp_0504 SMARTS [#6]:[#6](=[#8]):[#7], present 4.4%. Provide examples of drugs with same fingerprints. Provide same-drug cohort examples: CAL78, SNU1079, BEN, NCIH1184. Provide same-cell cohort examples: leptomy

---

## RPT-0005 - GSK461364 on MC116
_Source evidence: SHAP-0005_

analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Use rules: lower AUC means greater sensitivity; higher AUC means greater resistance. SHAP positive pushes toward higher AUC/resistance; negative pushes toward lower AUC/sensitivity. Provide local evidence separate from global diagnostics. Use training diagnostics only as diagnostics. Provide local case evidence. Provide metadata grounding: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Provide caveats: non-causal, SHAP explains RF prediction not biology directly, separate local case evidence from global training diagnostics.

We have data: observed_auc 17.4070, predicted 7.3230, error +10.0840, global_mean_auc 12.8580. So observed is higher than predicted, meaning more resistant than model predicted. The drug is GSK461364, target PLK1 inhibitor. The cell line MC116 is B cell lymphoma. The drug cohort mean AUC 7.3729, cell cohort mean 13.0759. So the observed AUC is higher than both drug cohort mean and cell cohort mean. So it's more resistant relative to both cohorts.

Now SHAP features: top 5 features. All first four are fingerprint bits pushing toward lower AUC (sensitivity). The fifth gene TNFRSF12A pushes toward lower AUC (sensitivity). Sixth gene SYTL2 pushes toward higher AUC (resistance). So overall, the SHAP contributions: negative contributions from fingerprints and TNFRSF12A, positive from SYTL2. But the net predicted AUC is lower than observed, so the model predicted lower AUC due to negative contributions dominating. The positive contribution from SYTL2 is small (+0.1654). The negative contributions sum to about -5.79? Let's sum: -2.5354 -2.5230 -0.4914 -0.3354 -0.2506 = -6.1368. Add +0.1654 gives -5.9714. So net negative SHAP ~ -5.97, which reduces predicted AUC relative to baseline. Baseline is global mean 12.8580? Actually baseline is global mean AUC? The model predicted 7.3230, which is lower than baseline. So the SHAP contributions explain that.

Now we need to ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Provide that.

Also mention that the drug cohort context: n=770, mean_auc=7.3729, etc. The cell cohort context: n=395, mean_auc=13.0759. So the observed AUC is above both.

Also mention same-drug cohort examples: NB4, SKM1,

---

## RPT-0006 - niclosamide on IALM
_Source evidence: SHAP-0006_

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
_Source evidence: SHAP-0007_

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
_Source evidence: SHAP-0008_

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
_Source evidence: SHAP-0009_

## Executive Summary  
The Random Forest model predicts a docetaxel AUC of **7.94** for the neuroblastoma cell line **KPN

---

## RPT-0010 - RITA on TE441T
_Source evidence: SHAP-0010_

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
_Source evidence: SHAP-0011_

## Executive Summary  
GSK2636771 shows an observed AUC of **21.95** in the SUDHL10 cell line, markedly higher than the RF‑predicted AUC (**12.54**) and both drug (mean 14.24) and cell (mean 12.76) cohort baselines. The large positive prediction error (+9.41) indicates exceptional resistance in this specific sample.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The 9.41‑point excess places the sample at the

---

## RPT-0012 - dabrafenib on DU4475
_Source evidence: SHAP-0012_

## Executive Summary  
The breast ductal carcinoma cell line **DU4475** shows an **observed AUC of 0.64** for **dabrafenib**, markedly lower than the **RF‑predicted AUC of 12.75** and the **global mean AUC of 12.86**. This places the sample in the 0.3 th percentile of the drug cohort and the 80 th percentile of the cell cohort, indicating exceptional sensitivity relative to both drug‑ and cell‑specific baselines. The large negative prediction error (≈ −12.1) prompted the selection of this case for detailed SHAP analysis.

## Evidence‑Based Interpretation  
The Random Forest model attributes the low predicted AUC primarily to the expression of **TNFRSF12A (51330)**, whose SHAP contribution of **−0.51** drives the prediction toward sensitivity. Two fingerprint bits (**fp_0760** and **fp_0062**) also push the prediction downward (−0.07 and −0.05, respectively). Conversely, three fingerprint bits (**fp_0204**, **fp_0443**, **fp_0227**) contribute positively (+0.12, +0.08, +0.06), nudging the prediction toward resistance. The net effect of these local features is a strong bias toward a high‑AUC (resistant) prediction, which contrasts with the observed low AUC.

## Feature and Neighborhood Analysis  
- **TNFRSF12A (51330)**: Gene expression near the cross‑cell‑line mean; appears in 166 drug RF signatures, indicating a recurrent predictive signal across compounds.  
- **fp_0204**: SMARTS `

---

## RPT-0013 - MLN2238 on KARPAS620
_Source evidence: SHAP-0013_

## Executive Summary  
The KARPAS620 cell line treated with MLN2238 exhibited an observed AUC of **18.65**, markedly higher than the RF‑predicted AUC of **9.25** (error + 9.41). Compared with the drug cohort (mean 9.14) and the cell cohort (mean 14.45), the sample is unusually resistant. The model’s prediction was driven by several fingerprint and gene‑expression features that collectively push the AUC downward, yet the actual response suggests additional, unmodeled factors.

## Evidence‑Based Interpretation  
- **Observed vs. Predicted**: The sample’s AUC exceeds both the global mean (12.86) and the cohort means, indicating a resistant phenotype.  
- **Local Cohort Context**: Within the MLN2238 drug cohort, the sample sits at the 100th percentile; within the KARPAS620 cell cohort, it also occupies the upper tail.  
- **Model Prediction**: The RF model, trained on

---

## RPT-0014 - AZD4547 on NCIH716
_Source evidence: SHAP-0014_

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
_Source evidence: SHAP-0015_

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
_Source evidence: SHAP-0016_

analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Must not give clinical advice. Must mention that SHAP explains RF prediction, not biology. Must separate local case evidence from global training diagnostics. Must treat train_r2 etc as diagnostics only. Must not mention training diagnostics in local interpretation. Must mention that observed AUC 0.9898 vs predicted 13.0950, huge negative error. Must note that sample percentile 0.1 in drug cohort, 0.3 in cell cohort. Must mention that the drug is an inhibitor of ceramidase activity. Must mention gene targets. Must mention top SHAP features and their direction. Must ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Must note that SHAP pushes toward higher AUC for fp_0443 and TNFRSF12A, pushes toward lower AUC for fp_0227, fp_0362, fp_1009, fp_0204. Must mention that fp_0204 pushes toward higher AUC but small effect. Must mention that the local case shows sensitivity relative to cohort baselines. Must mention that the same-drug cohort examples show variable responses. Must mention that same-cell cohort examples show variable responses. Must mention that the model predicted high AUC due to features like fp_0443 and TNFRSF12A. Must mention that the observed low AUC indicates sensitivity. Must mention that the model's prediction error is large. Must mention that the per-drug CV R2 is 0.3366, moderate. Must mention that global mean AUC is 12.8580. Must mention that the drug cohort mean AUC is 11.1811. Must mention that the cell cohort mean AUC is 12.6859. Must mention that the sample percentile is 0.1 drug, 0.3 cell. Must mention that the model predicted 13.0950, close to global mean. Must mention that the observed is 0.9898, far lower. Must mention that the model predicted high resistance but actual is sensitive. Must mention that the SHAP features indicate that the drug has fingerprint bits that push toward sensitivity (fp_0227, fp_0362, fp_1009) but also bits that push toward resistance (fp_0443, TNFRSF12A). The net effect is high predicted AUC. Must mention that the local case is exceptional sensitivity relative to cohort baselines. Must mention that the evidence is non-causal. Must mention that SHAP explains RF prediction. Must mention that training diagnostics are separate. Must mention that the model's per-drug R2 is moderate. Must mention that the training diagnostics show R2 0.4928, etc. Must mention that the model uses 202

---

## RPT-0017 - LBH-589 on 253JBV
_Source evidence: SHAP-0017_

analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, caveats. Use short paragraphs, under 550 words. Use only evidence from prompt. No invented pathways. Must mention that SHAP explains RF prediction not biology. Must separate local case evidence from global training diagnostics. Must not give clinical advice. Must not mention hidden reasoning. Must use the exact headings. Must include sample context: observed AUC, predicted AUC, local cohort baselines. Must mention that observed AUC 20.4490, predicted 11.2021, error +9.2469, global mean 12.8580. Must mention that it's exceptionally resistant relative to SHAP-predicted response and cohort baselines. Must mention that drug cohort mean 5.3007, cell cohort mean 13.6723. Must mention that sample percentile 100% for drug cohort, 99.4% for cell cohort. Must mention top SHAP features and their direction. Must ground feature descriptions in local metadata: gene recurrence counts, target matches, fingerprint SMARTS, prevalence across compounds, same-drug/same-cell cohort examples. Must note that SHAP pushes toward higher or lower AUC. Must mention that PLK2 and TNFRSF12A push toward higher AUC (resistance). fp_0223, fp_0362, fp_0623, fp_0902 push toward lower AUC (sensitivity). Must mention that PLK2 expression 10.5297, z=+1.69, recurs in 102 drugs. TNFRSF12A expression 7.8195, z=+0.62, recurs in 166 drugs. Must mention fingerprint bits prevalence percentages. Must mention SMARTS. Must mention same-drug cohort examples: KMS26, SEM, TE441T, HUCCT1. Must mention same-cell cohort examples: ouabain, leptomycin B, triazolothiadiazine, ML203. Must mention that the drug is HDAC inhibitor. Must mention that the cell line is transitional cell carcinoma of urinary tract. Must mention that the model's per-drug CV R2 is 0.2277. Must mention training diagnostics but treat them as diagnostics only. Must mention that the model's global mean AUC is 12.8580. Must mention that the observed AUC is above global mean. Must mention that the prediction error is large. Must mention that the SHAP explanation indicates that the high PLK2 and TNFRSF12A expression contributed to higher predicted AUC, but the fingerprint bits contributed to lower predicted AUC. Must mention that the net predicted AUC is lower than observed, indicating resistance. Must mention that the local case evidence is separate from global training diagnostics. Must mention that the SHAP explanation is for the RF prediction, not biology. Must mention that the model's per-drug R2 is low, so predictions may be uncertain. Must mention that the

---

## RPT-0018 - foretinib on EBC1
_Source evidence: SHAP-0018_

## Executive Summary  
Foretinib shows an **exceptionally low AUC (0.8572)** in the EBC1 squamous‑cell carcinoma line, far below the **RF‑predicted AUC of 12.92** and the **cell‑line cohort mean (12.74)**. The observed sensitivity places EBC1 at the 0.5th percentile of all cell lines tested with foretinib, underscoring a pronounced deviation from the model’s expectation.

## Evidence‑Based Interpretation  
The large negative prediction error (-12.06) indicates that the model overestimates resistance for this sample. The SHAP analysis attributes this discrepancy to a combination of gene expression and chemical fingerprint signals that collectively lower the predicted AUC. The overall interpretation is that EBC1 is **highly sensitive** to foretinib relative to both the drug’s global performance

---

## RPT-0019 - 1S,3R-RSL-3 on CAL62
_Source evidence: SHAP-0019_

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
_Source evidence: SHAP-0020_

analysisWe need to produce a markdown report with headings: Executive Summary, Evidence-Based Interpretation, Feature and Neighborhood Analysis, Model-Level Context, Confidence and Caveats. Must follow Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats. Use short paragraphs, under 550 words. Use only evidence provided. No invented pathways. Must not give clinical advice. Must not mention training diagnostics as generalization. Must separate local case evidence from global training diagnostics. Must treat train_r2 etc as diagnostics only. Must not mention any other info. Must use the given data.

We need to explain observed response of PHA-793887 on SNU398 using observed AUC, RF predicted AUC, local drug/cell cohort baselines. Observed AUC 1.5525, predicted 13.5394, error -11.9869. Cohort baselines: drug cohort mean 11.4834, cell cohort mean 12.6859. So observed is far lower, indicating high sensitivity relative to predictions and baselines. Provide interpretation: exceptionally sensitive relative to SHAP-predicted response and cohort baselines.

SHAP evidence: list top features with direction. Provide each feature and whether pushes toward higher AUC/resistance or lower AUC/sensitivity. Provide shap values.

Metadata grounding: ground feature descriptions in local metadata only: gene recurrence counts, target matches, fingerprint SMARTS annotations, prevalence across compounds, same-drug/same-cell cohort examples. Use the provided data: e.g., fp_0443 SMARTS, prevalence 0.4%, example drugs nilotinib, bleomycin A2. TNFRSF12A gene expression value 6.1374, z -0.05, supporting drugs 166. fp_1009 SMARTS, prevalence 9.1%, example drugs betulinic acid etc. fp_0367 SMARTS, prevalence 6.4%. fp_0623 SMARTS, prevalence 5.8%. fp_0062 SMARTS, prevalence 3.7%. Provide same-drug cohort examples: EOL1, OCIAML3, DMS454, KPL1 with AUCs. Same-cell cohort examples: ceranib-2, tosedostat, erlotinib, abiraterone with AUCs.

Model-level context: global mean AUC 12.8580, training diagnostics: train_r2 0.4928, train_rmse 1.8342, train_corr 0.7061. Also per-drug cross-validated R2 0.3621. Provide that these are diagnostics only. Provide global fingerprint features list. Provide most common genes across predictable per-drug models. Provide that the model predicted high AUC due to features like fp_0443 etc.

Confidence and Caveats: note non-causal, SHAP explains RF prediction not biology directly, separate local case evidence from global training diagnostics. Note that prediction error large, but local evidence shows features pushing toward sensitivity. Note that training diagnostics not generalization. Provide caveats about limited sample size, etc.

Word count: keep under

---

## RPT-0021 - KU-0063794 on SKMEL2
_Source evidence: SHAP-0021_

## Executive Summary  
KU‑0063794 shows an observed AUC of **21.23** in the SKMEL2 melanoma line, markedly higher than the RF‑predicted AUC of **12.30** and the cohort baselines (drug mean ≈ 11.85, cell mean ≈ 14.22). The prediction error (+8.93) places this case at the 100th percentile of drug‑specific errors, indicating exceptional resistance relative to both the model and the broader drug/cell populations.

## Evidence‑Based Interpretation  
The RF model attributes the low predicted AUC largely to several fingerprint bits that favor sensitivity:  
- **fp_0202** (SMARTS `[#6]:[#6](-[#8]):[#6]`) contributes **–0.42** toward lower AUC; present in 7.3 % of CTRPv2 compounds.  
- **fp_0623**, **fp_0227**, **fp_0771**, and **fp_0722** each add between **–0.09

---

## RPT-0022 - BRD-K99006945 on JHUEM1
_Source evidence: SHAP-0022_

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
_Source evidence: SHAP-0023_

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
_Source evidence: SHAP-0024_

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
_Source evidence: SHAP-0025_

## Executive Summary  
The kidney carcinoma cell line **TUHR10TKB** shows an **observed AUC of 29.35** for the cardiac glycoside **ouabain**, markedly higher than the **RF‑predicted AUC of 20.62** and the cohort baselines (drug mean ≈ 5.85, cell mean ≈ 13.75). The prediction error (+8.73) places this sample at the 100th percentile of both drug and cell cohorts, indicating exceptional resistance relative to the

---
