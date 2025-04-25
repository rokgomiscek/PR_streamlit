from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pickle

iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
knn.classes_ = iris.target_names

with open("pkl/model.pkl", 'wb') as fp:
    pickle.dump(knn, fp)