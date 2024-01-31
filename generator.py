from datetime import datetime
from random import randint

import requests

import urls
from helpers import generate_random_string, fake_make_order, fake
import handlers
import string
import random


def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


def make_new_order_and_return_data():
    order_data = []
    fake_firstName = fake.first_name()
    fake_lastName = fake.last_name()
    fake_address = fake.address()
    ran_metroStation = randint(1, 10)
    fake_phone = fake.phone_number()
    ran_rentTime = randint(1, 5)
    deliveryDate = datetime.now()
    fake_comment = generate_random_string(9)

    payload = {
        "firstName": fake_firstName,
        "lastName": fake_lastName,
        "address": fake_address,
        "metroStation": ran_metroStation,
        "phone": fake_phone,
        "rentTime": ran_rentTime,
        "deliveryDate": deliveryDate,
        "comment": fake_comment
    }
    response = \
        requests.post(
            f'{urls.HOME_URL}{handlers.MAKE_ORDER}',
            data=payload)

    if response.status_code == 201:
        order = fake_make_order()
        order_data.append(order)

    return order_data

def generate_random_data(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string