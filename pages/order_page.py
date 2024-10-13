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
        self.get_page(data.URLS['order_page'], self.locators.BUTTON_NEXT)

    def get_text_from_rent_header(self):
        self.get_text_from_element(self.locators.ABOUT_RENT_HEADER)

    def click_order_button_in_menu(self):
        self.click_element(self.locators.ORDER_BUTTON_MENU)
        self.wait_element(locator=self.locators.FIRST_NANE_INPUT, by_visibility=True)

    def click_order_button_in_main_page(self):
        self.click_element(self.locators.ORDER_BUTTON_MENU[1])
        self.wait.until(expected_conditions.element_to_be_clickable(self.locators.FIRST_NANE_INPUT))

    def click_next_button(self):
        self.click_element(self.locators.BUTTON_NEXT)
        self.wait_element(self.locators.ABOUT_RENT_HEADER, by_visibility=True)

    def set_metro_station_field(self, station_index: int):
        self.add_text_to_element(self.locators.METRO_STATION_INPUT, data.METRO_STATIONS_FOR_INPUT[station_index])
        self.click_element(self.locators.SELECT_ZERO_ELEMENT)
        self.wait.until_not(expected_conditions.visibility_of_element_located(self.locators.SELECT_SEARCH_OPTIONS))
        self.check_value_metro_field(station_index)

    def check_value_metro_field(self, station_index: int):
        element_text = self.get_element_attr(self.locators.METRO_STATION_INPUT)
        metro_station_text = data.METRO_STATIONS_FOR_INPUT[station_index]
        assert element_text == metro_station_text, \
            f'значения на совпадают. Текст элемента: {element_text}, станция: {metro_station_text}'

    def fill_form_fields(self, station_index):
        # заполняю поле Имя
        self.add_text_to_element(self.locators.FIRST_NANE_INPUT, helpers.get_first_name())
        # заполняю поле Фамилия
        self.add_text_to_element(self.locators.LAST_NAME_INPUT, helpers.get_last_name())
        # заполняю поле Адрес
        self.add_text_to_element(self.locators.ADDRESS_FIELD_INPUT, helpers.get_address())
        # выбираю Станцию метро
        self.set_metro_station_field(station_index)
        # заполняю поле Телефон
        self.add_text_to_element(self.locators.PHONE_NUMBER_INPUT, helpers.get_phone_number())
