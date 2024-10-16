import allure
import data

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helpers import helpers


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Открываю страницу заказа.')
    def get_order_page(self):
        self.get_page(data.URLS['order_page'], self.locators.ORDER_NEXT_BUTTON)
        self.click_accept_cookies()

    @allure.step('Получаю текст из заголовка страницы заказа.')
    def get_text_from_rent_header(self):
        return self.get_text_from_element(self.locators.ABOUT_RENT_HEADER)

    @allure.step('Нажимаю кнопку принять куки.')
    def click_accept_cookies(self):
        self.click_element(self.locators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Нажимаю на указанную кнопку Заказать.')
    def click_order_button_on_main_page(self, variant: str):
        """Метод нажимает на одну из кнопок Заказать на главной странице. Варианты кнопок: menu, main_page"""
        if variant == 'menu':
            self.click_element(self.locators.ORDER_BUTTON_MENU)
            self.basic_wait_element(locator=self.locators.FIRST_NANE_INPUT, by_visibility=True)
        elif variant == 'main_page':
            self.click_element(self.locators.ORDER_BUTTON_MAIN_PAGE)
            self.basic_wait_element(locator=self.locators.FIRST_NANE_INPUT, by_visibility=True)
        else:
            print('Необходимо указать конкретную кнопку Заказать. Варианты: main_page, menu.')

    @allure.step('Нажимаю кнопку Заказать на последней странице создания заказа.')
    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON_ORDER_PAGE)

    @allure.step('Нажимаю кнопку Далее.')
    def click_next_button(self):
        self.click_element(self.locators.ORDER_NEXT_BUTTON)
        self.basic_wait_element(self.locators.ABOUT_RENT_HEADER, by_visibility=True)

    @allure.step('Добавляю значение в поле Когда привезти самокат, через календарь.')
    def set_date_calendar_field(self, timeline: str):
        date = helpers.get_date(timeline)
        self.click_element(self.locators.WHEN_CALENDAR_INPUT)
        self.basic_wait_element(self.locators.CALENDAR_BODY, by_visibility=True)
        formated_date = self.format_locators(locator=self.locators.DATE_FOR_CALENDAR_INPUT, num=date[:2])
        self.click_element(formated_date)
        self.basic_wait_until_not_visibility(self.locators.CALENDAR_BODY)
        self.check_value_date_field(date)

    @allure.step('Сравниваю значение в поле Когда привезти самокат с ожидаемым значением.')
    def check_value_date_field(self, date):
        value = self.get_element_value(self.locators.WHEN_CALENDAR_INPUT)
        assert value == date

    @allure.step('Добавляю значение в поле Станция метро.')
    def set_metro_station_field(self, station_index: int):
        self.add_text_to_element(self.locators.METRO_STATION_INPUT, data.METRO_STATIONS_FOR_INPUT[station_index])
        self.click_element(self.locators.SELECT_ZERO_ELEMENT)
        self.basic_wait_until_not_visibility(self.locators.SELECT_SEARCH_OPTIONS)

    @allure.step('Сравниваю значение в поле Станция метро с ожидаемым значением.')
    def check_value_metro_field(self, station_index: int):
        element_text = self.get_element_value(self.locators.METRO_STATION_INPUT)
        metro_station_text = data.METRO_STATIONS_FOR_INPUT[station_index]
        assert element_text == metro_station_text, \
            f'значения на совпадают. Текст элемента: {element_text}, станция: {metro_station_text}'

    @allure.step('Выбираю значение в поле Срок аренды')
    def set_rent_period_field(self):
        self.click_element(self.locators.RENT_PERIOD_INPUT)
        self.basic_wait_element(self.locators.RENT_DROPDOWN_MENU, by_visibility=True)
        self.click_element(self.locators.RENT_OPTION_THREE_DAYS)

    @allure.step('Сравниваю значение в поле Срок аренды с ожидаемым значением.')
    def check_rent_field_text(self):
        text = self.get_text_from_element(self.locators.RENT_PERIOD_INPUT)
        assert text == "трое суток"

    @allure.step('Отмечаю чекбокс в поле Цвет самоката.')
    def enable_checkbox_color_field(self, color: str):
        if color == 'grey':
            grey = self.format_locators(self.locators.COLOR_CHECKBOX, color)
            self.click_element(grey)
        elif color == 'black':
            black = self.format_locators(self.locators.COLOR_CHECKBOX, color)
            self.click_element(black)

    @allure.step('Добавляю текст в поле Комментарий для курьера.')
    def set_text_comment_field(self):
        self.add_text_to_element(self.locators.COMMENT_COURIER_INPUT, data.LOREM_TEXT)

    @allure.step('Сравниваю значение в поле Комментарий для курьера с ожидаемым значением.')
    def check_comment_value(self):
        field_value = self.get_element_value(self.locators.COMMENT_COURIER_INPUT)
        assert field_value == data.LOREM_TEXT

    @allure.step('Сравниваю значение заголовка модального окна с ожидаемым значением.')
    def check_order_status_header(self):
        header_text = self.get_text_from_element(self.locators.MODAL_STATUS_HEADER)
        return 'Заказ оформлен' in header_text

    @allure.step('Заполняю поля на первой странице создания заказа.')
    def fill_form_fields_first_page(self, station_index):
        # заполняю поле Имя
        self.add_text_to_element(self.locators.FIRST_NANE_INPUT, helpers.get_first_name())
        # заполняю поле Фамилия
        self.add_text_to_element(self.locators.LAST_NAME_INPUT, helpers.get_last_name())
        # заполняю поле Адрес
        self.add_text_to_element(self.locators.ADDRESS_FIELD_INPUT, helpers.get_address())
        # выбираю Станцию метро
        self.set_metro_station_field(station_index)
        self.check_value_metro_field(station_index)
        # заполняю поле Телефон
        self.add_text_to_element(self.locators.PHONE_NUMBER_INPUT, helpers.get_phone_number())

    @allure.step('Заполняю поля на второй странице создания заказа.')
    def fill_form_fields_second_page(self, timeline: str, color: str):
        # заполняю поле Когда привезти самокат
        self.set_date_calendar_field(timeline)
        # заполняю поле Срок аренды
        self.set_rent_period_field()
        self.check_rent_field_text()
        # заполняю поле Цвет самоката
        self.enable_checkbox_color_field(color)
        # заполняю поле
        self.set_text_comment_field()
        self.check_comment_value()

    @allure.step('Нажимаю кнопку Заказать и подтверждаю заказ в модальном окне.')
    def finalize_order(self):
        self.click_order_button()
        self.basic_wait_element(self.locators.MODAL_YES_BUTTON, by_visibility=True)
        self.click_element(self.locators.MODAL_YES_BUTTON)
        self.basic_wait_element(self.locators.MODAL_STATUS_BUTTON, by_visibility=True)
