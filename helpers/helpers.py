from faker import Faker

fake = Faker(locale='ru')


def get_first_name() -> str:
    return fake.first_name_male()


def get_last_name() -> str:
    return fake.last_name_male()


def get_address() -> str:
    return fake.address()


def get_city() -> str:
    return fake.city()


def get_phone_number() -> str:
    return fake.phone_number()
