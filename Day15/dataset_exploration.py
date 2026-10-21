import pandas as pd
from sklearn.datasets import load_iris
# Load dataset
iris = load_iris()
# Convert into DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Display first 5 rows
print("First 5 rows:")
print(df.head())
# Display dataset information
print("\nDataset Information:")
print(df.info())
# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())
# Display dataset shape
print("\nRows and Columns:")
print(df.shape)
# Display flower species
print("\nFlower Species:")
print(iris.target_names)
