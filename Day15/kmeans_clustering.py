import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import os
# Create graphs folder
folder = os.path.dirname(os.path.abspath(__file__))
graph_folder = os.path.join(folder, "graphs")
os.makedirs(graph_folder, exist_ok=True)
# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Use petal length and petal width
X = df[["petal length (cm)", "petal width (cm)"]]
# Elbow Method
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.savefig(os.path.join(graph_folder, "elbow_method.png"))
plt.show()
# Apply K-Means with 3 clusters
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)
# Visualize clusters
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=df["Cluster"])
plt.title("Iris K-Means Clusters")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.savefig(os.path.join(graph_folder, "kmeans_clusters.png"))
plt.show()
print("Number of clusters:", df["Cluster"].nunique())
print(df[["petal length (cm)", "petal width (cm)", "Cluster"]].head())
