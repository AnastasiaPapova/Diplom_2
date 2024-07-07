

class User:

    data_correct = {
        "email": 'kotishka2012@yandex.ru',
        "password": "123456"}

    data_same = {
        "email": 'kotishka2012@yandex.ru',
        "password": "123456",
        "name": "Анастасия Папова"
    }

    data_negative = {
        "email": 'kotishka2012222@yandex.ru',
        "password": "123456"}

    data_without_email = {
        "email": '',
        "password": "123456",
        "name": "Анастасия Папова"}

    data_without_password = {
        "email": 'kotishka2012@yandex.ru',
        "password": "",
        "name": "Анастасия Папова"}

    data_without_name = {
        "email": 'kotishka2012@yandex.ru',
        "password": "123456",
        "name": ""}

    data_updated = {
        "email": 'kotishka2012@yandex.ru',
        "password": "123456",
        "name": "Анастасия"}


class Ingredients:
    correct_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    empty_order = {"ingredients": ""}

    incorrect_data = {
        "ingredients": ["660d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    }
