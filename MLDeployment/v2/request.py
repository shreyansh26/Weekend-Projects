import requests

to_predict_dict = {"sepal_l": 5, "sepal_w": 2, "petal_l": 3, "petal_w": 4}

url = 'http://127.0.0.1:8000/iris/classify_iris'
r = requests.post(url, json=to_predict_dict);
print(r.json())