from selenium.webdriver.common.by import By


class Locators:
    # основные urls проекта
    URLS: dict = {
        'main_page': 'https://qa-scooter.praktikum-services.ru/',
    }

    # элементы меню
    MENU_ORDER_BUTTON: tuple = (
        By.XPATH,
        '//div[starts-with(@class, "Header")]/button[contains(text(), "Заказать")]'
    )  # получаю кнопку Заказать в меню

    # элементы блока Вопросы о важном
    FAQ: tuple = (By.CSS_SELECTOR, '.accordion')

    FAQ_ELEMENT_TEMPLATE: tuple = (
        By.XPATH,
        '//div[@id="accordion__heading-{num}" and @role="button"]'
    )

    FAQ_ELEMENT_TEMPLATE_TEXT: tuple = (
        By.XPATH,
        '//div[@id="accordion__panel-0"]/p'
    )  # получаю текст нулевого элемента

    FAQ_LAST_QUESTION: tuple = (
        By.XPATH,
        '//div[@id="accordion__heading-7" and @role="button"]')
