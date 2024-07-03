import pytest
import requests

from urls import Urls, Handlers
from data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.create_user()
    login_data = payload.copy()
    login_data.pop("name")
    response = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.BASE_URL}{Handlers.DELETE_USER}", headers={'Authorization': f'{token}'})