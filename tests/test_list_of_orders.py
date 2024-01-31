import allure
import requests

from generator import make_new_order_and_return_data
import urls
import handlers


class TestReturnOrderList:
    data = []

    @classmethod
    def setup_class(cls):
        order = make_new_order_and_return_data()
        cls.data.append(order)

    @allure.title('Check response has list of orders')
    def test_response_has_list_orders(self):
        response = requests.get(f'{urls.HOME_URL}{handlers.MAKE_ORDER}')
        assert len(response.json()) > 0

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
