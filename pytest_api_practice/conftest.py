import pytest
import requests

from api_client import ApiClient

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def http_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="session")
def api_client(base_url,http_session):
    return ApiClient(base_url,http_session)
