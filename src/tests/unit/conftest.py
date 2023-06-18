import pytest
from requests import Response

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
    bytesData = b'Gender,Age,Education Level,Institution Type,IT Student,' \
                b'Location,Load-shedding,Financial Condition,Internet Type,Network Type,' \
                b'Class Duration,Self Lms,Device,Adaptivity Level\nGirl,21-25,University,' \
                b'Non Government,No,Yes,Low,Mid,Wifi,4G,3-6,No,Computer,Moderate\n'
    return bytesData

@pytest.fixture
def invalid_bytes_data():
    invalid_bytesData = b'Gender,Age,Education Level,Institution Type,IT Student,' \
                        b'Location,Load-shedding,Financial Condition,Internet Type,Network Type,' \
                        b'Class Duration,Self Lms,Device\nGirl,21-25,University,' \
                        b'Non Government,No,Yes,Low,Mid,Wifi,4G,3-6,No,Computer\n'
    return invalid_bytesData

@pytest.fixture
def list_data():
    listData = [{'Gender': 'Girl', 'Age': '21-25', 'Education_Level': 'University',
                 'Institution_Type': 'Non Government', 'IT_Student': 'No', 'Location': 'Yes',
                 'Load_shedding': 'Low', 'Financial_Condition': 'Mid', 'Internet_Type': 'Wifi',
                 'Network_Type': '4G', 'Class_Duration': '3-6', 'Self_Lms': 'No', 'Device': 'Computer'}]
    return listData


@pytest.fixture
def prediction():
    prediction_result = [[0.0233333353, 0.976665854, 0.0]]
    return prediction_result

@pytest.fixture
def final_result():
    final_result = ['Moderate']
    return final_result