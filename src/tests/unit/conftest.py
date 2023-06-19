import pytest
from requests import Response
import pandas as pd
from io import BytesIO
from app.model_info import modelInfo


class Data:
    def __init__(self):
        self.data_path = "../data/test.csv"
        self.invalid_data_path = "../data/invalid_test.csv"

        with open(self.data_path, 'rb') as f:
            self.bytesData = f.read()

        with open(self.invalid_data_path, 'rb') as f:
            self.invalid_bytesData = f.read()

    def file_path(self):
        return self.data_path

    def invalid_file_path(self):
        return self.invalid_data_path

    def bytes_data(self):
        return self.bytesData

    def invalid_bytes_data(self):
        return self.invalid_bytesData

    def list_data(self):
        df = pd.read_csv(BytesIO(self.bytesData))
        data = df.rename(columns=modelInfo.column_name_to_change)
        data[modelInfo.label] = data[modelInfo.label].map(modelInfo.classes.index)
        data = data.drop(modelInfo.label, axis=1)
        return data.to_dict('records')

    def prediction(self):
        return [[0.0233333353, 0.976665854, 0.0]]

    def final_result(self):
        return ['Moderate']
data = Data()



def mocked_requests_post(url, data, headers):
    class MockResponse:
        def __init__(self, url, data, header):
            self.url = url
            self.data = data
            self.header = header
        def get_response(self):
            response = Response()
            type(response).text = '{"predictions": [[0.0233333353, 0.976665854, 0.0]]}'
            return response
    return MockResponse(url, data, headers).get_response()



@pytest.fixture
def bytes_data():
    return data.bytes_data()

@pytest.fixture
def invalid_bytes_data():
    return data.invalid_bytes_data()

@pytest.fixture
def list_data():
    return data.list_data()

@pytest.fixture
def prediction():
    return data.prediction()

@pytest.fixture
def final_result():
    return data.final_result()

@pytest.fixture
def file_path():
    return data.file_path()

@pytest.fixture
def invalid_file_path():
    return data.invalid_file_path()