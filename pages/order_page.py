import time
import data

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from helpers import helpers


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def get_order_page(self):
        self.get_page(data.URLS['order_page'], self.locators.ORDER_NEXT_BUTTON)
        self.click_accept_cookies()

    def get_text_from_rent_header(self):
        return self.get_text_from_element(self.locators.ABOUT_RENT_HEADER)

    def click_accept_cookies(self):
        self.click_element(self.locators.ACCEPT_COOKIES_BUTTON)

    def click_order_button_in_menu(self):
        self.click_element(self.locators.ORDER_BUTTON_MENU)
        self.basic_wait_element(locator=self.locators.FIRST_NANE_INPUT, by_visibility=True)

    def click_order_button_in_main_page(self):
        self.click_element(self.locators.ORDER_BUTTON_MENU[1])
        self.wait.until(expected_conditions.element_to_be_clickable(self.locators.FIRST_NANE_INPUT))

    def click_order_page_button(self):
        self.click_element(self.locators.ORDER_BUTTON_ORDER_PAGE)

    def click_next_button(self):
        self.click_element(self.locators.ORDER_NEXT_BUTTON)
        self.basic_wait_element(self.locators.ABOUT_RENT_HEADER, by_visibility=True)

    def set_date_calendar_field(self):
        date = helpers.get_tomorrow_date()
        self.click_element(self.locators.WHEN_CALENDAR_INPUT)
        self.basic_wait_element(self.locators.CALENDAR_BODY, by_visibility=True)
        formated_date = self.format_locators(locator=self.locators.DATE_FOR_CALENDAR_INPUT, num=date[:2])
        self.click_element(formated_date)
        self.wait.until_not(expected_conditions.visibility_of_element_located(self.locators.CALENDAR_BODY))
        self.check_value_date_field(date)

    def check_value_date_field(self, date):
        value = self.get_element_value(self.locators.WHEN_CALENDAR_INPUT)
        assert value == date

    def set_metro_station_field(self, station_index: int):
        self.add_text_to_element(self.locators.METRO_STATION_INPUT, data.METRO_STATIONS_FOR_INPUT[station_index])
        self.click_element(self.locators.SELECT_ZERO_ELEMENT)
        self.wait.until_not(expected_conditions.visibility_of_element_located(self.locators.SELECT_SEARCH_OPTIONS))

    def check_value_metro_field(self, station_index: int):
        element_text = self.get_element_value(self.locators.METRO_STATION_INPUT)
        metro_station_text = data.METRO_STATIONS_FOR_INPUT[station_index]
        assert element_text == metro_station_text, \
            f'значения на совпадают. Текст элемента: {element_text}, станция: {metro_station_text}'

    def set_rent_period_field(self):
        self.click_element(self.locators.RENT_PERIOD_INPUT)
        self.basic_wait_element(self.locators.RENT_DROPDOWN_MENU, by_visibility=True)
        self.click_element(self.locators.RENT_OPTION_THREE_DAYS)

    def check_rent_field_text(self):
        text = self.get_text_from_element(self.locators.RENT_PERIOD_INPUT)
        assert text == "трое суток"

    def enable_checkbox_color_field(self):
        self.click_element(self.locators.GREY_COLOR_CHECKBOX)

    def set_text_comment_field(self):
        self.add_text_to_element(self.locators.COMMENT_COURIER_INPUT, data.LOREM_TEXT)

    def check_comment_value(self):
        field_value = self.get_element_value(self.locators.COMMENT_COURIER_INPUT)
        assert field_value == data.LOREM_TEXT

    def check_order_status_header(self):
        header_text = self.get_text_from_element(self.locators.MODAL_STATUS_HEADER)
        assert 'Заказ оформлен' in header_text

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

    def fill_form_fields_second_page(self):
        # заполняю поле Когда привезти самокат
        self.set_date_calendar_field()
        # заполняю поле Срок аренды
        self.set_rent_period_field()
        self.check_rent_field_text()
        # заполняю поле Цвет самоката
        self.enable_checkbox_color_field()
        # заполняю поле
        self.set_text_comment_field()
        self.check_comment_value()

    def finalize_order(self):
        self.click_order_page_button()
        self.basic_wait_element(self.locators.MODAL_YES_BUTTON, by_visibility=True)
        self.click_element(self.locators.MODAL_YES_BUTTON)
        self.basic_wait_element(self.locators.MODAL_STATUS_BUTTON, by_visibility=True)
        self.check_order_status_header()
