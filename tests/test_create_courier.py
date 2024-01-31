import allure
import requests
from generate_new_courier import register_new_courier_and_return_login_password as gen_data
import urls
import handlers


class TestCreateCourier:
    data = {}

    @classmethod
    def setup_class(cls):
        courier = gen_data()
        cls.data["password"] = courier[0]
        cls.data["login"] = courier[1]
        cls.data["firstName"] = courier[2]

    @allure.title('Check courier created')
    def test_create_courier(self):
        response_body = {
            "ok": True
        }
        response = requests.post(
            f'{urls.HOME_URL}{handlers.CREATE_COURIER}',
            data=TestCreateCourier.data)

        assert response.status_code == 201
        assert response.json() == response_body

    @allure.title('Check no same courier')
    def test_no_same_courier(self):
        response = requests.post(
            f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
            data=TestCreateCourier.data)
        assert response.status_code == 409, "Courier created with same data"


    @allure.title('Check status code')
    def test_status_code(self):
        response = requests.post(f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
                                 data=TestCreateCourier.data)
        assert response.status_code == 409, "Courier not created. Status " \
                                            "code wrong"


    @allure.title('Check message for creating courier with same login')
    def test_message_for_same_courier_login(self):
        response = requests.post(
            f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
            data=TestCreateCourier.data)
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.', \
            "Message for the same login is wrong"

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
