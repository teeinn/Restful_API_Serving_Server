from typing import List
from app.model_info import modelInfo
from app.service.errors import *

def preprocess_data(file: bytes) -> List[dict]:
    try:
        keys, values = list(), list()
        for idx, data in enumerate(file.split(b'\n')):
            element = data.decode('utf-8').split(',')
            if element[0] != '':
                if idx == 0: keys.append(element)
                else: values.append(element)

        for idx, key in enumerate(keys[0]):
            if key in modelInfo.column_name_to_change.keys():
                keys[0][idx] = modelInfo.column_name_to_change[key]
        datas = [dict(zip(keys[0], value)) for value in values]

        for data in datas:
            data.pop(modelInfo.label)
        return datas

    except:
        raise InvalidDataException("Error: Invalid input data format. Please provide valid file.")

