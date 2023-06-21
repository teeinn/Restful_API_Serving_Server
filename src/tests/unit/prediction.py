import pytest
from tests.unit.conftest import mocked_requests_post
from app.service.inference.prediction import *


def test_predict_data_returns_list_of_list(client, monkeypatch, list_data, prediction):
    monkeypatch.setattr(requests, "post", mocked_requests_post)
    result = predict_data(list_data)
    assert result == prediction


def test_predict_data_returns_error_when_serving_server_disconnected(client, list_data):
    with pytest.raises(NotConnectedException) as error:
        predict_data(list_data)
    assert str(error.value) == "Error: Serving server disconnected."


def test_decode_predictions_returns_final_result(client, prediction, final_result):
    result = decode_predictions(prediction)
    assert result == final_result


def test_predict_returns_final_result(client, monkeypatch, list_data, final_result):
    monkeypatch.setattr(requests, "post", mocked_requests_post)
    result = predict(list_data)
    assert result == final_result


def test_predict_returns_error_related_with_predict_data(client, monkeypatch, bytes_data, final_result):
    with pytest.raises(NotConnectedException) as error:
        predict(bytes_data)
    assert str(error.value) == "Error: Serving server disconnected."