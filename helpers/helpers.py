from faker import Faker

fake = Faker()


def get_first_name() -> str:
    return fake.first_name()


def get_last_name() -> str:
    return fake.last_name()


def get_address() -> str:
    return fake.address()
