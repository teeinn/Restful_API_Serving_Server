from tests.unit.conftest import mocked_requests_post
import requests

def test_predict_csv_returns_200(client, monkeypatch, file_path):
    monkeypatch.setattr(requests, "post", mocked_requests_post)
    with open(file_path, 'rb') as file:
        response = client.post("/predict/csv/", files={"file": ("filename", file, "multipart/form-data")})
    assert response.status_code == 200

def test_predict_csv_returns_404_when_input_invalid_data(client, monkeypatch, invalid_file_path):
    monkeypatch.setattr(requests, "post", mocked_requests_post)
    with open(invalid_file_path, 'rb') as file:
        response = client.post("/predict/csv/", files={"file": ("filename", file, "multipart/form-data")})
    assert response.status_code == 404
    assert response.json() == {'detail': "Invalid Input Data"}

def test_predict_csv_returns_500_when_serving_server_disconnected(client, monkeypatch, file_path):
    with open(file_path, 'rb') as file:
        response = client.post("/predict/csv/", files={"file": ("filename", file, "multipart/form-data")})
    assert response.status_code == 500
    assert response.json() == {'detail': "Internal Server Error"}