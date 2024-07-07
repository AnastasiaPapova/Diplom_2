import allure
import requests

import helpers
from conftest import create_user
from urls import Urls, Handlers


@allure.suite('Изменение данных пользовователя')
class TestChangingUserData:

    @allure.title("Изменение почты авторизованного пользователя")
    def test_changing_user_email_with_authorization(self, create_user):
        payload = {'email': helpers.create_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.title("Изменение пароля авторизованного пользователя")
    def test_changing_user_password_without_authorization(self, create_user):
        payload = {'password': helpers.create_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Изменение имени авторизованного пользователя")
    def test_changing_user_name_with_authorization(self, create_user):
        payload = {'name': helpers.create_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self):
        r = requests.patch(f"{Urls.BASE_URL}{Handlers.PATCH_USER}", data=helpers.create_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
