from fastapi.testclient import TestClient
from app.entrypoints.main import app
from tests.unit.conftest import *


@pytest.fixture(scope="function", autouse=True)
def client():
    return TestClient(app)

