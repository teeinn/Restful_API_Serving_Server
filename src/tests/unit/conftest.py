import pytest
from requests import Response
from app.service.preprocess.preprocess_data import convert_data


data_path = "../data/test.csv"
invalid_data_path = "../data/invalid_test.csv"


@pytest.fixture
def bytes_data():
    with open(data_path, 'rb') as f:
        bytesData = f.read()
    return bytesData

@pytest.fixture
def invalid_bytes_data():
    with open(invalid_data_path, 'rb') as f:
        invalid_bytesData = f.read()
    return invalid_bytesData

@pytest.fixture
def list_data(bytes_data):
    return convert_data(bytes_data)

@pytest.fixture
def prediction():
    return [[0.0233333353, 0.976665854, 0.0]]

@pytest.fixture
def final_result():
    return ['Moderate']


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


