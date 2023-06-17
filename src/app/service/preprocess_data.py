from typing import List
import pandas as pd
import numpy as np
from io import BytesIO

class DataConversion:
    column_name_to_change: dict = {
        "Adaptivity Level": 'Adaptivity_Level',
        "Education Level": "Education_Level",
        "Institution Type": "Institution_Type",
        "IT Student": "IT_Student",
        "Financial Condition": "Financial_Condition",
        "Internet Type": "Internet_Type",
        "Network Type": "Network_Type",
        "Class Duration": "Class_Duration",
        "Self Lms": "Self_Lms",
        "Load-shedding": "Load_shedding"
        }
    classes: list = ['Low', 'Moderate', 'High']
    label: str = "Adaptivity_Level"

    def preprocess_data(self, file: bytes) -> List[dict]:
        df = pd.read_csv(BytesIO(file))
        data = df.rename(columns=self.column_name_to_change)
        data[self.label] = data[self.label].map(self.classes.index)
        data = data.drop(self.label, axis=1)
        return data.to_dict('records')

    def decode_predictions(self, predictions: List[List[int]]) -> List[List[int]]:
        predictions = np.argmax(predictions, axis=1)
        return [self.classes[predict] for predict in predictions]



DataConversion = DataConversion()