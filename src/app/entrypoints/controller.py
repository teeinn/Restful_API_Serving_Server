from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.service.inference import prediction
from app.service.preprocess.preprocess_data import preprocess_data
from app.service.errors import *
from app.config import apiClient
import requests

router = APIRouter()

@router.get("/v1/health/live", status_code=200)
async def health():
    try:
        requests.get(apiClient.url)
    except NotConnectedException:
        raise HTTPException(status_code=503, detail="Service Unavailable")

@router.post("/v1/models/random_forest/infer", status_code=200)
async def predict_csv(uploaded_file: UploadFile):
    try:
        input_file = uploaded_file.file.read()
        data = preprocess_data(input_file)
        result = prediction.predict(data)
        return JSONResponse(content=jsonable_encoder(result))

    except InvalidDataException:
        raise HTTPException(status_code=404, detail="Invalid Input Data")
    except NotConnectedException:
        raise HTTPException(status_code=503, detail="Service Unavailable")
