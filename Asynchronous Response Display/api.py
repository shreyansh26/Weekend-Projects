from flask import Flask, request
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app) 

HOST = "0.0.0.0"
PORT = 9600

@app.route('/query1', methods=["GET"])
def answer1():
    query = request.args.get("query")
    a = random.randint(4, 10)
    print(f"Query1 received. Sleeping for {a} seconds")
    time.sleep(a)
    return {'answer': "This is query1 " + query}

@app.route('/query2', methods=["GET"])
def answer2():
    query = request.args.get("query")
    a = random.randint(4, 10)
    print(f"Query2 received. Sleeping for {a} seconds")
    time.sleep(a)
    return {'answer': "This is query2 " + query}

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
