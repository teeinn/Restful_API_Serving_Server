from typing import List
import pandas as pd
from io import BytesIO
from app.model_info import modelInfo
from app.service.errors import *

def preprocess_data(file: bytes) -> List[dict]:
    try:
        df = pd.read_csv(BytesIO(file))
        data = df.rename(columns=modelInfo.column_name_to_change)
        data[modelInfo.label] = data[modelInfo.label].map(modelInfo.classes.index)
        data = data.drop(modelInfo.label, axis=1)
        return data.to_dict('records')
    except:
        raise InvalidDataException("Error: Invalid input data format. Please provide valid file.")

