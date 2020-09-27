import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle


class IrisClassifier:
    def __init__(self):
        iris = load_iris()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(iris.data, iris.target, test_size=0.1)
        self.clf = self.train_model()
        self.iris_types = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self) -> AdaBoostClassifier:
        return AdaBoostClassifier(n_estimators=5).fit(self.X_train, self.y_train)

    def classify(self, features: dict):
        X = [features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]
        prediction = self.clf.predict_proba([X]).tolist()
        return {'class': self.iris_types[np.argmax(prediction)], 'probability': prediction}