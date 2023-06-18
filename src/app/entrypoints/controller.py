from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.service.inference import prediction

router = APIRouter()

@router.post("/predict/csv", status_code=200)
async def predict_csv(file: UploadFile):
    file_uploaded = file.file.read()
    result = prediction.predict(file_uploaded)
    return JSONResponse(content=jsonable_encoder(result))

