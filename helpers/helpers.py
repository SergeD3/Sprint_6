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


def get_date(timeline: str) -> date:
    """Функция возвращает текущую дату в формате dd.mm.yyyy."""
    if timeline == 'past':
        past_date = f'{int(date.today().day)-2}.{date.today().month}.{date.today().year}'
        return past_date
    elif timeline == 'future':
        future_date = f'{int(date.today().day)+2}.{date.today().month}.{date.today().year}'
        return future_date
    elif timeline == 'now':
        now_date = f'{int(date.today().day)}.{date.today().month}.{date.today().year}'
        return now_date
    else:
        print('Ошибка: укажите конкретный период времени.')
