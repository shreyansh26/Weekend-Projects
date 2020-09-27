from fastapi import APIRouter
from models.model import IrisClassifier
from starlette.responses import JSONResponse

router = APIRouter()

@router.post('/classify_iris')
def classify_iris(iris_features: dict):
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify(iris_features))