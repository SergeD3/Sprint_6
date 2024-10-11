import data

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def get_order_page(self):
        self.get_page(data.URLS['order_page'],)

    def click_order_button(self, button_index):
        pass
