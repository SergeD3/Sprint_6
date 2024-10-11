from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_BUTTONS = (By.XPATH, '//div/button[contains(text(), "Заказать")]')  # кнопки Заказать. Два штука
    # элементы формы заказа
    FIRST_NANE_INPUT = (By.XPATH, '//div/input[@placeholder="* Имя"]')  # поле Имя
    LAST_NAME_INPUT = (By.XPATH, '//div/input[@placeholder="* Фамилия"]')  # поле Фамилия
    ADDRESS_FIELD_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')  # поле Адрес
    METRO_STATION_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')  # поле Станция метро
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        '//div/input[@placeholder="* Телефон: на него позвонит курьер"]'
    )  # поле Телефон

    BUTTON_NEXT = (By.XPATH, '//div/button[contains(text(), "Далее")]')  # кнопка далее

    # поле-выпадающий список Станция метро
    SELECT_ZERO_ELEMENT = (By.XPATH, '//ul/li[contains(@class, "select-search") and @data-index="0"]')
