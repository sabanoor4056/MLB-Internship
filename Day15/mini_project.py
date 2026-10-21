import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Create graphs folder
folder = os.path.dirname(os.path.abspath(__file__))
graph_folder = os.path.join(folder, "graphs")
os.makedirs(graph_folder, exist_ok=True)
# Step 1: Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["Species"] = [iris.target_names[i] for i in iris.target]
print("First 5 rows:")
print(df.head())
print("\nDataset shape:")
print(df.shape)
print("\nMissing values:")
print(df.isnull().sum())
# Step 2: Select two features
X = df[["petal length (cm)", "petal width (cm)"]]
# Step 3: Elbow Method
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.savefig(os.path.join(graph_folder, "elbow_method.png"))
plt.close()
# Step 4: Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=df["Cluster"])
plt.title("K-Means Clusters")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.savefig(os.path.join(graph_folder, "kmeans_clusters.png"))
plt.close()
# Step 5: Original species visualization
for species in iris.target_names:
    data = df[df["Species"] == species]
    plt.scatter(
        data["petal length (cm)"],
        data["petal width (cm)"],
        label=species
    )
plt.title("Original Iris Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.savefig(os.path.join(graph_folder, "original_species.png"))
plt.close()
# Step 6: Apply PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(iris.data)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# Visualize PCA using K-Means cluster labels
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["Cluster"])
plt.title("PCA Visualization of K-Means Clusters")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.savefig(os.path.join(graph_folder, "pca_visualization.png"))
plt.close()
# Step 7: Display results
print("\nNumber of clusters:", df["Cluster"].nunique())
print("PCA explained variance:",
      round(pca.explained_variance_ratio_.sum() * 100, 2), "%")
print("\nProject completed!")
print("Graphs saved inside the graphs folder.")
