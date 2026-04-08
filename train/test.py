import pandas as pd

df = pd.read_csv("/sc/arion/projects/lin_lab/complexbehavior/drug_efficacy/data/processed/pairs.csv")

# Load additional required files
cell_features = pd.read_csv("/sc/arion/projects/lin_lab/complexbehavior/drug_efficacy/data/processed/cell_features_selected.csv")
drug_fingerprints = pd.read_csv("/sc/arion/projects/lin_lab/complexbehavior/drug_efficacy/data/processed/drug_fingerprints.csv")

# Merge pairs with cell_features on 'cell_id' (assumed first column in pairs as 'cell_id', adjust if column names are present)
df_merged = df.merge(
    cell_features, left_on=df.columns[0], right_on=cell_features.columns[0], how='left'
)
# Merge with drug_fingerprints on 'drug_id' (assumed second column in pairs as 'drug_id')
df_merged = df_merged.merge(
    drug_fingerprints, left_on=df.columns[1], right_on=drug_fingerprints.columns[0], how='left'
)

mem_usage = df_merged.memory_usage(deep=True).sum()
print(f"Combined merged DataFrame memory size: {mem_usage / (1024 ** 2):.2f} MB")