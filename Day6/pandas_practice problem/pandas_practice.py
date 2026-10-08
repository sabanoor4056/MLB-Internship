import pandas as pd
# =========================
# PANDAS PRACTICE
# =========================

print("\n\n===== PANDAS =====")

# Create a sample student dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 75, 95, 80],
}

df = pd.DataFrame(data)

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
    
# Add Grade column
df["Grade"] = df["Marks"].apply(calculate_grade)
print(df)

# Save dataset as CSV
df.to_csv("students.csv", index=False)
print("\nDataset:")
print(df)

# 1. Load CSV dataset
df = pd.read_csv("students.csv")
print("\nCSV Dataset Loaded:")
print(df)

# 2. Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# 3. Display last five rows
print("\nLast Five Rows:")
print(df.tail())

# 4. Display dataset information
print("\nDataset Information:")
df.info()

# 5. Find missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Filter data
print("\nStudents with marks greater than 80:")
print(df[df["Marks"] > 80])

# 7. Summary statistics
print("\nSummary Statistics:")
print(df.describe())