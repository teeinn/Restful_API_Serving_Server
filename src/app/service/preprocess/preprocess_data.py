from typing import List
from app.model_info import modelInfo
from app.service.errors import *

def convert_data(file: bytes) -> List[dict]:
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

def preprocess_data(file: bytes) -> List[dict]:
    try:
        data = convert_data(file)
        return data
    except:
        raise InvalidDataException("Error: Invalid input data format. Please provide valid file.")

