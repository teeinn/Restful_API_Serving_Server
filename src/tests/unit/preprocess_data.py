import pytest
from app.service.preprocess.preprocess_data import *


def test_preprocess_data_returns_dictionary_list(client, bytes_data, list_data):
    result = preprocess_data(bytes_data)
    assert result == list_data

def test_preprocess_data_returns_error_when_input_invalid_data_type(client):
    with pytest.raises(InvalidDataException) as error:
        preprocess_data('invalid data')
    assert str(error.value) == "Error: Invalid input data format. Please provide valid file."

def test_preprocess_data_returns_error_if_target_column_not_existed(client, invalid_bytes_data):
    with pytest.raises(InvalidDataException) as error:
        preprocess_data(invalid_bytes_data)
    assert str(error.value) == "Error: Invalid input data format. Please provide valid file."