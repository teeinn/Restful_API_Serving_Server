import json
import requests
from typing import List
from app.config import settings
from app.service.preprocess_data import DataConversion

def predict(file: bytes) -> List[List[int]]:
    input_data = DataConversion.preprocess_data(file)

    data = json.dumps({"signature_name": "serving_default", "instances": input_data})
    headers = {"content-type": "application/json"}

    json_response = requests.post(settings.url, data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']

    result = DataConversion.decode_predictions(predictions)
    return result


