from faker import Faker
import random

fake = Faker(locale='ru')


def get_first_name() -> str:
    return fake.first_name_male()


def get_last_name() -> str:
    return fake.last_name_male()


def get_address() -> str:
    address = f'улица {fake.first_name()} {fake.random_int(1, 99)}'
    return address


def get_phone_number() -> str:
    # Генерируем 10 случайных цифр
    random_digits = ''.join(random.choices('0123456789', k=10))
    # Формируем номер телефона в формате +7XXXXXXXXXX
    phone_number = f"+7{random_digits}"
    return phone_number


if __name__ == '__main__':
    print(get_address())
