import pandas as pd
import os

# Get the folder where this Python file is located
folder = os.path.dirname(__file__)
# Find the CSV file in the same folder
file_path = os.path.join(folder, "student_performance.csv")

# Load dataset
df = pd.read_csv(file_path)
print("===== STUDENT PERFORMANCE ANALYSIS =====")
print("\nFirst 5 Students:")
print(df.head())
print("\nLast 5 Students:")
print(df.tail())
print("\nDataset Information:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())
print("\nTotal Number of Students:")
print(len(df))

# Subjects
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]

# Average marks
print("\nAverage Marks:")
for subject in subjects:
    print(subject, ":", df[subject].mean())

# Student average
df["Average"] = df[subjects].mean(axis=1)

# Top 5 students
print("\nTop 5 Performing Students:")
top_5 = df.sort_values("Average", ascending=False).head(5)
print(top_5[["Student_ID", "Name", "Average"]])

# Class average
class_average = df["Average"].mean()
print("\nClass Average:")
print(class_average)

# Below average
print("\nStudents Below Class Average:")
below_average = df[df["Average"] < class_average]
print(below_average[["Student_ID", "Name", "Average"]])

# Save processed dataset
output_file = os.path.join(folder, "student_performance_processed.csv")
df.to_csv(output_file, index=False)
print("\nProcessed dataset saved successfully!")