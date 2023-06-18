from typing import List
import json
import requests
import numpy as np
from app.service.preprocess import preprocess_data
from app.config import settings
from app.model_info import modelInfo

def predict_data(data: List[dict]) -> List[List[int]]:
    data = json.dumps({"signature_name": "serving_default", "instances": data})
    headers = {"content-type": "application/json"}
    json_response = requests.post(settings.url, data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    return predictions

def decode_predictions(predictions: List[List[int]]) -> List[List[int]]:
    predictions = np.argmax(predictions, axis=1)
    return [modelInfo.classes[predict] for predict in predictions]

def predict(file: bytes) -> List[List[int]]:
    input_data = preprocess_data.preprocess_data(file)
    predictions = predict_data(input_data)
    result = decode_predictions(predictions)
    return result


