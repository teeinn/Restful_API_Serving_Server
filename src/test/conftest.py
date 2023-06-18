from fastapi.testclient import TestClient
from app.entrypoints.main import app
import pytest


@pytest.fixture(scope="function", autouse=True)
def client():
    return TestClient(app)