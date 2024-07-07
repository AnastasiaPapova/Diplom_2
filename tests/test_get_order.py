import allure
import requests
from conftest import create_user
from urls import Urls, Handlers
from data import Ingredients


@allure.suite("Получение заказов конкретного пользователя")
class TestGetOrder:

    @allure.step("Получение заказов пользователя с авторизацией")
    def test_get_order_user_with_authorization(self, create_user):
        token = {'Authorization': create_user[3]}
        request = requests.post(f"{Urls.BASE_URL}{Handlers.CREATE_ORDER}", headers=token,
                                data=Ingredients.correct_data)
        response_get_order = requests.get(f"{Urls.BASE_URL}{Handlers.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == \
               request.json()['order']['number']

    @allure.step("Получение заказов при неавторизованном пользователе")
    def test_get_order_user_without_authorization(self):
        r = requests.get(f"{Urls.BASE_URL}{Handlers.GET_ORDERS}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"
