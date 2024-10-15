from selenium.webdriver.common.by import By


class OrderPageLocators:

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button"]')  # получаю кнопку Принять куки

    ORDER_BUTTON_MENU = (
        By.XPATH,
        '//div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]'
    )  # кнопка Заказать в меню

    ORDER_BUTTON_MAIN_PAGE = (
        By.XPATH,
        '//div[contains(@class, "Home_FinishButton")]/button[contains(text(), "Заказать")]'
    )  # кнопка Заказать на странице main page

    ORDER_BUTTON_ORDER_PAGE = (
        By.XPATH,
        '//div[contains(@class, "Order_Buttons")]/button[contains(text(), "Заказать")]'
    )  # кнопка Заказать на странице заказа

    # элементы формы заказа
    FIRST_NANE_INPUT = (By.XPATH, '//div/input[@placeholder="* Имя"]')  # поле Имя
    LAST_NAME_INPUT = (By.XPATH, '//div/input[@placeholder="* Фамилия"]')  # поле Фамилия
    ADDRESS_FIELD_INPUT = (By.XPATH, '//div/input[@placeholder="* Адрес: куда привезти заказ"]')  # поле Адрес
    METRO_STATION_INPUT = (By.XPATH, '//div/input[@placeholder="* Станция метро"]')  # поле Станция метро
    METRO_STATION_DIV = (
        By.XPATH,
        '//div/input[@placeholder="* Станция метро"]/parent::div'
    )  # родитель поля Станция метро
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        '//div/input[@placeholder="* Телефон: на него позвонит курьер"]'
    )  # поле Телефон

    ORDER_NEXT_BUTTON = (By.XPATH, '//div/button[contains(text(), "Далее")]')  # кнопка далее

    # поле-выпадающий список Станция метро
    SELECT_SEARCH_OPTIONS = (By.XPATH, '//ul[@class="select-search__options"]')  # основной блок выпадающего списка
    SELECT_ZERO_ELEMENT = (By.XPATH, '//li/button[@tabindex="-1"]')  # первый элемент выпадающего списка

    ABOUT_RENT_HEADER = (
        By.XPATH,
        '//div[contains(@class, "Order_Header") and contains(text(),"Про аренду")]'
    )  # заголовок страницы Про аренду

    # поле-календарь Когда привезти самокат
    WHEN_CALENDAR_INPUT = (
        By.XPATH,
        '//input[contains(@placeholder,"* Когда привезти самокат")]'
    )  # поле Когда привезти
    CALENDAR_BODY = (By.XPATH, '//div[@class="react-datepicker"]')  # календарь поля
    DATE_FOR_CALENDAR_INPUT = (
        By.XPATH,
        '//div[contains(@class, "react-datepicker") and starts-with(text(), "{num}")]'
    )  # дата в календаре

    # поле Срок аренды
    RENT_PERIOD_INPUT = (By.XPATH, '//div[contains(@class,"Dropdown-placeholder")]')  # поле Срок аренды
    RENT_DROPDOWN_MENU = (By.XPATH, '//div[@class="Dropdown-menu"]')  # выпадающий список поля Срок аренды
    RENT_OPTION_THREE_DAYS = (By.XPATH, '//div[contains(text(), "трое суток")]')  # опция вып. списка - трое суток

    COLOR_CHECKBOX = (By.XPATH, '//input[@id="{num}"]')  # чекбокс поля Цвет самоката

    COMMENT_COURIER_INPUT = (
        By.XPATH,
        '//input[contains(@placeholder, "Комментарий для курьера")]'
    )  # поле Комментарий для курьера

    # элементы модального окна подтверждения заказа
    MODAL_FORM = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]/parent::div')  # модальное окно
    MODAL_YES_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]'
    )  # кнопка Да в модальном окне

    MODAL_STATUS_HEADER = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader")]'
    )  # заголовок статуса модального окна

    MODAL_STATUS_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Order_NextButton")]/button[contains(text(), "Посмотреть статус")]'
    )  # кнопка Посмотреть статус
