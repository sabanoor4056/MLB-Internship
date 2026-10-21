import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os
folder = os.path.dirname(os.path.abspath(__file__))
graph_folder = os.path.join(folder, "graphs")
os.makedirs(graph_folder, exist_ok=True)
# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
# Reduce 4 features to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# Create DataFrame
pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
# Visualize PCA data
plt.scatter(pca_df["PC1"], pca_df["PC2"])
plt.title("Iris PCA Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.savefig(os.path.join(graph_folder, "pca_visualization.png"))
plt.show()
print("Original features:", df.shape[1])
print("PCA features:", pca_df.shape[1])
print("Explained variance:", pca.explained_variance_ratio_.sum())
