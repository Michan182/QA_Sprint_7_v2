import pytest
import string
import random
from generate_new_courier import register_new_courier_and_return_login_password as gen_data
@pytest.fixture
def registered_courier_data():
    return gen_data()

@pytest.fixture
def generate_fake_login_and_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
