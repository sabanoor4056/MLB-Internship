import pandas as pd
from pathlib import Path
# Find the folder where this Python file is saved
folder = Path(__file__).parent
# Load dataset
df = pd.read_csv(r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day6\student performance\student_performance.csv")
print("Original Dataset:")
print(df.head())
# Remove duplicate rows
df = df.drop_duplicates()
# Remove rows with missing subject scores
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]
df = df.dropna(subset=subjects)
# Create Average_Score column
df["Average_Score"] = df[subjects].mean(axis=1)
# Save cleaned dataset
df.to_csv(folder / "student_performance.csv", index=False)
print("\nCleaned Dataset:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nAverage_Score column created successfully!")
print("Cleaned dataset saved.")
