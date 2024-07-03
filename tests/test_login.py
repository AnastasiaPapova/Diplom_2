import allure
import requests

from urls import Urls, Handlers
from data import User


@allure.suite('Авторизация пользователя')
class TestLogin:

    @allure.step('Авторизация под пользователем, который есть в системе')
    def test_login_user(self):
        response = requests.post(f'{Urls.BASE_URL}{Handlers.LOGIN_USER}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.step('Авторизация с некорректным логином и паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.BASE_URL}{Handlers.LOGIN_USER}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
