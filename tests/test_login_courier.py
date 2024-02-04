import allure
import pytest
import requests

from generate_new_courier import register_new_courier_and_return_login_password as gen_data
import urls
import handlers
from helpers import fake_courier_registration as fake


class TestLoginCourier:

    @allure.title('Check courier authorisation')
    def test_courier_authorisation(self, registered_courier_data):
        login, password, first_name = registered_courier_data
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_COURIER}",
                                 data={'login': login,
                                       'password': password,
                                       'first_name': first_name})
        assert response.status_code == 200
        print(registered_courier_data)

    @pytest.mark.parametrize('login, password',
                             [
                                 ('', gen_data()[0]),
                                 (gen_data()[1], '',),
                                 ('', '')
                             ]
                             )
    @allure.title('Check you need all data for login')
    def test_need_all_data_for_login(self, login, password):
        negative_login_data = {'login': login, 'password': password}
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_COURIER}", data=negative_login_data)
        assert response.status_code == 400, "Courier login with not all data"

    @pytest.mark.parametrize('login, password',
                             [
                                 ('123456', gen_data()[1]),
                                 (gen_data()[0], '123456',),
                                 ('123456', '654321')
                             ]
                             )
    @allure.title('Check_error_message_if_wrong_login_or_password')
    def test_return_error_message_for_negative_login(self, login, password):
        wrong_login_data = {'login': login, 'password': password}
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_COURIER}", data=wrong_login_data)
        assert response.status_code == 404

    @pytest.mark.parametrize('login, password',
                             [
                                 ('', gen_data()[1]),
                                 (gen_data()[0], '',),
                                 ('', '')
                             ]
                             )
    @allure.title('Check_error_message_if_not_all_data')
    def test_error_message_not_all_data(self, login, password):
        not_all_data = {"login": login, 'password': password}
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_COURIER}", data=not_all_data)
        assert response.json()['message'] == 'Недостаточно данных для входа', 'Wrong message'

    @allure.title('Check_error_message_if_user_have_not_registration')
    def test_return_error_for_unknown_user(self):
        faker_data = {"login": fake()[0], 'password': fake()[1]}
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_COURIER}", data=faker_data)
        assert response.json()['message'] == 'Учетная запись не найдена', 'Wrong message'
        print(response.json)

