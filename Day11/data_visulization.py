import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# 1. SET FOLDER PATHS
day11_folder = r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day11"
csv_file = os.path.join(day11_folder, "cleaned_student_performance.csv")
charts_folder = os.path.join(day11_folder, "charts")
# Create charts folder inside Day11
os.makedirs(charts_folder, exist_ok=True)
# 2. LOAD DATASET
df = pd.read_csv(r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day6\student performance\student_performance.csv")
print("Dataset loaded successfully!")
print("Columns:", df.columns.tolist())
# 3. SET STUDENT NAME COLUMN
if "Student_Name" in df.columns:
    name_column = "Student_Name"
elif "Name" in df.columns:
    name_column = "Name"
else:
    name_column = None
# 4. SUBJECT COLUMNS
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]
# Check whether subject columns exist
for subject in subjects:
    if subject not in df.columns:
        raise ValueError(f"Column '{subject}' is missing from the CSV file.")

# Calculate Average_Score if it is missing
if "Average_Score" not in df.columns:
    df["Average_Score"] = df[subjects].mean(axis=1)
# 5. BAR CHART
# Average marks of each student
if name_column is not None:
    plt.figure(figsize=(10, 5))
    plt.bar(df[name_column].astype(str), df["Average_Score"])
    plt.title("Average Marks of Students")
    plt.xlabel("Student Name")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_folder, "bar_chart.png"))
    plt.close()
    print("Bar chart saved!")
else:
    print("Bar chart skipped: Student name column not found.")
# 6. HISTOGRAM
# Distribution of Average Scores
plt.figure(figsize=(8, 5))
plt.hist(df["Average_Score"].dropna(), bins=5, edgecolor="black")
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, "histogram.png"))
plt.close()
print("Histogram saved!")
# 7. SCATTER PLOT
# Python vs Machine Learning
plt.figure(figsize=(8, 5))
plt.scatter(df["Python"], df["Machine_Learning"])
plt.title("Python vs Machine Learning Marks")
plt.xlabel("Python Marks")
plt.ylabel("Machine Learning Marks")
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, "scatter_plot.png"))
plt.close()
print("Scatter plot saved!")
# 8. PIE CHART
# Student Performance Distribution
# Create Performance column if it does not exist
if "Performance" not in df.columns:
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
# Count students in each category
performance_count = df["Performance"].value_counts()
# Create and save pie chart
plt.figure(figsize=(7, 7))
plt.pie(
    performance_count,
    labels=performance_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Performance Distribution")
plt.tight_layout()
plt.savefig(
    os.path.join(charts_folder, "pie_chart.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close()
print("Pie chart saved successfully!")
# 9. BOX PLOT
# Spread of marks in all subjects
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[subjects])
plt.title("Marks Distribution Across All Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, "box_plot.png"))
plt.close()
print("Box plot saved!")
# 10. COMPLETION MESSAGE
print("\nAll available charts have been saved!")
print("Charts folder:", charts_folder)
