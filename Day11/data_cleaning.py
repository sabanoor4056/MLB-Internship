import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# 1. LOAD THE DATASET
df = pd.read_csv(r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day6\student performance\student_performance.csv")
print("Original Dataset:")
print(df.head())
# 2. CHECK MISSING VALUES
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# Fill missing subject marks with the average of that subject
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]
for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())
# 3. REMOVE DUPLICATE RECORDS
df = df.drop_duplicates()
print("\nDuplicate Records Removed.")
# 4. RENAME A COLUMN
df = df.rename(columns={"Name": "Student_Name"})
print("\nColumns Renamed.")
# 5. CREATE AVERAGE_SCORE COLUMN
df["Average_Score"] = df[subjects].mean(axis=1)
print("\nAverage Score Added.")
# 6. CREATE PERFORMANCE COLUMN
def check_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    else:
        return "Needs Improvement"
df["Performance"] = df["Average_Score"].apply(check_performance)
print("\nStudent Performance Added.")
# 7. SAVE THE CLEANED DATASET
folder = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(folder, "cleaned_student_performance.csv")
df.to_csv(output_file, index=False)