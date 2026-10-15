import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Read cleaned dataset
folder = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(folder, "cleaned_student_performance.csv")
)
# Create charts folder
charts_folder = os.path.join(folder, "charts")
os.makedirs(charts_folder, exist_ok=True)
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]
# Select student name column
if "Student_Name" in df.columns:
    name_column = "Student_Name"
else:
    name_column = "Name"
# Create Average_Score if it does not exist
if "Average_Score" not in df.columns:
    df["Average_Score"] = df[subjects].mean(axis=1)
# Create Performance if it does not exist
if "Performance" not in df.columns:
    def get_performance(score):
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Good"
        elif score >= 70:
            return "Average"
        else:
            return "Needs Improvement"

    df["Performance"] = df["Average_Score"].apply(get_performance)
# 1. Total students
print("\nSTUDENT PERFORMANCE DASHBOARD")
print("=" * 35)
print("\n1. Total number of students:")
print(len(df))
# 2. Average score for each subject
print("\n2. Average marks by subject:")
subject_averages = df[subjects].mean().round(2)
print(subject_averages)
# 3. Top 5 students
print("\n3. Top 5 performing students:")
top_students = df.nlargest(5, "Average_Score")
print(top_students[[name_column, "Average_Score", "Performance"]])
# 4. Students who need improvement
print("\n4. Students who need improvement:")
needs_improvement = df[df["Average_Score"] < 70]
if needs_improvement.empty:
    print("No students have an average below 70.")
else:
    print(
        needs_improvement[
            [name_column, "Average_Score", "Performance"]
        ]
    )

# 5. Subject with the highest class average
print("\n5. Subject with the highest class average:")
best_subject = subject_averages.idxmax()
best_average = subject_averages.max()
print(best_subject, ":", best_average)
# 6. Performance category counts
print("\n6. Students in each performance category:")
print(df["Performance"].value_counts())
# 7. Average Marks by Subject Chart
plt.figure(figsize=(9, 5))
plt.bar(subject_averages.index, subject_averages.values)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(
    os.path.join(charts_folder, "average_marks_by_subject.png")
)
plt.close()
# 8. Top 5 Students Chart
top_students = df.nlargest(5, "Average_Score")
plt.figure(figsize=(9, 5))
plt.bar(
    top_students[name_column].astype(str),
    top_students["Average_Score"]
)
plt.title("Top 5 Students by Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    os.path.join(charts_folder, "top_5_students.png")
)
plt.close()
print("\nBoth charts saved successfully!")
print("Dashboard analysis completed!")
