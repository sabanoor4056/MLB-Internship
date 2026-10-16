import subprocess
import sys
from pathlib import Path
folder = Path(__file__).parent
print("STUDENT SCORE PREDICTION SYSTEM")
print("=" * 35)
# Step 1: Prepare the dataset
print("\nStep 1: Data Preprocessing")
subprocess.run(
    [sys.executable, str(folder/"data_preprocessing.py")],
    check=True
)
# Step 2: Train and evaluate the model
print("\nStep 2: Machine Learning Model")
subprocess.run(
    [sys.executable, str(folder/"linear_regression_model.py")],
    check=True
)
print("\nProject completed successfully!")
