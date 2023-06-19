from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.service.inference import prediction
from app.service.errors import *

router = APIRouter()

@router.post("/predict/csv", status_code=200)
async def predict_csv(file: UploadFile):
    try:
        file_uploaded = file.file.read()
        result = prediction.predict(file_uploaded)
        return JSONResponse(content=jsonable_encoder(result))
    except InvalidDataException:
        raise HTTPException(status_code=404, detail="Invalid Input Data")
    except NotConnectedException:
        raise HTTPException(status_code=500, detail="Internal Server Error")
