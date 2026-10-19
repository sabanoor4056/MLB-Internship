# 1. Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
import matplotlib.pyplot as plt
# 2. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# 3. Explore the dataset
print("Dataset Shape:", X.shape)
print("Feature Names:", iris.feature_names)
print("Target Classes:", iris.target_names)
print("\nFirst 5 rows:")
print(X[:5])
print("\nFirst 5 target values:")
print(y[:5])
# 4. Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
# 5. Create and train Logistic Regression model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)
print("\nModel training completed!")
# 6. Make predictions
y_pred = model.predict(X_test)
# 7. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test, y_pred, average="weighted"
)
recall = recall_score(
    y_test, y_pred, average="weighted"
)
f1 = f1_score(
    y_test, y_pred, average="weighted"
)
print("\n--- Model Evaluation Results ---")
print(f"Accuracy:  {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1-Score:  {f1:.2f}")
# 8. Show detailed classification report
print("\n--- Classification Report ---")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))
# 9. Generate confusion matrix
cm = confusion_matrix(
    y_test, y_pred, labels=[0, 1, 2]
)
print("\n--- Confusion Matrix ---")
print(cm)
# 10. Display and save confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
display.plot(cmap="Blues")
plt.title("Iris Flower Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.show()
# 11. Compare actual and predicted values
print("\n--- Actual vs Predicted ---")
for i in range(10):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[y_pred[i]]
    print(f"Actual: {actual:12} Predicted: {predicted}")
