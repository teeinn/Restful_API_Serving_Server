from typing import List
import json
import requests
import numpy as np
from app.config import apiClient
from app.model_info import modelInfo
from app.service.errors import *

def predict_data(data: List[dict]) -> List[List[int]]:
    try:
        apiClient.datas["instances"] = data
        json_response = requests.post(apiClient.url, data=json.dumps(apiClient.datas), headers=apiClient.headers)
        predictions = json.loads(json_response.text)['predictions']
        return predictions
    except:
        raise NotConnectedException("Error: Serving server disconnected.")


def decode_predictions(predictions: List[List[int]]) -> List[List[int]]:
    predictions = np.argmax(predictions, axis=1)
    return [modelInfo.classes[predict] for predict in predictions]


def predict(data: List[dict]) -> List[List[int]]:
    try:
        predictions = predict_data(data)
        result = decode_predictions(predictions)
        return result
    except Exception as err:
        raise err

