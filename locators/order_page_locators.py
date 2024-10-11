from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_BUTTONS = (By.XPATH, '//div/button[contains(text(), "Заказать")]')
    # элементы формы заказа
    FIRST_NANE_INPUT = (By.XPATH, '//div/input[@placeholder="* Имя"]')  # поле Имя
    LAST_NAME_INPUT = (By.XPATH, '//div/input[@placeholder="* Фамилия"]')  # поле Фамилия
    ADDRESS_FIELD_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')
