import allure
import urls
import handlers
import requests
import pytest
from generator import generate_random_data


class TestCreateCourierMissedData:

    @pytest.mark.parametrize('password, login, firstName',
                             [
                                 ("", generate_random_data(5), generate_random_data(5)),
                                 (generate_random_data(5), "", generate_random_data(5)),
                                 (generate_random_data(5), "", generate_random_data(5)),
                                 ("", "", "")
                             ]
                             )
    @allure.story('Check authorisation status code with missed data')
    @allure.title('Test create courier with missing data and check status code')
    def test_create_user_status_code_with_not_all_data(self, login, password, firstName):
        negative_auth_data = {'login': login, 'password': password,
                              'firstName': firstName}

        response = requests.post(f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
                                 data=negative_auth_data)
        assert response.status_code == 400, "Courier created with not all data"

    @pytest.mark.parametrize('password, login, firstName',
                             [
                                 ("", generate_random_data(5), generate_random_data(5)),
                                 (generate_random_data(5), "", generate_random_data(5)),
                                 (generate_random_data(5), "", generate_random_data(5)),
                                 ("", "", "")
                             ]
                             )
    @allure.story('Check authorisation error message with missed data')
    @allure.title('Test create courier with missing data and check error message')
    def test_create_user_error_message_with_not_all_data(self, login, password,
                                                         firstName):
        negative_auth_data = {'login': login, 'password': password,
                              'firstName': firstName}

        response = requests.post(f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
                                 data=negative_auth_data)
        assert response.json()['message'] == \
               'Недостаточно данных для создания учетной записи', 'Wrong ' \
                                                                  'message'
