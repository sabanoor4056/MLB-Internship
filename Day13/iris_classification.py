# STEP 1: Import libraries
import os
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
# STEP 2: Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
print("=" * 50)
print("IRIS FLOWER CLASSIFICATION SYSTEM")
print("=" * 50)
# STEP 3: Explore the dataset
print("\nDataset Shape:", X.shape)
print("\nFeature Names:")
print(iris.feature_names)
print("\nFlower Species:")
print(iris.target_names)
print("\nFirst 5 Flower Measurements:")
print(X[:5])
print("\nFirst 5 Target Values:")
print(y[:5])
# STEP 4: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))
# STEP 5: Train Logistic Regression
logistic_model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
logistic_model.fit(X_train, y_train)
print("\nLogistic Regression Training Completed!")
# STEP 6: Predict flower species
y_pred = logistic_model.predict(X_test)
# STEP 7: Evaluate Logistic Regression
print("\n--- LOGISTIC REGRESSION RESULTS ---")
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

print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-Score:  {f1:.2%}")
print("\nDetailed Classification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))
# STEP 8: Show Confusion Matrix
cm = confusion_matrix(
    y_test, y_pred, labels=[0, 1, 2]
)
print("\nConfusion Matrix:")
print(cm)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
disp.plot(cmap="Blues")
plt.title("Iris Flower - Logistic Regression")
plt.tight_layout()
folder = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(folder, "iris confusion_matrix.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
print("iris Confusion Matrix saved at:", save_path)
plt.show()
# STEP 9: Print actual vs predicted species
print("\n--- SAMPLE PREDICTIONS ---")
for i in range(min(10, len(y_test))):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[y_pred[i]]

    print(f"Actual: {actual:12} | Predicted: {predicted}")

# STEP 10: Predict a new flower
# Measurements: sepal length, sepal width,
# petal length, petal width (in centimeters)
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = logistic_model.predict(new_flower)[0]
print("\n--- NEW FLOWER PREDICTION ---")
print("Flower Measurements:", new_flower[0])
print("Predicted Species:", iris.target_names[prediction])
# STEP 11: BONUS - Decision Tree
tree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
tree_model.fit(X_train, y_train)
tree_pred = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_pred)
tree_precision = precision_score(
    y_test, tree_pred, average="weighted"
)
tree_recall = recall_score(
    y_test, tree_pred, average="weighted"
)
tree_f1 = f1_score(
    y_test, tree_pred, average="weighted"
)
print("\n--- MODEL COMPARISON ---")
print(f"{'Metric':<15}{'Logistic Regression':<23}{'Decision Tree'}")
print(f"{'Accuracy':<15}{accuracy:.2%}{'':<19}{tree_accuracy:.2%}")
print(f"{'Precision':<15}{precision:.2%}{'':<19}{tree_precision:.2%}")
print(f"{'Recall':<15}{recall:.2%}{'':<19}{tree_recall:.2%}")
print(f"{'F1-Score':<15}{f1:.2%}{'':<19}{tree_f1:.2%}")
print("\nProject Completed Successfully!")
