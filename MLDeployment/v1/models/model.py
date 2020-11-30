import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

iris = load_iris()
ada = AdaBoostClassifier(n_estimators=5)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)
model = ada.fit(X_train, y_train)

print("Model score: ", ada.score(X_train, y_train))
print("Test Accuracy: ", ada.score(X_test, y_test))

pickle.dump(model, open("model.pkl", "wb"))