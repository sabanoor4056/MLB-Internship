import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Create baseline model
baseline = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=5000)
)
# Train baseline
baseline.fit(X_train, y_train)
baseline_pred = baseline.predict(X_test)
# Create parameter search
parameters = {
    "logisticregression__C": [0.01, 0.1, 1, 10, 100]
}
grid = GridSearchCV(
    baseline,
    parameters,
    cv=5,
    scoring="accuracy"
)
# Train tuned model
grid.fit(X_train, y_train)
tuned_pred = grid.predict(X_test)
# Evaluation function
def evaluate_model(name, actual, predicted):
    print("\n", name)
    print("Accuracy:", accuracy_score(actual, predicted))
    print("Precision:", precision_score(actual, predicted))
    print("Recall:", recall_score(actual, predicted))
    print("F1-Score:", f1_score(actual, predicted))
# Show results
evaluate_model("BASELINE MODEL", y_test, baseline_pred)
evaluate_model("TUNED MODEL", y_test, tuned_pred)
print("\nBest Parameters:")
print(grid.best_params_)
# Compare model accuracy
comparison = pd.DataFrame({
    "Model": ["Baseline", "Tuned"],
    "Accuracy": [
        accuracy_score(y_test, baseline_pred),
        accuracy_score(y_test, tuned_pred)
    ],
    "F1-Score": [
        f1_score(y_test, baseline_pred),
        f1_score(y_test, tuned_pred)
    ]
})
print("\nModel Comparison:")
print(comparison)
# Create confusion matrix for tuned model
cm = confusion_matrix(y_test, tuned_pred)
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=data.target_names,
    yticklabels=data.target_names
)
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Breast Cancer Prediction - Tuned Model")
plt.tight_layout()
# Save image inside Day-14
folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(folder, "confusion_matrix.png")
plt.savefig(image_path)
plt.close()
print("\nConfusion matrix saved to:", image_path)