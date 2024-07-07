from faker import Faker


def create_user():
    fake = Faker()

    reg_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()}
    return reg_data
