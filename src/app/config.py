from pydantic import BaseSettings

class ApiClient(BaseSettings):
    url: str = 'http://tfserving:8501/v1/models/saved_model:predict'
    headers: dict = {"content-type": "application/json"}
    datas: dict = {"signature_name": "serving_default", "instances": None}

apiClient = ApiClient()

