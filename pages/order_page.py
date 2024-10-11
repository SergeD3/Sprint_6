import data

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from helpers import helpers


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()
        self.get_order_page()

    def get_order_page(self):
        self.get_page(data.URLS['order_page'], self.locators.BUTTON_NEXT)

    def click_order_button(self, button_index):
        self.click_element_with_wait(self.locators.ORDER_BUTTONS[0])
        self.wait.until(expected_conditions.element_to_be_clickable(self.locators.FIRST_NANE_INPUT))

    def fill_form_fields(self):
        # заполняю поле Имя
        self.add_text_to_element(self.locators.FIRST_NANE_INPUT, helpers.get_first_name())
        # заполняю поле Фамилия
        self.add_text_to_element(self.locators.FIRST_NANE_INPUT, helpers.get_last_name())
        # заполняю поле Адрес
        self.add_text_to_element(self.locators.FIRST_NANE_INPUT, helpers.get_address())
        # выбираю Станцию метро
        self.click_element_with_wait()
