from selenium.webdriver.common.by import By


class OrderPageLocators:

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button"]')

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
    METRO_STATION_DIV = (By.XPATH, '//div/input[@placeholder="* Станция метро"]/parent::div')
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        '//div/input[@placeholder="* Телефон: на него позвонит курьер"]'
    )  # поле Телефон

    ORDER_NEXT_BUTTON = (By.XPATH, '//div/button[contains(text(), "Далее")]')  # кнопка далее

    # поле-выпадающий список Станция метро
    SELECT_SEARCH_OPTIONS = (By.XPATH, '//ul[@class="select-search__options"]')
    SELECT_ZERO_ELEMENT = (By.XPATH, '//li/button[@tabindex="-1"]')

    ABOUT_RENT_HEADER = (
        By.XPATH,
        '//div[contains(@class, "Order_Header") and contains(text(),"Про аренду")]'
    )

    # поле-календарь Когда привезти самокат
    WHEN_CALENDAR_INPUT = (
        By.XPATH,
        '//input[contains(@placeholder,"* Когда привезти самокат")]'
    )  # поле Когда привезти
    CALENDAR_BODY = (By.XPATH, '//div[@class="react-datepicker"]')
    DATE_FOR_CALENDAR_INPUT = (By.XPATH, '//div[contains(@class, "react-datepicker") and starts-with(text(), "{num}")]')

    # поле Срок аренды
    RENT_PERIOD_INPUT = (By.XPATH, '//div[contains(@class,"Dropdown-placeholder")]')
    RENT_OPTION_THREE_DAYS = (By.XPATH, '//div[contains(text(), "трое суток")]')
    RENT_DROPDOWN_MENU = (By.XPATH, '//div[@class="Dropdown-menu"]')

    # поле Цвет самоката
    GREY_COLOR_CHECKBOX = (By.XPATH, '//input[@id="grey"]')  # чекбокс серая безысходность

    # поле Комментарий для курьера
    COMMENT_COURIER_INPUT = (By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]')

    # элементы алерта подтверждения заказа
    MODAL_FORM = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]/parent::div')
    MODAL_YES_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]'
    )

    MODAL_STATUS_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')

    MODAL_STATUS_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Order_NextButton")]/button[contains(text(), "Посмотреть статус")]'
    )
