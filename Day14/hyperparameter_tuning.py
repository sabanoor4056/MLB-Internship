from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Create baseline model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=5000)
)
# Train baseline model
model.fit(X_train, y_train)
baseline_pred = model.predict(X_test)
print("Baseline Accuracy:", accuracy_score(y_test, baseline_pred))
print("Baseline F1-Score:", f1_score(y_test, baseline_pred))
# Parameters to test
parameters = {
    "logisticregression__C": [0.01, 0.1, 1, 10, 100]
}
# Search for the best parameter
grid = GridSearchCV(
    model,
    parameters,
    cv=5,
    scoring="accuracy"
)
grid.fit(X_train, y_train)
# Predict using the best model
tuned_pred = grid.predict(X_test)
print("\nBest Parameters:", grid.best_params_)
print("Tuned Accuracy:", accuracy_score(y_test, tuned_pred))
print("Tuned F1-Score:", f1_score(y_test, tuned_pred))