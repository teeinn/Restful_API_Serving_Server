from pydantic import BaseSettings

class Settings(BaseSettings):
    url: str = 'http://tfserving:8501/v1/models/saved_model:predict'

settings = Settings()
