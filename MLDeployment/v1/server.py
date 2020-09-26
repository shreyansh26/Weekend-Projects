import pickle
import logging
from fastapi import FastAPI
from models.iris import Iris

app = FastAPI(title="Iris Classifier API", description="API for Iris classification using ML", version="1.0")

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')

model = None

@app.on_event("startup")
def load_model():
    global model
    model = pickle.load(open("models/model.pkl", "rb"))

@app.post("/api", tags=["prediction"])
async def get_predictions(iris: Iris):
    try:
        data = dict(iris)['data']
        print(data)
        prediction = model.predict(data).tolist()
        log_proba = model.predict_log_proba(data).tolist()
        return {"prediction": prediction, "log_proba": log_proba}
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}