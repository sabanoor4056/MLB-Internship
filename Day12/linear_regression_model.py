import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
folder = Path(__file__).parent
# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day6\student performance\student_performance.csv")
# Input features (X) and target (y)
df = pd.read_csv(folder / "student_performance.csv")
# Create Average_Score if it does not exist
subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine_Learning"
]
if "Average_Score" not in df.columns:
    df["Average_Score"] = df[subjects].mean(axis=1)
# Select features and target
X = df[["Age", "Program", "Attendance"]]
y = df["Average_Score"]
# Identify categorical and numerical columns
categorical_features = ["Program"]
numerical_features = ["Age", "Attendance"]
# Convert Program categories into numerical columns
preprocessor = ColumnTransformer([
    ("category", OneHotEncoder(handle_unknown="ignore"),
     categorical_features),
    ("numbers", "passthrough", numerical_features)
])
# Create the complete Machine Learning pipeline
model = make_pipeline(
    preprocessor,
    LinearRegression()
)
# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)
# Train the model
model.fit(X_train, y_train)
# Predict scores for test data
predictions = model.predict(X_test)
# Compare actual and predicted scores
comparison = pd.DataFrame({
    "Actual_Score": y_test.values,
    "Predicted_Score": predictions.round(2)
})
print("\nActual vs Predicted Scores:")
print(comparison)
# Calculate evaluation metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("\nModel Evaluation:")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")
# Save comparison table
comparison.to_csv(
    folder / "prediction_results.csv",
    index=False
)
# Create graphs folder
graph_folder = folder / "graphs"
graph_folder.mkdir(exist_ok=True)
# Plot actual vs predicted scores
plt.figure(figsize=(7, 5))
plt.scatter(y_test, predictions)
# Reference line for perfect predictions
minimum = min(y_test.min(), predictions.min())
maximum = max(y_test.max(), predictions.max())
plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--"
)
plt.xlabel("Actual Average Score")
plt.ylabel("Predicted Average Score")
plt.title("Actual vs Predicted Student Scores")
plt.tight_layout()
plt.savefig(
    graph_folder / "actual_vs_predicted.png"
)
plt.show()
plt.close()
print("\nPrediction table saved.")
print("Graph saved in the graphs folder.")
