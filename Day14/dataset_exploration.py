import pandas as pd
from sklearn.datasets import load_breast_cancer
# Load dataset
data = load_breast_cancer()
# Convert dataset into DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
# Add target column
df["target"] = data.target
# Explore dataset
print("First 5 Rows:")
print(df.head())
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
print(df.describe())
# Check target class distribution
print("\nTarget Class Distribution:")
print(df["target"].value_counts())
print("\nClass Names:")
print(data.target_names)