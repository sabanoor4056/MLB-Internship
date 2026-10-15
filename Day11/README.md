# Day-11: Student Performance Dashboard
## Project Overview
This project analyzes student performance using Python, Pandas, Matplotlib, and Seaborn. It cleans the dataset, calculates average scores, categorizes student performance, and visualizes the results.
## Data Cleaning
- Checked missing values.
- Removed duplicate records.
- Renamed the student name column.
- Filled missing subject marks using subject averages.
- Calculated `Average_Score`.
- Created `Performance` categories: Excellent, Good, Average, and Needs Improvement.
- Saved the cleaned dataset as `cleaned_student_performance.csv`.
## Visualizations
Six charts were created:
1. **Bar Chart:** Compares students' average scores.
2. **Histogram:** Shows the distribution of average scores.
3. **Scatter Plot:** Compares Python and Machine Learning marks.
4. **Pie Chart:** Shows the percentage of students in each performance category.
5. **Box Plot:** Displays the spread of marks across subjects.
6. **Subject Average Chart:** Compares average marks across subjects.
All charts are saved as PNG images in the `charts` folder.
## Key Insights
1. **Top performers:** Identified the five students with the highest average scores.
2. **Student improvement:** Identified students whose average score is below 70.
3. **Subject performance:** Identified the subject with the highest class average.
*Note: The specific findings can be confirmed by running `student_dashboard.py` on the dataset.*
## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
## How to Run
1. Install the required libraries: `pip install pandas matplotlib seaborn`
2. Run `data_cleaning.py`.
3. Run `data_visualization.py`.
4. Run `student_dashboard.py`.
## Project Deliverables
- Data cleaning script
- Data visualization script
- Student dashboard script
- Cleaned CSV dataset
- Six generated charts
- README documentation
- Project screen recording