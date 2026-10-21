# Day-15: Iris Flower Clustering & PCA
## Objective
To group similar Iris flowers using K-Means and visualize the data using PCA.
## What is Clustering?
Clustering is an unsupervised learning technique that groups similar data points together.
## What is PCA?
PCA reduces the number of features while keeping as much important information as possible.
## Tools Used
- Python
- Pandas
- Matplotlib
- Scikit-learn
## Implementation
1. Loaded and explored the Iris dataset.
2. Applied the Elbow Method to examine the best number of clusters.
3. Applied K-Means with K = 3.
4. Reduced four features to two using PCA.
5. Generated graphs for the original species, clusters, Elbow Method, and PCA.
## Observations
- K-Means formed three clusters.
- Setosa is generally easier to separate than Versicolor and Virginica.
- Clusters do not always match the actual flower species perfectly.
- PCA made the four-dimensional data easier to visualize in two dimensions.
## Conclusion
Successfully implemented K-Means clustering and PCA using the Iris dataset and generated visualizations to understand the results.