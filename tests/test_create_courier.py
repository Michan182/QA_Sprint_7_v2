import allure
import requests
import urls
import handlers

class TestCreateNewCourier():
    @allure.title('Check courier created')
    def test_create_courier(self, generate_fake_login_and_password):
        response_body = {
            "ok": True
        }
        response = requests.post(
            f'{urls.HOME_URL}{handlers.CREATE_COURIER}',
            data=generate_fake_login_and_password)

        assert response.status_code == 201
        assert response.json() == response_body

    @allure.title('Check no same courier create')
    def test_no_same_courier(self, registered_courier_data):
        login, password, first_name = registered_courier_data
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        response = requests.post(
            f"{urls.HOME_URL}{handlers.CREATE_COURIER}",
            data=payload)
        assert response.status_code == 409, "Courier created with same data"
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.', \
            "Message for the same login is wrong"

