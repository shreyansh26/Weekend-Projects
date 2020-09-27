import pickle
import logging
from fastapi import FastAPI
from models.routers import iris_classifier_router

app = FastAPI(title="Iris Classifier API", description="API for Iris classification using ML", version="1.0")
app.include_router(iris_classifier_router.router, prefix='/iris')

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')

@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'