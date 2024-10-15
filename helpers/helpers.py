from faker import Faker
import random
from datetime import date

fake = Faker(locale='ru')


def get_first_name() -> str:
    """Функция возвращает случайное мужское имя."""
    return fake.first_name_male()


def get_last_name() -> str:
    """Функция возвращает случайную мужскую фамилию."""
    return fake.last_name_male()


def get_address() -> str:
    """Функция возвращает случайное название улицы и номер строения."""
    address = f'улица {fake.first_name()} {fake.random_int(1, 99)}'
    return address


def get_phone_number() -> str:
    """Функция возвращает случайный номер телефона в формате +7XXXXXXXXXX."""
    # Генерируем 10 случайных цифр
    random_digits = ''.join(random.choices('0123456789', k=10))
    # Формируем номер телефона в формате +7XXXXXXXXXX
    phone_number = f"+7{random_digits}"
    return phone_number


def get_tomorrow_date():
    """Функция возвращает текущую дату в формате dd.mm.yyyy."""
    tomorrow_date = f'{int(date.today().day)+1}.{date.today().month}.{date.today().year}'
    return tomorrow_date


if __name__ == '__main__':
    text = get_tomorrow_date()
    print(text[:2])
