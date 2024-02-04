import allure
import requests
import json
import pytest
import handlers
import urls
from scooter_color_methods import without_color_scooter_order


class TestMakeOrder:

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY']])
    @allure.title('Check can choose Black, Grey color for scooter')
    def test_choose_black_color(self, color):
        payload = without_color_scooter_order()
        payload["color"] = color
        json_payload = json.dumps(payload)
        response = requests.post(
            f'{urls.HOME_URL}{handlers.MAKE_ORDER}',
            data=json_payload)
        response_data = response.json()
        assert "track" in response_data.keys()

    @allure.title('Check order scooter without color')
    def test_order_without_scooter_color(self):
        response = requests.post(
            f'{urls.HOME_URL}{handlers.MAKE_ORDER}',
            data=without_color_scooter_order())
        response_data = response.json()
        assert "track" in response_data.keys()


