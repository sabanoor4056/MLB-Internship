# Day-14: Breast Cancer Prediction System
## Project Overview
This project uses the Breast Cancer Wisconsin Dataset from Scikit-learn to classify tumors as malignant or benign using Logistic Regression.
## Tasks Completed
- Loaded and explored the dataset using Pandas.
- Split the dataset into training and testing sets.
- Trained a baseline Logistic Regression model.
- Evaluated Accuracy, Precision, Recall, and F1-Score.
- Generated a Confusion Matrix.
- Used GridSearchCV for hyperparameter tuning.
- Compared baseline and tuned model performance.
- Generated a confusion matrix heatmap.
## Hyperparameter Tuning
GridSearchCV tested different values of `C` using 5-fold cross-validation to find the best model configuration.
## Model Evaluation
The baseline and tuned models were evaluated using the same test dataset. Their accuracy and F1-score were compared to observe whether tuning improved performance.
## Best Parameters
The best parameters are printed automatically when `hyperparameter_tuning.py` or `prediction_pipeline.py` runs.
## Key Learnings
- Learned how to explore a dataset using Pandas.
- Understood classification and model evaluation metrics.
- Learned how to split data into training and testing sets.
- Understood hyperparameter tuning using GridSearchCV.
- Learned to compare baseline and tuned models.
- Generated and saved a confusion matrix heatmap.
## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
## Project Files
- `dataset_exploration.py` — Dataset exploration.
- `baseline_model.py` — Baseline Logistic Regression model.
- `hyperparameter_tuning.py` — GridSearchCV and model comparison.
- `prediction_pipeline.py` — Complete prediction and evaluation pipeline.
- `confusion_matrix.png` — Confusion matrix heatmap.
- `README.md` — Project documentation.
## How to Run
Install the required libraries:
```bash
pip install pandas scikit-learn matplotlib seaborn
```
Run the Python files:
```bash
python dataset_exploration.py
python baseline_model.py
python hyperparameter_tuning.py
python prediction_pipeline.py
```
## Important Note
This project is for educational purposes only and is not intended for medical diagnosis.