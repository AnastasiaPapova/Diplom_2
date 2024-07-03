import allure
import requests
from conftest import create_user
from urls import Urls, Handlers
from data import User


@allure.suite('Изменение данных пользовователя')
class TestChangingUserData:

    @allure.title("Изменение почты авторизованного пользователя")
    def test_changing_user_email_with_authorization(self, create_user):
        payload = {'email': User.create_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.title("Изменение пароля авторизованного пользователя")
    def test_changing_user_password_without_authorization(self, create_user):
        payload = {'password': User.create_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Изменение имени авторизованного пользователя")
    def test_changing_user_name_with_authorization(self, create_user):
        payload = {'name': User.create_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self):
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", data=User.create_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
