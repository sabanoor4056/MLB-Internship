# Day 12 — Student Score Prediction System
## Overview
This project uses Python and Scikit-learn to predict student average scores using Linear Regression.
## Tasks Completed
- Loaded and cleaned the student performance dataset.
- Removed duplicate rows and rows with missing subject scores.
- Created the `Average_Score` column.
- Selected input features and target variable.
- Applied One-Hot Encoding to categorical data.
- Split the dataset into 80% training and 20% testing data.
- Trained a Linear Regression model.
- Generated predictions and compared actual versus predicted scores.
- Visualized prediction results using a scatter plot.
## Evaluation Metrics
- Mean Absolute Error (MAE): [Add your result]
- Mean Squared Error (MSE): [Add your result]
- R² Score: [Add your result]
## Observations
The model was evaluated on the testing dataset. The results show how accurately it predicted student average scores using age, program, and attendance.
The dataset is small, so the evaluation results may not represent performance on a larger dataset.
## What I Learned
- Data preprocessing and handling missing values.
- Features, target variables, and categorical encoding.
- Train-test splitting and data leakage.
- Training a Linear Regression model using Scikit-learn.
- Evaluating a model with MAE, MSE, and R².
- Visualizing actual and predicted values.
## Tools Used
Python, Pandas, Scikit-learn, Matplotlib.
## How to Run
1. Install the required libraries.
2. Place `student_performance.csv` in the Day-12 folder.
3. Run `python student_score_prediction.py`.
