import datetime
import random as r
import string
from faker import Faker
from datetime import datetime


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(r.choice(letters) for i in range(length))
    return random_string


fake = Faker(locale="ru_RU")


def fake_courier_registration():
    fake_data = []
    fake_login = fake.email()
    fake_password = fake.password()
    fake_first_name = fake.first_name()

    fake_data.append(fake_login)
    fake_data.append(fake_password)
    fake_data.append(fake_first_name)
    return fake_data


def fake_make_order():
    fake_order = []
    fake_firstName = fake.first_name()
    fake_lastName = fake.last_name()
    fake_address = fake.address()
    ran_metroStation = r.randint(1, 10)
    fake_phone = fake.phone_number()
    ran_rentTime = r.randint(1, 5)
    deliveryDate = datetime.now()
    fake_comment = generate_random_string(9)

    fake_order.append(fake_firstName)
    fake_order.append(fake_lastName)
    fake_order.append(fake_address)
    fake_order.append(ran_metroStation)
    fake_order.append(fake_phone)
    fake_order.append(ran_rentTime)
    fake_order.append(deliveryDate)
    fake_order.append(fake_comment)
    return fake_order


