import allure
import requests
from conftest import create_user
from urls import Urls, Handlers
from data import Ingredients


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.step("Создание заказа авторизованным пользователем")
    def test_create_order_with_authorization(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_ORDER}", headers=token, data=Ingredients.correct_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.step("Создание заказа не авторизованного пользователя")
    def test_create_order_not_authorized(self):
        r = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_ORDER}", data=Ingredients.correct_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.step("Создание заказа с ингредиентами")
    def test_create_order_with_ingridient(self):
        r = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_ORDER}", data=Ingredients.correct_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.step("Создание заказа без ингредиентов")
    def test_create_order_without_ingridient(self):
        r = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_ORDER}")
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.step("Создание с невалидным хешем ингредиента")
    def test_create_order_invalid_hash(self):
        response = requests.post(Urls.BASE_URL + Handlers.CREATE_ORDER, headers={"Content-Type": "application/json"},
                                 json=Ingredients.incorrect_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
