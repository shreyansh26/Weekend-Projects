import requests

to_predict_dict = {
    "data": [
        [4.8, 3, 1.4, 0.3],
        [2, 1, 3.2, 1.1]
    ]
}

url = 'http://127.0.0.1:8000/api'
r = requests.post(url, json=to_predict_dict)
print(r.json())