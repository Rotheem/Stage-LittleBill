from fastapi.testclient import TestClient
from app.main import get_application
from app.utils.settings import Settings

import pytest


@pytest.fixture(scope="module", autouse=True)
def client() -> TestClient:
    return TestClient(get_application(settings=Settings()))  # type: ignore
