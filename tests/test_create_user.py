import pytest
import allure
import requests

from urls import Urls, Handlers
from data import User


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.step('Создание нового пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.BASE_URL}{Handlers.CREATE_USER}', data=User.create_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.step('Создание пользователя который уже есть в системе')
    def test_create_same_user(self):
        response = requests.post(f'{Urls.BASE_URL}{Handlers.CREATE_USER}', data=User.data_same)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.step('Создание пользователя с некорректными данными')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_with_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.BASE_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
