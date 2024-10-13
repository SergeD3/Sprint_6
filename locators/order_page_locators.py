from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_BUTTON_MENU = (
        By.XPATH,
        '//div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]'
    )  # кнопка Заказать в меню

    ORDER_BUTTON_MAIN_PAGE = (
        By.XPATH,
        '//div[contains(@class, "Home_FinishButton")]/button[contains(text(), "Заказать")]'
    )  # кнопка Заказать на странице main page

    # элементы формы заказа
    FIRST_NANE_INPUT = (By.XPATH, '//div/input[@placeholder="* Имя"]')  # поле Имя
    LAST_NAME_INPUT = (By.XPATH, '//div/input[@placeholder="* Фамилия"]')  # поле Фамилия
    ADDRESS_FIELD_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')  # поле Адрес
    METRO_STATION_INPUT = (By.XPATH, '//div/input[@placeholder="* Станция метро"]')  # поле Станция метро
    METRO_STATION_DIV = (By.XPATH, '//div/input[@placeholder="* Станция метро"]/parent::div')
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        '//div/input[@placeholder="* Телефон: на него позвонит курьер"]'
    )  # поле Телефон

    BUTTON_NEXT = (By.XPATH, '//div/button[contains(text(), "Далее")]')  # кнопка далее

    # поле-выпадающий список Станция метро
    SELECT_SEARCH_OPTIONS = (By.XPATH, '//ul[@class="select-search__options"]')
    SELECT_ZERO_ELEMENT = (By.XPATH, '//li/button[@tabindex="-1"]')
